# Celery_beat

> **Need three cli to open** 

1) activate environment
2) one cli--> python manage.py runserver
3) two cli--> celery -A mysite worker -l INFO
4) three cli--> celery -A mysite beat -l INFO
