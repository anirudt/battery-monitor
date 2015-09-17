#!/usr/bin/python
import os

'''
This script checks if the battery percentage is lesser
than 20%, and reminds the user to charge the laptop using a voice automated system.
'''
cmd1 = "upower -i /org/freedesktop/UPower/devices/battery_BAT0 | grep percentage | awk '{print $2}' > /home/anirudt/Projects/battery_monitor/temp.energy"

os.system(cmd1)

f = open('/home/anirudt/Projects/battery_monitor/temp.energy', 'rb')
a = f.read()
b = a[0:a.find('%')+1]
c = int(a[0:a.find('%')])

cmd2 = "echo 'Your battery percentage is falling, it is"+b+" now' | /home/anirudt/Projects/battery_monitor/test.sh"
cmd3 = "echo 'Your battery has been fully charged. You could unplug the charger now' | /home/anirudt/Projects/battery_monitor/test.sh"
# Only if the battery is lesser than 20%
if c<=20:
    os.system(cmd2)
elif c==100:
    os.system(cmd3)
else:
    print "You're doing fine."
