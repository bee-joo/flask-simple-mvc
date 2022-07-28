from flask import Flask
from views.controllers import controller

from model import db


app = Flask(__name__)
app.register_blueprint(controller)
app.config.from_pyfile('./config.py')

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
