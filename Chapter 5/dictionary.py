marks = {
    "ss":100,
    "Shubham":56,
    "Rohan":23
}

print(marks, type(marks))  #  {'ss': 100, 'Shubham': 56, 'Rohan': 23} <class 'dict'>

print(marks['ss'])   #100 

print(marks.keys())   #dict_keys(['ss', 'Shubham', 'Rohan'])

print(marks.values())   # dict_values([100, 56, 23])

print(marks.items())   # dict_items([('ss', 100), ('Shubham', 56), ('Rohan', 23)])

print(marks.get("ss"))  #100

marks.update({"ss":99, "ram":100})

print(marks.get("ss"))  #99

print(marks)    #{'ss': 99, 'Shubham': 56, 'Rohan': 23, 'ram': 100}

