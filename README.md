# FastAPI Text Translation API

This project is a RESTful API built with **FastAPI** that translates user-provided text into various languages using **GPT-4**. The API allows users to input text, specify a target language, and receive the translated text as output.

---

## Features

- **User-Friendly Translation**: Translate text into a wide range of languages.
- **Powered by GPT-4**: Leverages OpenAI's GPT-4 for accurate and context-aware translations.
- **FastAPI Integration**: Provides a high-performance, lightweight RESTful API.
- **PostgreSQL Database**: Stores translation history and user preferences securely.
- **JavaScript Frontend**: A simple web interface for user interaction.

---

## Prerequisites

To run this project, you need:

- **Python 3.9+**
- An **OpenAI API Key** for GPT-4 access
- **PostgreSQL Database**

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/TranslationService.git
   cd translation-service
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate # On Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project root and add your keys:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   DATABASE_URL=postgresql://username:password@localhost:5432/your_database
   ```

5. **Set Up PostgreSQL**:
   - Create a new database (e.g., `translations_db`).
   - Update the `DATABASE_URL` in the `.env` file with your PostgreSQL credentials.

## Usage

1. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

2. **Access the API**:
   Open your browser and go to:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the automatically generated Swagger UI for testing the endpoints.

---

## Project Structure

```
translation-service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   └── templates/
│       └── index.html
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```
