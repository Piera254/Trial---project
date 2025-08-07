my_list = [23,45,7,8,90,67]
values =[10, 20, 30, 40]

for i in values:
    my_list.append(i)

my_list.insert(1, 15)

lst_2 = [50,60,70]
my_list.extend(lst_2)

print(my_list)

my_list.pop(-1)

print(my_list)

my_list.sort()
print (my_list)


value = 30
print(value)
print(my_list.index(value))



