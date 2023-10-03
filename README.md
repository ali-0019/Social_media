# Social_media
this is a simple social media can make account and share content whith django (python)

## Features of this 

### A. Admin Users Can
1. Manage Acounts (Add, Update, Filter and Delete)
2. Manage posts (Add, Update, Filter and Delete)
3. Manage following requests (Add, Update, Filter and Delete)

### B. Users can
1. Make Profile (username,phone number, age, avatar)
2. account register(username, first_name, last_name, email, password)
3. share posts(file, title, description)
4. add comment(any posts)
5. add like(any posts)



## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/ali-0019/Social_media.git
```

Then, Enter the project
```
$  cd social_media
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the settings**

- Got to settings.py file
- create file like local_settings.py.example
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (Admin)

Command for PC:
```
$  python manage.py createsuperuser
```

Command for MAC:
```
$  python3 manage.py createsuperuser
```
Then Add Email, Username and Password
