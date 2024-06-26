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
>
git clone https://github.com/valeabrahaml/fraude.git
cd fraude

Abrir una terminal y asegurarse que se encuentre dentro de la carpeta, en la terminal correr estos comandos:

Primero: docker-compose build
segundo: docker-compose up

Para probar he creado un archivo, se puede correr en una nueva terminal:
python test_api.py

al correrlo en la terminal debe de salir la probabilidad de predicción, puede modificar el archivo para probar más valores con el modelo.


Al mismo tiempo, he añadido el codigo con el que se entreno el modelo, en caso de dudas acerca de como se hizo:
-Preproceso de datos: creación y eliminación de columnas
- Undersampling
- Encontrar hiperparametros con Optuna
- Entrenamiento del modelo con esos hiperparametros
- Evaluación del modelo
- Caso de negocio: Ganancia y perdida para encontrar el treshold ideal. 

