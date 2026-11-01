# Aplicación de informes · Práctica de EGC

Esta aplicación Python se ha utilizado hasta ahora de forma interna en una empresa ficticia. La empresa está estudiando **publicarla y compartirla con la comunidad**, pero todavía no ha decidido con qué licencia hacerlo.

El programa genera un informe muy sencillo a partir de varios componentes. Los componentes, sus autores y sus nombres son **ficticios y se han creado para esta práctica**.

## Estructura del proyecto

- `src/`: código de la aplicación.
- `tests/`: pruebas automáticas.
- `componentes/`: código y metadatos de las bibliotecas utilizadas.
- `wheelhouse/`: paquetes Python preparados para instalar las dependencias sin conexión.
- `requirements.lock`: versiones y hashes de las dependencias.
- `tools/`: una utilidad auxiliar para consultar un SBOM en formato SPDX JSON.

## Preparar y ejecutar (Linux / macOS)

Necesitas **Python 3.10 o posterior**, con `venv` y `pip`.

Desde la carpeta del proyecto:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --no-index --find-links=wheelhouse --require-hashes -r requirements.lock
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m src.app
```

## Preparar y ejecutar (Windows / PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --no-index --find-links=wheelhouse --require-hashes -r requirements.lock
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m src.app
```

No es necesario activar el entorno virtual ni instalar los componentes desde Internet. Para repetir la instalación desde cero, elimina `.venv` y vuelve a crearlo.

## Sobre las licencias

La aplicación principal **todavía no tiene una licencia de publicación elegida**. Las bibliotecas utilizadas tienen su propia documentación; su presencia en el proyecto no implica que todas puedan redistribuirse bajo cualquier licencia. La práctica consiste en investigar este aspecto y justificar una propuesta.
