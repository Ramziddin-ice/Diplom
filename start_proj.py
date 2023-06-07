command = '/home/www/Diplom/demo/bin/gunicorn'
pythonpath = '/home/www/Diplom'
bind = '127.0.0.1:8000'
workers = 17
user = 'www'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=config.settings'
