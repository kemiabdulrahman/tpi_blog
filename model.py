from flask_sqlalchemy import SQLAlchemy

app.config['SQALCHEMY_DATABASE_URI'] = 'postgresql://drsims:folarin1090@127.0.0.1/tpi_db'

app.config[SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLALCHEMY(app)

Class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    posts = db.relationship('Posts', backref='author', lazy=True)


    def __repr__(self):
        return f"(User {self.id}, {self.username}, {self.email})"

Class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return f"(Posts {self.id}, {self.user_id}, {self.title}, {self.content})"



