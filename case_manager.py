import sqlite3

def connect_db():
    return sqlite3.connect("lawyer_cases.db")

def insert_case(client_id, court_id, case_type, description, status, opened_date):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Cases (client_id, court_id, case_type, description, status, opened_date)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (client_id, court_id, case_type, description, status, opened_date))
    conn.commit()
    conn.close()
    print("✅ Case inserted successfully.")

def search_similar_cases(keyword):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("""
        SELECT case_id, case_type, description, status FROM Cases
        WHERE case_type LIKE ? OR description LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    results = cur.fetchall()
    conn.close()
    
    print("\n🔍 Similar Cases Found:")
    for row in results:
        print(f"- Case #{row[0]}: {row[1]} | {row[2]} | Status: {row[3]}")
    if not results:
        print("No similar cases found.")

# --- Example Usage ---
if __name__ == "__main__":
    print("Welcome to the Case Manager.\n")

    # Add a new case (you can change these values)
    insert_case(
        client_id=1,
        court_id=1,
        case_type="Contract Dispute",
        description="Disagreement over payment terms in a tech project.",
        status="Open",
        opened_date="2025-04-28"
    )

    # Search for similar cases
    search_similar_cases("contract")
