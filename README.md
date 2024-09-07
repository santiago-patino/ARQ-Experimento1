# Proyecto: Experimento 1

## Descripción

Una breve descripción del proyecto:  
Explica de manera concisa qué hace el proyecto y cuál es su propósito.

## Requisitos

Ya que se utiliza Redis solo es posible ejecutarlo en equipos con sistema operativo UNIX

Antes de empezar, asegúrate de tener instalados los siguientes requisitos:

- **Python 3.x**: Si no lo tienes instalado, puedes descargarlo desde la [página oficial de Python](https://www.python.org/downloads/).

  - Para **Linux** (Ubuntu/Debian):
    ```bash
    sudo apt update
    sudo apt install python3
    ```

  - Para **macOS** (con Homebrew):
    ```bash
    brew install python
    ```

- **Entorno Virtual**: Es recomendable crear un entorno virtual para aislar las dependencias del proyecto.

  - En **Linux/macOS**:
    ```bash
    source venv/bin/activate
    ```

- **Celery**: Para manejar tareas asincrónicas, debes instalar Celery.

  - Instalar **Celery** con pip:
    ```bash
    pip install celery
    ```
- **Redis** como broker:
    - Para **Ubuntu**:
      ```bash
      sudo apt install redis-server
      ```
    - Para **macOS** (con Homebrew):
      ```bash
      brew install redis
      ```

## Instalación

### Paso 1: Clonar el repositorio

```bash
git clone https://github.com/santiago-patino/ARQ-Experimento1.git
cd ARQ-Experimento1
```

### Paso 2: Instalar dependencias

**Instalar dependencias**: Se deben instalar las dependencias encontradas en requirements.txt.

  - En **Linux/macOS**:
    ```bash
    pip install -r requirements.txt
    ```


pip install celery // instalar celery
pip install redis // instalar redis

redis-server // iniciar redis server

celery -A tareas worker -l info // activar worker

flask run -p 5001 // Arrancar flask
