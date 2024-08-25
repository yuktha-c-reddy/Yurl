from flask import Flask, request, redirect, jsonify, render_template
import string
import random

app = Flask(__name__)

# Dictionary to store short and original URLs
url_mapping = {}

# Base URL for the shortener
BASE_URL = "https://yurl.vercel.app/"

# Function to generate a random short string
def generate_short_url():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

@app.route('/', methods=['GET', 'POST'])
def home():
    short_url = None
    if request.method == 'POST':
        original_url = request.form.get('url')
        if original_url:
            short_url = generate_short_url()
            while short_url in url_mapping:
                short_url = generate_short_url()
            url_mapping[short_url] = original_url
            short_url = BASE_URL + short_url
    return render_template('index.html', short_url=short_url)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')
    if not original_url:
        return jsonify({'error': 'No URL provided'}), 400
    
    short_url = generate_short_url()
    
    # Ensure the generated short URL is unique
    while short_url in url_mapping:
        short_url = generate_short_url()
    
    # Store the original URL with the generated short URL
    url_mapping[short_url] = original_url
    return jsonify({'short_url': BASE_URL + short_url}), 201

@app.route('/<short_url>')
def redirect_to_url(short_url):
    original_url = url_mapping.get(short_url)
    
    if original_url:
        return redirect(original_url)
    else:
        return jsonify({'error': 'URL not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

