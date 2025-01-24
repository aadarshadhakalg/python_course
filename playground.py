# Variables and Data Types
# Inlike C and C++, in Python we do not specify the data type for the variable

name = "Harish Aale" #String
age = 23 #Int
gpa = 3.8 #Float
gpas = [3.4, 3.0, 3.8, 4] #List, by default mutable.
city, province, country = "Kathmandu", "Bagmati", "Nepal"
graduated = False #Boolean o or 1
achievements = None #Null
parents = ("Gita Aale", "Ramu Aale") #Tuple aka Immutable List


# Since we have not defined types for the variable
# Let's see type inference in action
type(name)
type(age)
type(gpa)

# No of semester Harish Aale has passed ?
# len() function prints the length of a list
len(gpas)

# What is the gpa obtained by Harish Aale in 3rd semester?
print(gpas[2])

# What is the gpa obtained by Harish Aale upto 3rd semester?

print(gpas[:3]) #or
print(gpas[0:3])

# To Print whole list
gpas[:] #or
gpas[0:len(gpas)]
gpas[::]

# Print odd semester marks of Harish Aale
gpas[0:4:2] # Prints from zeroth index to third index with step size 2. 

# Modify Items in a List
gpas[0] = 3.0
gpas[-1] = 4

# We cannot modify a tuple. Why? Because tuple is immutable.
gpas[0] = "Sita Aale" # throws error


# Other than this
# Complex Numeric Literal
# c = 10+4j

#Set 
#Unordered and No Duplicates Values, no indexing
# vowels = {'a', 'e', 'i', 'o', 'u'}
# print(vowels)

# chars = {'a', 'b', 'a', 'e', 'z', 'z', 'x'}
# print(chars) 

# Dictionary
dictionary = {"name": "Alice", "Age": 30, "city": "New York"} 
name = dictionary["name"]
dictionary["occupation"] = "Engineer" 
del dictionary["city"]


####################
####################

# list = ["Hello", 23, 34.5,{1,2,1},("a","b")] # Valid??
#What is the output of ?
# list[4][0]
# list[5]
# list[3][0]
# list[0]




###### If Else
# gender = "Gay"

# if gender == "Male":
#     print("Harish probably has short hair.")
# elif gender == "Female":
#     print("Harish probably has long hair.")
# else:
#     print("Invalid Gender")

## Classwork GPA to Grade Converter


#### Loop

## For Loop

# fruits = ["apple", "banana", "orange"]
# for fruit in fruits:
#     print(fruit)

# for i in range(5): 
#     print(i)  # Prints numbers from 0 to 4


## While Loop
# count = 0
# while count < 5:
#     print(count)
#     count += 1


## Loop Control
# for i in [0,1,2,3,4,5,6,7,8,9]:
#     if i == 5:
#         break  # Exit the loop when i is 5
#     if i % 2 == 0:
#         continue  # Skip even numbers
#     print(i)  # Prints odd numbers from 0 to 4




# What are the gpas optained by Harish Aale in even semesters?
gpas = [3.4, 3.0, 3.8, 4] 
for index in range(len(gpas)):
    if index % 2 == 0:
        continue
    print(gpas[index])


# Calculate CGPA of harish aale?
total_gpa = sum(gpas)
num_semesters = len(gpas)
cgpa = total_gpa / num_semesters
print(cgpa)


#Functions