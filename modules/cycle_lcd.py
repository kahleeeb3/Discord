import drivers
from time import sleep

# defines how the display cycles
def cycle_display(list_of_lines):
    display = drivers.Lcd()
    for position, line in enumerate(list_of_lines):

        display.lcd_display_string("                ", 2)
        display.lcd_display_string(line, 2)
        sleep(0.5)
        display.lcd_display_string("                ", 1)
        display.lcd_display_string(line, 1)
        
    display.lcd_clear()
    display.lcd_backlight(0)

cycle_display(["This","is","a","test","of","cycle","feature"])