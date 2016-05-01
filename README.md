# bond\_street\_sample
Code sample for Bond Street.

## Setup

````bash
pip install -r requirements/local.txt
cd sample_app
export DJANGO_SETTINGS_MODULE="sample_app.settings.local"
# use sample_app.settings.base to turn off DEBUG mode
python manage.py migrate
python manage.py loaddata steps
python manage.py createsuperuser
python manage.py runserver
````

This will host the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

