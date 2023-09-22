#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
import models
from sqlalchemy import Column, Integer, String, DateTime, Foreignkey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan', backref='state')

    @property
    def cities(self):
        """
        Returns list of City instances with state_id equals to the current State.id
        """
        from models import storage
        my_list = []
        tmp_dict = storage.all(City)
        for city in tmp_dict.values():
            if self.id == city.state_id:
                my_list.append(city)
        return my_list
