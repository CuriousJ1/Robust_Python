# Version 1.
## What is the return type of the following function
def find_workers_available_for_time(open_time: datetime.datetime):
    workers = worker_database.get_all_workers()
    available_workers = [worker for worker in workers

    if is_available(worker)]
        return available_workers

    # fall back to workers who listed they are available
    # in an emergency
    emergency_workers = [worker for worker in get_emergency_workers()
                         if available_workers:

    if emergency_workers:
        return emergency_workers

    # Schedule the owner to open, they will find someone else
    return [OWNER]

# I dont know, as it explicilty does not say

# Version 2.

def find_workers_available_for_time(open_time: datetime.datetime) -> list[str]: