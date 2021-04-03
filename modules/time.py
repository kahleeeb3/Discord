import datetime
import pytz

def curr_time():
    # current time info
    tz_NY = pytz.timezone('America/New_York') 
    date = datetime.datetime.now(tz_NY).strftime("%m/%d/%y")
    day = datetime.datetime.now(tz_NY).strftime('%a')
    hour = datetime.datetime.now(tz_NY).strftime('%I')
    minute = datetime.datetime.now(tz_NY).strftime('%M')
    suffix = datetime.datetime.now(tz_NY).strftime('%p')

    curr_time = (f'{hour}:{minute} {suffix}')
    return day, curr_time, date