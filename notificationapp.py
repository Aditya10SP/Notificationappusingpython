import time
from plyer import notification
if __name__=="__main__":

    i=0
    while i!=3:
        notification.notify(
            title="Take a class",
            message="I have to take a python workshop",
            timeout = 10
        )
        time.sleep(15)
        i=i+1