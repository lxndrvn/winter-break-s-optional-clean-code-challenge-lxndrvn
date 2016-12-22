import random
import shutil
import feedparser  # -> pip install feedparser
import os
import textwrap
import bs4  # -> pip install beautifulsoup4
import urllib

feed = feedparser.parse("http://index.hu/24ora/rss/")

i = 0
while i < 5:
    e = feed['entries'][i]
    max_len = len(e.title)
    print(e.title)
    if len(e.id) > max_len:
        max_len = len(e.id)
    print(e.id)
    if e.summary:
        if len(e.summary) > max_len:
            max_len = len(e.summary)
        print(e.summary)
    size = shutil.get_terminal_size((80, 20))
    if max_len > size.columns - 10:
        max_len = size.columns-10
    else:
        pass
    print("\033[91m", end='')
    for j in range(max_len):
        print("-", sep='', end='')
    print("\033[0m")
    i = i + 1

rand_int = random.randint(0, len(feed['entries']) - 1)
randEntry = feed['entries'][rand_int]
print()
print("Your handpicked article for today:")
print()
max_len = len(randEntry.title)
print(randEntry.title)
if len(randEntry.id) > max_len:
    max_len = len(randEntry.id)
print(randEntry.id)
if randEntry.summary:
    if len(randEntry.summary) > max_len:
        max_len = len(randEntry.summary)
    print(randEntry.summary)
size = shutil.get_terminal_size((80, 20))
if max_len > size.columns-10:
    max_len = size.columns - 10
print("\033[91m", end='')
for j in range(max_len):
    print("-", sep='', end='')
print("\033[0m")
# gettin' the text of the random article like a boss
soup = bs4.BeautifulSoup(urllib.request.urlopen(randEntry.id), "html.parser")
p_tags = soup.select("div.cikk-torzs p")
for tag in p_tags:
    if tag.string:
        size = shutil.get_terminal_size((80, 20))
        try:
            print(textwrap.fill(tag.string, size.columns-1)) # word wrapping at whitespace characters to terminal width in order to avoid chunced words at line ends
        except:
            print("Unsupported unicode character in the paragraph")
