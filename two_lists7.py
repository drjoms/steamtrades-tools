import sys
positional_parameter = sys.argv[1:]

from subprocess import call
call(["emacs", "list1.txt"])
call(["emacs", "list2.txt"])

list1=open('list1.txt')
list2=open('list2.txt')
list1=list(list1)
list2=list(list2)


list1_lower=[]
list2_lower=[]

person1wants=[]
person1has=[]
person2wants=[]
person2has=[]

for x in list1:
    list1_lower.append(x.lower())


for x in list2:
    list2_lower.append(x.lower())


for x in list1_lower:

    if 'i want...' in x:
        break
    person1has.append(x)


for x in list2_lower:

    if 'i want...' in x:
        break
    person2has.append(x)

'''
print('person one has:')
for x in person1has:
    print (x, end='')

print('person two has:')
for x in person2has:
    print (x, end='')
'''

for x in reversed(list1_lower):

    if 'i want...' in x:
        break
    person1wants.append(x)


for x in reversed(list2_lower):

    if 'i want...' in x:

        break
    person2wants.append(x)
'''
print('person one wants:')
for x in person1wants:
    print (x, end='')

print('person 2 wants:')
for x in person2wants:
    print (x, end='')
'''

print('I can offer you, in your want list:______________')
for x in person1has:
    if x in person2wants:
        print(x, end='')


print ('\n\n\n')
print('You have that I want:_______________')
for x in person2has:
    if x in person1wants:
        print(x, end='')

#call(["rm", "list1.txt"])
call(["rm", "list2.txt"])
