# ask user when was python created. it was 1991
# compare values. if correct, approve. if not,dont.

# request should be an integer.

# prompt the question
print("when was python created?")
# gather input from the user
date = int(input())

# compare answers
if date == int(1991):
    print("you are as current as you claim!")
    input("would you like to tell me what else has happened in 1991?")
else:
    if date <1991:
        print("you are close to the date, keep coming up!")
    else:
        print("that is way beyond the date. why not try again!")