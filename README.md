# worktion-api
API encargada de proveer servicios a los clientes de Worktion

## Configuración del entorno virtual

### Instalación de dependencias

Instalar **Pipenv**, este se encarga de administrar las dependencias y crear un ambiente virtual:

Para sistemas Linux, Ubuntu

```bash
pip install pipenv
```

Para sistemas UNIX, MacOS

```bash
brew install pipenv
```

Crear el entorno de desarrollo:

```bash
pipenv install
```

> Se crearan dos archivos, Pipfile y Pipfile.lock

Entrar en el entorno virtual 

```bash
pipenv shell
```

Instalar una nueva dependencia con pipenv:

```bash
pipenv install nuevadependencia
```

Actualizar el archivo requirements.txt con una nueva dependencia instalada:

```bash
pipenv lock -r > ./app/requirements.txt
```

## Levantar entorno de desarrollo

### Requerimientos

1. Tener instalado Docker
2. Tener instalado Docker Compose

### Procedimiento

En el directorio raíz del proyecto construir los contenedores

```bash
docker-compose build
```

Levantar los contenedores en segundo plano

```bash
docker-compose up -d
```

> Revisar si existen errores en el compose con: docker-compose logs -f

Parar y remover los contenedores

```bash
docker-compose down
```


