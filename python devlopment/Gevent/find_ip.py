import time
import gevent
import socket
urls = ['www.google.com', 'www.example.com', 'www.python.org']
start_time =time.time()
for url in urls:
    ip = socket.gethostbyname(url)
    print(f'{url} has IP address {ip}')
end_time = time.time()
e_time = (end_time - start_time)
print(e_time)

jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]
start_time = time.time()
gevent.joinall(jobs,timeout=2)
end_time = time.time()
e_time = (end_time - start_time)

print("this is gevent time")
print(e_time)

for job in jobs:
    print(job.value)