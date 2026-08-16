# 📚 Library Management System (LMS)

An enterprise-grade, full-stack management solution engineered to automate asset cataloging, membership lifecycles, and circulation workflows. Built on a modular **Python Flask** architecture and powered by **Flask-SQLAlchemy**, this system delivers a secure, role-based platform for managing library operations with real-time analytical insights and comprehensive activity tracking.

---

## 🚀 Core Features

### 👤 Identity & Access Management (IAM)
* **Role-Based Access Control (RBAC):** Tiered system permissions separating administrative capabilities from standard **Student** and **Faculty** workflows.
* **Session Security:** Secure user registration, credential-validated login protocols, and route protection middleware.
* **Member Registry:** Centralized portal for profiling, monitoring, and structural offboarding of library members.

### 📖 Inventory & Catalogue Architecture
* **Asset Lifecycle Management:** Full CRUD (Create, Read, Update, Delete) capability for library resources.
* **Real-Time Stock Serialization:** Dynamic tracking of available stock quantities that auto-increments or decrements upon transaction events to eliminate race conditions.
* **Unified Catalogue:** High-performance, searchable interface exposing real-time book metadata and availability states.

### 🔖 Transactional Circulation Engine
* **Circulation Lifecycle:** Automated workflows linking book issuance and returns directly to active member accounts.
* **Automated Fine Aggregator:** Embedded arithmetic module calculating late return fees against strict, custom due dates.
* **Exceeded-Term Tracking:** Proactive flag systems identifying and isolating overdue materials.

### 📊 Operational Intelligence Dashboard
* **Dynamic Analytics:** Real-time visibility into mission-critical metrics:
  | Metric | Functional Description |
  | :--- | :--- |
  | **Total Cataloged** | Global aggregate of unique books managed across the ecosystem. |
  | **Active Directory** | Total count of verified system members (Admin, Student, Faculty). |
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

* **Backend Framework:** Python, Flask
* **Object-Relational Mapping (ORM):** Flask-SQLAlchemy (ACID Compliant)
* **API Security Middleware:** Flask-CORS (Cross-Origin Resource Sharing handling)
* **Database Layer:** SQLite3 (Embedded relational database)
* **Frontend Ecosystem:** Semantic HTML5, CSS3, Vanilla JavaScript (ES6+), Font Awesome 

---

## ⚙️ Installation & Environment Setup

Follow these steps to configure and run the application in a local development environment:

### 1. Repository Initialization
```bash
git clone [https://github.com/your-username/library-management-system.git](https://github.com/your-username/library-management-system.git)
cd library-management-system