import sqlite3
from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///listings.db', echo=True)
Base = declarative_base(engine)
print(engine.table_names())


class InHost:
    def __(self):
        print("name, host_id and listing count:")
        self.pname = input("Enter Name:")
        self.listing_count_update = input("Enter Listing Count:")

    def PrintDetails(self):
        print("\n\n Name: ", self.name)
        print("Current Listing Count: ", self.listing_count_update)


class InProperty:
    def __init__(self):
        print("Please enter the listing details")

        self.name = input("Listing name: ")
        self.host_id = int(input("Host ID number: "))
        self.latitude = int(input("Latitude of property:"))
        self.longitude = int(input("Longitude of property: "))
        self.room_type = input("Room Type (shared room, private room or entire home/apt?): ")
        self.price = int(input("Price per night: "))
        self.min_nights = int(input("Min nights: "))
        self.last_review = int(input("Enter date: "))
        self.reviews_per_month = float(input("average reviews per month:"))
        self.availability_365 = int(input("Days available throughout the year"))


class InLocation:
    def __init__(self):
        print("Please enter Neighbourhood details (i.e Central Region, Singapore River")

        self.neigh_group("Neighbourhood group: ")
        self.neighbourhood("Neighbourhood: ")


class Lister(InHost, InProperty, InLocation):
    def __init__(self):
        InHost.__init__(self)
        InProperty.__init__(self)
        InLocation.__init__(self)

    def PrintEntry(self):
        InHost.PrintEntry(self)
        InProperty.PrintEntry__init__(self)
        InLocation.PrintEntry(self)


lister = Lister()
lister1.PrintEntry()

