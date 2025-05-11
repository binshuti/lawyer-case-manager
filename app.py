from flask import Flask, render_template, request, redirect, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

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

        flash("✅ Case added successfully.")
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

# ✅ New route to add a client
@app.route('/add-client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']

        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Clients (name, email, phone)
            VALUES (?, ?, ?)
        """, (name, email, phone))
        conn.commit()
        conn.close()

        flash("✅ Client added successfully.")
        return redirect('/')

    return render_template('add_client.html')

# ✅ New route to view full case details
@app.route('/case/<int:case_id>')
def case_detail(case_id):
    conn = connect_db()
    cur = conn.cursor()

    # Fetch full case info
    cur.execute("""
        SELECT c.case_id, cl.name, ct.court_name, c.case_type, c.description, c.status, c.opened_date
        FROM Cases c
        JOIN Clients cl ON c.client_id = cl.client_id
        JOIN Courts ct ON c.court_id = ct.court_id
        WHERE c.case_id = ?
    """, (case_id,))
    case = cur.fetchone()

    # Fetch status updates
    cur.execute("""
        SELECT update_date, status_detail
        FROM StatusUpdates
        WHERE case_id = ?
        ORDER BY update_date DESC
    """, (case_id,))
    updates = cur.fetchall()

    conn.close()
    return render_template('case_detail.html', case=case, updates=updates)

if __name__ == '__main__':
    app.run(debug=True)
