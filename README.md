XBTrack
=======

Aplicación para el 1º Xackatón, rutas y puntos clave de ciclismo urbano.

## Setup Inicial

Todos estos pasos se realizan en la consola, cualquier duda: @categulario en twitter o a.wonderful.code@gmail.com
Tratar de seguir este procedimiento en windows podría ser un dolor en el trasero... y en la cabeza... y en todas partes

* instalar python, python-virualenv y git de ser necesario
* Crear un entorno virtual `virtualenv --distribute --system-site-packages EntornoBicitacora`
* Entrar en el entorno `cd EntornoBicitacora`
* Activar el entorno `source bin/activate`
* Clonar el proyecto `git clone https://github.com/developingo/Bicitacora.git`
* Entrar al repositorio `cd Bicitacora`
* Instalar las dependencias `pip install -r requirements_weak.txt`
* Instalar la base de datos `./manage_dev.py syncdb --all`
* Correr las migraciones `./manage_dev.py migrate --fake`

## Desarrollar

4 sencillos pasos

*