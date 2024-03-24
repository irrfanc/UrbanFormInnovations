from flask import Flask, render_template, request, redirect, url_for, flash
from cs50 import SQL

app = Flask(__name__)
app.secret_key = 'secret_key'

db = SQL("sqlite:///contacts.db")

@app.route('/')
def index():
    contacts = db.execute('SELECT * FROM contacts')
    return render_template('index.html', contacts=contacts)

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    if request.method == 'POST':
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        message = request.form.get('message')

        db.execute('INSERT INTO contacts (full_name, email, message) VALUES (?, ?, ?)',
                    full_name, email, message)
        flash('Message Sent!')

        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
