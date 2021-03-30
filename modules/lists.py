from modules import drivers
from time import sleep

def read(file_name):
    a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt', "r")
    list_of_lines = a_file.readlines()
    a_file.close()
    return list_of_lines

def to_string(file_name):
    a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt')
    content = a_file.read()
    a_file.close()
    return content

def edit(file_name,new_list):
    #make changes to text file
    a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt', "w")
    a_file.write(new_list)
    a_file.close()

def add(file_name,new_info):
    a_file = open(f'/home/pi/Desktop/Discord/modules/lists/{file_name}.txt', "a")
    a_file.write(f'{new_info.content}\n')
    a_file.close()

def delete(file_name, index):
    list_of_lines = read(file_name)
    print(list_of_lines)
    #edit the text file
    list_of_lines[index] = ''
    new_list = ''.join(list_of_lines)
    edit(file_name, new_list)

def in_list(file_name,phrase):
    locations = []
    a_list = read(file_name)
    for index, lines in enumerate(a_list):
        if phrase in lines:
            locations.append(index)
    return locations

# defines how the display cycles
def cycle_display(list_of_lines):
    display = drivers.Lcd()
    for position, line in enumerate(list_of_lines):

        display.lcd_display_string("                ", 2)
        display.lcd_display_string(line, 2)
        sleep(2)
        display.lcd_display_string("                ", 1)
        display.lcd_display_string(line, 1)
        
    display.lcd_clear()
    display.lcd_backlight(0)