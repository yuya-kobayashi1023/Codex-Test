from flask import Flask, request, jsonify

app = Flask(__name__)

SYNONYMS = {
    'utilize': 'use',
    'commence': 'start',
    'terminate': 'end',
    'implement': 'do',
    'numerous': 'many',
    'approximately': 'about',
    'investigate': 'look into',
    'demonstration': 'example',
}

def simplify_text(text):
    words = text.split()
    simplified = []
    for w in words:
        lw = w.lower()
        if lw in SYNONYMS:
            new = SYNONYMS[lw]
            # preserve capitalization
            if w[0].isupper():
                new = new.capitalize()
            simplified.append(new)
        else:
            simplified.append(w)
    return ' '.join(simplified)

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.get_json(force=True)
    text = data.get('text', '')
    lang = data.get('language', 'en')
    # translation step would go here
    result = simplify_text(text)
    return jsonify({'rewritten': result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
