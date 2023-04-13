from APIs import db, login_manager
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user


class User(db.Model, UserMixin):
    __tablename__ = "sf_user_table1"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.is_active = True

    def __repr__(self):
        return '<User %r>' % self.name
    
    def is_active(self):
        return True
    

    

class TableA(db.Model):
    __tablename__ = "table_a"
    id = db.Column(db.Integer, primary_key=True)
    nameA = db.Column(db.String(80))
    B = db.Column(db.String(80))
    C = db.Column(db.String(80))
    D = db.Column(db.String(80))
    E = db.Column(db.String(80))
    F = db.Column(db.String(80))
    
    
    
class TableB(db.Model):
    __tablename__ = "table_b"
    id = db.Column(db.Integer, primary_key=True)
    A = db.Column(db.String(80))
    B = db.Column(db.String(80))
    C = db.Column(db.String(80))
    D = db.Column(db.String(80))
    E = db.Column(db.String(80))
    F = db.Column(db.String(80))
    
    
    
    
class TableC(db.Model):
    __tablename__ = "table_c"
    id = db.Column(db.Integer, primary_key=True)
    A = db.Column(db.String(80))
    B = db.Column(db.String(80))
    C = db.Column(db.String(80))
    D = db.Column(db.String(80))
    E = db.Column(db.String(80))
    F = db.Column(db.String(80))
    
    
class TableD(db.Model):
    __tablename__ = "table_d"
    id = db.Column(db.Integer, primary_key=True)
    A = db.Column(db.String(80))
    B = db.Column(db.String(80))
    C = db.Column(db.String(80))
    D = db.Column(db.String(80))
    E = db.Column(db.String(80))
    F = db.Column(db.String(80))
    
    
    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))