import json
import requests
from html.parser import HTMLParser

dictword = {}                           #stores required words with occurance


class MyHTMLParser(HTMLParser):
              
    def __init__(self, *, convert_charrefs: bool = True, tag = "") -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.tag = tag

    def handle_starttag(self, tag, attrs):
        self.tag = str(tag)              #stores tags

    def handle_data(self, data):
        if (data.isspace()):
            return
        if(self.tag!="script"):          #words we need are except script part
            words = str(data).split()
            for w in words:
                if w.isalnum():          #word assumed to be Alpha-numeric
                    global dictword
                    if w in dictword:
                        dictword[w] += 1
                    else:
                        dictword[w] = 1

def main():
    
    url = "https://" + input ("enter a static url [ex: www.india.gov.in/] : ")
    webUrl = requests.get(url=url).text
    
    parser = MyHTMLParser()
    parser.feed(webUrl)
    
    result = open("result.json","w+")
    y= json.dumps(dictword)
    if result.mode=='w+':
        result.write(y)
    result.close()
     

if __name__ == "__main__":
    main()
  
