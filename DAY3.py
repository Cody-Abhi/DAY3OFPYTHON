# List--. [], hetro, duplication, indexing, slicing, functions, methods

# empty list
# empty_list = []
# print(empty_list)


#homo list
# color = ["red", "green", "blue", "yellow", "purple", "orange"]
#print(color)

# #hetro list
# mixed_doubles = ["yug",20,"Anamika", 22]
# print(mixed_doubles)

#dublication in list
# fruits = ["apple", "banana", "orange", "apple", "grape"]
# print(fruits)

# indexing, slicing 

# numbers = [10, 20, 30, 40, 50]
# print(numbers[-1])  
# print(numbers[::-1])  

# # functions-----------------------------------------------------------------
# # to add element----------------------------------------

# numbers.append(100)
# print(numbers)

# numbers.insert(2, 200)
# print(numbers)

# # to remove element----------------------------------------------------

# # numbers.remove(20)  
# # print(numbers)

# numbers.extend("hi")
# numbers.extend([60, 70, 80])
# print(numbers)

# numbers.insert(3, 1000)
# print(numbers)


# numbers.pop(1)
# print(numbers)

# numbers.clear()
# print(numbers)

# del numbers
# print(numbers)

# sublist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # print(sublist[1])
# # print(sublist[1][1])
# print("Printing cols")
# for rows in sublist:
#     # print(rows)
#     for cols in rows:
#         print(cols, end=" ")
#     print()


# #concatination
# fruits = ["apple", "banana", "orange", "grape"]
# colors = ["red", "green", "blue", "yellow"]
# combined = fruits + colors
# print(combined)

# num1 = [10, 20, 30, 40, 50]
# num2 = [1, 2, 3, 4, 5]

# for element in range(0,5):
#     print(num1[element] + num2[element])

# for i in range(len(num1)):
#     print(num1[i] + num2[i])

# final_num_result = []

# for index in range(0,5):
#     final_num_result.append(num1[index] + num2[index])
# print(final_num_result)



# ---------------list combination----------------

# final_num_result2 = [num1[index] + num2[index] for index in range(0,5)]
# print(final_num_result2)

# multiple_of_two = [element * 2 for element in num1]
# print(multiple_of_two)

# print("Printing rows")
# for rows in sublist:
#     for cols in rows:
#         print(cols, end=" ")
#     print(rows)



# list1 = [10, 20, 30, 40, 50]
# list2 = list1
# print(list1) #pass by reference
# print(list2)

# list2[0] = 100
# print(list1)
# print(list2)


# list1 = [10, 20, 30, 40, 50]
# list2 = list1.copy()  # creates a shallow copy
# print(list1) #pass by value
# print(list2)

# list2[0] = 100
# print(list1)
# print(list2)


# tuple --> # immutable, hetro, duplication, indexing, slicing

# tup1 = ()
# print(type(tup1))  # empty tuple

colors = ("red", "green", "blue", "blue")
# print(colors)
# print(colors[0][-1])  # indexing

# nums= (10)
# print(nums)
# print(type(nums))  # int, not a tuple

# nums2 = (20)
# print(nums2)
# print(type(nums2))  # int, not a tuple  


#functions

# print(colors.index("blue"))  

# print("Multi index for same value")
# for element in colors:
#     if "blue" in element:
#         print(colors.index(element))  # will return first index only


# tup3 = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")

# list2  = list(tup3)  # converting tuple to list
# print(list2)

# colors = ("red", "green", "blue", "yellow")
# for index in range(len(colors)):
#     if colors[index] =="blue":
#         print("Blue is present at index:", colors.index(colors[index]))

# colors = ("red", "green", "blue", "yellow")
# for index in range(len(colors)):
#     if colors[index] == "blue":
#         print(f"Index:{index} , value = {colors[index]}")  # using index directly
        

#dictionary --> {key:value}, hetro, duplication not allowed, indexing not allowed, slicing not allowed


# dict1 = {}  # empty dictionary
# print(type(dict1))

# about_person = {"name": "Abhinav" , "age": 25, "city": "Delhi"}
# print(about_person)

# about_person = {"name": "Abhinav" , "age": 25, "city": "Delhi"}
# print(about_person["name"])

# address = {20202: "Lucknow"}
# # print(address)

# student_id = {(101,102,103,104):"Abhinav"}
# print(student_id)
# print(student_id[(101,102,103,104)])  # accessing value using key

# fruits = {"mango":["yellow", "2kg"], "banana":{"color": ["yellow", "red"]}}
# print(fruits["banana"]["color"])


# #finctions

# student = {"name": ["A","B","C","D"], "age": [10, 20, 30, 40]}
# print(student)
# sid= {"ids": [101, 102, 103, 104]}
# student.update(sid)
# print(student)

# student["id"]= [101, 102, 103, 104]
# print(student)

# #to updat any 
# student["blood_group"] = ["A+", "B+", "O+", "AB+"]
# print(student)

# student.pop("id")
# print(student)

# student.popitem()  # removes last item or arbitary key 
# print(student)

# #Sets => {}
# empty_set = {}
# print(empty_set)
# print(type(empty_set))

# empty_set2 = set()
# print(empty_set)
# print(type(empty_set2))

# team = {"Arjun", "Pragnandha", "Gukesh", "Akshay"}

# # Operations
# team.add("Vishwnathan Anand")
# print(team)

# team.add("Vidhit")
# print(team)

# team.add("Divya")
# print(team)

# team.remove("Vishwnathan Anand")
# print(team)

# # Maths functions
# set1 = {1,2,3,4,5}
# set2 = {1,2,7,8,9}

# print(set1.intersection(set2))
# print(set1.union(set2))
# print(set1.symmetric_difference(set2))
# print(set1.difference(set2))
# set3 = {2,7,10, 11, 12}

# print(set1 & set2)
# print(set1 | set2)
# print(set1 ^ set2)
# print(set1 - set2)


# print(set1.union(set2).union(set3))
# print(set1 | set2 | set3)
# print(set1.union(set2) | set3)

# ----------------------FILE HANDELING----------------------

# file2 = open("Data.txt", "r")  # open file in write mode
# print(file2.read())
# print(file2.readline())
# print(file2.readlines())

# file2.open("Data.txt", "r")  # open file in read mode
# file2.write("Hello, this is a test file.\n")

# file3 = open("Data.txt", "r")  # open file in append mode
# file3.write("Adding more content to the file.\n")
# print(file3.read())

# copy from 1 to another file

file = open("Data.txt", "r")  # open file in read mode
file2 = open("Data2.txt", "w")  # open file in write mode
for data in file:
    file2.write(data)  # write data to the new file
print(file2.read())  # read the new file to verify content
file2.close()  # close the file
print(file2.read())  # this will not work as file2 is closed")
