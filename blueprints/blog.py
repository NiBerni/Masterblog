from flask import Blueprint, redirect, render_template, request, url_for

from services.blog_services import (
    add_post,
    delete_post,
    fetch_post_by_id,
    get_all_posts,
    update_post,
)

blog_bp = Blueprint("blog", __name__)


@blog_bp.route("/")
def index() -> str:
    """
    Handles the index route and displays all blog posts.

    Fetches blog posts via the service layer and passes them to the template.

    :return: Rendered HTML templ,ate with the list of blog
    :rtype: str
    """
    posts = get_all_posts()
    return render_template("index.html", posts=posts)


@blog_bp.route("/add", methods=["GET", "POST"])
def add():
    """
    Handles the route for adding a new blog post.

    On GET: Renders the form to add a new post.
    On POST: Extracts form data, calls the service layer to save the post,
    and redirects to the index page.

    :return: Rendered HTML template on GET, or a redirection response on POST.
    """
    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        if author and title and content:
            add_post(author, title, content)

        return redirect(url_for("blog.index"))

    return render_template("add.html")


@blog_bp.route("/delete/<int:post_id>")
def delete(post_id: int):
    """
    Handles the route for deleting a specified blog post.

    Calls the service layer to remove the post and redirects back to the index page.

    :param post_id: The unique identifier of the blog post to delete.
    :return: A redirection response to the index page.
    """
    delete_post(post_id)
    return redirect(url_for("blog.index"))


@blog_bp.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id: int):
    """
    Handles the route for updating a specified blog post.

    on GET: Renders the form pre-populated with existing post data
    on POST: Extracts form data, updates the post via service layer,
    and redirects to the index page.
    :param post_id: The unique identifier of the blog post to update.
    :return: Rendered HTML template on GET, a redirection response on POST, or a 404 error string.
    """
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == "POST":
        author = request.form.get("author")
        title = request.form.get("title")
        content = request.form.get("content")

        if author and title and content:
            update_post(post_id, author, title, content)

        return redirect(url_for("blog.index"))

    return render_template("update.html", post=post)
