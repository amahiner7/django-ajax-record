from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES_SETTING = \
    {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# DATABASES_SETTING = \
#     {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'NAME': 'django-ajax-record',
#             'USER': 'dev',
#             'PASSWORD': 'klb7#I0Ofl3FA%uLtcDF@JNvdl!xQ2mk',
#             'HOST': 'siliconcube.asuscomm.com',
#             'PORT': '3306',
#         }
#     }
