from flask import Flask
from flask_migrate import Migrate
from routes import blueprint
from models import db, create_admin_user, populate_post

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    with app.app_context():
        db.create_all()
        create_admin_user()
        populate_post()

    return app

app = create_app()

app.register_blueprint(blueprint)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=True)