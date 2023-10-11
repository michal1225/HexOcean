To run this application we need to do some steps.
1. First of all we need to build docker image. Afrer run Docker Desktop app type in venv: docker build .
2. Second step is type: docker compose up, in terminal
3. I used PostgreSQL. Its necessary to install that software from producent site.
4. Next step is to change db settings in main settings file. Just change parameters in DATABASE to yours.
5. Now database needs migrations. Type: python manage.py migrate, in terminal to make migrations.
6. Program need to loaddata from json file to db. To do this step you need to type: python manage.py loaddata db.json, in terminal,
you must be in main folder.

Now you can go to http://localhost:8000/admin and login by username: admin password: admin

To add picture you need go to http://localhost:8000/api/v1/img/

In application admin are 4 groups to test. I made one account - admin - and 
to test thumbnail part we need to change exsisting groups.
There are basic, premium, enterprise, admin. You schould go to http://localhost:8000/admin/accounts/customuser/ Just take the group you want to test and save account.


To check available options of thumbnail pictures (depending on group you chose) go to http://localhost:8000/media/listimg

