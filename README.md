# Masterblog

Masterblog is a lightweight, file-based blogging application built with Python and Flask. It provides a clean,
user-friendly web interface to perform complete CRUD (Create, Read, Update, Delete) operations on blog posts, utilizing
a local JSON file for straightforward data persistence.

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python:** Version 3.10 or higher (required for modern union type hints used in the service layer).
- **Package Manager:** `pip` (Python package installer).

## Installation

Follow these step-by-step instructions to set up and run the project locally.

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd Masterblog
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # On macOS and Linux
   python3 -m venv venv
   source venv/bin/activate

   # On Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   The core dependency for this project is Flask. Install it using `pip`:
   ```bash
   pip install Flask
   ```

## Environment Variables

While the application can execute directly via the `app.py` script, it is highly recommended to establish a `.env` file
in your root directory to handle standard Flask configurations.

Create a `.env` file and populate it with the following dummy examples:

```bash
# .env
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

## Usage

1. **Start the application:**
   You can start the server using the built-in Python runner:
   ```bash
   python app.py
   ```
   Alternatively, you can run it via the Flask CLI (if environment variables are set):
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

2. **Access the application:**
   Open your preferred web browser and navigate to:
   ```text
   http://localhost:5000
   ```

3. **Core Features:**
    - **Read:** The home page (`/`) reads from `data.json` and dynamically lists all published posts.
    - **Create:** Click "Add a new post" (`/add`) to submit a new entry.
    - **Update:** Click "Update" (`/update/<id>`) on an existing post to modify its author, title, or content.
    - **Delete:** Click "Delete" (`/delete/<id>`) to permanently remove a post from the JSON storage.

## Project Structure

A quick overview of the application's layered architecture:

```text
Masterblog/
├── app.py                  # Application entry point and app initialization
├── data.json               # File-based JSON database for post persistence
├── blueprints/
│   └── blog.py             # Route definitions and web controller logic
├── services/
│   └── blog_services.py    # Decoupled business logic and JSON data manipulation
├── static/
│   └── style.css           # Global application stylesheet
└── templates/              # Jinja2 HTML views
    ├── index.html
    ├── add.html
    └── update.html
```

## ToDo / Future Improvements

- [ ] **REST API Expansion:** Expose the existing decoupled service layer (`blog_services.py`) via dedicated API
  endpoints (e.g., `/api/v1/posts`) returning raw JSON.
- [ ] **Database Migration:** Replace the temporary `data.json` storage with a robust relational database (e.g., SQLite
  or PostgreSQL) using SQLAlchemy.
- [ ] **Data Validation:** Implement Pydantic models for strict request payload validation and unified response
  serialization.
- [ ] **Automated Testing:** Introduce a comprehensive test suite using `pytest` covering both the blueprint routes and
  service layer logic.
- [ ] **Authentication & Authorization:** Secure the add, update, and delete routes to require valid user sessions or
  API tokens.
- [ ] **Centralized Error Handling:** Implement global error handlers for robust and consistent HTTP exception
  management.