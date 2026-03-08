# A Python script that reads a log file where each line has a timestamp and an event. 
# Your job — find the busiest 60-second window. The one with the most requests in any
# 60-second stretch.
from collections import deque

timestamps = [1,15,45,79,110,120,150,180,210,240,270,300]




def find_busiest_window(timestamps, window_size=60):
    window = deque()
    max_requests = 0
    for timestamp in timestamps:
        window.append(timestamp)
        while window and window[0] <= timestamp - window_size:
            window.popleft()
        max_requests = max(max_requests, len(window))
    return max_requests
busiest_window = find_busiest_window(timestamps)
print(f"The busiest 60-second window has {busiest_window} requests.")