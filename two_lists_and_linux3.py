import sys
import requests
from threading import Thread

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


#this function checks if game is on linux. Regardless if it's in my wish list.
#may be its new game i am not aware of
#def check_for_linux(input):
def check_for_linux(input):
    #print('check fo rlinux game?', input)
    search_page = 'https://store.steampowered.com/search/?term='
    search_page = search_page + input
    page = requests.get(search_page)

    actual_data = str(page.content)

    game_search_string = str('a href="https://store.steampowered.com/app/')
    first_slash = actual_data.split(game_search_string, 1)
    href_content = str(first_slash[1])
    # shorter_href = href_content.split('"', 1)

    href_content = href_content.split('"', 1)
    # print(href_content[0])
    full_link_to_game = 'https://store.steampowered.com/app/' + str(href_content[0])


    data_page = requests.get(full_link_to_game)
    data_page_content = str(data_page.content)

    if data_page_content.find('platform_img linux') > 0:
        print('linux supported, name of game: ', input, full_link_to_game)



for x in person2has:
    try:
        dont_want_titles = open('linux_titles.txt','r')
        dont_want = str(dont_want_titles.read())
        if x in dont_want:
            print('dont want that title:', x)
        else:
            Thread(target=check_for_linux(x)).start()
        dont_want_titles.close()

    except:
        None

    if x in person1wants:
        print('i want:', x, end='')


#call(["rm", "list1.txt"])
call(["rm", "list2.txt"])

