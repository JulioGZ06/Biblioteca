
# Biblioteca Universitaria

## Descripción
Este proyecto consiste en crear un sitio web para una biblioteca universitaria utilizando Flask y Bootstrap. La página muestra información general, el catálogo, los servicios y los medios de contacto.

## Archivos del proyecto

### server.py
Es el archivo principal de la aplicación. Contiene las cuatro rutas de Flask: Inicio, Catálogo, Servicios y Contacto. Utiliza `render_template()` para mostrar las páginas y enviar las variables `titulo` y `mensaje`.

### layout.html
Es la plantilla base que contiene la estructura HTML, el título del documento, la referencia a Bootstrap y el menú de navegación. También incluye el bloque `content` donde aparece el contenido de las demás páginas.

### index.html
Es la página de inicio. Presenta el nombre de la biblioteca, un mensaje de bienvenida, una breve descripción y el horario de atención.

### catalogo.html
Muestra los materiales disponibles en la biblioteca: libros, revistas, tesis y recursos digitales, con una breve descripción de cada categoría.

### servicios.html
Presenta los servicios de la biblioteca, como el préstamo de libros, la consulta en sala, el acceso a recursos digitales y la orientación bibliográfica.

### contacto.html
Muestra los medios de contacto de la biblioteca, incluyendo la dirección, un correo electrónico institucional ficticio y el horario de atención.

### requirements.txt
Contiene las dependencias necesarias para ejecutar el proyecto.

## Elementos implementados
- Rutas de Flask para las cuatro páginas.
- Uso de `render_template()` para cargar las plantillas.
- Variables `titulo` y `mensaje`.
- Herencia de plantillas mediante `{% extends "layout.html" %}`.
- Bloques de contenido mediante `{% block content %}`.
- Menú de navegación con Bootstrap.
- Enlaces creados con `url_for()`.
- Organización del contenido con `container-fluid`.
