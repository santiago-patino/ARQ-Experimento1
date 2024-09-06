from celery import Celery
from datetime import datetime
#from ..monitoreo import services

celery_app = Celery('task', broker='redis://localhost:6379/0')

#Mensajes para enviar
@celery_app.task(name="monitor.enviar_mensaje.autenticacion")
def enviar_mensaje_autenticador(message):
    pass

#Mensajes para recibir
@celery_app.task(name='monitor.recibir_mensaje')
def recibir_mensaje(message):
    print("Respuesta microservicio: " + message)
    #cambiar_estado("Autenticacion")
    #if "Autenticacion" in message:
    #services.Autenticacion = True
    # else:

def enviar_mensajes():
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Mensaje de control enviado: Autenticador - "+date)
    args = ("Mensaje de control",)
    enviar_mensaje_autenticador.apply_async(args)