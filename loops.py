# lets try to create an app with a counter on it where we input numbers until it hits the target which is 0. the system will keep allowing us to try again until we get it. this is a loop.
counter = 0
my_number = 9

while(counter < my_number):
    print(f"Counter's value is {counter}")
    # take note of the letter f introduced before the double quotes in the code above. this is used to format the strings instead of using str nd formatting individually.


    counter = counter + 1
    # the above code is the same as counter +=1

    # when you find yourself running an infinite loop, press control and c inside the terminal and the app will stop running.
    # looping means to keep running the same line of code over and over again. you can stop the loop by adding the condition.
