import json
import os

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "data.json")


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
