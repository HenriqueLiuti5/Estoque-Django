<div align="center">

# 📦 Inventory

![Badge Development](http://img.shields.io/static/v1?label=STATUS&message=IN%20DEVELOPMENT&color=GREEN&style=for-the-badge)
<br>
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<p align="center">
  <b>Corporate system for inventory management and stock control.</b><br>
  Focus on performance, security, and modern UX.
</p>

</div>

---

## 💻 About the Project

**Inventory** is a web application developed to simplify product control in small and medium-sized businesses.

Unlike common administrative systems, this project focuses on a high-level **User Experience (UX)**, using locally processed **Tailwind CSS** for maximum performance and a clean, responsive design.

---

## ✨ Features

- **🔐 Secure Authentication**: Login and route protection (@login_required).
- **📦 Product Management (CRUD)**: Add, List, Edit, and Delete.
- **🛡️ Extra Security**: Deletion with **Confirmation Modal** to prevent errors.
- **🔍 Smart Search**: Fast filtering on the dashboard with a clear button (UX).
- **🎨 Professional UI**: Custom Design System with brand colors ("Verdão Green").
- **📱 Responsiveness**: Works on Desktop and Mobile.

---

## 🚀 How to Run

```bash
# 1. Clone the repository
$ git clone https://github.com/HenriqueLiuti5/Estoque-Django.git

# 2. Enter the folder
$ cd Estoque-Django

# 3. Create and activate the virtual environment
$python -m venv venv$ venv\Scripts\activate  # Windows

# 4. Install dependencies
$ pip install -r requirements.txt

# 5. Prepare the Database
$ python manage.py migrate

# 6. Create the Administrator
$ python manage.py createsuperuser

# 7. Run the server
$ python manage.py runserver
```

Access: `http://127.0.0.1:8000`

---

## ⚙️ Tailwind (Development)

CSS is generated locally (without online CDN dependency). To edit styles:

```bash
# Install Node dependencies (if necessary)
$ npm install

# Run the Tailwind watcher
$ npx tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch
```
---

## 📝 License

This project is under the MIT license.

---

<div align="center">
  <sub>Made by Henrique Liuti</sub>
</div>
