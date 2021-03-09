import json

from sqlalchemy import create_engine, inspect, Column, Integer, String
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///listings.db', echo=True)
Base = declarative_base(engine)


def loadSession():
    metadata = Base.metadata
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


class Airbnb(Base):
    __tablename__ = 'airbnb'
    # __table_args__ = {'autoload': True}
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer)
    location_id = Column(Integer)
    name = Column(String)
    latitude = Column(String)
    longitude = Column(String)
    room_type = Column(String)
    price = Column(Integer)
    minimum_nights = Column(Integer)
    number_of_reviews = Column(Integer)
    last_review = Column(Integer)
    reviews_per_month = Column(Integer)
    availability_365 = Column(Integer)

    def __repr__(self):
        return f"\n* Host ID * = {self.host_id}\nListing Name = {self.name}\nLatitude = {self.latitude}\nLongitude = {self.longitude}\n" \
               f"Room Type = {self.room_type}\nPrice = {self.price}\nMinimum Nights = {self.minimum_nights}\n" \
               f"Number of Reviews = {self.number_of_reviews}\nLast Review = {self.last_review}\n" \
               f"Reviews Per Month = {self.reviews_per_month}\nAnnual Availability = {self.availability_365}" \
               f"\n_________________"


session = loadSession()
test = session.query(Airbnb).first()
print(test)


class Hosts(Base):
    __tablename__ = 'hosts'
    # __table_args__ = {'autoload': True}

    host_id = Column(Integer, primary_key=True)
    host_name = Column(String)
    calculated_host_listings_count = Column(String)

    def __repr__(self):
        return f"\n* Host ID * = {self.host_id}\nHost Name = {self.host_name}\nListing Count = {self.calculated_host_listings_count}" \
               f"\n_________________"


session = loadSession()
test = session.query(Hosts).first()
print(test)


class Locations(Base):
    __tablename__ = 'locations'
    # __table_args__ = {'autoload': True}

    location_id = Column(Integer, primary_key=True)
    neighbourhood = Column(String)
    neighbourhood_group = Column(String)

    def __repr__(self):
        return f"\n* Location ID * = {self.location_id}\nNeighbourhood = {self.neighbourhood}\n" \
               f"Neighbourhood Group = {self.neighbourhood_group}" \
               f"\n_________________"


session = loadSession()
test = session.query(Locations).first()
print(test)

new_listing = Airbnb()
new_listing.name = "New Listing Test - Add to database"
new_listing.latitude = 00000000
new_listing.longitude = 00000000
new_listing.room_type = 'Private Room'
new_listing.price = 00
new_listing.minimum_nights = 00
new_listing.number_of_reviews = 00
new_listing.last_review = 00
new_listing.reviews_per_month = 00
new_listing.availability_365 = 00
session.add(new_listing)

session.commit()

















session.close()

