In command line

(1) Type:
sudo crontab -e

(2) Add the line:
@reboot sh /home/pi/Desktop/Discord/boot/launcher.sh > /home/pi/Desktop/Discord/boot/log.txt 2>&1

(3) Save and exit