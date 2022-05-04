names = {"Bogdan", "Dmitrii", "Petr", "Petr"}
# add
names.add("Olga")
# update
names.update([1 , 3, 5])
# remove
names.remove("Bogdan")
# pop
names.pop()
# copy
names2 = names.copy()
# union
names3 = {"Kykyshka", "Pet9", "Polina"}
names4= names3.union(names2)
# intersection
set1 = {1, 4, 6, 7, 8}
set2 = {4, 5, 2, 9, 4}
set3 = set1.intersection(set2)
# difference
set4 = set1.difference(set2)
#  symmetric_difference
set5 = set1.symmetric_difference(set2)
# issubset
check_set = set1.issubset(set2)
#  issuperset
check_superset = set2.issuperset(set1)
#  isdisjoint
x = set1.isdisjoint(set2)
# len
print(len(set1))
# clear
set2.clear()


