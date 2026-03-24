"""
List:
-stored in single variable
-ordered(means have sequence)
-mutable
- starting from index 0
-Syntax:
    list_name = [item1,item2,item3....]
 -printing list
    print(list_name) //for whole list
    print(list_name[index_number]) //for specfic index
-operations on list
    append() -> list_name.append(item)    #for adding element in the end
    insert()  -> list_name.insert(position,item)   #for adding element at a specific position
    pop(index) -> list_name.pop()   #remove last element if index is not given, remove element of given index 
    remove(item) -> list_name.remove(item)   #remove the specific item in list
    clear()  -> list_name.clear()   #remove all the element from the list
"""

"""
Looping Through List:
# for printing all the list
for item in list_name:
    print(f"-{item}")
    ->>>>output
    -item_1
    -item_2

#with index
for index, item in enumerate(list_name):
    print(f"{index+1}. {item}")
    ->>>>output
    1.item_1
    2.item_2
"""

"""
List Methods:
sort the list -> list_name.sort()
reverse the list ->list_name.reverse()
"""
"""
condition check if any item in list or not
 if not list_name:
"""