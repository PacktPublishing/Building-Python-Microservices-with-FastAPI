import uvicorn

original_callback = uvicorn.main.callback

def callback(**kwargs):
    from celery.contrib.testing.worker import start_worker
    import services.billing

    with start_worker(services.billing.celery, perform_ping_check=False, loglevel="info"):
        original_callback(**kwargs)

uvicorn.main.callback = callback


if __name__ == "__main__":
    uvicorn.main()