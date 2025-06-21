# Chrome Extension: Simplify Page

This extension replaces the text of the current web page with a rewritten version obtained from a Large Language Model (LLM). The goal is to make complex language easier to read while preserving the original meaning.

## How it works
1. Click the extension's icon to trigger rewriting.
2. The content script collects all text nodes from the page.
3. Each text snippet is sent to a server that calls an LLM API (replace `https://example.com/rewrite` in `content.js` with your service).
4. The returned text is injected back into the page, replacing the original content.

## Setup
1. Host a server that exposes a `/rewrite` endpoint accepting `{text, language}` and returning `{rewritten}` using an LLM of your choice.
2. Load this folder as an unpacked extension in Chrome.

This project provides a minimal skeleton. Error handling and selective rewriting can be added as needed.
