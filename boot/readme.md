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
The "launcher.sh" file will run the bot from the "selfboot.py" file in the main directory. Any Error in running thsi code will be placed in the "log.txt" file in this directory.