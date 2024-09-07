from celery import Celery
from datetime import datetime

celery_app = Celery('task', broker='redis://localhost:6379/0')
#celery_app2 = Celery('task2', broker='redis://localhost:6379/0')

# celery_app.conf.update(
#     task_acks_on_failure_or_timeout=False,
#     task_ignore_result=True,
#     task_routes={
#         'monitor.enviar_mensaje.autenticacion',
#         'monitor.enviar_mensaje.usuarios',
#     }
# )

@celery_app.task(name="monitor.recibir_mensaje")
def responder_mensaje_monitor(message):
    pass

@celery_app.task(name='monitor.enviar_mensaje.usuarios')
def recibir_mensaje_monitor(mensaje):
    print("Mensaje de control recibido: Monitor->Usuarios")
    responder_mensaje()

def responder_mensaje():
    print("Envio respuesta: Autenticador->Monitor")
    args = ("Usuarios",)
    responder_mensaje_monitor.apply_async(args)

@celery_app.task(name='monitor.enviar_mensaje.autenticacion')
def recibir_mensaje_autenticador(mensaje):
    print()