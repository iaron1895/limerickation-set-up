from datapackage import Package
import unidecode

package = Package('https://datahub.io/core/world-cities/datapackage.json')

# create list of all city and country names using instructions in https://datahub.io/core/world-cities\#readme
def get_places():
    with open('places/places.txt', 'w') as f:
        for resource in package.resources:
            if resource.descriptor['datahub']['type'] == 'derived/csv':
                data = resource.read()
                countries = [x[1] for x in data if x[1].isalpha()]
                unique_countries = set(countries)
                for uc in unique_countries:
                    uc = unidecode.unidecode(uc)
                    f.write(uc)
                    f.write('\n')
                for d in data:
                    if d[0].isalpha():
                        city = unidecode.unidecode(d[0])
                        f.write(city)
                        f.write('\n')
get_places()