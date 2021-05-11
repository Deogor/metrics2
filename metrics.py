import os
hostname = os.uname()[1]
print(hostname)

import socket
print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname(socket.getfqdn()))

import shutil
total, used, free = shutil.disk_usage("/")
print("Total: %d GiB" % (total // (2**30)))
print("Used: %d GiB" % (used // (2**30)))
print("Free: %d GiB" % (free // (2**30)))

