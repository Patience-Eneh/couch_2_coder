student = {
    "first_name": "Anna",
    "last_name": "Henderson",
    "subject": "chemistry",
    "result": 92,
    "contact_details": {
        "phone": "+441234567",
        "email": "enehpatience9@gmail.com"
    }
}
# print(student["first_name"])

# if you want to print out the first name in student, do the below.
# print(student["first_name"])


# however, if you want to find out if there is a first name in  student, do the below;
print("first_name" in student)

# you can modify existing results and also add a value that never existed for example,
student["date_of_birth"]= "1990/01/01" 

# the command below will print out all the dictionary keys available from your data above. KEYS
print(student.keys())


# the command below will produce all the values of the represented variables. e.g, anna, hernderson, chemistry, 92, etc..VALUES
print(student.values())

# to get the phone number printed out only; in accessing details from a dictionary, you use a square bracket to parse your code. STUDENT is a dictionary, CONTACT DETAILS is another dictionary in side the dictionary, so for both codes, we use a square bracket
print(student["contact_details"]["phone"])