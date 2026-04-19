# A Python script that reads a log file where each line has a timestamp and an event. 
# Your job — find the busiest 60-second window. The one with the most requests in any
# 60-second stretch.
from collections import deque

timestamps = [1,15,45,79,110,120,150,180,210,240,270,300]




def find_busiest_window(timestamps, window_size=60):
    active_window_timestamps = deque()
    max_requests_in_window = 0

    for current_time in timestamps:
        active_window_timestamps.append(current_time)
        cutoff_time = current_time - window_size

        while (
            active_window_timestamps
            and active_window_timestamps[0] <= cutoff_time
        ):
            active_window_timestamps.popleft()

        max_requests_in_window = max(
            max_requests_in_window,
            len(active_window_timestamps)
        )

    return max_requests_in_window
busiest_window = find_busiest_window(timestamps)
print(f"The busiest 60-second window has {busiest_window} requests.")

#data flow 
# For your data:
# [1, 15, 45, 79, 110, 120, 150, 180, 210, 240, 270, 300]

# Step-by-step flow:

# current=1, cutoff=-59, window=[1], count=1
# current=15, cutoff=-45, window=[1, 15], count=2
# current=45, cutoff=-15, window=[1, 15, 45], count=3
# current=79, cutoff=19, remove 1 and 15, window=[45, 79], count=2
# current=110, cutoff=50, remove 45, window=[79, 110], count=2
# current=120, cutoff=60, remove none, window=[79, 110, 120], count=3
# current=150, cutoff=90, remove 79, window=[110, 120, 150], count=3
# current=180, cutoff=120, remove 110 and 120, window=[150, 180], count=2
# current=210, cutoff=150, remove 150, window=[180, 210], count=2
# current=240, cutoff=180, remove 180, window=[210, 240], count=2