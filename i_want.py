import sys
import time
from random import randint
positional_parameter = sys.argv[1:]

from subprocess import call
call(["emacs", "list1.txt"])
call(["emacs", "list2.txt"])

list1=open('list1.txt')
list2=open('list2.txt')
list1=list(list1)
list2=list(list2)

for x in list1:
    URL=str('empty string')
#    URL="https://www.steamtrades.com/trades/search?have=" + str(x) + str("&want=") + str(list2)
    for y in list2:
        URL = "https://www.steamtrades.com/trades/search?have=" + str(x) + str("&want=") + str(y)
        print (URL)
        call(["firefox", URL])
        time.sleep(randint(0, 9))



