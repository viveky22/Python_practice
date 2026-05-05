#Reverse a string (without slicing [::-1])
# a = "vivekyadav"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b += a[i]
# print(b)

#Check if a string is palindrome
# a = "abcbda"
# if a == a[::-1]:
#     print("string is palindrone")
# else:
#     print("string is not palindrone")

#Count vowels and consonants in a string
# a = "vivekayadv"
# l = len(a)
# count_v = 0
# count_c = 0
# v = "aeiou"
# for i in a:
#     if i in v:
#         count_v += 1
# count_c  = l-count_v
# print("no of vowels  and consonant are ", count_v,count_c)


#Find largest element in a list

# a = [2,5,7,3,8,9,4]
# maxi = 0
# for i in a:
#     maxi = max(i,maxi)
# print(maxi)

#Find second largest element (without sorting)
# a = [2,5,7,3,8,9,4]
# lar = 0
# second = 0
# for i in a:
#     if i >lar:
#         second = lar
#         lar = i
#     elif i>second:
#         second = i
# print(second)

#Remove duplicates from a list
# a = [2,5,7,3,8,9,4]
# print(list(set(a)))

#Count frequency of characters in a string (use dict)Count frequency of characters in a string (use dict)
# a = "vivekyadav"
# d = {}
# for i in a:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i] = 1
# print(d)

#Swap two numbers without using third variable
# a = 2
# b = 5
# a,b = b,a
# print(a,b)

#Find sum of digits of a number
# a = 342435
# sum = 0
# for i in str(a):
#     sum = sum +int(i)
# print(sum)

#Print Fibonacci series (iterative)
# n = 5
# a = 0
# b = 1
# for i in range(n):
#     print(a,end = " ")
#     a, b = b, a + b

#find factorial
# def fun(n):
#     fact = 1
#     while n>0:
#         fact =  fact*(n)
#         n = n-1
#     return fact
# print(fun(5))

#Find common elements in two listsFind common elements in two lists
# a = [2,3,4,5]
# b = [4,5,6,7]
# for i in a:
#     if i in b:
#         print(i,end = " ")

#Merge two sorted lists
# a = [2,3,4,5]
# b = [4,5,6,7]
# c = a+b
# print(sorted(c))

#Find missing number in array (1 to n)
# n = [2,3,4,5,7,8,9]
# for i in range(len(n)-1):
#     if n[i]+1 != n[i+1]:
#         print(n[i]+1)

#Move all zeros to end of list
# a = [2,43,6,9,0,4,7,9,0,4,0,5]
# for i in range(len(a)):
#     if a[i] == 0:
#         a.remove(a[i])
#         a.append(0)
# print(a)

#Find duplicates in a list
# a = [3,4,5,6,7,7,8,9,0]
# for i in range(len(a)-1):
#     if a[i] in a[i+1:]:
#         print(a[i])

#Count words in a sentence
# a = "my name is vivek yadav"
# b = a.split()
# print(len(b))

#Find first non-repeating character
# a = [2,3,4,2,3,5,4,3,1,3]
# for i in a:
#     if a.count(i) == 1:
#         print(i)
#         break

#Check if two strings are anagrams
# a = 'listenb'
# b = 'silenta'
# if len(a)  != len(b):
#     print('string are not anagrams')
# if sorted(a) == sorted(b):
#     print("strings are anagrams")
# else:
#     print("strings are not anagrams")


        
        

