# 📚 Enterprise Library Management System (ELMS)

A robust, full-stack web application engineered to streamline asset management, membership lifecycles, and operational workflows for modern library infrastructures. Built on a modular **Python Flask** backend and powered by an optimized **SQLite** relational database, this platform features role-based access control, an automated fiscal engine for compliance, and granular activity auditing.

---

## 🚀 Core Architecture & Features

### 👤 Identity & Access Management (IAM)
* **Role-Based Access Control (RBAC):** Tiered permissions mapping specific access boundaries for **Admin**, **Student**, and **Faculty** roles.
* **Session Security:** State-managed user registration, secure credential verification, and protected routing.
* **Member Lifecycle Administration:** Centralized registry for adding, profiling, and deprecating system actors.

### 📖 Asset & Catalog Management
* **Inventory Control:** Full CRUD capabilities for resource ingestion, metadata maintenance, and asset deletion.
* **Real-time Stock Serialization:** Dynamically tracks available quantities across the inventory pool, reducing concurrency conflicts.
* **Global Catalogue:** Performance-focused view layout for instantaneous resource indexing and discovery.

### 🔖 Transactional Circulation Engine
* **Circulation Lifecycle:** Automated workflows linking book issuance and returns directly to active member accounts.
* **Automated Fine Aggregator:** Embedded arithmetic module calculating late return fees against strict, custom due dates.
* **Exceeded-Term Tracking:** Proactive flag systems identifying and isolating overdue materials.

### 📊 Operational Intelligence Dashboard
* **Dynamic Analytics:** Real-time visibility into mission-critical metrics:
  | Metric | Description |
  | :--- | :--- |
  | **Total Cataloged** | Global aggregate of books managed across the ecosystem. |
  | **Active Directory** | Total count of verified system members. |
  | **Circulation Load** | Real-time counter of assets checked out by consumers. |
  | **Deficit Monitoring** | Live calculation of overdue books outstanding. |
* **Daily Ledger:** Real-time visibility into transaction metrics executing within the active 24-hour window.

### 📝 Immutable System Auditing
* **Central Log Broker:** System-wide audit logging for accountability tracking, including:
  - User Authentication & Authorization Events
  - Inventory Structural Modifications (Additions/Deletions)
  - Circulation Ingestion and Termination Records
  - Member Sign-ups

---

## 🛠️ Technical Specification

* **Backend Framework:** Python 3.x, Flask (Microframework)
* **Object-Relational Mapping (ORM):** Flask-SQLAlchemy (Ensures ACID compliance)
* **API Security Middleware:** Flask-CORS (Cross-Origin Resource Sharing handling)
* **Database Layer:** SQLite3 (Embedded, file-based relational engine)
* **Frontend Ecosystem:** Semantic HTML5, Modular CSS3, Vanilla ECMAScript 6+, Font Awesome Typography

---

## ⚙️ Deployment & Local Environment Setup

### 1. Prerequisites
Ensure your local host contains **Python 3.8+** and **Git** within the system environment path.

### 2. Repository Initialization
```bash
git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
cd library-management-system