#it will print unique or intersection for both
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
intersection = []
for i in A | B:
    intersection.append(i)
        
print(intersection)


#it is for common in both list
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
intersection = []
for i in A & B:
    intersection.append(i)
        
print(intersection)