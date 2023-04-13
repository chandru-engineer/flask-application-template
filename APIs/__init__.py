import logging
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from APIs.config import Config
from APIs.log_config import formatter, handler
from flask_admin import Admin
from flask_login import LoginManager
from flask_admin.menu import MenuLink


# creating class instance
app = Flask(__name__, template_folder='templates')


login_manager = LoginManager()
db = SQLAlchemy()
ma = Marshmallow()


# setup the logging congiguration
app.logger.addHandler(handler)
# avoid the http message print in termainal
app.logger.setLevel(logging.INFO) 
handler.setFormatter(formatter)
# prevent the Flask logger from propagating log messages to the root logger
app.logger.propagate = False

# configure admin panel
admin = Admin(app, name='Control', template_mode='bootstrap3')

def create_app(config_class=Config):
    
    global db, ma
    app.config.from_object(Config)
    
    db.init_app(app)
    ma.init_app(app)
    
    login_manager.init_app(app)
    login_manager.login_view = 'login'
    
    from APIs.package1.viewsets import package_main
    app.register_blueprint(package_main)
    
    from APIs.MMUser.viewsets.urls import auth_main
    app.register_blueprint(auth_main)
    
    from APIs.SampleRoutes.viewsets.urls import sample_routes
    app.register_blueprint(sample_routes)
    
    from APIs.admin_view.viewsets.urls import admin_panel_new
    app.register_blueprint(admin_panel_new)
    
    # to add the logout button in Admin panel. 
    admin.add_link(MenuLink(name='Logout', url='/logout'))
    
    # add models in admin panel 
    from APIs.MMUser.model.user_model import User, TableA, TableB, TableC, TableD
    from APIs.admin_view.schema.modelViewSchema import CustomModelView
    
    admin.add_view(CustomModelView(User, db.session))
    admin.add_view(CustomModelView(TableA, db.session))
    admin.add_view(CustomModelView(TableB, db.session))
    admin.add_view(CustomModelView(TableC, db.session))
    admin.add_view(CustomModelView(TableD, db.session))
    
    return app
    
    
    

    