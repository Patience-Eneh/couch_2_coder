# An algorithm is a step by step procedure to solve a problem or accomplish an end. 

pin = 1234
balance = 50000
number_of_trials = 3

input_pin = input("please enter your PIN number!")

while(number_of_trials>0):

    if (not input_pin.isdigit()):
        input("please type in a digit")
        break

    if(pin==int(input_pin)):
        print("your balance is " + str(balance))
        break
    else:
        number_of_trials-=1
        if(number_of_trials ==0):
            break
        # this is called a guard clause
        input_pin = input("incorrect PIN! Please try again! ") 


# notice the use of different values for input_pin. at the first instance, input_pin would prompt the user to enter their PIN numbeer for a correct pin, the code proceeds. else, if the pin is wrong, input_pin has been reassigned to incorrect pin, please try again.
# to indent, you use ctrl + [ or ], to indent to the left or right
# ctrl + / is used to write non readable lines on your codes
#  IMPROVE ON THE USE OF -= To mean a variable - 1 = the variables new value.k
# please note that the sequence of your code lines matters a lot when executing a code. learn to interprete your lines of code in english while writing them  
# stackoverflow is still one of the best forums to solve code problems.[]



# RED-GREEN -REFACTOR; method a good algorithm should follow.