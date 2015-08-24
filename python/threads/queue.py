# -*- coding: utf-8 -*-
"""
The purpose of threading is to prevent I/O blocking.
This is a Queue Process example modified from a SO page.
"""
import Queue
import threading
import urllib2

def fetch_url(queue, url):
    # Put the content into the Queue to output at the end
    source = urllib2.urlopen(url).read()
    queue.put(source)

urls = [
    "http://google.com",
    "http://github.com"
]

# Create a Queue
queue = Queue.Queue()

# Loop the URLs
for url in urls:
    # Call the method within a thread using the Queue
    t = threading.Thread(target=fetch_url, args=(queue, url))
    # Run Thread as Daemon?
    t.daemon = True
    # Run Thread
    t.start()

# The Results
print queue.get()