from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from APIs import create_app, db

app = create_app()   # replace this with your factory function for Flask application
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()