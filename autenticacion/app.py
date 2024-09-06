from monitor import create_app
from flask_restful import Resource, Api
from flask import Flask
import json
from celery import Celery

#celery_app = Celery('task', broker='redis://localhost:6379/0')

app = create_app('default')
app_context = app.app_context()
app_context.push()

api = Api(app)

# @celery_app.task(name="tabla.registrar")
# def registrar_puntaje(cancion_json):
#     pass

# def enviar_mensajes():
#     args = ("Mensaje de control",)
#     registrar_puntaje.apply_async(args)