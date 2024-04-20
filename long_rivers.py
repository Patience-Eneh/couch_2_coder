rivers = [
    {"name": "Nile", "length": 4157},
    {"name": "Yangtze", "length": 3434},
    {"name": "Murray-Darling", "length": 2310},
    {"name": "Volga", "length": 2290},
    {"name": "Mississippi", "length": 2540},
    {"name": "Amazon", "length": 3915}
  ]
 
# Task 1: Printing out each river's name
# print("Task 1:")
# for river in rivers:
#     print(river["name"])
# total=0
# # Task 2: Calculate and print total length of all rivers
# for river in rivers:
#     total+=river["length"]
# print(total)
    
for river in rivers:
    total_length = sum(river["length"]for river in rivers)
print(total_length)
# # total_length = sum(river["length"] for river in rivers)
# # print("\nTask 2:")
# # print(f"Total length of all rivers: {total_length} miles")

# # Extension 1: Print river names beginning with "M"
# print("\nExtension 1:")
# for river in rivers:
#     if river["name"].startswith("M"):
#         print(river["name"])

# # Extension 2: Print river lengths in kms
# print("\nExtension 2:")
# for river in rivers:
#     length_km = river["length"] * 1.6
    # print(f"{river['name']}: {length_km:.2f} km")
 