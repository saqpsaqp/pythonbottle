from bottle import Bottle

aplicacion=Bottle()

@aplicacion.get("/")
def mostrar():
    return "tales y tales"

aplicacion.run(port=8888)
