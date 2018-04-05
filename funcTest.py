def extend_list(val, list=[]):
    list.append(val)
    return list

list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print(list1) # list1 = [10, 'a']
print(list2) # list2 = [123, []]
print(list3) # list3 = [10, 'a']

class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)  # [1,1,1]
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)  # [1,2,1]
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)  # [3,2,3]