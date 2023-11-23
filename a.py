from stem import Signal
from stem.control import Controller
import os

with Controller.from_port(port=9051) as controller:
    controller.authenticate()
    controller.signal(Signal.NEWNYM)

a=os.system("torify curl http://icanhazip.com/")
print(a)
