s = " "

len_max = 0
set1 = set()

if len(s) == 1:
    len_max = 1

for i in range(0, len(s)):
    set1 = set(s[i])
    for j in range(i+1, len(s)):
        if s[j] in set1:
            # print("i,",i,"j",j)
            length = j-i
            if length > len_max:
                len_max = length
            break
        set1.add(s[j])
        if j == len(s)-1:
            # print("no break:","i,",i,"j",j)
            length = j-i+1
            if length > len_max:
                len_max = length


print("len_max:", len_max)