list = ["Apple", "Orange", 5, 345.06, False]
print(list) #['Apple', 'Orange', 5, 345.06, False]

print(list[0])  # Apple

list[0] = "Grapes"  #Unlike String lists are mutable
print(list[0]) #Grapes
print(list[1:4]) #['Orange', 5, 345.06]
list.append("sudhanshu")
print(list) #['Grapes', 'Orange', 5, 345.06, False, 'sudhanshu']

list.insert(2, 5464) # Insert such that its index 2
print(list) #['Grapes', 'Orange', 5464, 5, 345.06, False, 'sudhanshu']

list.pop(4)
print(list) #['Grapes', 'Orange', 5464, 5, False, 'sudhanshu']