#filter() = creates a collection of elements from an interable
#filter(function, iterable)

#make a seperate list of friends 18>

friends = [("Rachel",19),
           ("Monica",18),
           ("Phoebe",17),
           ("Joey",16),
           ("Chandler",21),
           ("Ross",20)]

# def age_check(data):
#     return data[1] >= 18

age_check = lambda data: data[1] >= 18

filtered_friends = filter(age_check, friends)

filtered_friends = list(filtered_friends)
print(filtered_friends)