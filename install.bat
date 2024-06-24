pip install virtualenv
python -m virtualenv TUho_Env
call TUho_Env/Scripts/activate.bat
cd TUho
python -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py install