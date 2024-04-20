
# pseudo code
# prompt the user the question- what is their favorite animal

print("what is your favourite animal?")
# gather input from the user, save it to a variable
input_animal = input()

# if the value is a dog, we print out an amazing message.
if input_animal == "dog":
    input(f"The {input_animal} is the most amazing animal in the world! Would you like to tell me more about your encounter with {input_animal}s?")
# but if it is not a dog, print out something else

else:
    if input_animal == "hedgehog":
        print(f"{input_animal}s are awesome too!")
    else:
        print(f"{input_animal}s do the most. I love {input_animal}s too!")

# end the code