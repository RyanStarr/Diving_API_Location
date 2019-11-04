import urllib.request
import json

def get_jsonparsed_data(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def entries_to_remove(entries, the_dict):
    for key in entries:
        if key in the_dict:
            del the_dict[key]
def main():
    url = 'http://api.divesites.com/?mode=sites&lat=50.3352&lng=-4.1485&dist=25'
    print("ARRAY: ---", get_jsonparsed_data(url))
    site_array = get_jsonparsed_data(url)['sites']
   # print(site_array)

    remove_words = ("currents", "distance", "hazards")
    #
    number = 0
    sites = site_array[0]
    for location in site_array:
        number = number +1
      # print(location)

        #print("DICT" + str(sites))
        for i in ["currents", "distance", "hazards", "mindepth", "maxdepth", "equipment", "description", "predive", "marinelife", "water"]:
            location.pop(i)
        for key in sorted(location.keys()):
            print("%s: %s" % (key, location[key]))

   # entries_to_remove(dict(sites), list(remove_words))
if __name__=='__main__':
    main()