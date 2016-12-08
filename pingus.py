#!/usr/bin/python2.7
 
import ping, socket, subprocess, sys, time
 
if len(sys.argv) > 1:
    host = sys.argv[1]
else:
    host = "127.0.0.1"
 
started = None
while True:
    try:
        result = ping.do_one(host, 2, 64)
        print result
        if result == None:
            started = time.time()
        elif started != None:
            end = time.time()
            diff = end-started
            print "Migration time: " + diff
    except socket.error, e:
        print "Ping Error:", e
