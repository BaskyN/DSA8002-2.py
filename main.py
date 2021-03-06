import sqlite3

import pandas as pandas
import pandas as pd

# here is a fake change you can review

conn = sqlite3.connect("listings.db")
c = conn.cursor()

listings = pd.read_csv('Singapore_Airbnb_Data.csv')
listings.to_sql('listings', conn, if_exists='append', index=False)


c.executescript('''

DROP TABLE IF EXISTS airbnb;
DROP TABLE IF EXISTS hosts;
DROP TABLE IF EXISTS locations;

CREATE TABLE IF NOT EXISTS airbnb
    (
    id INTEGER PRIMARY KEY,
    host_id INTEGER,
    location_id INTEGER,
    name TEXT,
    latitude TEXT,
    longitude TEXT,
    room_type TEXT,
    price INTEGER,
    minimum_nights INTEGER,
    number_of_reviews INTEGER,
    last_review INTEGER,
    reviews_per_month INTEGER,
    availability_365 INTEGER
    );

CREATE TABLE IF NOT EXISTS hosts
    (
    host_id INTEGER NOT NULL PRIMARY KEY,
    host_name TEXT NOT NULL,
    calculated_host_listings_count INTEGER NOT NULL
    );

CREATE TABLE IF NOT EXISTS locations
    (
    location_id INTEGER NOT NULL PRIMARY KEY,
    neighbourhood TEXT,
    neighbourhood_group TEXT
    );
''')

conn.commit()


c.execute('''
INSERT OR REPLACE INTO hosts (host_id, host_name, calculated_host_listings_count)
SELECT DISTINCT host_id, host_name, calculated_host_listings_count FROM listings

''')

c.execute('''
INSERT OR REPLACE INTO locations (neighbourhood, neighbourhood_group)
SELECT DISTINCT neighbourhood, neighbourhood_group
FROM listings
 ''')

c.execute('''
INSERT OR REPLACE INTO airbnb (id, host_id, name, location_id, latitude, longitude, room_type, price, minimum_nights,
number_of_reviews, last_review, reviews_per_month, availability_365)

SELECT id, host_id, name, loc.location_id, latitude, longitude, room_type, price, minimum_nights, number_of_reviews,
last_review, reviews_per_month, availability_365 FROM listings li

INNER JOIN locations loc on li.neighbourhood_group = loc.neighbourhood_group and li.neighbourhood = loc.neighbourhood

''')

conn.commit()
c.fetchall()


conn = sqlite3.connect("listings.db")
c = conn.cursor()

class listing(object):
    listing_loc = "listings.db"

    def __init__(self):
        self.conn = sqlite3.connect(listing.listing_loc)
        self.cur = self.conn.cursor()

class DBObject(object):
    pass

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






