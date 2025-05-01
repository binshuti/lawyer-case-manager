-- Clients
INSERT INTO Clients (name, email, phone) VALUES 
('John Doe', 'john@example.com', '555-1234'),
('Jane Smith', 'jane@example.com', '555-5678'),
('Robert Johnson', 'robert@example.com', '555-8765');

-- Courts
INSERT INTO Courts (court_name, location) VALUES 
('Superior Court of California', 'Los Angeles, CA'),
('District Court of New York', 'New York, NY');

-- Cases
INSERT INTO Cases (client_id, court_id, case_type, description, status, opened_date) VALUES 
(1, 1, 'Contract Dispute', 'Dispute over service contract terms.', 'Open', '2025-04-01'),
(2, 2, 'Personal Injury', 'Slip and fall at retail store.', 'Open', '2025-04-15'),
(1, 2, 'Employment Law', 'Wrongful termination case.', 'Closed', '2025-02-10');

-- Status Updates
INSERT INTO StatusUpdates (case_id, update_date, status_detail) VALUES
(1, '2025-04-02', 'Initial hearing scheduled.'),
(2, '2025-04-16', 'Filed documents received.'),
(3, '2025-03-01', 'Case closed by settlement.');
