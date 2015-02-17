#!/usr/bin/env python
#! -*- encoding:utf-8

import sys
import requests
import requests_cache

from os.path import dirname
from BeautifulSoup import BeautifulSoup
from model import *

VERBOSE_LEVEL = 0

def fetch_villages(url, town):
    i = 0
    while True:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            i += 1
            print >> sys.stderr, u"下载失败 %s" % url
            print >> sys.stderr, u"重试第 %d 次" % i

    response.encoding= 'gb2312'
    responseText = response.text
    soup = BeautifulSoup(responseText)
    soup_villages = soup.findAll("tr", "villagetr")

    villages = []
    for soup_village in soup_villages:
        village_name = soup_village.td.nextSibling.nextSibling.text
        if VERBOSE_LEVEL > 0:
            print >> sys.stderr, u"        %s" % village_name
        village = Village(int(soup_village.td.text), village_name, town,
            int(soup_village.td.nextSibling.text))
        # try:
        #     VillageRepository().add(village)
        # except sqlite3.IntegrityError:
        #     if VERBOSE_LEVEL > 0:
        #         print >> sys.stderr, u"%d %s 记录存在" % (village.id, \
        #             village.name)
        villages.append(village)
    return villages

def fetch_towns(url, county):
    i = 0
    while True:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            i += 1
            print >> sys.stderr, u"下载失败 %s" % url
            print >> sys.stderr, u"重试第 %d 次" % i
    response.encoding= 'gb2312'
    responseText = response.text
    soup = BeautifulSoup(responseText)
    soup_towns = soup.findAll("tr", "towntr")

    towns = []
    for soup_town in soup_towns:
        town_name = soup_town.td.nextSibling.text
        town_id = int(soup_town.td.a['href'].split("/")[-1][:-5])
        village_url = dirname(url) + "/" + soup_town.td.a['href']
        if VERBOSE_LEVEL > 0:
            print >> sys.stderr, u"      %s" % town_name

        town = Town(town_id, town_name, county)
        # try:
        #     TownRepository().add(town)
        # except sqlite3.IntegrityError:
        #     if VERBOSE_LEVEL > 0:
        #         print >> sys.stderr, u"%d %s 记录存在" % (town.id, town.name)
        towns.append(town)
    return towns

def fetch_counties(url, city):
    i = 0
    while True:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            i += 1
            print >> sys.stderr, u"下载失败 %s" % url
            print >> sys.stderr, u"重试第 %d 次" % i
    response.encoding= 'gb2312'
    responseText = response.text
    soup = BeautifulSoup(responseText)
    soup_counties = soup.findAll("tr", "countytr")

    counties = []
    for soup_county in soup_counties:
        county_name = soup_county.td.nextSibling.text

        town_url = soup_county.td.a and soup_county.td.a['href'] \
            or soup_county.td.text
        town_url = dirname(url) + "/" + town_url
        county_id = int(town_url.split("/")[-1][:-5])

        county = County(county_id, county_name, city)
        # try:
        #     CountyRepository().add(county)
        # except sqlite3.IntegrityError:
        #     if VERBOSE_LEVEL > 0:
        #         print >> sys.stderr, u"%d %s 记录存在" % (county.id, county.name)

        if VERBOSE_LEVEL > 0:
            print >> sys.stderr, u"    %s" % county_name
        counties.append(county)
    return counties

def fetch_cities(url, province):
    i = 0
    while True:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            i += 1
            print >> sys.stderr, u"下载失败 %s" % url
            print >> sys.stderr, u"重试第 %d 次" % i
    response.encoding= 'gb2312'
    responseText = response.text
    soup = BeautifulSoup(responseText)
    soup_cities = soup.findAll("tr", "citytr")

    cities = []
    for soup_city in soup_cities:
        city_name = soup_city.td.nextSibling.text
        city_id = int(soup_city.td.a['href'].split("/")[-1][:-5])
        city_url = dirname(url) + "/" + soup_city.td.a['href']
        if VERBOSE_LEVEL > 0:
            print >> sys.stderr, u"  %s" % city_name

        city = City(city_id, city_name, province)
        # try:
        #     CityRepository().add(city)
        # except sqlite3.IntegrityError:
        #     if VERBOSE_LEVEL > 0:
        #         print >> sys.stderr, u"%d %s 记录存在" % (city.id, city.name)
        cities.append(city)
    return cities

def fetch_provinces():
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/index.html"
    i = 0
    while True:
        try:
            response = requests.get(url)
            break
        except requests.exceptions.ConnectionError:
            i += 1
            print >> sys.stderr, u"下载失败 %s" % url
            print >> sys.stderr, u"重试第 %d 次" % i
    response.encoding= 'gb2312'
    responseText = response.text
    soup = BeautifulSoup(responseText)
    provincetr = soup.findAll("tr", {"class": "provincetr"})

    provinces = []
    size = len(provincetr)
    i = 1
    for province1 in provincetr:
        for province in province1.findAll("td"):
            province_id   = int(province.a['href'][0:-5])
            province_name = province.text
            province_url  = dirname(url) + "/" + province.a['href']
            if VERBOSE_LEVEL > 0:
                print >> sys.stderr, u"%s" % province_name

            provinceObj = Province(province_id, province_name)
            # try:
            #     ProvinceRepository().add(provinceObj)
            # except sqlite3.IntegrityError:
            #     if VERBOSE_LEVEL > 0:
            #         print >> sys.stderr, u"%d %s 记录存在" % (province.id, 
            #             province.name)
            # fetch_cities(province_url, provinceObj)
            provinces.append(provinceObj)
            i += 1

    return provinces