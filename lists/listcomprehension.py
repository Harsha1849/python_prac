#list comprehension is used as a shorter syntax when you want to create a new list based on values of existing list

fruits=["apple","banana","kiwi","mango","cherry"]
# newlist=[]

# for x in fruits:
#     if "a" in x:
#         newlist.append(x)

# print (newlist)

newlist=[x for x in fruits if "a" in x] #prints fruits with letter 'a'
newlist=[x for x in fruits if x!="apple"] #prints list without apple
print (newlist)