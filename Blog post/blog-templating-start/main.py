from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

response =requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()
blog_posts = []
for post in response:
    all_post = Post(post['id'], post['title'], post['subtitle'], post['body'] )
    blog_posts.append(all_post)

@app.route('/')
def home():
   
    return render_template("index.html", all_blog_post = blog_posts)


@app.route('/post/<int:blog_num>')
def full_blog(blog_num):
    required_post = None
    for blog in blog_posts:
        if blog.id == blog_num:
            required_post = blog 
    return render_template("post.html", blog_post = required_post )

if __name__ == "__main__":
    app.run(debug=True)
