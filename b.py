from stem import Signal
from stem.control import Controller
import os

def change_identity():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
        print("Identity changed successfully.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    change_identity()
    a=os.system("torify curl http://icanhazip.com/")
    print(a) 
