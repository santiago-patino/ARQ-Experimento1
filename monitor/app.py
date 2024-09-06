from monitor import create_app
from flask_restful import Resource, Api
from celery import Celery
from .tareas.tareas import enviar_mensajes
import threading
import time
from .monitoreo import imprimir_estado

celery_app = Celery('task', broker='redis://localhost:6379/0')

app = create_app('default')
app_context = app.app_context()
app_context.push()

def iniciar_hilo():
    hilo = threading.Thread(target=ejecutar_cada_5_segundos)
    hilo.daemon = True  # El hilo se cierra cuando la app se cierra
    hilo.start()

def ejecutar_cada_5_segundos():
    contador = 0
    while contador < 5:
        print("Función ejecutada cada 5 segundos")
        enviar_mensajes()
        imprimir_estado()
        time.sleep(5)
        contador += 1
    print("La función ha terminado después de 5 ejecuciones.")

class VistaEmpezarMonitoreo(Resource):

    def get(self):
        iniciar_hilo()
        #enviar_mensajes()
    
api = Api(app)

api.add_resource(VistaEmpezarMonitoreo, '/monitoreo')





