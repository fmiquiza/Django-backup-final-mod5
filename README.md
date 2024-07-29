==========================
**Proyecto Final Mod5**

Author: Fernando Miguel Iquiza Ramirez
CI: 3519535

==========================
**Objetivo:**
Demostrar los conocimientos adquiridos en la creación de un proyecto en
Django.

**Requisitos:**
- Cree un Proyecto en Django con al menos una Aplicación
- Su Aplicación debe tener al menos 4 Models (Modelos o Tablas)
- Sus Models deben contener al menos 2 validaciones personalizadas
- Su Administrador de Django debe tener al menos 2 Models registrados
- Utilice Django Rest Framework para crear al menos 3 ModelViewSet o
GenericAPIView
- Utilice Django Rest Framework para crear al menos 1 Custom API
- Debe incluir el archivo requirements.txt en la raíz del repositorio

===========================
**Instalación:**

1. Clonar el repositorio
   git clone https://github.com/fmiquiza/Django-backup-final-mod5.git
2. Instalar las dependencias
   virtualenv env
    source venv/bin/activate
    pip3 install Django
    django-admin start calendarapp
3. Levantar el servidor
   Python3 manage.py migrate
   python3 manage.py createsuperuser
   Python3 manage.py runserver

TROUBBLESHOOTING
- Si no se encuentra el archivo requirements.txt, ejecutar pip3 freeze > requirements.txt

Si existiera algún error de dependencias/paquetes, instalarlos manualmente:

pip install djangorestframework
pip install djangorestframework-oauth
pip install dj_rest_auth
pip install drf-yasg
pip install djangorestframework-simplejwt

python3 -m pip install --upgrade pip setuptools


