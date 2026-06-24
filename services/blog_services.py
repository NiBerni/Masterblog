import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "..", "data.json")


def get_all_posts() -> list:
    """
    Fetches all blog posts from the JSON storage file.

    Acts as a decoupled service function that can be used by both
    standard web view and API endpoints.

    :return: A list of dictionaries containing blog post data. Returns an empty list if the file is missing or invalid.
    :rtype: list
    """
    if not os.path.exists(DATA_FILE_PATH):
        return []

    with open(DATA_FILE_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def add_post(author: str, title: str, content: str) -> dict:
    """
    Adds a new blog post to the JSON storage file.

    Reads existing posts, generates a new unique ID based on the highest existing ID,
    appends the new post, and saves the updated list back to the file.

    :param author: The author of the blog post.
    :param title: The title of the blog post.
    :param content: The content of the blog post.
    :return: The newly created blog post dictionary.
    :rtype: dict
    """
    posts = get_all_posts()
    # Generate a new unique ID based on the max ID currently in the file
    new_id = 1
    if posts:
        new_id = max(post.get("id", 0) for post in posts) + 1

    new_post = {"id": new_id, "author": author, "title": title, "content": content}
    posts.append(new_post)

    with open(DATA_FILE_PATH, "w", encodinf="utf-8") as file:
        json.dump(posts, file, indent=4)

    return new_post
