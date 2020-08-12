import feedparser, datetime

tistory_blog_uri="https://isholiday.tistory.com" #Your blog address here
feed = feedparser.parse(tistory_blog_uri+"/rss")

lst = []

for i in feed['entries']:
    dt = datetime.datetime.strptime(i['published'], "%a, %d %b %Y %H:%M:%S %z").strftime("%b %d, %Y")
    markdown_text = f"- [{i['title']}]({i['link']}) - {dt}<br>\n"
    print(i['link'], i['title'])

f = open("test.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()