#Tuple

# tuple=(1,2,3,4,5,3)
# print(tuple[1])
# print(tuple.count(3))
# print(tuple.index(3))

#set
# set={1,2,3,4,5,5,5,5}
# print(set)
# set.add(6)
# print(set)
# print(1 in set)
# print(len(set))

my={3,4,4}
your={3,4,5,6,7}
# print(my.difference(your))
# print(my)
# my.difference_update(your)
# print(my)
# my.discard(3)
# print(my)
print(my.intersection(your))
print(your & my)
print(my.isdisjoint(your))
print(my.union(your))
print(my.issubset(your))

print(your.issuperset(my))