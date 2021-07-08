# Self Boot
To have the discord bot automatically start when the Raspberry Pi boots:
```
sudo crontab -e
```
Paste in:
```
@reboot sh /home/pi/Desktop/Discord/boot/launcher.sh > /home/pi/Desktop/Discord/boot/log.txt 2>&1
```
Save and exit
### Note:
This will have the bot boot from the "selfboot.py" file in the main directory