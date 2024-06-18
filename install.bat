pip install virtualenv
python -m virtualenv TUho_Env
call TUho_Env/Scripts/activate.bat
python -m pip install -r requirements.txt
cd TUho
python manage.py makemigrations
python manage.py migrate
python manage.py install