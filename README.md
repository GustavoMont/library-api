# Library API

<a name="readme-top"></a>

<div align="center" >

[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

</div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="project-images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">A Studing Case Library API</h3>

</div>

---

## About Project 🤔

This project is a studing case to learn more about django restframework. Is kind of system to a Library that make possible its clients loan book and the administer make control of these loans. The API is builded using restful archteture returning alll data in json format.

## Technologies used 🧑🏿‍💻

<br>

[![Python][python-shield]][python-url]
[![Django][django-shield]][django-url]
[![Django Rest Framework][drf-shield]][drf-url]
[![Sqlite][sqlite-shield]][sqlite-url]

---

## Run it ▶️

**To run this project you need to have python installed in your machine.**

### Clone It

```bash
git clone git@github.com:GustavoMont/library-api.git
```

### **Create a virtual enviroment and Activate**

Acctually you don't need to create a virtual enviroment but I really recommend it. You enter in project path and run:

**Linux**

_Create_

```
python3 -m venv <enviroment_name>
```

_Activate_

```bash
source <enviroment_name>/bin/activate
```

**Windows**

_Create_

```python
python3 -m venv <enviroment_name>
```

_Activate_

```powershell
<enviroment_name>/scripts/activate
```

### **Install all dependences**

```
pip install -r requirements.txt
```

### **Run migrations**

```
python manage.py migrate
```

### **Run and enjoy 😄**

```
python manage.py runserver 0.0.0.0:8000
```

---

## Routes 🛣️

### **/admin/** 🕴🏿

To access admin dashboard and add data.

---

### **/books/** 📚

Every type of user can access the **get** route but **only** super user can **create or edit** one book

---

### **/loans/** 🗞️

Only **authenticated user** can access this route: clients have access only to own data and **super admin** can access every user data.

Some changes only admin can make in loans, clients can only create and read.

---

### **/users/** 🧑🏾‍🤝‍🧑🏼

Only **authenticated user** can access this route: clients have access only to own data and **super admin** can access every user data

### **/user/register/**

To create a new user, only post route

---

### **/token/**

To loggin in aplication, only post route. Send email and password in request body

### **/token/refresh/**

In request body send a field called refresh and send refresh token

---

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://linkedin.com/in/luis-gustavo-monteiro
[django-shield]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[django-url]: https://docs.djangoproject.com/en/4.1/
[drf-shield]: https://img.shields.io/badge/django%20rest-ff1709?style=for-the-badge&logo=django&logoColor=white
[drf-url]: https://www.django-rest-framework.org/
[python-shield]: https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue
[python-url]: https://www.python.org/
[sqlite-shield]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[sqlite-url]: https://www.sqlite.org/docs.html
