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
1. Install dependencies from [`requirements.txt`](./requirements.txt)
```
pip3 install -r requirements.txt
```
>You can also use [venv](https://docs.python.org/3/library/venv.html)  
2. (Optional) Configure [`config.py`](./config.py):  
2.1. Add secret string to `SECRET_KEY` variable for CSFR token (you can use any long string)  
2.2. You can change database directory (`SQLALCHEMY_DATABASE_URI`) or [DBMS](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/) there  
2.3. Maybe you want to hide this info - use [dotenv](https://pypi.org/project/python-dotenv/)
3. Run it
```
python3 main.py
```

## Project structure
```
-\
 |-- images                ## generated qr-codes
 |   \-- images            ## just file
 |
 |-- templates
 |   |-- 404.html          ## template for 404 error
 |   |-- allusers.html     ## table of users
 |   |-- error.html        ## layout of error
 |   |-- form.html         ## main form of app
 |   |-- layout.html       ## base layout of all templates
 |   |-- post.html         ## template for POST method
 |   \-- user.html         ## user page
 |
 |-- views                 ## web presentation
 |   |-- __init__.py
 |   |-- controllers.py    ## controllers logic
 |   \-- form.py           ## wtform file
 |
 |-- .gitattributes
 |-- .gitignore 
 |-- Flask MVC.pdf         ## slides about app
 |-- LICENSE
 |-- README.md
 |-- config.py             ## configuration file
 |-- main.py               ## main app file
 |-- model.py              ## model
 \-- requirements.txt      ## dependencies
```
