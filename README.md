# YouTube Video Summarizer

A browser extension integrated with a Python backend that extracts transcripts from YouTube videos and generates concise summaries. This project helps users quickly grasp key points of long videos, saving time and improving productivity.

---

## Features
- Extracts video transcripts (English).
- Generates summaries with three sections: **Introduction, Explanation, Conclusion**.
- Easy-to-use Chrome extension popup.
- Handles errors when transcripts are not available.

---

## Project Structure
youtube-summarizer/
│── app.py # Python backend for transcript processing
│── .env # Environment variables (API keys/config)
│
├── extension/ # Chrome Extension Files
│ ├── manifest.json # Extension configuration (Manifest V3)
│ ├── background.js # Background script
│ ├── content.js # Content script to interact with YouTube
│ ├── popup.html # Popup UI
│ ├── popup.css # Popup styling
│ ├── popup.js # Popup logic
│ └── images/ # Extension icons
│ ├── icon16.png
│ ├── icon48.png
│ └── icon128.png


---

## Setup

### Backend
1. Go to the `backend/` folder.
2. (Optional) Create a virtual environment.
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Copy .env.example → .env and add 
    ```ini
    your Google API key:

GOOGLE_API_KEY=your_api_key_here

5. Run the Server:
    ```bash
    python app.py
The server runs at: http://127.0.0.1:5000

### Extension
1. Open Chrome → go to chrome://extensions/.

2. Enable Developer Mode.

3. Click Load unpacked and select the extension/ folder.

4. The extension will appear in your toolbar.

### Usage
1. Open any YouTube video.

2. Click the extension icon → press Summarize Video.

3. The popup will display the AI-generated summary.

4. If transcripts are not available, you’ll see an error message.

### Tech Stack 
-Backend: Flask (Python - transcript processing)
-Transcripts: youtube-transcript-api
-AI: Google Gemini (google-generativeai)
-Frontend: Chrome Extension (HTML, CSS, JavaScript)

### Final Note
-The extension works only when the backend Flask server is running locally.
-Do not commit your real .env file. Use .env.example for sharing.
