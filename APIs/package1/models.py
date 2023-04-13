from APIs import db, login_manager


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
    