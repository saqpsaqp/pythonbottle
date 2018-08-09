from bottle import Bottle

def loadapp ():
    aplicacion=Bottle()
    @aplicacion.get("/")
    def mostrar():
        return "tales y tales"

    return aplicacion

aplicacion=loadapp()

#aplicacion.run(port=8888)