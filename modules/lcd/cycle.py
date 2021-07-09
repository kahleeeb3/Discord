import drivers
from time import sleep
import socket
        
# Get the Machines IP Address
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    IPAddr= s.getsockname()[0]
    s.close()
    return IPAddr

# Gets the todo list from files
def read(file_name):
    a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt', "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    return list_of_lines

# defines how the display cycles
def cycle_display(list_of_lines):
    display = drivers.Lcd()
    for position, line in enumerate(list_of_lines):

        display.lcd_display_string("                ", 2)
        display.lcd_display_string(line, 2)
        sleep(1)
        display.lcd_display_string("                ", 1)
        display.lcd_display_string(line, 1)
        
    display.lcd_clear()
    display.lcd_backlight(0)

cycle_display(read('todo'))     # Cycle The todo List
cycle_display([get_ip()])         # Display my IP Address