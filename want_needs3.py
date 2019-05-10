'''    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.'''


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
    page_notail = page_nohead.split('</div>')
    page_notail = str(page_notail[0])
    #returns string
   # print('list of games user wants:',page_notail)
    #print(page_notail)
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

def strip_html(html_content):
    html_content_head_split = html_content.split('</')
    html_content_head_split = str(html_content_head_split[0])
    html_content_tail_split = html_content_head_split.split('>')
    html_content_tail_split = str(html_content_tail_split[-1])
    #returns string, single game name, supposedly...
    return html_content_tail_split



def check_steam(input):
    search_page = 'https://store.steampowered.com/search/?term='
    search_page = search_page + input
    page = requests.get(search_page)
    actual_data = str(page.text)
    app_page = '<a href="https://store.steampowered.com/app'
    # <a href="https://store.steampowered.com/app
    if app_page in actual_data and input != '' and input != ' ':
        print('game found in steam database')
        slice_off_left = actual_data.split('<a href="https://store.steampowered.com/app')
        slice_off_left = str(slice_off_left[1])
        slice_off_right = slice_off_left.split('"')
        slice_off_right = str(slice_off_right[0])
        first_result = slice_off_right
        title_page = 'https://store.steampowered.com/app' + first_result
        title_page = str(title_page)
        title_content = requests.get(title_page)
        title_content = title_content.text
        if '<div class="game_area_sys_req sysreq_content " data-os="linux">' in title_content and input != '' and input != ' ':
            print('Linux supported game and URL:"', input, '"', title_page)
        return input
    else:
        return 'game not found'


def check_for_linux_games():
    import webbrowser

    list_of_games= he_has.split('\n')
    #so we got list of games, with HTML tags. gonna strip tags:
    for x in list_of_games:
        if '<' in x:
            check_steam(strip_html(x))

        else:
            check_steam(x)

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
#print('games_matched_for_him\n\n', str(games_matched_for_him),'\n\n')
#print('games_matched_for_me\n\n', str(games_matched_for_me),'\n\n')

print('I have those games you want', str(games_matched_for_him),'\n\n')
print('I want that:', str(games_matched_for_me),'\n\nLets have an exchange? State your offer, please.')

positional_parameter = str(sys.argv[1:])
#print('pos paremeter is: ', str(positional_parameter))
#print('type is: ', type(positional_parameter))

#checking other dude's have' collection for linux title
if 'l' in positional_parameter:
    check_for_linux_games()
