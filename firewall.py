import time
import random
from collections import defaultdict

THRESHOLD = 3

packets = []
blocked_ips = set()
packet_count = defaultdict(int)
start_time = [time.time()]
log = open('blocked.txt', 'w')

for i in range(50):
    packets.append(f'192.168.1.{random.randint(1, 20)}')

for packet in packets:
    packet_count[packet] += 1
    time_count = time.time() - start_time[0]
    if time_count >= 1:
        for ip, count in packet_count.items():
            
            if count >= THRESHOLD and ip not in blocked_ips:
                blocked_ips.add(ip)
                log.write(f'{ip} \n')
                print(f"Blocked IPs this round: '{ip}'")
        print(f"--- Time window ended ({round(time_count, 2)}s) ---")
        packet_count.clear()
        start_time[0] = time.time()   
    time.sleep(0.3)

log.close()


print("Final blocked IPs:", blocked_ips)
