# Version 1.
## We don't know the type value that goes into open_time or workers needed

def schedule_restaurant_open(open_time, workers_needed):

# Version 2.

import datetime
import random

                                            # duck typing :dattetime
def schedule_restaurant_open(open_time: datetime.datetime, workers_needed: int):

    workers = find_workers_available_for_time(open_time)

    # Use random.sample to pick X available workers
    # where X is the number of workers needed.
    for worker in random.sample(workers, workers_needed):
        worker.schedule(open_time)


# Whaast