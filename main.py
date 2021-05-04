'''
Description: 
Version: 2.0
Autor: xinmang
Date: 2021-05-04 19:47:34
LastEditors: xinmang
LastEditTime: 2021-05-04 22:43:35
'''
import feedparser
import os
import re
import time
import pytz
from datetime import datetime

def get_link_info(feed_url, num):
    result = ""
    feed = feedparser.parse(feed_url)
    feed_entries = feed["entries"]
    feed_entries_length = len(feed_entries)
    all_number = 0;
    if(num > feed_entries_length):
        all_number = feed_entries_length
    else:
        all_number = num
    for entrie in feed_entries[0: all_number]:
        title = entrie["title"]
        link = entrie["link"]
        result = result + "\n" + "[" + title + "](" + link + ")" + "\n"
    return result
    
def main():

    insert_info =  get_link_info("https://xingmang.net/posts/index.xml", 6)

    insert_info = "<!---blog_start--->\n ## 最近更新的文章 \n > 更新时间：" 
    + datetime.fromtimestamp(int(time.time()), pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
    + insert_info + "\n<!---blog_end--->"

    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()
        
    new_readme_md_content = re.sub(r'<!---blog_start--->(.|\n)*<!---blog_end--->', insert_info, readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

main()
