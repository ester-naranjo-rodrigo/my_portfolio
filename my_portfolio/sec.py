from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True
SECRET_KEY = 'kre4e)=9b&g1#7crihf+0c6^5-8nct+!ahj-bi*f+i6$n($h(q'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}