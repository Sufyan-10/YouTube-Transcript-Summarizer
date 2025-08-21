import os
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import google.generativeai as genai
from flask_cors import CORS

# Load environment variables
load_dotenv()

# Setup API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from the extension

# Summarization prompt
prompt = """Please analyze the following YouTube transcript and summarize the content in a structured manner. Provide the summary under three main headings:
1.Introduction: A brief introduction to the topic discussed in the video.
2.Explanation: Detailed points explaining the main concepts, ideas, or arguments presented in the video.
3.Conclusion: A concise conclusion with the key takeaways or final thoughts.
Make sure the explanation is pointwise, easy to understand, and covers the core aspects of the video.Use double quotes to highlight the headings and remove asterisks.
"""

# Extract the YouTube transcript
def extract_transcript_details(youtube_video_url):
    try:
        print("Incoming URL:", youtube_video_url)

        # Handle both youtube.com and youtu.be formats
        parsed_url = urlparse(youtube_video_url)
        if 'youtube.com' in parsed_url.netloc:
            video_id = parse_qs(parsed_url.query).get('v', [None])[0]
        elif 'youtu.be' in parsed_url.netloc:
            video_id = parsed_url.path.lstrip('/')
        else:
            return None, "Invalid YouTube URL format."

        print("Extracted video ID:", video_id)

        if not video_id:
            return None, "No video ID found in URL."

        # Try fetching transcript with multiple languages
        transcript_text = YouTubeTranscriptApi.get_transcript(
            video_id,
            languages=['en', 'en-US', 'hi', 'auto']
        )

        transcript = " ".join([i["text"] for i in transcript_text])
        return transcript, None

    except TranscriptsDisabled:
        return None, "Transcripts are disabled for this video."
    except NoTranscriptFound:
        return None, "No transcript found for this video."
    except Exception as e:
        print("FULL ERROR:", repr(e))
        return None, f"Error extracting transcript: {str(e)}"

# Generate summary using Google Generative AI
def generate_summary(transcript_text):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        print(f"Error generating summary: {e}")
        return "Error generating summary."

# Endpoint to handle summarization request
@app.route('/summarize', methods=['GET'])
def summarize_video():
    youtube_url = request.args.get('url')
    if not youtube_url:
        return jsonify({"summary": "No URL provided."}), 400

    transcript_text, error = extract_transcript_details(youtube_url)
    if error:
        return jsonify({"summary": error}), 400

    summary = generate_summary(transcript_text)
    return jsonify({"summary": summary})

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
