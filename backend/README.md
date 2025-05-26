# Backend (FastAPI)

This directory contains the FastAPI backend application.

## Setup and Running

1.  **Navigate to the `backend` directory:**
    ```bash
    cd backend
    ```

2.  **Create/Activate Virtual Environment (Recommended):**
    While the initial setup might have installed dependencies globally as a workaround, for consistent development, it's highly recommended to use a virtual environment.
    ```bash
    # Create a virtual environment (if you haven't already)
    python3 -m venv .venv 

    # Activate it
    # On macOS and Linux:
    source .venv/bin/activate
    # On Windows:
    # .venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    If you have an activated virtual environment, or if you need to reinstall/update dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *Note: The `requirements.txt` was generated during the initial setup. It includes FastAPI, Uvicorn, SQLAlchemy, etc.*

4.  **Run the Development Server:**
    From within the `backend` directory:
    ```bash
    uvicorn main:app --reload
    ```
    The server will typically be available at `http://127.0.0.1:8000`.

## Project Structure

-   `main.py`: The main FastAPI application file, including API routers and CORS configuration.
-   `crud.py`: Contains CRUD (Create, Read, Update, Delete) operations for the database.
-   `database.py`: Handles database connection (SQLite) and session management.
-   `models.py`: Defines SQLAlchemy database models.
-   `schemas.py`: Defines Pydantic models for request/response data validation.
-   `requirements.txt`: Lists Python dependencies.
-   `sql_app.db`: The SQLite database file (will be created when the app runs and interacts with the DB).
