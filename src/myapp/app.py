from flask import Flask
from myapp.config import TEMPLATES_PATH, STATIC_PATH

app = Flask(__name__, template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)


@app.route("/")
def index():
    """Show the index page for the blog."""
    return "index"


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