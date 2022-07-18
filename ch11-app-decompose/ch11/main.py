from fastapi import FastAPI
from config.db import create_async_db, close_async_db
from api import login, officials, players

# Prometheus
from starlette_exporter import PrometheusMiddleware, handle_metrics

# OpenTracing 
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor

# Service Discovery
from py_eureka_client.eureka_client import EurekaClient

# Flask integration
from ch11_flask.app import app as flask_app
from fastapi.middleware.wsgi import WSGIMiddleware

# Django integration
from django.core.wsgi import get_wsgi_application
import os
from importlib.util import find_spec
from fastapi.staticfiles import StaticFiles

# Django setup
# Export Django settings env variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ch11_django.settings')

# Get Django WSGI app
django_app = get_wsgi_application()

app = FastAPI()

# Prometheus configuration
app.add_middleware(PrometheusMiddleware, app_name="osms") # this is ok
app.add_route("/metrics", handle_metrics)

# Flask integration
app.mount("/ch11/flask", WSGIMiddleware(flask_app))

# Serve Django static files and integration
app.mount('/static',
    StaticFiles(
         directory=os.path.normpath(
              os.path.join(find_spec('django.contrib.admin').origin, '..', 'static')
         )
   ),
   name='static',
)
app.mount('/ch11/django', WSGIMiddleware(django_app))

#OpenTracing configuration
resource=Resource.create({SERVICE_NAME: "online-sports-tracer"})
tracer = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer)

jaeger_exporter = JaegerExporter(
    # configure agent
    agent_host_name='localhost',
    agent_port=6831,
    # optional: configure also collector
    # collector_endpoint='http://localhost:14268/api/traces?format=jaeger.thrift',
    # username=xxxx, # optional
    # password=xxxx, # optional
    # max_tag_value_length=None # optional
)
span_processor = BatchSpanProcessor(jaeger_exporter)
tracer.add_span_processor(span_processor)
FastAPIInstrumentor.instrument_app(app, tracer_provider=tracer)
LoggingInstrumentor().instrument(set_logging_format=True)

app.include_router(login.router, prefix='/ch11')
app.include_router(officials.router, prefix='/ch11')
app.include_router(players.router, prefix='/ch11')

@app.on_event("startup")
async def init():
    create_async_db() 
    global client
    client = EurekaClient(eureka_server="http://DESKTOP-56HNGC9:8761/eureka", 
                          app_name="sports_service", instance_port=8000, instance_host="192.168.1.5")
    await client.start()


@app.on_event("shutdown")
async def destroy():
    close_async_db() 
    await client.stop()


