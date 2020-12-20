# printout current time with time zone
import time

t = time.localtime()
print("===== current time: =====\n", (t.tm_hour + 8) % 24, ":", t.tm_min, ":", t.tm_sec)