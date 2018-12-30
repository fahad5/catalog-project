import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'

	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	email = Column(String(250), nullable=False)
	picture = Column(String(250))

class Category(Base):
	__tablename__ = 'category'

	id = Column(Integer, primary_key = True)
	name = Column(String(80), nullable = False)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User, backref="category")

	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	    	'id': self.id,
	        'name': self.name,
	    }

class Books(Base):
	__tablename__ = 'books'

	name = Column(String(80), nullable = False)
	description = Column(String(2000))
	id = Column(Integer, primary_key = True)
	category_id = Column(Integer, ForeignKey('category.id'))
	category = relationship(Category, backref=backref('books', cascade='all, delete'))
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship(User, backref="books")

	@property
	def serialize(self):
	    """Return object data in easily serializeable format"""
	    return {
	        'category': self.category.name,
	        'description': self.description,
	        'name': self.name,
	    }

engine = create_engine('sqlite:///itemcatalog.db')
Base.metadata.create_all(engine)