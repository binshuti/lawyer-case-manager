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

-- ✅ INDEXES FOR OPTIMIZATION

-- Speeds up searching for similar cases
CREATE INDEX idx_case_type ON Cases(case_type);
CREATE INDEX idx_case_description ON Cases(description);

-- Speeds up joins on foreign keys
CREATE INDEX idx_cases_client_id ON Cases(client_id);
CREATE INDEX idx_cases_court_id ON Cases(court_id);
CREATE INDEX idx_updates_case_id ON StatusUpdates(case_id);
