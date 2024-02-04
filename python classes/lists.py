n1 = [x for x in range(10) if x % 2 == 0]   #[0, 2, 4, 6, 8]
n2 = [x for x in range(10) if x % 2 != 0]   #[1, 3, 5, 7, 9]

zipped = list(zip(n1,n2))   #[(0, 1), (2, 3), (4, 5), (6, 7), (8, 9)]
zipped2 = zipped[::-1]  #[(8, 9), (6, 7), (4, 5), (2, 3), (0, 1)]
zipped2.extend(n2[::-1])    #[(8, 9), (6, 7), (4, 5), (2, 3), (0, 1), 9, 7, 5, 3, 1]

n1[-5:-5] = [999]   #[999, 0, 2, 4, 6, 8]
n1[1:4] = ['a','b', 'c']    #[999, 'a', 'b', 'c', 6, 8]

lst = sorted(n1, key = lambda x: (isinstance(x, int), x), reverse=True) #[999, 'a', 'b', 'c', 6, 8]
print(lst)
remove  = lst.pop() #remove and return the last element in the list
remove  = lst.pop(2) #remove and return the item of index 2
remove  = lst.remove("b") #remove and the first occurence of "b"
lst.insert(2, "d") # insert at index 2, value
lst.extend([iterable]) # add the items in the specified iteable to the end of the list

lst[:] # start at the beggining the list : end of the list
lst[1:] # start at index 1 : end of the list
lst[1:6] # start at index 1 : end at index 6, but not include!

lst[::] # start : end : step (default 1)
ls [1:6:2] # start at index 1 : stop but not include index 6 : skip the N element
lst[:-1] # start at the beggining the list : end but not include the last element
lst[::-1] # reverse a list (fast way)
lst[2:4] = [1000, 1000] # replace the items on index 2, 3 with items from = ...

contains = 2 in lst # True / False
index = lst.index(2)     # returns the index of element
lst.count(3)    # return the number of occurremces of value in the list
lst.sort()  # modify the list in place, returns none, attributes reverse=True for descending
lst.reverse()   # reverse the list in place
sorted(lst)     # returns a new list sorted
reverse(lst)    # the same

#copy the list:
lst2 = lst[:]

#zip
names = ["Andreea", "Marian", "Vlad"]
ages = [46,45,7]
zipped = zip(names, ages)   #("Andreea", 46), ("Marian", 45), ("Vlad", 7) creates tuples with coresponding indexes, returns a iterator
zipped_lst = list(zipped)   #[("Andreea", 46), ("Marian", 45), ("Vlad", 7)]

lst = [x for x in range(10)] # list comprehensions
lst = [x for x in range(10) if x % 2 == 0] # list comprehensions

tup = (1,2,3)   # imutable iterable 
tup[0] = 100 # will not work
