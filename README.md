# AySA / consola Interactiva (v2019.12.1)

Consola interactiva para el despliegue de contenedores (Prototipo).

> **WARNING!**
> Está pensado para implementar en capas de desarrollo, no para uso productivo.

## Instalación

Se requiere la versión de `python` **>=3.6**, en adelante.

### Con entorno virtual

```bash
# creamos el entorno virtual
> virtualenv --python=python37 interactive-console

# ingresamos al directorio del entorno
> cd interactive-console

# iniciamos el entorno
> source ./bin/activate

# instalamos dentro del entorno
> pip install https://github.com/aysa-sa/interactive-console/archive/2019.12.1.zip
```

### Sin entorno virtual

```bash
# Instalar
> pip install https://github.com/aysa-sa/interactive-console/archive/2019.12.1.zip

# Actualizar
> pip install https://github.com/aysa-sa/interactive-console/archive/2019.12.1.zip --upgrade
```

### Desde el código fuente

```bash
# clonamos el repositorio
> git clone https://github.com/aysa-sa/interactive-console.git --branch 2019.12.1 --single-branch

# ingresamos al directorio del repositorio
> cd interactive-console

# instalamos
> python setup.py install
```

# Desarrollo

## Repositorio

```bash
# clonación
> git clone https://github.com/aysa-sa/interactive-console.git

# acceso al proyecto
> cd interactive-console
```

## Dependencias

Las dependencias se encuentran definidas en el archivo `Pipfile`, para la gestión de las mismas es requerido tener instalado `pipenv`, visitar [**site**](https://pipenv.readthedocs.io/).

### Pipenv

* Documentación: [**usage**](https://pipenv.readthedocs.io/en/latest/#pipenv-usage).
* Instalación: `pip install pipenv`.

#### Instalación de las dependencias:

```bash
> pipenv install
```

#### Iniciar el Shell:

```bash
> pipenv shell
```

#### Crear el archivo `requirements.txt`

```bash
> pipenv lock --requirements > requirements.txt
```
