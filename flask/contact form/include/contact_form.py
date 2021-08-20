from include.db import *
from flask import request
from passlib.hash import sha256_crypt

def contact_from() :
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = sha256_crypt.encrypt(request.form['password'])
        cr.execute(f"INSERT INTO users ( name , email  , password ) VALUES(?,?,?) ",(name,email,password))
        db.commit()

        