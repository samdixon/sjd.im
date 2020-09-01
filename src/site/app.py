from flask import Flask, render_template, redirect
from easy_publish import generate_posts
import mistune

posts = generate_posts("~/fakenotes")

app = Flask(__name__, static_url_path="/static")

@app.route('/')
def index():
    return redirect("/blog")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    metadata = posts.metadata
    return render_template("blog.html", metadata=posts.metadata) # feed it the list of posts which includes metadata

@app.route('/blog/<p>')
def blogpost(p):
    post=posts.posts[p]
    return render_template(
        "post.html",
        post=post,
        markdown=mistune.markdown(post.content))

@app.route('/notes')
def notes():
    return render_template("notes.html")

@app.route('/projects')
def projects():
    return render_template("projects.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
