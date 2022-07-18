from ch11_flask.app import app 

@app.route("/index")
def testing():
    return "flask integration"