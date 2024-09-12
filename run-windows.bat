cd ".\autostrade"

IF NOT EXIST ".venv" (
    python -m venv ".venv"
) 

call ".venv\Scripts\activate.bat"
pip install -r requirements.txt
python manage.py runserver

cd ..
pause