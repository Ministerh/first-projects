from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.timeout.com/film/best-movies-of-all-time")
movies = response.text
soup = BeautifulSoup(movies, "html.parser")

titles = soup.find_all(name="h3", class_="_h3_cuogz_1")

new_movie = []
movie_title = [title.getText() for title in titles ]
for index in movie_title:
    new_movie.append(index.split("\xa0"))


with open("./web-scraping/movies.text", mode="w") as file:
    for n in new_movie:
        new = "".join(n)
        file.write(f'{new}\n')













# response = requests.get("https://news.ycombinator.com/newest")
# current_news = response.text
# soup = BeautifulSoup(current_news, "html.parser")

# articles = soup.find_all(name="span", class_="titleline")
# Article_text = [article.getText() for article in articles]

# Article_link = soup.select(".titleline a")
# new_link = [link.get("href") for link in Article_link]

# article_upvote = soup.find_all(name="span", class_="score")
# votes = [vote.getText() for vote in article_upvote]

# print(Article_text)
# print(Article_link)
# print(article_upvote)

























# with open("web-scraping/website.html", encoding="utf8") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# #this will help to indent the printed out document
# #print(soup.prettify())

# # to get all tags of a particular tag
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
# #to get all the href in the anchor tag
# for tags in all_anchor_tags:
#     #print(tags.get("href"))
# #to get only the tags in the anchor tag
#     #print(tags.getText)
#     pass
# #this will help to navigate a perticular tag
# heading = soup.find("h3", class_="heading")
# #print(heading.string)

# #Using css selector
# company_url = soup.select_one(selector="p a")
# print(company_url)