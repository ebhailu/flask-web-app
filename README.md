[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Zi860vbl)
# Secure Programming Learning GitHub Action Template for Python

## 🌐 Live Demos

- 🛒 [Product Service](https://assingment-2-rest-apis-ebhailu.onrender.com)
- 🛍️ [Cart Service](https://assingment-2-rest-apis-ebhailu-1.onrender.com)
  
In this assignment, I put into practice several Flask capabilities for website development, such as templates, error handling, URL handling, forms, etc. 

I designed a web application using Flask to process course override requests at VCU. This application allows students to submit an override request via a web form, and after successful submission, the application displays a confirmation message.

---

### ✅ Features
* A web form with the following fields:
  * Student Name (required)
  * Student ID (required)
  * Course Name (required)
  * Course Number (required)
  * Justification (not-required)
* Form validation using `Flask-WTF` with success notification.
* Flash messages for user feedback after successful submission.
* Error handling for 404 and 500 errors.
---
### 🚀 Getting Started

### 1. Clone the Repository
```bash 
git clone https://github.com/vcu-cmsc-damevski/assignment-3-flask-web-application-ebhailu.git
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/Scripts/activate        
# On non-windows devices switch Scripts for bin
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```
