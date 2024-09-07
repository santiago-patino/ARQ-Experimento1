from celery import Celery
from datetime import datetime
import time
import redis
from datetime import datetime

celery_app = Celery('task', broker='redis://localhost:6379/0')
#celery_app2 = Celery('task2', broker='redis://localhost:6379/0')

celery_app.conf.update(
    task_acks_on_failure_or_timeout=False,
    task_ignore_result=True,
)

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

services = {
    "Autenticacion": {
        "enviado": 0,
        "respondido": 0,
        "hora_enviado": "",
        "hora_recibido": ""
    },
    # "Usuarios": {
    #     "enviado": 0,
    #     "respondido": 0,
    #     "hora_enviado": "",
    #     "hora_recibido": ""
    # },
}

# Guardar los estados iniciales de cada servicio en Redis
for service_name, service_data in services.items():
    service_data_converted = {
        "enviado": service_data["enviado"],
        "respondido": service_data["respondido"],
        "hora_enviado": service_data["hora_enviado"],
        "hora_recibido": service_data["hora_recibido"]
    }
    r.hset(service_name, mapping=service_data_converted)

#Mensajes para enviar
@celery_app.task(name="monitor.enviar_mensaje.autenticacion")
def enviar_mensaje_autenticador(message):
    pass

@celery_app.task(name="monitor.enviar_mensaje.usuarios")
def enviar_mensaje_usuarios(message):
    pass

#Mensajes para recibir
@celery_app.task(name='monitor.recibir_mensaje')
def recibir_mensaje(service):
    print("Respuesta microservicio: " + service)
    r.hset(service, "respondido", 1)
    r.hset(service, "hora_recibido", datetime.now().strftime("%H:%M:%S"))

def restablecer_estado():
    for servicio, estado in services.items():
        r.hset(servicio, "enviado", 0)
        r.hset(servicio, "respondido", 0)
        r.hset(servicio, "hora_enviado", "")
        r.hset(servicio, "hora_recibido", "")

def enviar_mensajes():
    restablecer_estado()
    args = ("Mensaje de control",)
    
    for servicio_nombre, servicio_data in services.items():
       if servicio_nombre == "Autenticacion":
           enviar_mensaje_autenticador.apply_async(args)
       elif servicio_nombre == "Usuarios":
           print()
           enviar_mensaje_usuarios.apply_async(args)
       else:
           return
        
       r.hset(servicio_nombre, "enviado", 1)
       r.hset(servicio_nombre, "hora_enviado", datetime.now().strftime("%H:%M:%S"))

    time.sleep(1)
    validar_respuesta()


def validar_respuesta():
    imprimir_estado()
    for servicio_nombre, servicio_data in services.items():
        if r.hgetall(servicio_nombre).get("respondido") == "0":
            mostrar_notificacion(servicio_nombre + " no responde!")

def imprimir_estado():
    # Imprimir encabezado
    print("\n")
    print(f"{'Servicio':<20} {'Enviado':<10} {'Respondido':<12} {'Hora enviado':<14} {'Hora recibido':<10}")
    print("-" * 75)

    # Obtener todos los servicios de Redis
    servicios = r.keys('*')  # Obtiene todas las claves en Redis

    # Imprimir el estado de cada servicio
    for servicio in servicios:
        tipo = r.type(servicio)
        if tipo == 'hash':
            estado = r.hgetall(servicio)  # Obtiene todos los campos y valores del hash
            enviado = estado.get('enviado', 'N/A')
            respondido = estado.get('respondido', 'N/A')
            hora_enviado = estado.get('hora_enviado', 'N/A')
            hora_recibido = estado.get('hora_recibido', 'N/A')

            # Traducir 1/0 a sí/no
            enviado = 'sí' if enviado == '1' else 'no'
            respondido = 'sí' if respondido == '1' else 'no'

            print(f"{servicio:<20} {enviado:<10} {respondido:<12} {hora_enviado:<14} {hora_recibido:<10}")

def mostrar_notificacion(mensaje):
    # Crear una línea de borde
    borde = '*' * (len(mensaje) + 4)
    
    # Mostrar notificación
    print()
    print(borde)
    print(f"* {mensaje} *")
    print(borde)
    print()


