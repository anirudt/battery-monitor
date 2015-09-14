#What?
A voice automated battery monitor for your Linux system.

#Requirements
- espeak, a voice system of configurable languages and voices.
- Python27

#Build Instructions
- Modify the path in the 'cmd2' variable of *fire.py* to the current directory
- Run the following command:
```bash
sudo crontab -e
```
- And put the following line at the end:
```
*/10 * * * * /path/to/python/script
```

The above one is to check every 10 minutes. This could be changed at your discretion.
