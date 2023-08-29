from flask import Flask, request, render_template_string
import sqlite3

"""This is a basic Flask page that does the following:
• connects to (and creates) a sqlite3 database file named 'database.db'
• creates a table 'names'
• has HTML form asking for a person's name; names are recorded in the table
• has Jinja2 HTML displaying the names taken from the table
"""

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('/data/database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS names (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);''')
    conn.commit()
    conn.close()

def get_db_connection():
    conn = sqlite3.connect('/data/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template_string('''
        <form action="/submit" method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <input type="submit" value="Submit">
        </form>
    ''')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO names (name) VALUES (?)", (name,))
    conn.commit()
    cursor.execute("SELECT name FROM names")
    all_names = cursor.fetchall()
    conn.close()

    return render_template_string('''
        <h1>Thank you, {{ name }}! Your name has been recorded.</h1>
        <h2>All names in the database:</h2>
        <ul>
            {% for name in names %}
                <li>{{ name['name'] }}</li>
            {% endfor %}
        </ul>
    ''', name=name, names=all_names)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=2225)
