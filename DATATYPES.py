# Data Types is the categories of the data which are are storing in the 
# variables which can be - numbers , characters , alphabets , True and False , decimal values

#1. NUMBER TYPES
print("Below is the example of number type datatypes")
normalno = 25 
floatno = 5.9
complexno = 1j

# Now checking the data types are correct or not using type()
print(type(normalno))
print(type(floatno))
print(type(complexno))

# Below is the output

# <class 'int'>
# <class 'float'>
# <class 'complex'>

# Conversion of the numeric datatypes from one to another 
x=1 #int
y=2.8 #float
z=1j #complex

#converting  int to float
a = float(x)

#converting float to int
b = int(y)

#converting int to complex
c = complex(x)

#NOTE -  We can't change the complex no to any other numeric type
print(a)
print(b)
print(c)


print(type(a))
print(type(b))
print(type(c))
# OUTPUT

# 1.0
# 2
# (1+0j)
# <class 'float'>
# <class 'int'>
# <class 'complex'>



#2. SEQUENCE TYPES
#2.1 Str
string = "hello" 
print(string)
print(type(string))
# inside the string we can also define multiline string
multilinestring = "My name is Shriyanshu and right now im practicing python"
multilinestring2 = """Now by using 3 double or single quotes we 
can print the paragraph same as we have written in 
the code """
print(multilinestring)
print(type(multilinestring))
print(multilinestring2)
print(len(multilinestring2)) #to check the length of the string
# Output
# hello
# <class 'str'>
# My name is Shriyanshu and right now im practicing python
# <class 'str'>
# Now by using 3 double or single quotes we
# can print the paragraph same as we have written in
# the code
# 104


#2.2 List 
# List is a collection which is ordered and changeable. Allows duplicate members.
# Uses []
mylist = ["apple","banana","cherry"]
print(mylist)
fstelement = mylist[0]  # Accesses the first element (1)
print(fstelement)
mylist[2] = "mango"
print(mylist)

# append() method to add an element to the end of the list.
mylist.append("cherry")
print(mylist)
# pop() method to remove and return the last element from the list.
popped = mylist.pop(2)
print(mylist)
# Output
# ['apple', 'banana', 'cherry']
# apple
# ['apple', 'banana', 'mango']
# ['apple', 'banana', 'mango', 'cherry']
# ['apple', 'banana', 'cherry']


#2.3 Tuples
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Uses ()
mytuple = ("zebronics" , "soney" , "samsung" , "nokia","nokia")
print(mytuple)
print(type(mytuple))
#tuple should have atleast two members then it called as tuple
mytuple2 = ("zebronics")
print(type(mytuple2)) 
# output
# ('zebronics', 'soney', 'samsung', 'nokia', 'nokia')
# <class 'tuple'>
# <class 'str'>



#3. MAPPING TYPES

#dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

dictionary = {"name" : "Shriyanshu" , "age":19 , "city":"sitka"}

variable = dictionary["name"]
print(dictionary)
print(variable)

dictionary["email"] = "shriyanshu@gmail.com" # Adding new key-value pair
dictionary["age"] = 23 # Modifying the value associated with key"age"
print(dictionary)

del dictionary["city"] # Remove the key-value pair with the key "city"
age = dictionary.pop("age")  # Removes the key-value pair with the key "age" and returns the value
print(dictionary)

