import random
import string

from django.apps import AppConfig


class CarConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carpoint'

    def ready(self):
        load_unzips_data()


def load_unzips_data():
    import csv
    from findCar.models import State, County, Location, Car
    try:
        states = []
        counties = []
        locations = []
        with open('./uszips.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                state = State(state_id=row['state_id'], state_name=row['state_name'])
                states.append(state)

                county = County(county_fips=row['county_fips'], county_name=row['county_name'])
                counties.append(county)

                location = Location(
                    zip=row['zip'],
                    lat=float(row['lat']),
                    lng=float(row['lng']),
                    city=row['city'],
                    state=state
                )
                locations.append(location)
        State.objects.bulk_create(states)

        Location.objects.bulk_create(locations)
        County.objects.bulk_create(counties)

        county_zips = {location.zip: location for location in locations}
        County.objects.filter(location_zip__in=county_zips.keys()).update(location_zip=None)
        for county in counties:
            if county.location_zip:
                county.location_zip = county_zips[county.location_zip]
                county.save()

        from findCar.service import graf
        graf.deleteGrafCars(Car.objects.all())
        Car.objects.all().delete()
        for i in range(0, 21):
            car = Car.objects.create(
                number=f"{random.randint(1000, 9999)}{random.choice(string.ascii_uppercase)}",
                current_location=Location.objects.order_by('?').first(),
                carrying_capacity=random.randrange(0, 10000),
            )
            car.save()
        graf.updateGrafCars(Car.objects.all())

    except Exception as e:
        print(e)