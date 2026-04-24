# Repo para EIEC - DevOps - UNIR

Este repositorio nos servirá para demostrar el uso de Git en la asignatura de EIEC y muchas cosas mas.

---

Los comandos del Makefile funcionarán en Linux y MacOS. En caso de usar Windows, necesitarás adaptarlos o ejecutarlos en una máquina virtual Linux.

## Ejecución

python3 main.py <filename> <dup>
  filename: **ruta** al fichero que contiene la lista de palabras, una por línea
  dup: **yes|no**, yes para eliminar palabras duplicadas, no para mantener la lista

## Ejecución de prueba

```bash
python3 main.py prueba.txt yes
```

Salida esperada (si no existe prueba.txt):

```text
Se leerán las palabras del fichero prueba.txt
El fichero prueba.txt no existe
['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
```

En caso contrario, se mostrarán las del fichero.

## Ejecución de prueba con Docker

```bash
docker run --rm --volume `pwd`:/opt/app --env PYTHON_PATH=/opt/app -w /opt/app python:3.6-slim python3 main.py words.txt yes
```

Salida esperada:

```text
Se leerán las palabras del fichero words.txt
El fichero words.txt no existe
['gryffindor', 'hufflepuff', 'ravenclaw', 'slytherin']
```
