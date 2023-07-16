from blog import db, login_manager
from datetime import datetime     # Using it on the date posted
from flask_login import UserMixin  # To access sessions of the user

# To know if it is a registered user, To manage sessions

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))

# Creation of Models
class User(db.Model, UserMixin):                 # Preventing Overiding, inheriting from the user mixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Integer, primary_key=True)
    image_file = db.Column(db.String(20), nullable=False, default='data:image/jpeg;base64,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')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


