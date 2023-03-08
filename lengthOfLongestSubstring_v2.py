s = " "

len_max = 0
set1 = set()
i = 0
j = 0
while j < len(s):
    if s[j] not in set1:
        set1.add(s[j])
        j += 1
        len_max = max(j-i, len_max)
    else:
        set1.remove(s[i])
        i += 1

print("len_max:", len_max)