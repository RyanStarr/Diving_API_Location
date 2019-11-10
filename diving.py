# Libraries for connection to API
import urllib.request
# Reading JSON
import json


# Perform API GET request
def get_diving_data(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode("ISO-8859-1")
    return json.loads(data)

# Output each site to an individual json file
def write_to_file(site):
    file_name = (site["lat"] + "," + site["lng"])
    out = json.dumps(site)
    f = open(file_name + ".json", "w")
    f.write(out)
    f.close()


def main():
    # Define API information
    url = 'http://api.divesites.com/?mode=sites&lat=50.3352&lng=-4.1485&dist=10'

    # Retrieve only diving site locations
    diving_site_array = get_diving_data(url)['sites']

    # Trim useless data from array
    for site in diving_site_array:
        for i in ["id", "currents", "distance", "hazards", "mindepth", "maxdepth", "equipment", "description",
                  "predive", "marinelife", "water"]:
            site.pop(i)

            write_to_file(site)


# Start program from main()
if __name__ == '__main__':
    main()

#end