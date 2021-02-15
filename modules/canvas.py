import pytz
from icalendar import Calendar, Event
import datetime
from pytz import UTC # timezone
import requests

skip = {'Theory of Programming Language','Combinatorics','Complex Analysis'}
skip_class = {'PHY-112','PHY-ORG'}

def get_file():
    url = 'https://wabash.instructure.com/feeds/calendars/user_8q6sNMVzdbiK1t3ruZyJkFCBH60Cvmi8738FKAHY.ics'
    r = requests.get(url, allow_redirects=True)
    open('./modules/canvas.ics', 'wb').write(r.content)
    g = open('./modules/canvas.ics','rb')
    gcal = Calendar.from_ical(g.read())
    g.close()
    return gcal

def get_date(offset):
    time = datetime.datetime.today()+ datetime.timedelta(days=offset)
    date= str(time).split()
    return date[0]

def in_skip(event):
    in_skip = False
    for item in skip:
        if item in str(event):
            in_skip = True
    return in_skip

def in_skip_class(event):
    in_skip_class = False
    for item in skip_class:
        if item in str(event):
            in_skip_class = True
    return in_skip_class

def get_item(component):
    assignment = component.get('summary')
    assignment = assignment.split(' [')

    start = component.decoded('dtstart')
    start = str(start)
    time = str(start).split()[1][0:5]

    #get the name of the class
    myclass = assignment[1].replace(',','').replace(']','')
    myclass = myclass.split()
    if len(myclass) >= 2:
        myclass = myclass[1]
        myclass = myclass.split('-')
        myclass = myclass[0:2]
        myclass = '-'.join(myclass)
    else:pass

    assignment = assignment[0].replace(' Assignment','').replace(' Sections','').replace(' Section','').replace(' Corrections','C')

    return start,assignment,myclass,time

def get_list(offset):
    my_list = ''
    date = get_date(offset)
    gcal = get_file()
    for component in gcal.walk():
        if component.name == "VEVENT":
            event = get_item(component)
            if date in event[0]:
                if not in_skip(event[1]) and not in_skip_class(event[2]) :
                    my_list = f'{my_list}{event[2]}: {event[1]}\n'
    return my_list

def main(offset):
    my_list = get_list(int(offset))
    return my_list
        
