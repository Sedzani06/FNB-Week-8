# Tuples

my_tuple = (1, 2, 3, 4, 5)

print(my_tuple)     # prints all elements
print(my_tuple[0])  # prints 1
print(my_tuple[2])  # prints 3
print(my_tuple[-1]) # prints the last value in the data collection in lists and tuples

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

conc_tuple = tuple1 + tuple2  # conc stand for concatinate
print(conc_tuple)

rep_tuple = tuple1 * 3   # rep stand for repeat
print(rep_tuple)


# tuple is unchangable , we cant add / remove  . we use it when we want to store a collection of elements that should not be changed in the execution of the program
# used for storing fixed collection of data such as RGB  codes,coordinates