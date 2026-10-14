                                                        # Dct
# name=input()
# age=int(input())
# city=input()
# dct={"Name": name,"Age": age,"City": city}
# print(f"Name: {name}")
# print(f"Age: {age}")
# print(f"City: {city}")

# task2

# dct={"apple":20,"orange":15,"banana":10}
# total=sum(dct.values())
# print(total)

# task3

# fruits="apple banana apple orange banana apple"
# text=fruits.split()
# count={}
# for word in text:
#     if word in count:
#         count[word]+=1
#     else:
#         count[word]=1
# print(count)

#task 4

# dct={'Ali': 90, 'Sara': 85,'Omar': 70}
# name=input()
# if name in dct:
#     print(dct[name])
# else:
#     print("Not Found")

#task 5

# mevagi={'banana': 10,'apple': 20}
# mevagi.update({'ananas': 300})
# print(mevagi)

#task 6

# dct={'phone': 500, 'laptop': 1200, 'tv': 700}
# max=0
# for name,age in dct.items():
#     if age>max:
#         max=age
#         max2=name,age
# print(max2)

#task 7

# dct={'Ali': 90, 'Sara': 85, 'Omar': 70}
# n=input()
# if n in dct:
#     dct.pop(n)
# print(dct)

#task 8

# dct={'a': 1, 'b': 2}
# dct2={'b': 5, 'c': 3}
# dct.update(dct2)
# print(dct)

#task 9

# studentho={'Ali': 90, 'Sara': 75, 'Omar': 85, 'Zara': 60}
# for name,age in studentho.items():
#     if age>80:
#         print(name)

#task 10
# dct={'Ali': 1, 'Sara': 2, 'Omar': 3}
# text={}
# for name,age in dct.items():
#     text[age]=name
# print(text)

                                                    # String
# text="Hello World"
# cnt=0
# result=text.replace(" ","")
# for i in result:
#     cnt+=1
# print(cnt)

#task 2

# zabon="PyThOn"
# zabonkalon=zabon.upper()
# zabonmayda=zabon.lower()
# print(zabonkalon)
# print(zabonmayda)

#task 3

# text="    hello world    "
# print(text.strip())

# task 4

# text="This is a bad day"
# print(text.replace("bad","good"))

#task 5

# text="Programming"
# print(text.startswith("Pro"))
# print(text.endswith("ing"))

#task 6

# text="mandarin,ananas,mango"
# print(text.split(","))

#task 7

# text=['Python', 'is', 'easy']
# text2=text="-".join(text)
# print(text2)

#task 8

# meva="banana"
# banan=meva.count("an")
# print(banan)

#task 9

# rakam="12345"
# rakam2="abc123"
# print(rakam.isdigit())
# print(rakam2.isdigit())

#task 10

# name="aLi ahmEd"
# print(name.title())
                                                  # function
# def greet(name):
#     name=input()
#     print(f"Hello, {name}!")
# greet('name')

#task 2

# a1=int(input())
# b1=int(input())
# def sum(a,b):
#     print(a1+b1)
# sum(a1,b1)

#task 3

# n1=int(input())
# def juft(n):
#     if n1%2==0:
#         print("Even")
#     else:
#         print("Odd")
# juft(n1)

#task 4

# n1=int(input())
# def square(n):
#     print(n1**2)
# square(n1)

#task 5

# a1=int(input())
# b1=int(input())
# def maximum(a,b):
#     if a1>b1:
#         print(a1)
#     else:
#         print(b1)
# maximum(a1,b1)

#task 6

# n1=int(input())
# def factorial(n):
#     if n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(n1)) 

#task 7

# n1=int(input())
# def sumrakam(n):
#     sum2=0
#     for i in range(0,n+1,+1):
#         sum2+=i
#     print(sum2)
# sumrakam(n1)

# task 8

# n1=int(input())
# def digitcnt(n):
#     print(len(str(n)))
# digitcnt(n1)
    
# task 9

# n1=int(input())
# def sumdigit(n):
#     sum=0
#     while n>0:
#         sum+=n%10
#         n=n//10
#     print(sum)
# sumdigit(n1)

#task 10

# def isprime(n):
#     for i in range(2,n):
#         if n==1:
#             return False
#         elif n%i==0:
#             return False
#         else:
#             return True
# print(isprime(7))

#task 11

# def text(s):
#     print(s[::-1])
# text("python")
            
#task 12

# def vovel(s):
#     text="aeiuo"
#     cnt=0
#     for i in s:
#         if i in text:
#             cnt+=1
#     return cnt
# print(vovel("education"))

#task 13

# def sum(numbers):
#     sum=0
#     for i in numbers:
#         sum+=i
#     return sum
# print(sum([1,2,3,4,5]))


#task 14

# def maxnumbers(n):
#     max=-9999
#     for i in n:
#         if i>max:
#             max=i
#     print(max)
# maxnumbers([2,3,4,5,1])

#task 15

# def musbat(n):
#     cnt=0
#     for i in n:
#         if i > 0:
#             cnt+=1
#     print(cnt)
# musbat([-9,-2,3,4,5,98])

#task 16

# p=input()
# def palindrome(n):
#     print(n == n[::-1])
# palindrome(p)

#task 17

# def numbers(n):
#     print(list(set(n)))
# numbers([1,2,3,4,3,5,6])

#task 18

# def celcia(c):
#     return c*9 / 5 + 32
# print(celcia(25))

#task 19

# a1=int(input())
# b1=int(input())
# c1=input()
# def calculate(a,b,op):
#     if op=="+":
#         return a1+b1
#     if op=="-":
#             return a1-b1 
#     if op=="*":
#             return a1*b1
#     if op=="/":
#         if b1==0:
#             return None
#         else:
#             return a//b
# print(calculate(a1,b1,c1))

#task 20

# def statictic(numbers):
#     dct={"sum":sum(numbers),"max":max(numbers),"min":min(numbers)}
#     print(dct)
# statictic([4, 8, 2, 10, 6])

                                    # rikursiya

# def rakam(n):
#     if n==0:
#         return
#     rakam(n-1)
#     print(n)
# rakam(5)

#task 2

# def rakam(n):
#     if n==0:
#         return
#     print(n)
#     rakam(n-1)
# rakam(5)

#task 3

# def rakam(n):
#     if n==1:
#         return 1
#     return n+rakam(n-1)
# print(rakam(5))

#task 4

# def rakam(n):
#     if n==1:
#         return 1
#     return n*rakam(n-1)
# print(rakam(5))

#task 5

# def rakam(a,n):
#     print(pow(a,n))
# rakam(2,5)

#task 6

# def rakam(n):
#     if n==1:
#         return 1
#     return n%10+rakam(n//10)
# print(rakam(1234))

#task 7

# def rakam(n):
#     if n==0:
#         return 0
#     return 1+rakam(n//10)
# print(rakam(123450))

#task 8
# ?

#task 9
# ?

#task 10
# ?
                                        # Quiz
# def rakam(n):
#     if n==1:
#         return 1
#     return n**2+rakam(n-1)
# print(rakam(3))

#task 2

# def kub(n):
#     if n==1:
#         return 1
#     return n**3+kub(n-1)
# print(kub(2))

#task 3