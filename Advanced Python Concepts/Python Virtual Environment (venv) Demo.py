# 🐍 Python Virtual Environment (venv) Demo

# 1. Naya Project Folder Banao

# mkdir python_venv_demo
# cd python_venv_demo

# 2. Virtual Environment Create Karo
# python3 -m venv venv

# 👉 Isse ek venv/ folder banega jisme Python aur libraries install hongi (project ke liye isolated).


# 3. Activate Virtual Environment

# Mac/Linux
# source venv/bin/activate


# Windows (PowerShell)
# venv\Scripts\activate


# 👉 Ab tumhara terminal prompt aisa dikhega:
# (venv) vishal@MacBook-Air python_venv_demo %


# 4. Libraries Install Karo
# pip install requests pandas
# 👉 Ye sirf is environment me install hongi (global system ko effect nahi karegi).

# Check installed packages:
# pip list

# 5. Freeze Dependencies
# pip freeze > requirements.txt


# 👉 Ye file banegi jisme sab dependencies ka exact version hoga:

# pandas==2.2.2
# requests==2.32.3

# 6. Deactivate Environment
# deactivate


# 👉 Ab tum global Python environment pe wapas aa gaye.

# 7. Restore Dependencies in New System (Ya dusra developer)

# Naya venv banao:

# python3 -m venv venv
# source venv/bin/activate


# Install dependencies from file:
# pip install -r requirements.txt
