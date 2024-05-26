# Fraude
Entrenamiento de modelo de predicción de fraude con una base de datos en un csv, el modelo y dependencias se entregan en un docker file. 

# API de Predicción de Modelos con FastAPI

Este repositorio contiene una aplicación FastAPI para predecir resultados utilizando un modelo de aprendizaje automático previamente entrenado. La aplicación está containerizada utilizando Docker para facilitar su despliegue.

## Requisitos

Antes de comenzar, asegúrate de tener Docker y Docker Compose instalados en tu máquina.

- [Instalación de Docker](https://docs.docker.com/get-docker/)
- [Instalación de Docker Compose](https://docs.docker.com/compose/install/)

## Instrucciones

Sigue estos pasos para configurar y ejecutar la aplicación FastAPI:

### 1. Clona el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/valeabrahaml/fraude.git
cd fraude

Abrir una terminal y asegurarse que se encuentre dentro de la carpeta, en la terminal correr estos comandos:
docker-compose build
docker-compose up

Para probar he creado un archivo:
python test_api.py

al correrlo en la terminal debe de salir la probabilidad de predicción, puede modificar el archivo para probar más valores con el modelo. 

