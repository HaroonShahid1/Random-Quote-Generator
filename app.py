# app.py
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Function to fetch a random quote based on category
def get_quote(category):
    url = f"https://api.quotable.io/random?category={category}"
    response = requests.get(url)
    data = response.json()
    return f'"{data["content"]}" - {data["author"]}'

# Route to display the quote for a specific category
@app.route('/')
def index():
    categories = ['inspire', 'management', 'sports', 'life', 'funny']
    selected_category = request.args.get('category', 'funny')  # Get category from query parameters, default to 'funny'
    quote = get_quote(selected_category)
    return render_template('index.html', quote=quote, categories=categories, selected_category=selected_category)

if __name__ == '__main__':
    app.run(debug=True)
