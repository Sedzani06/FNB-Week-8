my_set = {1, 2, 3, 4, 5}

print(my_set)

my_set.add(6)   # adds 6 to the set
print(my_set)

my_set.remove(3)  # removes 3 from the set
print(my_set)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union = adds sets together and removes any duplicate data
union_set = set1.union(set2)
print(union_set)

# Intersection
inter_set = set1.intersection(set2)  # prints the common elements within the sets which is 3 here
print(inter_set)

# Difference
# finds elements that are in one set and not present in the other set
diff_set = set1.difference(set2) # find element that are in set1 and not in set2
print(diff_set)


# We use sets when we need to work with collection of unique elements and perform operation like difference,intersection and union between sets
# sets are also used to remove duplicate data from the list of collection checking membership efficiently