import os

# filepath = "C:\\Users\\mishen\\Downloads\\\u5e73\u4e95 \u5927 \u29f8 Romeo+Juliet -Love goes on-\uff08Lyric Video\uff09.m4a"
# if os.path.exists(filepath):
#     print("OK")
# else:
#     print("SHIT")

sum = 0

for i in range(10):
    sum += (70 + i*14)
    print(70 + i*14)

print(sum)

# 0.2 per sec
speed = 0.2
remain = 370
remian_sec = remain/speed

print('remian sec:', remian_sec)
print('H:M:S', int(remian_sec/3600), ":", int(remian_sec/60)%60, ":", int(remian_sec)%60)