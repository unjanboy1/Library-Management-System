# 📚 Library Management System

A production-ready, full-stack Web Application built to streamline day-to-day library operations, automate inventory tracking, and manage member activities with high efficiency.

---

## 🚀 Key Features

### 👤 User & Role Management
* **Authentication:** Secure user registration, authentication, and session handling.
* **Role-Based Access Control (RBAC):** Granular permissions split across Admin, Faculty, and Student roles.
* **Member Lifecycle:** Streamlined onboarding, profile updates, and member offboarding.

### 📖 Book Inventory Management
* **Catalog Control:** Add, edit, soft-delete, and search book records across categories.
* **Real-time Stock Tracking:** Dynamic stock updates reflect physical availability instantly.
* **Metadata Indexing:** Track ISBNs, authors, publishers, editions, and categories.

### 🔖 Issue & Return Workflow
* **Automated Transactions:** Seamless book checkout and check-in workflows.
* **Quantity Syncing:** Auto-increment/decrement stock counts upon checkout or return.
* **Fine Engine:** Automatic overdue detection and fine calculation based on daily rental policy rates.

### 📊 Operations Dashboard
* **High-Level Metrics:** Single-pane view of total books, registered users, active loans, and total overdues.
* **Daily Summary:** Track daily returns and outstanding fine collections.
* **Activity Stream:** Live audit feed showing real-time platform actions.

### 📝 Audit & System Logging
* **User Audit:** Log login attempts, timestamped user registrations, and permission updates.
* **Inventory Logs:** Track book additions, modifications, checkouts, and returns for accountability.

---

## 🛠️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Backend Framework** | Python, Flask, Flask-CORS |
| **Database & ORM** | SQLite, Flask-SQLAlchemy |
| **Frontend UI** | HTML5, CSS3, JavaScript (ES6+) |
| **Icons & Aesthetics** | Font Awesome |

---

## 🏗️ System Architecture & Workflow