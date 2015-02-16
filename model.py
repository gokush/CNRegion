#!-*- encoding:utf-8 -*-
import sqlite3
import pinyin

connection = sqlite3.connect('/tmp/region.sqlite3')

class Province:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cities = []

class City:
    def __init__(self, id, name, province):
        self.id = id
        self.name = name
        self.province = province
        self.county = []

class County:
    def __init__(self, id, name, city):
        self.id = id
        self.name = name
        self.city = city
        self.town = []

class Town:
    def __init__(self, id, name, county):
        self.id = id
        self.name = name
        self.county = county
        self.village = []

class Village:
    def __init__(self, id, name, town, category):
        self.id = id
        self.name = name
        self.town = town
        self.category = category
        

class ProvinceRepository:
    def create(self):
        statement = """CREATE TABLE IF NOT EXISTS province (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            pinyin TEXT
        )
        """

        cursor = connection.cursor()
        cursor.execute(statement)
        connection.commit()

    def add(self, province):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO province(id, name, pinyin) VALUES " \
            "(?, ?, ?)", (province.id, province.name, 
                          pinyin.get(province.name),))
        connection.commit()

class CityRepository:
    def create(self):
        statements = [
            """CREATE TABLE IF NOT EXISTS city (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province INTEGER,
                name TEXT,
                pinyin TEXT
            );""",
            """
            """
        ]

        cursor = connection.cursor()
        for statement in statements:
            cursor.execute(statement)
        connection.commit()

    def add(self, city):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO city(id, province, name, pinyin) VALUES " \
            "(?, ?, ?, ?)", (city.id, city.province.id, city.name, 
                             pinyin.get(city.name),))
        connection.commit()

class CountyRepository:
    def create(self):
        statements = [
            """CREATE TABLE IF NOT EXISTS county (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province INTEGER,
                city INTEGER,
                name TEXT,
                pinyin TEXT
            );""",
            """
            """
        ]

        cursor = connection.cursor()
        for statement in statements:
            cursor.execute(statement)
        connection.commit()

    def add(self, county):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO county (id, province, city, name, pinyin)" \
            " VALUES (?, ?, ?, ?, ?)",
            (county.id, county.city.province.id, county.city.id, \
             county.name, pinyin.get(county.name),))
        connection.commit()

class TownRepository:
    def create(self):
        statements = [
            """CREATE TABLE IF NOT EXISTS town (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province INTEGER,
                city INTEGER,
                county INTEGER,
                name TEXT,
                pinyin TEXT
            );""",
            """
            """
        ]

        cursor = connection.cursor()
        for statement in statements:
            cursor.execute(statement)
        connection.commit()

    def add(self, town):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO town (id, province, city, county, name, " \
            "pinyin) VALUES (?, ?, ?, ?, ?, ?)",
            (town.id, town.county.city.province.id, town.county.city.id,\
             town.county.id, town.name, pinyin.get(town.name),))
        connection.commit()

class VillageRepository:
    def create(self):
        statements = [
            """CREATE TABLE IF NOT EXISTS village (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                province INTEGER,
                city INTEGER,
                county INTEGER,
                town INTEGER,
                category INTEGER,
                name TEXT,
                pinyin TEXT
            );""",
            """
            """
        ]

        cursor = connection.cursor()
        for statement in statements:
            cursor.execute(statement)
        connection.commit()

    def add(self, village):
        cursor = connection.cursor()
        cursor.execute("INSERT INTO village (id, province, city, county, " \
            "town, category, name, pinyin) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (village.id, village.town.county.city.province.id, \
             village.town.county.city.id,\
             village.town.county.id, village.town.id, village.category,
             village.name, pinyin.get(village.name),))
        connection.commit()

ProvinceRepository().create()
CityRepository().create()
CountyRepository().create()
TownRepository().create()
VillageRepository().create()

if "__main__" == __name__:
    province = Province(11, u"北京")
    city = City(1101, u"市辖区", province)
    county = County(110101, u"东城区", city)
    town = Town(110101001, u"东华门街道办事处", county)
    village = Village(110101001001, u"多福巷社区居委会", town, 111)

    ProvinceRepository().add(province)
    CityRepository().add(city)
    CountyRepository().add(county)
    TownRepository().add(town)
    VillageRepository().add(village)