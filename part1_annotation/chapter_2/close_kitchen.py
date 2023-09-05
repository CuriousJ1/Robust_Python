#Version 1.
def close_kitchen_if_past_cutoff_time(point_in_time):
    if point_in_time >= closing_time():
            close_kitchen()
            log_time_closed(point_in_time)

# Questions from inheriting this code
# what type are we dealing with?
# is it a str, int, datetime, or some customer class?
# what operatings are you allowed to perform on point_int_time?


#Version 2.
def close_kitchen_if_past_cutoff_time(point_in_time: datetime.datetime):
    if point_in_time >= closing_time():
            close_kitchen()
            log_time_closed(point_in_time)
