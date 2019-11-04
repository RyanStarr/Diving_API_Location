# Libraries for connection to API
import urllib.request
# Reading JSON
import json
# And storing output in database
import pymongo


# Perform API GET request
def get_diving_data(url):
    response = urllib.request.urlopen(url)
    data = response.read().decode("ISO-8859-1")
    return json.loads(data)


def main():
    # Connect to database
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["diving_location_db"]
    mycol = mydb["location"]

    # Define API information
    url = 'http://api.divesites.com/?mode=sites&lat=50.3352&lng=-4.1485&dist=2500000000000000000000'

    # Retrieve only diving site locations
    diving_site_array = get_diving_data(url)['sites']

    # Trim useless data from array
    for location in diving_site_array:
        for i in ["id", "currents", "distance", "hazards", "mindepth", "maxdepth", "equipment", "description",
                  "predive", "marinelife", "water"]:
            location.pop(i)

        # -----Used to view output-----
        '''
        for key in (location.keys()):
            print("%s: %s" % (key, location[key]))
        '''

        # Output each location to database
        x = mycol.insert_one(location)


# Start program from main()
if __name__ == '__main__':
    main()
