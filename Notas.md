
# Establecer variable de entorno windows
set FLASK_APP=app.py
set FLASK_ENV=development

# Correr flask
flask run 

# Levantar flask con app + debug
flask --app app.py --debug run
