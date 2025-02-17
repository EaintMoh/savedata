from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_books():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_books(books):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(books, f, ensure_ascii=False, indent=4)

@app.route('/')
def main():
    books = load_books()
    return render_template('main.html', books=books)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        new_book = {
            'date': request.form['date'],
            'title': request.form['title'],
            'price': request.form['price']
        }
        books = load_books()
        books.append(new_book)
        save_books(books)
        return redirect(url_for('main'))
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
