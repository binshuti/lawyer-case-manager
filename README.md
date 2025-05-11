# 🧾 Lawyer Case Manager

A lightweight web-based case management system designed to help lawyers track legal cases, clients, and courts efficiently. The system allows legal professionals to add new cases, search for existing ones, and avoid redundant data entry — all through a clean, searchable, and organized interface.

## 🚀 Features

- Add new legal cases linked to existing clients and courts
- Create new clients dynamically as needed
- View case details, including descriptions and status updates
- Search cases using keywords (optimized with indexing)
- Flash messages to confirm successful actions
- Clean UI with HTML, CSS, and Jinja templates
- Indexes added to improve performance on key queries

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – lightweight web framework
- **SQLite** – embedded database for storing cases, clients, courts, and updates
- **HTML/CSS** – frontend structure and styling

## 📂 File Structure

```
lawyer_case_manager/
├── app.py                 # Flask backend
├── lawyer_cases.db        # SQLite database
├── schema.sql             # Table + index creation
├── seed_data.sql          # Sample data to test the app
├── static/
│   └── style.css          # CSS styling
├── templates/
│   ├── index.html         # Home page with case list
│   ├── add_case.html      # Form to add new cases
│   ├── add_client.html    # Form to add new clients
│   ├── search.html        # Case search interface
│   └── case_detail.html   # View full case details
└── README.md              # Project documentation
```

---

## 💡 Interesting Challenges Encountered

- Designing a normalized relational schema with foreign keys
- Using `LIKE` search in SQL with indexes to avoid full scans
- Connecting form inputs to SQL INSERT operations in Flask
- Displaying JOINed table data cleanly in templates
- Adding real-time feedback using Flask flash messages
- Structuring routes and templates for both readability and performance

---

## 📦 How to Bundle and Run the Code

### 1. Clone the Repository
```bash
git clone https://github.com/binshuti/lawyer-case-manager.git
cd lawyer-case-manager
```

### 2. Install Dependencies
```bash
pip install Flask
```

### 3. Set Up the Database
```bash
sqlite3 lawyer_cases.db < schema.sql
sqlite3 lawyer_cases.db < seed_data.sql
```

### 4. Run the App
```bash
python3 app.py
```

### 5. Visit in Your Browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🧠 Future Improvements

- Add status update form per case
- Implement user authentication
- Add export to CSV or PDF
- Improve search with full-text indexing
- Deploy online using Render or Heroku

---

## 👨‍🏫 Author & Course

**Built by**: Bertrand Aristide  
**Course**: [Introduction to Databases]  
**Instructor**: [Riccardo Pucella]
