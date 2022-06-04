import os, sys

def migrate() : 
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
	from django.core.management import execute_from_command_line
	execute_from_command_line(["python3" "main.py" , "makemigrations", "ModelsLab"])
	execute_from_command_line(["python3" "main.py" , "migrate", "ModelsLab"])
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
	from django.core.wsgi import get_wsgi_application
	application = get_wsgi_application()
