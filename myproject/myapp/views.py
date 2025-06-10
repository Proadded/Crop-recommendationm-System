from django.shortcuts import render
import mysql.connector as sql

first_name = ""
last_name = ""
gender = ""
dob = "" #dd/mm/yyyy
email = ""
pwd = ""

def login_action(request):
    global email,pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="mysql@123", database="website")
        cursor = m.cursor()
        d = request.POST 
        for key, value in d.items():
            if key == "email":
                email = value
            if key == "password":
                pwd = value
        c = "select * from users where email = '{}' and password = '{}'".format(email, pwd)
        cursor.excute(c)
        t = tuple(cursor.fetchall())
        if t == ():
            return render(request, 'erroR.html')
        else:
            return render(request, 'welcome.html')
    
    return render(request, 'myapp/login_page.html')      
        