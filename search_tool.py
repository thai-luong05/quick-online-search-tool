import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def contains(list, string):
    for i in list: 
        if i in string:
            return True
    return False

def search(query):
    url  = f'https://www.google.com/search?q={query}&start=0' #url for a search on google with query being your search phrase, this is searching on the first page only
    response = requests.get(url) #getting a response from the url
    if (response.status_code == 200): #this indicate that the requested is success
        #getting the html contents
        html = BeautifulSoup(response.text, 'html.parser')
        html_tags = html.find_all('a') #anchor tags are the tags that hold urls
        links = []#getting all the links
        for i in html_tags:
            if 'https' in str(i):
                i = str(i)[str(i).index('https'):str(i).index('&amp')] #extracting the link out of the tag
                if i != '' and not contains(['policies', 'preference', 'account', 'jpg', 'png', 'vi', 'vn'], str(i)):
                    # test = requests.head(i).headers.get("Content-Type", "")
                    # if 'image' not in test: #this is for filtering image results, dont have to care since this has been commented
                    links.append(i)

        for i in links:
            if 'https://www.google.com/search?sca_esv' not in i: #preventing from opening a google home page
                webbrowser.open_new_tab(i) #open the url in browser
                return #since we only need to open the first one, we stop here
                        
    else:
        print(f"Failed to get the search result, request status {response.status_code}")

#main
query = input('search > ')
while query != 'stop':
    search(query)
    query = input('search > ')
