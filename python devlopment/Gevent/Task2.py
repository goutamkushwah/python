# FIX 1: Use patch_all() to patch SSL alongside standard sockets
from gevent import monkey
monkey.patch_all()

import gevent
import urllib.request  
import json            

def fetch(pid):
    # FIX 2: Using a stable, public API designed for testing latency/delays
    url = 'https://httpbin.org/delay/1'
    
    # We add a User-Agent header so the website knows it's a valid browser request
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    )
    
    try:
        response = urllib.request.urlopen(req)
        result = response.read()
        json_result = json.loads(result)
        
        # httpbin returns the origin IP address in its JSON payload
        origin_ip = json_result['origin']
        print(f"Process {pid}: Finished successfully! (Server IP recorded: {origin_ip})")
        return origin_ip
        
    except Exception as e:
        print(f"Process {pid} failed due to: {e}")

def synchronous():
    for i in range(1, 4):  # Reduced to 3 loops to keep your output clean
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1, 4):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

if __name__ == "__main__":
    print('--- Starting Synchronous (One by one) ---')
    synchronous()

    print('\n--- Starting Asynchronous (All at once via Gevent) ---')
    asynchronous()