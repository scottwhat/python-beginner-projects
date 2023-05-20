# lambda function = function written in 1 line using lambda keywor
# accepts any number of args
# like anon funcs, thrown away, not assigned
# lambda parameters: expression


double = lambda x: x * 2

multiply = lambda x,y : x*y

age_check = lambda age: True if age > 18 else False

print(age_check(19))
print(double(5))