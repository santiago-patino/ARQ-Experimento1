from celery import Celery
from datetime import datetime

celery_app = Celery('task', broker='redis://localhost:6379/0')

@celery_app.task(name="monitor.recibir_mensaje")
def responder_mensaje_monitor(message):
    pass

@celery_app.task(name='monitor.enviar_mensaje.autenticacion')
def recibir_mensaje_monitor(mensaje):
    print("Mensaje de control recibido: Monitor->Autenticador")
    responder_mensaje()

def responder_mensaje():
    print("Envio respuesta: Autenticador->Monitor")
    args = ("Autenticador",)
    responder_mensaje_monitor.apply_async(args)