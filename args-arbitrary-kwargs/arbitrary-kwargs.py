# *args = allowed to pass multiple non key args - packed into a tuple
# **kwargs = allowed to pass multiple keyword args - packed into a dict

# * unpacking operator
# 1.positional 2.default 3. keyword 4. arbitrary

#args must be before kwargs
def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end="")


shipping_label("dr.", "spongebob", "squarepants", "III",
               street="123 fakey",
               apt="100",
               city="detroit",
               state="MI")

# def add(*args):
#
#     total = 0
#     for arg in args:
#         total += arg
#
#     print(total)
#     return total
#
# add(3,2,4,2)


#**kwargs saved into a dict
# def print_address(**kwargs):

    # for value in kwargs.values():
    #     print(value)
    #
    # for key in kwargs.keys():
    #     print(key)

#     for key, value in kwargs.items():
#         print(f"{key} = {value}")
#
# print_address(street="Blondes", city="Okinawa", state="Hawaii", zip="7474")

