from flask import Flask, render_template, request, redirect
from os import listdir
from db_operations import fetchone, update

import psycopg2

<<<<<<< Updated upstream
conn = psycopg2.connect( 
    dbname="padelpar", 
    user="aj7951",
    password="ez2g1c1h",
    host="pgserver.mah.se")

cur = conn.cursor()
=======
>>>>>>> Stashed changes
def editProfile(username):
    # cur.execute("select max(id) from profile1")
    # for row in cur:
    #     id=row[0]
    #     id=id+1
    img = request.form["img"]
    info = request.form["info"]
    level = request.form["level"]
    age = request.form["age"]
    #asd = "select pid from registration where username = %s", [username]
<<<<<<< Updated upstream
    cur.execute("select pid from registration where username = %s", [username])
    asd = cur.fetchone()
    sql = "update profile set img = %s, info = %s, level = %s, age = %s where pid = %s" 
    val = img, info, level, age, asd
    cur.execute(sql, val)
    conn.commit()
    cur.close()

conn.close()
=======
    asd = fetchone("select pid from registration where username = %s", [username])
    sql = "update profile set img = %s, info = %s, level = %s, age = %s where pid = %s"
    val = (img, info, level, age, asd)
    update(sql, val)
>>>>>>> Stashed changes


# def getImg(username):



#     cur.execute("select img from(profile join registration on profile.pid = registration.pid) where username = %s", [username])

#     pic = []
#     for record in cur:
#         pic.append(record[0])
#     con.commit()
#     return pic



    # pic = []
    # pic = cur.fetchall()
    # print(pic)
    # img = pic[0]
    # img = ("".join(str(img)))
    # print(img)

    # return img


    # img = "select img from(profile join registration on profile.pid = registration.pid) where username = %s"
    # val = username


    # cur.execute(img, val)





# def getProfile():

#     sql = "select info, picture from profile"
