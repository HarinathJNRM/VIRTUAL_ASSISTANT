# https://www.google.com/search?q=weather+patna
#https://www.google.com/search?q=weather+in+anantapur
#   span id="wob_tm"

from requests_html import HTMLSession
import speech_to_text

def weather():
    s = HTMLSession()
    #query1 = input("Enter Place")
    query = "Anantapur"

    url = f'https://www.google.com/search?q=weather+{query}'
    r = s.get(url, headers={'User-Agent': ''})  #For 'User-Agent' Go to Google Then Searc "My user agent" in search box, and paste it here.
    
    temp  = r.html.find('span#wob_tm' , first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_t' , first= True).text
    desc  = r.html.find('span#wob_dc' , first= True).text
    return temp+" "+unit+" "+ desc
    
    """temp = r.html.find('span#wob_tm', first= True).text
    unit = r.html.find('div.vk_bk.wob-unit span.wob_tm', first= True).text
    desc = r.html.find('span#wob_dc', first= True).text
    return temp+" " + unit+" "+ desc"""
#Main program
weather()