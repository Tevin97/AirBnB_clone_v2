#!/usr/bin/python3
"""A new dbstorage engine"""
from os import getenv
from models.base_model import Base
from sqlalchemy import create_engine
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


class DBStorage():
    """A dbstorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes and links the engine to the db"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                        getenv("HBNB_MYSQL_USER"),
                                        getenv("HBNB_MYSQL_PWD"),
                                        getenv("HBNB_MYSQL_HOST"),
                                        getenv("HBNB_MYSQL_DB")
                                        ), pool_pre_ping=True)
        if getenv("HBNB_ENV") == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session all objects of the class name
        """
        all_classes = (User, State, City, Amenity, Place, Review)
        tmp_dict = {}
        instance = []
        if cls is None:
            for classs in all_classes:
                instance.extend(self.__session.query(classs).all())
        else:
            instance.extend(self.__session.query(cls).all())

        for obj in instance:
            keyy = "{}.{}".format(obj.__class.__name, obj.id)
            tmp_dict[keyy] = obj

        return tmp_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)

        my_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        new_session = scoped_session(my_session)
        self.__session = new_session()

    def close(self):
        """Close the session"""
        self.__session.close()
