from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///listings.db', echo=True)
Base = declarative_base(engine)
print(engine.table_names())


class Airbnb(Base):
    __tablename__ = 'airbnb'
    __table_args__ = {'autoload': True}

    def __init__(self, name, host_name, neighbourhood_group, neighbourhood, latitude, longitude, room_type, price,
                 minimum_nights, number_of_reviews, last_review, reviews_per_month, availability_365):
        self.name = name
        self.host_name = host_name
        self.neighbourhood_group = neighbourhood_group
        self.neighbourhood = neighbourhood
        self.latitude = latitude
        self.longitude = longitude
        self.room_type = room_type
        self.price = price
        self.minimum_nights = minimum_nights
        self.number_of_reviews = number_of_reviews
        self.last_review = last_review
        self.reviews_per_month = reviews_per_month
        self.availability_365 = availability_365


def loadSession():
    metadata = Base.metadata
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


if __name__ == "__main__":
    session = loadSession()
    results = session.query(Airbnb).all()


class Hosts(Base):
    __tablename__ = 'hosts'
    __table_args__ = {'autoload': True}

    def __init__(self, host_id, host_name, calculated_host_listings_count):
        self.host_id = host_id
        self.host_name = host_name
        self.calculated_host_listings_count = calculated_host_listings_count


def loadSession():
    metadata = Base.metadata
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


if __name__ == "__main__":
    session = loadSession()
    results = session.query(Hosts).all()


class Locations(Base):
    __tablename__ = 'locations'
    __table_args__ = {'autoload': True}

    def __init__(self, location_id, neighbourhood, neighbourhood_group):
        self.location_id = location_id
        self.neighbourhood = neighbourhood
        self.neighbourhood_group = neighbourhood_group


def loadSession():
    metadata = Base.metadata
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    return session


if __name__ == "__main__":
    session = loadSession()
    results = session.query(Locations).all()


