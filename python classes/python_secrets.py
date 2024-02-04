list_of_pairs = [["A", "B"],["C", "D"],["E", "F"],]

second_element_from_list = [b for _,b in list_of_pairs] # ['B', 'D', 'F']

#items = ["a", "b", "c", "d", "e"]

# generator
# def get_data():
#     for i in range(10):
#         yield i
#     yield -1

# def process(data):
#     print(data)

# gen = get_data()

# while(data := next(gen)) != -1:
#     process(data)

# def f(x):
#     return x -1

#result = [f(x) for x in range(10) if f(x) > 3]
# result_walrus = [result for x in range(10) if (result := f(x)) > 3]
# print(result_walrus )

list2 = [10,10,10]
result = sum([x for x in list2])
list = [{"name": "A", "value" : 10},{"name": "B", "value" : 10},{"name": "C", "value" : 10},]
result2 = sum(x["value"] for x in list)
print(result2)