import datetime
import pytz

def curr_time():
    # current time info
    day = datetime.datetime.now().strftime('%a')
    tz_NY = pytz.timezone('America/New_York') 
    hour = datetime.datetime.now(tz_NY).strftime('%I')
    minute = datetime.datetime.now(tz_NY).strftime('%M')
    suffix = datetime.datetime.now(tz_NY).strftime('%p')

    curr_time = (f'{hour}:{minute} {suffix}')
    return day, curr_time