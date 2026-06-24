from flask import Blueprint, render_template

from services.blog_services import get_all_posts

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
