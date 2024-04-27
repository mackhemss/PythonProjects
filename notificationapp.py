import time 
from plyer import notification

while(True):
    notification.notify(
        title="Start coding now" ,
        message = "Don't be studip",
        app_icon="",
        timeout=10
    )
    time.sleep(10)