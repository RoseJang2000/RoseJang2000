import feedparser

blog_url = "https://RoseJang2000.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
    if idx > MAX_NUM:
        break
    feed_date = entrie['published_parsed']
    latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """
# ▎FrontEnd Developer
  
  ![rose's GitHub stats](https://github-readme-stats-sand-six-91.vercel.app/api?username=RoseJang2000&show_icons=true&count_private=true&line_height=24&theme=radical&hide=stars)
  ![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=RoseJang2000&layout=compact&theme=radical)

## ▎ 🛠 Tech Stacks
  <p>
    <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=white">&nbsp 
    <img src="https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=HTML5&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=CSS3&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white"/>&nbsp 
    <img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=GitHub&logoColor=white"/>&nbsp 
  </p>

## ▎📚 Blog For Learning

- ### https://rosejang2000.github.io/

## ▎💌 Email

- ### dev.rosejang@gmail.com

## ▎📑 Latest Posts


"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f:
    f.write(resultREADME)
