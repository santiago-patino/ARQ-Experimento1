from monitor import create_app
from flask_restful import Resource, Api
from celery import Celery
from .tareas.tareas import enviar_mensajes, mostrar_notificacion, services
import threading
import time
import redis

celery_app = Celery('task', broker='redis://localhost:6379/0')
r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

app = create_app('default')
app_context = app.app_context()
app_context.push()

def iniciar_hilo():
    hilo = threading.Thread(target=ejecutar_cada_5_segundos)
    hilo.daemon = True  # El hilo se cierra cuando la app se cierra
    hilo.start()

def ejecutar_cada_5_segundos():
    contador = 0
    times_execute = 5
    while contador < times_execute:
        enviar_mensajes()
        contador += 1
        if contador == times_execute:
            print("\nMensajes enviados: "+ str(times_execute))
            for servicio_nombre, servicio_data in services.items():
                if r.hgetall(servicio_nombre).get("responde") == "0":
                    mostrar_notificacion("¡"+servicio_nombre + " no responde!")
                else:
                    print("\n"+servicio_nombre + ": Correcto")
                    r.hset(servicio_nombre, "responde", 0)


        time.sleep(5)

class VistaEmpezarMonitoreo(Resource):

    def get(self):
        iniciar_hilo()

iniciar_hilo()
    
api = Api(app)
api.add_resource(VistaEmpezarMonitoreo, '/monitoreo')





