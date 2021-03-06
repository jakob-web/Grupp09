from flask import Flask, render_template, request, redirect, session, flash
from os import listdir
from db_operations import fetchone, update
from werkzeug.utils import secure_filename
import os
import user_login
import user_registration
import psycopg2

UPLOAD_FOLDER = 'python/static/img/uploads'
ALLOWED_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]


def editProfile(username):

    asd = fetchone("select pid from registration where username = %s", [username])
    oldpic = fetchone("select img from profile where pid = %s", [asd])

    img = validatepicture(username)
    info = request.form["info"]
    level = request.form["level"]
    age = request.form["age"]

    if img == oldpic and age == "" and info == "":
        print("ifsats 1")
        sql = "update profile set level = %s where pid = %s"
        val = (level, asd)
        update(sql, val)

    elif img == oldpic and age == "":
        print("ifsats 2")
        sql = "update profile set level = %s, info = %s where pid = %s"
        val = (level, info, asd)
        update(sql, val)
    
    elif img == oldpic:
        print("ifsats 3")
        sql = "update profile set level = %s, info = %s, age = %s where pid = %s"
        val = (level, info, age, asd)
        update(sql, val)
    
    elif img != oldpic and age =="" and info == "":
        print("ifsats 4")        
        sql = "update profile set level = %s, img = %s where pid =%s"
        val = (level, img, asd)
        update(sql, val)

    elif img != oldpic and age=="":
        print("ifsats 5")
        sql = "update profile set level = %s, img = %s, info = %s where pid = %s"
        val = (level, img, info, asd)
        update(sql, val)
    
    else:
        print("ifsats 6")
        sql = "update profile set level = %s, img = %s, info = %s, age = %s where pid =%s"
        val = (level, img, info, age, asd)
        update(sql, val)

    for item in oldpic:
        if os.path.exists(str(item)):
            os.remove(str(item.rsplit('/')[3]))
            print("bild borttagen")
 

def allowed_image(filename):
    
    if not "." in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in ALLOWED_EXTENSIONS:
        return True 
    else:
        return False

def validatepicture(username):

    if request.method == "POST":
        print("1 validate")
        print(request.files)
        if request.files:
            print("2 validate")
            image = request.files["image"]
            print(image)
            if image.filename == "":
                asd = fetchone("select pid from registration where username = %s", [username])
                oldpic = fetchone("select img from profile where pid = %s", [asd])
                return oldpic
            
            if not allowed_image(image.filename):
                
                print(image.filename)
                print("That image extension is not allowed")
                return redirect(request.url)

            else:
                filename = secure_filename(image.filename)

            print(image)
            image.save(os.path.join(UPLOAD_FOLDER, image.filename))

            return "static/img/uploads/" + str(image.filename)

def change_password(password,new_password):
    
    cred = fetchone("select password from registration where username=%s", [session["username"]])
    stored_password = cred[0]
    user_login.verify_password(stored_password, password)

    if user_login.verify_password(stored_password, password) == True:
        new_password = user_registration.hash_password(new_password)
        sql = "update registration set password = %s WHERE username = %s"
        val = new_password, session["username"]
        update(sql,val)
        print("update")
        return True
        
    else:
        flash("Fel lösenord")
        return False


    
