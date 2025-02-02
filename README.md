# 📝 FAQ API - Multilingual Support 🚀

A Django-based REST API for managing **Frequently Asked Questions (FAQs)** with **multilingual support, caching, and WYSIWYG editor integration**.

## 📌 Features
✅ Store and manage FAQs  
✅ Multi-language translation (English, Hindi, Bengali)  
✅ WYSIWYG editor (`django-ckeditor`) for formatted answers  
✅ REST API for retrieving FAQs  
✅ Caching mechanism (Redis)  
✅ Admin panel for easy management  
✅ Unit tests using `pytest`

---

## 📌 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/AnuushMB/BharathFD_intern_proj.git
cd BharathFD_intern_proj
```
### **2️⃣ Create Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows

```
### **3️⃣ Install Dependencies**
```
pip install -r requirements.txt

```
### **4️⃣ Run Migrations**
```
python manage.py makemigrations faq
python manage.py migrate

```
### **5️⃣ Create Superuser (Optional)**
```
python manage.py createsuperuser

```
### **6️⃣ Start Redis Server (For Caching)**
```
redis-server

```
### **7️⃣ Run Django Server**
```
python manage.py runserver

```
http://localhost:8000/api/faq/

## 📌 Running Tests

### **1️⃣ Install pytest**
```bash
pip install pytest pytest-django

```
### **2️⃣ Run Tests**
```
pytest
```

