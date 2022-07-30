# flask-simple-mvc

## About

Implementation of [this](https://github.com/bee-joo/mvc-vanilla-python) app using Flask  
  
Summary:
* SQLAlchemy as ORM
* SQLite as database
* Blueprint to hide controller logic from main.py
* Jinja2 as template engine
* WTForms for making, validating and data processing
* pyqrcode for QR-code generation

The goal was to show as many Flask concepts and libraries as possible in a small application
  
P.S. [Slides (rus lang)](https://github.com/bee-joo/flask-simple-mvc/blob/main/Flask%20MVC.pdf)

## Setup
0. Clone repository
```
git clone https://github.com/bee-joo/flask-simple-mvc
```
1. Install dependencies from [`requirements.txt`](./requirments.txt)
```
pip3 install -r requirements.txt
```
>You can also use [venv](https://docs.python.org/3/library/venv.html)  
2. (Optional) Configure [`config.py`](./config.py):  
2.1. Add secret string to `SECRET_KEY` variable for CSFR token (you can use any long string)  
2.2. You can change database directory (`SQLALCHEMY_DATABASE_URI`) or [DBMS](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) there  
3. Run it
```
python3 main.py
```
