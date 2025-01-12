ECHO "Deployment started"

python3.13 -m venv env

source env/bin/activate

pip install -r requirements.txt

python manage.py collectstatic --noinput

ECHO "Deployment completed"