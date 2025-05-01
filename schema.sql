CREATE TABLE Clients (
    client_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT,
    phone TEXT
);

CREATE TABLE Courts (
    court_id INTEGER PRIMARY KEY AUTOINCREMENT,
    court_name TEXT NOT NULL,
    location TEXT
);

CREATE TABLE Cases (
    case_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    court_id INTEGER,
    case_type TEXT,
    description TEXT,
    status TEXT,
    opened_date DATE,
    FOREIGN KEY (client_id) REFERENCES Clients(client_id),
    FOREIGN KEY (court_id) REFERENCES Courts(court_id)
);

CREATE TABLE StatusUpdates (
    update_id INTEGER PRIMARY KEY AUTOINCREMENT,
    case_id INTEGER,
    update_date DATE,
    status_detail TEXT,
    FOREIGN KEY (case_id) REFERENCES Cases(case_id)
);
