from bottle import Bottle

def loadapp ():
    aplicacion=Bottle()
    @aplicacion.get("/")
    def mostrar():
        return "What's up Bro?"

    return aplicacion

aplicacion=loadapp()

#aplicacion.run(port=8888)
