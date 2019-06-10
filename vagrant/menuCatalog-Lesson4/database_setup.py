import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
Base = declarative_base()
# Declarative_base() will let SQLAlchemy know that our classes are special SQLAlchemy classes that correspond to tables in our database.

class Restaurant(Base):

    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MenuItem(Base):

    __tablename__ = 'menu_item'
    # "__tablename__" lets SQLAlchemy know the name we'll use for the table.

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)
    # Tells SQLAlchemy the type of relationship one table has to another.
    # "nullable" is an attribute. If set to False indicates a column must have a 
    # value in order for the row to be created.
    # "primary_key=True" indicates a value we can use to identify

    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course
        }

##### insert at end of file #####
engine = create_engine(
'sqlite:///restaurantmenu.db'
)
# create_engine() will create a new file that we can use, similarly to a more robust database like MySQL or PostgreSQL

Base.metadata.create_all(engine)
# Goes into the database and takes the classes we will soon make to create tables in our database.
