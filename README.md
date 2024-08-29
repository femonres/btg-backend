# BTG Pactual - Backend

Este es el backend del proyecto de BTG Pactual que permite a los clientes manejar sus fondos de inversión. El backend está desarrollado en Python utilizando FastAPI, DynamoDB como base de datos, y está diseñado para ser desplegado en AWS utilizando Serverless Framework y CloudFormation.

## Arquitectura del Proyecto

El proyecto sigue una **arquitectura hexagonal** (puertos y adaptadores) y está dividido en varias capas:

- **Dominio**: Contiene las entidades, agregados, servicios de dominio, repositorios, y excepciones. Esta capa es independiente de las demás y representa las reglas de negocio.

- **Aplicación**: Contiene los casos de uso y servicios que orquestan la lógica de negocio del dominio y se comunican con las demás capas.

- **Infraestructura**: Contiene la implementación de los repositorios, la configuración de la base de datos (DynamoDB), la integración con SNS para notificaciones, y las configuraciones necesarias para el despliegue.

- **Interfaces**: Contiene los controladores (routers) que exponen la API utilizando FastAPI. Aquí también se encuentran los schemas (DTOs) utilizados para la validación de datos.

## Requisitos

- Python 3.9+
- [pipenv](https://pipenv.pypa.io/en/latest/) para manejar dependencias.
- AWS CLI configurado si se desea desplegar en AWS.
- DynamoDB Local para pruebas locales (opcional).
- Node.js y npm (para Serverless Framework).

## Instalación y Configuración

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/femonres/btg-backend.git
    cd btg-backend
    ```

2. **Instalar dependencias**:
    ```bash
    pipenv install
    ```

3. **Crear las tablas en DynamoDB**:
    Se puede usar el archivo `dynamodb-tables.yaml` para crear las tablas en DynamoDB utilizando AWS CloudFormation.

    ```bash
    aws cloudformation create-stack --stack-name btg-pactual-backend --template-body file://dynamodb-tables.yaml
    ```

4. **Cargar datos iniciales**:
    Ejecuta el script para poblar las tablas `ClientTable` y `FundTable` en DynamoDB.

    ```bash
    pipenv run python migrations/populate_tables.py
    ```

## Ejecución de la Aplicación

### Ejecución Local

1. **Ejecutar DynamoDB Local** (si se desea ejecutar localmente):
    ```bash
    java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
    ```

2. **Ejecutar la aplicación**:
    ```bash
    pipenv run uvicorn src.main:app --reload

    ó

    pipenv run python src/main.py
    ```

    La API estará disponible en `http://127.0.0.1:8080`.

### Despliegue en AWS

1. **Deploy usando Serverless Framework**:
    ```bash
    serverless deploy
    ```

2. **Desplegar la infraestructura**:
    Puedes utilizar el archivo `cloudformation.yaml` para desplegar la infraestructura utilizando CloudFormation.

    ```bash
    aws cloudformation deploy --template-file cloudformation.yaml --stack-name btg-pactual-backend
    ```

## Ejecución de Pruebas y Cobertura

1. **Ejecutar pruebas**:
    ```bash
    pipenv run pytest
    ```

2. **Obtener reporte de cobertura**:
    ```bash
    pipenv run pytest --cov=src
    ```

    Esto generará un reporte de cobertura que mostrará qué partes del código están cubiertas por las pruebas.

3. **Ver el reporte en HTML**:
    ```bash
    pipenv run pytest --cov=src --cov-report=html --cov-report=term-missing
    ```

    El reporte en HTML estará disponible en `htmlcov/index.html`.

## Estructura del Proyecto

```plaintext
btg-pactual-backend/
├── src/
│   ├── domain/
│   │   ├── entities/
│   │   ├── value_objects/
│   │   ├── repositories/
│   ├── application/
│   │   ├── use_cases/
│   │   └── services/
│   ├── infrastructure/
│   │   ├── persistence/
│   │   ├── messaging/
│   └── interfaces/
│       ├── routers/
│       └── schemas/
├── tests/
│   ├── unit/
│   └── integration/
├── dynamodb-tables.yaml
├── cloudformation.yaml
├── serverless.yml
└── README.md
