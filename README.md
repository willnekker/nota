# Nota - Your Local-First Canvas LMS Assistant

Nota is a local-first application that connects to Canvas LMS to pull your course data, summarize it, and provide a local dashboard for you to interact with your courses.

## Features

- **Canvas API Integration:** Pulls all courses, assignments, announcements, pages, files, and due dates.
- **File & Video Handling:** Downloads lecture files and transcribes videos locally using Whisper.
- **Summarization:** Summarizes assignments, documents, and video transcripts.
- **Local Dashboard:** A FastAPI backend and React frontend to view your course data.
- **Calendar View:** A calendar-style view of key dates.
- **Export:** Export summaries as Markdown/PDF.

## Tech Stack

- **Backend:** FastAPI, PostgreSQL, SQLAlchemy
- **Frontend:** React, Tailwind CSS
- **Transcription:** OpenAI Whisper
- **Deployment:** Docker, GitHub Actions

## Getting Started

### 1. Obtain Canvas API Keys

To connect Nota with your Canvas LMS account, you need to generate a Canvas API access token. Follow these steps:

1.  Log in to your Canvas LMS account.
2.  Navigate to your **Account** settings (usually found in the global navigation menu on the left).
3.  Click on **Settings**.
4.  Scroll down to **Approved Integrations** or **New Access Token**.
5.  Click on the **+ New Access Token** button.
6.  Give the token a purpose (e.g., "Nota App") and optionally set an expiration date.
7.  Click **Generate Token**.
8.  **Important:** Copy the generated token immediately. You will not be able to see it again.

### 2. Configure Environment Variables

Create a `.env` file in the `backend` directory (`Nota/backend/.env`) with the following content, replacing the placeholder values with your actual Canvas API details:

```
CANVAS_API_URL=https://<YOUR_CANVAS_INSTANCE>.instructure.com # e.g., https://canvas.instructure.com
CANVAS_CLIENT_ID=your_client_id # This is not used for personal access tokens, but required by the OAuth2 flow
CANVAS_CLIENT_SECRET=your_client_secret # This is not used for personal access tokens, but required by the OAuth2 flow
CANVAS_REDIRECT_URI=http://localhost:8080/api/v1/auth/callback
```

**Note:** For personal access tokens, `CANVAS_CLIENT_ID` and `CANVAS_CLIENT_SECRET` are not directly used for authentication, but they are part of the OAuth2 flow setup in the application. You can use placeholder values if you are using a personal access token.

### 3. Run with Docker

Nota is designed to run entirely within a single Docker container. Make sure you have Docker installed on your system.

1.  **Build the Docker image:**
    Navigate to the root directory of the `Nota` project (where the `Dockerfile` is located) in your terminal and run:
    ```bash
    docker build -t nota-app .
    ```

2.  **Run the Docker container:**
    Once the image is built, you can run the application:
    ```bash
    docker run -p 8080:8080 nota-app
    ```

    This command will:
    -   `-p 8080:8080`: Map port 8080 on your host machine to port 8080 inside the container, allowing you to access the dashboard.

3.  **Access the Dashboard:**
    Open your web browser and go to `http://localhost:8080`.

## Development

For development purposes, you can run the backend and frontend separately.

### Backend (FastAPI)

1.  Navigate to the `backend` directory:
    ```bash
    cd Nota/backend
    ```
2.  Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    ./venv/Scripts/activate # On Windows
    source venv/bin/activate # On macOS/Linux
    pip install -r requirements.txt
    ```
3.  Run the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```
    The API will be available at `http://localhost:8000`.

### Frontend (React)

1.  Navigate to the `frontend` directory:
    ```bash
    cd Nota/frontend
    ```
2.  Install dependencies:
    ```bash
    npm install
    ```
3.  Start the React development server:
    ```bash
    npm start
    ```
    The frontend will be available at `http://localhost:3000`.