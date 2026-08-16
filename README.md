# 📚 Library Management System

A modern, full-stack **Library Management System** built using **Python Flask** and **SQLite**. Designed for educational institutions and community libraries, this platform streamlines the management of catalogs, memberships, and circulation workflows while offering real-time insights through an interactive dashboard.

---

## 🚀 Key Features

### 👤 User & Membership Management
* **Secure Authentication:** User registration and session-based login.
* **Role-Based Access Control (RBAC):** Distinct permissions and workflows for **Admins**, **Students**, and **Faculty**.
* **Member Administration:** Full lifecycle management including profile registration and structural deletion.

### 📖 Book Inventory Management
* **Dynamic Catalogue:** Comprehensive view of the entire book inventory with advanced tracking.
* **Automated Stock Control:** Live tracking of "Available Quantity" that auto-updates upon issue or return events.
* **Full CRUD Operations:** Add, update, and remove book listings with ease.

### 🔖 Circulation & Fine Automation
* **Issue & Return Workflow:** Seamless checkout and check-in pipelines mapped to specific members.
* **Fine Calculation Engine:** Automated logic to calculate penalties for late returns based on due dates.
* **Overdue Tracking:** Proactive tracking of outstanding items to identify late returns instantly.

### 📊 Analytics Dashboard & Activity Logging
* **Real-time Metrics:** High-level counters for *Total Books*, *Active Members*, *Currently Issued*, and *Overdue Items*.
* **Audit Trails & Logs:** System-wide activity feeds logging structural events (logins, additions, issues, and returns) for security compliance.

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask, Flask-SQLAlchemy (ORM), Flask-CORS
* **Database:** SQLite3
* **Frontend:** HTML5, CSS3, JavaScript (ES6+), Font Awesome (Icons)

---

## ⚙️ Installation & Setup

Follow these steps to configure and run the application in a local development environment.

### 1. Prerequisites
Ensure you have **Python 3.x** and **Git** installed on your machine.

### 2. Clone the Repository
```bash
git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
cd library-management-system