import eel;

# Code before execution
@eel.expose
def hello():
    return "Hello World!"

eel.init("web")
eel.start("index.html")