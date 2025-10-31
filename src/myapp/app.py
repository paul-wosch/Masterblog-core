from flask import Flask, render_template
from myapp.storage import write_json_file
from myapp.config import TEMPLATES_PATH, STATIC_PATH, BLOG_FILE_PATH
from myapp.models.blog import Blog

# Create blog storage if missing (new blog)
if not BLOG_FILE_PATH.exists():
    data = []
    write_json_file(BLOG_FILE_PATH, data)
# Create the blog instance
my_blog = Blog()

app = Flask(__name__, template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)

@app.route("/")
def index():
    """Show the index page for the blog."""
    my_blog.get_posts()
    blog_posts = my_blog.get_posts()
    return render_template('index.html', posts=blog_posts)


@app.route("/<post_id>")
def show(post_id):
    """Show a single blog post."""
    return "show"


@app.route("/add", methods=["GET", "POST"])
def add():
    """Show a form for adding a blog post."""
    return "add"


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    """Show a form for updating a blog post."""
    return "update"


@app.route("/like/<post_id>", methods=["POST"])
def like(post_id):
    """Route to like a blog post."""
    return "like"


@app.route("/delete/<post_id>", methods=["POST"])
def delete(post_id):
    """Route to delete a blog post."""
    return "delete"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)