#!/bin/bash
source /home/www/Diplom/demo/bin/activate
source /home/www/Diplom/demo/bin/postactivate
exec gunicorn  -c "/home/www/Diplom/start_proj.py" config.wsgi:application --reload
