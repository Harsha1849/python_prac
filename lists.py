#declaring list and printing
my_list=["cherry","apple","banana","mango"]
print(my_list[-2]) #0 would print cherry and -1 would print mango

#slicing and accessing range
my_list2=["apple","banana","mango","cherry","kiwi","guava"]
print(my_list2[2:4]) #2nd position till 3rd position with 4th not included

my_list3=["apple","banana","mango","cherry","kiwi","guava"]
print(my_list3[:3]) #By leaving out the start value, the range will start at the first item

my_list4=["apple","banana","mango","cherry","kiwi","guava"]
print(my_list4[2:]) #By leaving out the end value, the range will go on to the end of the list

#append method
my_list4.append("pineapple") #adds new element at the end
print (my_list4)

#insert method
my_list.insert(0,"pineapple") #can add new element at any position
print (my_list)

#extend method
my_list.extend(my_list2) #merge lists
print (my_list)

#remove method
my_list.remove("pineapple")
print (my_list)

my_list.remove("banana") #If there are more than one item with the specified value, the remove() method removes the first occurrence
print (my_list)

#remove specified index
my_list.pop(1)
print(my_list)

my_list.pop() #If you do not specify the index, the pop() method removes the last item.
print(my_list)

#delete entire list
del my_list
#print (my_list) #shows error

#clear method
my_list2.clear() 
print (my_list2)