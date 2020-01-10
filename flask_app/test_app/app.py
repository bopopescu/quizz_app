from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security


app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = "super_mega_strong_secret_key"

SECRET_KEY='very_powerful_secretkey'
app.config['SECRET_KEY']



db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


### Admin ###
from models import *
admin = Admin(app)
admin.add_view(ModelView(Quizz, db.session))
admin.add_view(ModelView(User, db.session))

### Flask_security ###
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
