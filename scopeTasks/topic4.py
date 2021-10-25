# Basic Operators
# Variant 1
x = object()
y = object()
x_list = [x]*10
y_list = [y]*10
big_list = []
for x, y in zip(x_list, y_list):
        big_list.append(x)
        big_list.append(y)
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))
# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")

# Variant 2
x = object()
y = object()
x_list = [x]*10
y_list = [y]*10
big_list = x_list + y_list
print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))
# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
