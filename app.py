from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect("lawyer_cases.db")

@app.route('/')
def index():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT c.case_id, cl.name, ct.court_name, c.case_type, c.status FROM Cases c JOIN Clients cl ON c.client_id = cl.client_id JOIN Courts ct ON c.court_id = ct.court_id ORDER BY c.case_id DESC")
    cases = cur.fetchall()
    conn.close()
    return render_template('index.html', cases=cases)

@app.route('/add', methods=['GET', 'POST'])
def add_case():
    conn = connect_db()
    cur = conn.cursor()

    if request.method == 'POST':
        client_id = request.form['client_id']
        court_id = request.form['court_id']
        case_type = request.form['case_type']
        description = request.form['description']
        status = request.form['status']
        opened_date = request.form['opened_date']

        cur.execute("""
            INSERT INTO Cases (client_id, court_id, case_type, description, status, opened_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (client_id, court_id, case_type, description, status, opened_date))
        conn.commit()
        conn.close()
        return redirect('/')

    # for GET
    cur.execute("SELECT * FROM Clients")
    clients = cur.fetchall()
    cur.execute("SELECT * FROM Courts")
    courts = cur.fetchall()
    conn.close()
    return render_template('add_case.html', clients=clients, courts=courts)

@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q', '')
    results = []

    if keyword:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT case_id, case_type, description, status FROM Cases
            WHERE case_type LIKE ? OR description LIKE ?
        """, (f'%{keyword}%', f'%{keyword}%'))
        results = cur.fetchall()
        conn.close()

    return render_template('search.html', keyword=keyword, results=results)

if __name__ == '__main__':
    app.run(debug=True)
