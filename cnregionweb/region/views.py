from django.http import HttpResponse
from StringIO import StringIO
from models import Province
from pdb import set_trace as bp
import services
import json

def response(request, data, content_type):
    r = StringIO()
    callback = request.GET.get("callback", "province")
    if "jsonp" == content_type:
        r.write("%s(" % callback)
    r.write(json.dumps(data, indent=4))
    if "jsonp" == content_type:
        r.write(")")
    r.seek(0)
    return HttpResponse(r.read(), content_type="application/json")

def provinces(request, content_type):
    return response(request, services.provinces(), content_type)
    
def cities(request, content_type, province_id):
    return response(request, services.cities(province_id), content_type)

def counties(request, content_type, city_id):
    return response(request, services.counties(city_id), content_type)

def towns(request, content_type, county_id):
    return response(request, services.towns(county_id), content_type)

def villages(request, content_type, town_id):
    return response(request, services.villages(town_id), content_type)