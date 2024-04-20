# numbers =[1,2,3,4,5,0]
# total = 0
# # for number in numbers:
# #     print(number)
# #     print(number *3)

# for number in numbers:
#     if (number !=2):
#          total += number
#     # remember that the command above reassigns values. for example, total + number = new total, which will then be used to calculate for the num ber 2, get a new total again and reassign again, and so on.

# print(total)

# Students = ["Anna", "Colin", "ed", "Joe"]

# for Student in Students:
#     print(Student.casefold())

# combining lists and dictionaries
# to duplicate these values below, click on alt+shift+down arrow
students = [
    {"name": "Anna", "result":92},
    {"name": "Ed", "result":88},
    {"name": "Colin", "result":98},
    {"name": "Joe", "result":67},
    
]

# # to print out only their names,
# for student in students:
#     print(student["name"])



#     # to print out only their results,
# for student in students:
#     print(student["result"])

# # to print out names begining with letter c

# for student in students:
#     if student["name"].startswith("E"):
#         print(student["name"])
#     # since name is a list inside a dictionary, it will be covered in square brackets here. hence ["name"]

# to print out total result only,
# total = 0
# for student in students:
#     total +=student["result"]
# print(total)
# # for the above, always remember that the print should be properly indented starting from the first indent point, else, the results will produce cumulative values 



# to calculate the average of the results, we do the below;
total=0
for student in students:
    total+=student["result"]
mean_result =total/len(students)
print(mean_result)


