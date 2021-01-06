from flask import Flask, render_template, redirect
from easy_publish import generate_posts
import mistune

posts = generate_posts("~/fakenotes")

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    return render_template("blog.html", metadata=posts.metadata)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template("blog.html", metadata=posts.metadata)

@app.route('/blog/<p>')
def blogpost(p):
    post=posts.posts[p]
    return render_template(
        "post.html",
        post=post,
        markdown=mistune.markdown(post.content))

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
