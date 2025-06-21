# Rewrite Server

This folder contains a small Flask application that exposes a `/rewrite` endpoint.
It provides a simple placeholder implementation for rewriting text. The server
accepts JSON payloads containing a piece of text and an optional language code
and returns a simplified version of the text.

The current implementation replaces certain complex English words with simpler
alternatives. You can replace the `simplify_text` function in `server.py` with a
call to an LLM or any other rewriting logic.

## Usage

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the server:
   ```bash
   python server.py
   ```
   The service listens on port `5000` by default.

Your Chrome extension can POST requests to `http://localhost:5000/rewrite` with
`{"text": "...", "language": "en"}` to retrieve rewritten text.
