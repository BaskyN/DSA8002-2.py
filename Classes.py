
import sqlite3
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///listings.db', echo=True)
Base = declarative_base(engine)
print(engine.table_names())


conn.commit()
c.fetchall()


class DBObject(object):
    conn = sqlite3.connect("listings.db")
    c = conn.cursor()

class Listing(DBObject):
    def _init_(self, id):
        self.id = id
        self.host_id = host_id
    @classmethod
    def get(cls, id: int = None) -> 'Listing':
        ret = c.execute(f"select * from listings where id = '{id}'")
        res = ret.fetchone()
        if not res:
            raise Exception(f"object with id {id} not found")
        return Listing(res [id],res[ host_id])


    def _str_(self) -> str:
        return json.dumps(self._dict_)

l = Listing.get(31114726)
print(f"{l}")
print("hello")






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



