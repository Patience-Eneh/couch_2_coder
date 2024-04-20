animals = [
 {"name": "capybara", "group": "mammal", "weight": 110},
 {"name": "hedgehog", "group": "mammal", "weight": 0.5},
 {"name": "bearded dragon", "group": "reptile", "weight": 1},
 {"name": "tortoise", "group": "reptile", "weight": 40},
 {"name": "hummingbird", "group": "bird", "weight": 0.01},
 {"name": "elephant", "group": "mammal", "weight": 10000},
 {"name": "ostrich", "group": "bird", "weight": 280},
 {"name": "python", "group": "reptile", "weight": 180},
 {"name": "blue whale", "group": "mammal", "weight": 300000},
 {"name": "lion", "group": "mammal", "weight": 350}
]

# []= List
# {}= Dictionaries

# 1. Print out all the animals names that are heavier than 100 pounds!
# Loop through all the animal dicts inside the animals List
# check if the animal weight value is more than 100.
# if it does, print our the names of the animal
print(1)
for animal in animals:
    if(animal["weight"]>100):
     print(animal["name"])

# 2. Print out the heaviest animal!
# Loop through all the animal dicts inside the animals List
# find out which animal has the highest value
# compare animals weights to each other
# once finished, display those with highest weight. 

#For the code, nominate the first animal as the heaviest. [0] gives us the first animal in the list. If animal is > than the heaviest animal, then heaviest animal = animal. same for the lightest
print(2)
heaviest_animal = animals[0]

for animal in animals:
    if(animal["weight"] > heaviest_animal["weight"]):
      heaviest_animal = animal
print(heaviest_animal)
#     #   a loop(for) compares  every animal from start to finish while executing the code.

# 3. Print out the lightest animal!

print(3)
lightest_animal = animals[0]

for animal in animals:
   if(animal["weight"] < lightest_animal["weight"]):
      lightest_animal = animal

print(lightest_animal)
# 4. Print out all mammals as a list!

print(4)
mammals=[]
for animal in animals:
   if(animal["group"] == "mammal"):    
      mammals.append(animal)
print(mammals)


# print out a list of animals with longer names than 7 letters
print(5)

animals_with_long_names = []

for animal in animals:
    if( len(animal["name"]) > 7):
       animals_with_long_names.append(animal)
print(animals_with_long_names )
      
# 
