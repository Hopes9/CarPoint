import random
import string

def update_car_locations():
    from findCar.service import graf
    from findCar.models import Car
    graf.deleteGrafCars(Car.objects.all())
    Car.objects.all().delete()
    for i in range(0, 21):
        from findCar.models import Location
        car = Car.objects.create(
            number=f"{random.randint(1000, 9999)}{random.choice(string.ascii_uppercase)}",
            current_location=Location.objects.order_by('?').first(),
            carrying_capacity=random.randrange(0, 10000),
        )
        car.save()
    graf.updateGrafCars(Car.objects.all())

def start_scheduler(*args, **kwargs):
    from apscheduler.jobstores.memory import MemoryJobStore
    from apscheduler.schedulers.background import BackgroundScheduler
    from apscheduler.triggers.interval import IntervalTrigger

    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(MemoryJobStore(), "default")

    scheduler.add_job(
        update_car_locations,
        IntervalTrigger(minutes=3),
        id="update_car_locations",
        name="Update Car Locations",
        replace_existing=True,
    )
    scheduler.start()
def start_scheduler_on_startup():
    start_scheduler()
    update_car_locations()



