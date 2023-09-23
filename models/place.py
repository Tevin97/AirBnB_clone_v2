#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer
from sqlalchemy import primary_key, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


place_amenity = Table(
        'place_amenity', Base.metadata,
        Column('place_id', String(60), ForeignKey('places.id'),
                primary_key=True, nullable=False),
        Column('amenity_id', String(60), ForeignKey('amenities.id'),
                primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
                'Review', cascade='all, delete-orphan', backref='place')
        amenities = relationship(
                'Amenity', secondary='place_amenity', viewonly=False)

    else:
        from models import storage

        @property
        def reviews(self):
            """
            returns the list of Review instances with place_id equals
            to the current Place.id
            """
            objs = []
            instances = storage.all("Review")
            for value in instances.values():
                if value.place_id == Place.id:
                    objs.append(value)
            return objs

        @property
        def amenities(self):
            """
            Returns the list of Amenity instances based on the attribute
            amenity_ids
            """
            objs = []
            instances = storage.all("Amenity")
            for value in instances.values():
                if value.id in self.amenity_ids:
                    objs.append(value)
            return objs

        @amenities.setter
        def amenities(self, obj):
            """
            Adds an Amenity.id to the attribute amenity_ids list
            """
            from models.amenity import Amenity
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)
