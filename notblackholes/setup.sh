# Setup virtual environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Setup database schemas
python manage.py makemigrations
python manage.py migrate

# Create and load seed fixtures into database
python -m utilities.seed
python manage.py loaddata galaxy