max_len = 1
curr_len = 1
a = [1,5,6,7,0,12,2,3,4,5,7,13,21,23,22,30]
for i in range(1, len(a)):   # ✅ go till last index
    if a[i] >= a[i-1]:
        curr_len += 1
    else:
        max_len = max(max_len, curr_len)
        curr_len = 1

max_len = max(max_len, curr_len)

print(max_len)