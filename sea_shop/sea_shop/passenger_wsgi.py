import os, sys
from django.core.wsgi import get_wsgi_application
from config import BEGET_DIR_ROOT

site_user_root_dir = BEGET_DIR_ROOT
sys.path.insert(0, os.path.join(site_user_root_dir, 'sea_shop'))
sys.path.insert(1, os.path.join(site_user_root_dir, 'venv/lib/python3.6/site-packages'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sea_shop.settings')

application = get_wsgi_application()
