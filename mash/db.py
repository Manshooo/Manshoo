from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:325s5zqQJml;@localhost/mash'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))

post_tags = db.Table('post_tags',
    db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
)
class Post(db.Model):
    """Table of posts"""

    __tablename__ = "posts"
    id = db.Column(db.Integer(), unique=True, primary_key=True)
    title = db.Column(db.String(255), nullable=False,)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    category_id = db.Column(db.Integer(), db.ForeignKey('categories.id'))

class Category(db.Model):
    """Table of categories"""

    __tablename__ = "categories"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on  =  db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Post', backref='category')

class  Tag(db.Model):
    """Table of tags"""

    __tablename__ = 'tags'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_on  =  db.Column(db.DateTime(), default=datetime.utcnow)
    posts = db.relationship('Post', secondary=post_tags, backref='tags')