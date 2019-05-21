from bottle import Bottle

def loadapp ():
    aplicacion=Bottle()
    @aplicacion.get("/")
    def mostrar():
        return "What's up Bro? V2"

    return aplicacion

aplicacion=loadapp()

#aplicacion.run(port=8888)
