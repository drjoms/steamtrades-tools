import requests
import sys



def content_extract(page_addr):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}  # This is chrome, you can set whatever browser you like
    #(because site doesnt like 'non browsers')

    #print('page addr: ', page_addr)
    page_content = requests.get(page_addr, headers=headers)
    page_content = page_content.text
    #returns string
    return page_content

def has(page_content):
    # exact list of what user has. no disambiguations
    page_nohead = page_content.split('<div class="trade_heading">I have...</div><div class="have markdown">')
    #print(page_nohead[1])
    #print('page_nohead',page_nohead)
    page_nohead = str(page_nohead[1])
    page_notail = page_nohead.split('</p></div>')
    page_notail = page_notail[0]
    list_of_games= page_notail.split('<br />\n')
#    returns list
    return (list_of_games)


def wants(page_content):
    #exact list of what user wants. no disambiguations
    page_nohead = page_content.split('<div class="trade_heading">I want...</div><div class="want markdown">')
    page_nohead = str(page_nohead[1])
    page_notail = page_nohead.split('</div><div class="markdown">')
    page_notail = page_notail[0]
    list_of_games = page_notail.split('<br />\n')
    #returns list
    return(list_of_games)


def has_bucket(page_content):
    # exact list of what user has. no disambiguations
    page_nohead = page_content.split('<div class="trade_heading">I have...</div><div class="have markdown">')
    #print(page_nohead[1])
    #print('page_nohead',page_nohead)
    page_nohead = str(page_nohead[1])
    page_notail = page_nohead.split('</p></div>')
    page_notail = str(page_notail[0])
    #returns string
    return (page_notail)

def wants_bucket(page_content):
    # exact list of what user has. no disambiguations
    page_nohead = page_content.split('<div class="trade_heading">I want...</div><div class="want markdown">')
    #print(page_nohead[1])
    #print('page_nohead',page_nohead)
    page_nohead = str(page_nohead[1])
    page_notail = page_nohead.split('</div><div class="markdown">')
    page_notail = str(page_notail[0])
    #returns string
   # print('list of games user wants:',page_notail)
    return (page_notail)

def other_wants(user_has, other_user_wants):
    games_that_mached=[]
    #user_has - string, other_user_wants - list
    user_has = user_has.lower()
    #print ('user_has:________________________-', user_has)
    for x in other_user_wants:
        entity=x.lower()
        if entity in user_has:
            games_that_mached.append(entity)
        else:
            None
    return (games_that_mached)


my_addr=input('insert your trade site url:\n\n')
other_user_addr=input('insert other dudes url:\n\n')

if my_addr == '':
    want_need_file=open('want_need.txt', 'r')
    my_addr= want_need_file.read()
    want_need_file.close()
else:
    want_need_file=open('want_need.txt', 'w')
    want_need_file.write(my_addr)
    want_need_file.close()


if my_addr == '':
    print ('other dude address is empty?')

if other_user_addr == '':
    print ('other dude address is empty?')

i_have=has(content_extract(my_addr)) #returns list
he_has=has_bucket(content_extract(other_user_addr))#returns string
i_want=wants(content_extract(my_addr))#returns list
he_wants=wants_bucket(content_extract(other_user_addr))#returns string

games_matched_for_him = other_wants(he_wants, i_have)
games_matched_for_me = other_wants(he_has, i_want)
print('games_matched_for_him\n\n', games_matched_for_him,'\n\n')
print('games_matched_for_me\n\n', games_matched_for_me,'\n\n')