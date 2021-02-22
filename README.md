# Tasks with email reminders
Simple app to manage daily duties. User is reminded with an email before task's execution date.
Web framework: **Django**
Mailing service: **MailGun**

## How to run:
###### In first terminal:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

###### In second terminal:
```
python manage.py runworkers
```
