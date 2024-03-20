# langchain

Este proyecto es un ejemplo de aplicación usando LangChain y Streamlit.
La aplicación permite cargar un archivo csv de hasta 200 mb y realizar preguntas
a un chatbot sobre este archivo.

## Proyecto

* `agent.py`: funciones relacionadas a llm y agentes con langchain.
*`app.py`: ejecuta la aplicación web.
*`webpage.py`: funciones relacionadas con la configuración de la aplicación web.

## Instalación

Este proyecto usa la versión de Python 3.9.5.

```
git clone https://github.com/nimatura/langchain.git
```

Crear un ambiente virtual y activarlo:

```
python3.9.5 -m venv venv
source venv/bin/activate  # para mac
venv\Scripts\activate     # para windows
```

Instalar las librerías necesarias:

```
pip install -r requirements.txt
```

También es necesario agregar la ruta base del proyecto al `PYTHONPATH`, para
esto podemos agregar al archivo `~/.bashrc`:

```
export PYTHONPATH="${PYTHONPATH}:/project/path"
```

## Ejecución

```
cd /project/path
python 3.9.5 src/app.py
```

**Nota**: para usar la aplicación es necesario tener una API Key de OpenAI. Si
no está en las variables de entorno (`OPENAI_API_KEY`), la aplicación web la
pedirá.
