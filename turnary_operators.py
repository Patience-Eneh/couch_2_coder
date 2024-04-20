# input_animal = "goat"
# input("what is your favourite animal?")

# result = "Such nice animal" if input_animal == "dog" else "no way. call the cops!"
# print(result)

# BOOLEAN TRUE OR FALSE, USE OF AND.
Patience_hungry = True
Patience_tired = True

if Patience_hungry == True and Patience_tired == True:
    print("its best to avoid you!")

# this can also be written in the way below;
if Patience_hungry and Patience_tired:
    print("its best to avoid you!")

# BOOLEAN TRUE OR FALSE AND THE USE OF OR
Patience_hungry = True
Patience_tired = False

if Patience_hungry == True or Patience_tired == True:
    print("you might need food or get a rest!")

# this can also be written in the way below;
if Patience_hungry or Patience_tired:
    print("you might need food or get a rest!")


