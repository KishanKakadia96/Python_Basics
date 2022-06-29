# Lists can be homogeneous or heterogeneous

List = [3, 22, 30, 5.3, 20]
print(List)

# Accessing values

print(List[0])  # to access 3
List[1]  # to access 22
List[4]  # to access 20
List[-1]  # to access 20

# List slicing

print(List[:])  # [3, 22, 30, 5.3, 20] all the members of the List
List[1:3]  # [22, 30] members of the List from index 1 to index 3, without the member at index 3
List[:4]  # [3, 22, 30, 5.3] members of the List from index 0 to index 4, without the member at index 4
List[2:-1]  # [30, 5.3] members of the List from index 2, which is the third element, to the second to the last element in the List, which is 5.3

# Updating Lists

List = ['physics', 'chemistry', 'mathematics']
List[0] = 'biology'
print(List)

# Deleting List elements

List = [3, 5, 7, 8, 9, 20]

List.remove(3)
# List.pop[0]
# del List[0]

# Appending List elements

List_1 = [3, 5, 7, 8, 9, 20]
List_1.append(3.33)
print(List_1)  # [3, 5, 7, 8, 9, 20, 3.33]

List_1.append("cats")
print(List_1)  # [3, 5, 7, 8, 9, 20, 3.33, "cats"]

# lconverts a tuple object a List
animals = ('cat', 'dog', 'fish', 'cow')
print(list(animals))  # ['cat', 'dog', 'fish', 'cow']

# Looping through lists

List = [10, 20, 30, 40, 50, 60, 70]

for elem in List:
    elem = elem + 5
    print(elem)

# To loop through the first three elements of the list, and delete all of them
for elem in List[:3]:
    List.remove(elem)

# To loop through the 3rd (index 2) to last element on the list, and append them to a new list
List = [10, 20, 30, 40, 50, 60, 70]
new_list = []
for elem in List[2:]:
    new_list.append(elem)
print("New List: {}".format(new_list))

# List Comprehensions
# Normal
list_of_squares = []
for int in range(1, 10):
    square = int ** 2
    list_of_squares.append(square)
print(list_of_squares)

# Using list comprehension
list_of_squares_2 = [int**2 for int in range(1, 10)]
print('List of squares using list comprehension: {}'.format(list_of_squares_2))
