# is vs ==
# print([] is [])
# print([] == [])

#forloop
# user={
#     'name':'sop',
#     'Id':2,
#     'can_swim':True
# }


# for item in user.keys():
#     print(item)
# for item in user.values():
#     print(item)
# for item in user.items():
#     print(item)
# for k,v in user.items():
#     print(k,v)

#enumerate
# for i,item in enumerate ("hifdso"):
#     print(i,item)

#*args    
# def add(*args):
#     sum=0
#     for n in args:
#       sum+=n
#     print(sum)   

# add(1,2,4,5)
    
# def multy (*args):
#     result=1
#     for num in args:
#         result*=num
#     print(result)
# multy(2,3,4)
    
# #**kwargs
# def calculate (n, **kwargs):
#     n+=kwargs['add']
#     n*=kwargs['multiply']
#     print(n)
# calculate(2,add=3, multiply=5)

# def calculate (n, **kwargs):
#     n-=kwargs['minus']
#     n-=kwargs['minus']
#     n*=kwargs['mul']
#     print(n)
# calculate (5, minus=2, mul=4)
    
# def super(*args, **kwargs):
#     total=0
#     for n in kwargs.values():
#         total+=n
#     print(sum(args)+total)
# super(1,2,3,4,num1=5,num2=5)

#pure functions
#map
# def multiply(li):
#     return li*2
# print(list(map(multiply, [1,2,3])))


#filter
# def filterF(li):
#     return li%2==0
# print(list(filter(filterF, [2,3,4,5,6])))

#zip
# listOne=[1,2,3]
# listTwo=[4,5,6,7]
# print(list(zip(listOne,listTwo)))

#reduce
# from functools import reduce
# list=[1,2,3]
# def accu(acc,item):
#     return acc+item
# print(reduce(accu, list,10))


#list comprehension
# print([char for char in "hofds"])
# print([item*2 for item in [1,2,3,4]])
# print([item*2 for item in range(10)])
# print ([item**2 for item in range(0,5) if item%2==0])

# #set comprehension
# print({item+1 for item in range(2)})

#set dictionary
# dict={'a':1,'b':2,"c":3}
# print({key:value*2 for key,value in dict.items()})

# print({num:num*2 for num in [1,2,3] })


#class
class User:
    def __init__(self,userid,name):
        self.userid=userid
        self.name=name
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        self.following+=1
user_1=User("001","asd")
user_2=User("001","fds")  













































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    