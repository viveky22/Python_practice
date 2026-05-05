i = "aabcbd"
res = ""
for j in i:
    if j not in i[i.index(j)+1:]:
        print(j)
        break
