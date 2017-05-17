import os
import time

response_time = {}

servers = [{'ip': "8.8.8.8", 'mac': "00:00:00:00:00:50", 'out_port': 1},
           {'ip': "8.8.4.4", 'mac': "00:00:00:00:00:51", 'out_port': 2},
           {'ip': "www.msn.com", 'mac': "00:00:00:00:00:52", 'out_port': 3},
           {'ip': "www.google.com", 'mac': "00:00:00:00:00:53", 'out_port': 4},
           {'ip': "www.yahoo.com", 'mac': "00:00:00:00:00:54", 'out_port': 5}]

for i in range(len(servers)):
    srever_ip_test = servers[i]['ip']
    start = time.time()
    r = os.system("ping -n 1 %s" % (srever_ip_test))
    response_time[i] = time.time() - start

    if r == 0:
        print("up")
    else:
        print("down")


print(response_time)

min_index = min(response_time, key=lambda k: response_time[k])
print(min_index)

min_time = min(response_time.items(), key=lambda x: x[1])
print(min_time[1])
