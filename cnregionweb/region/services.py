from cnregion import fetch

def provinces():
    return [i.json() for i in fetch.fetch_provinces()]

def cities(province_id):
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/%d.html" %\
        int(province_id)
    return [i.json() for i in fetch.fetch_cities(url, None)]

def counties(city_id):
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/%s/%s.html" %\
        (city_id[:2], city_id,)
    return [i.json() for i in fetch.fetch_counties(url, None)]

def towns(county_id):
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/"\
        "%s/%s/%s.html" % (county_id[:2], county_id[2:4], county_id)
    return [i.json() for i in fetch.fetch_towns(url, None)]

def villages(town_id):
    url = "http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2013/"\
    "%s/%s/%s/%s.html" % (town_id[:2], town_id[2:4], town_id[4:6], town_id)
    return [i.json() for i in fetch.fetch_villages(url, None)]