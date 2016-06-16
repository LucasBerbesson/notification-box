# notification-box
This is the python code used in this video : 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/Uv6EkKaG8wQ/0.jpg)](https://www.youtube.com/watch?v=Uv6EkKaG8wQ)

If you want to run it. 
Connect a wifi dongle, some rgb LEDS and a speaker to your raspberry pi. 

Make sure you have git installed on your raspberry :
```
sudo apt-get install git
```
Clone the repo
```
git clone https://github.com/LucasBerbesson/notification-box.git
```
Go inside the notification folder
```
cd notification-box
```
Update the variables inside the file with your API credentials. You can use nano or vim to edit the file. 
You can also control the Refresh time of the box, the GPIO you want to use...
```
nano notify.py
```
Run the script
```
python notify.py
```

