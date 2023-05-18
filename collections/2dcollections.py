#
# fruits = ["apple", "orange", "banana"]
#
# vegetables = ["celery", "carrots", "potatoes"]
#
# meats = ["chicken", "fish", "turkey"]
#
# #array of arrays / list of lists
# groceries = [["apple", "orange", "banana"], ["celery", "carrots", "potatoes"],["chicken", "fish", "turkey"]]
#
#
#
# for collection in groceries:
#     for food in collection:
#         print(food)



#PHONE PAD

#tuple ordered, unchangeable and fast

num_pad = ((1,2,3),
           (4,5,6),
           (7,8,9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")

    print()

