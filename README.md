# multiroleapp

**multiroleapp** is a demo application showcasing how to implement a **multiple role-based user system** using **Django** and **Nuxt**.  
It’s designed to help developers understand how to structure applications where a single user account can have multiple roles and switch between them seamlessly.

---

## 🚀 Features

1. **Multiple Role-Based Users**  
   - Built with Django's `AbstractUser` class for maximum flexibility.  
   - Supports defining multiple roles (e.g., Job Seeker, Job Supplier) under a single account.

2. **Role Switching**  
   - Remembers the **last active role** after login.  
   - Allows smooth switching between roles without multiple logins.

3. **Django + Nuxt Integration**  
   - Backend: Django (REST Framework)  
   - Frontend: Nuxt.js (latest version)  
   - Demonstrates how to connect a modern frontend with a Django backend.

4. **Real-World Use Cases**  
   - Platforms like **Upwork** (both job providers and seekers)  
   - Marketplaces with buyer/seller dual roles  
   - Educational platforms with student/teacher roles

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** Nuxt.js
- **Database:** SQLite (for demo purposes; can be replaced with Postgres/MySQL)
- **Auth:** Django's built-in authentication with token/session handling

---

## 📦 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/multiroleapp.git
cd multiroleapp

