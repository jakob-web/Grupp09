from flask import Flask, render_template, request, redirect, session
from os import listdir
import hashlib, binascii, os
<<<<<<< Updated upstream

import psycopg2

conn = psycopg2.connect( 
    dbname="padelpar", 
    user="aj7951",
    password="ez2g1c1h",
    host="pgserver.mah.se")

cur = conn.cursor()
=======
from db_operations import fetchall, fetchone
>>>>>>> Stashed changes

def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    print("input password " + pwdhash)
    print("Stored password " + stored_password)
    if pwdhash == stored_password:
        return True
    else:
        return False

# #rename 'cred' to stored_password
# stored_password = password
# # remove if password in cred and instead:
# verify_password(stored_password,povided_password)

def login():
    cred = []
<<<<<<< Updated upstream
    cur.execute("select username from registration")
    cred = cur.fetchall()
    conn.commit()
    cur.close()
=======
    cred = fetchall("select username from registration", "")
>>>>>>> Stashed changes
    usernameList = ("".join(str(cred)))
    username = request.form["userName"]
    password = request.form["pwd"]

    if username in usernameList:
<<<<<<< Updated upstream
        print("Username exists")
        cur.execute("select password from registration where username='%s'" % (username))
        cred = cur.fetchone()
        conn.commit()
        cur.close()
=======
        usernameToFind = (username,)
        cred = fetchone("select password from registration where username=%s", usernameToFind)
>>>>>>> Stashed changes
        stored_password = cred[0]
        print(stored_password)
        print(password)
        if verify_password(stored_password,password):
                print("Password is correct")
                return True
        else:
            print(stored_password)
            print(password)
            print("fel lösenord")
            return False
    else:
        print("Kmr returna false")
        return False

conn.close()
