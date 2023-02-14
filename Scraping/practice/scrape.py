import csv
from requests_html import HTML, HTMLSession

with open('Python/Scraping/practice/simple.html', 'r') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)
print(match.html)

# session = HTMLSession()
# r = session.get('https://coreyms.com/')
# links = r.html.links
# 
# for link in links:
#     print(link)

## csv_file = open('Website-text_scrape.csv', 'w')
## csv_writer = csv.writer(csv_file)
## csv_writer.writerow(['headline','text','video_src'])


## articles = r.html.find('article')

## for article in articles:
##     try:
##         headline = article.find('.entry-title-link',first=True).text
##         print(headline)
## 
##         text = article.find('.entry-content p', first=True).text
##         print(text)
## 
##         contentSpan = article.find('.entry-content span', first=True)
##         video_src = contentSpan.find('iframe', first=True).attrs['src']
##         video_id = video_src.split('/')[-1].split('?')[0]
##         yt_link = f'https://www.youtube.com/watch?v={video_id}'
## 
##     except Exception as e:
##         yt_link = None
##     
##     print(yt_link)
##     print()
## 
##     csv_writer.writerow([headline,text,yt_link])
## 
## csv_file.close()