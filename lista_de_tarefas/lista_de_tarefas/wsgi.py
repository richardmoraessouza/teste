
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lista_de_tarefas.settings')
application = get_wsgi_application()
