from flask import Flask, render_template, request, redirect, url_for, session, logging, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util
from bson.objectid import ObjectId
import json

#from werkzeug.security import generate_password_hash, check_password_hash
#from sqlalchemy import create_engine
#from sqlalchemy.orm import scoped_session, sessionmaker
#from passlib.hash import sha256_crypt
# from pip install passlib import MySQL,MySQLdb
#import bcrypt

# engine = create_engine("mysql+pymysql://root:1234567@localhost/register")
# ("mysql+pymysql://username:passoword@localhost/databasename)
# bd = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
#app.secret_key = 'myawesomesecretkey'
# configuración de la base de datos MONGO después del slash va el nombre /reddelcafe
app.config['MONGO_URI'] = 'mongodb://cafe:melisita2020@170.239.84.107:27017/reddelcafe?authSource=admin'

mongo = PyMongo(app)

# vamos a iniciar con un formulario sencillo


@app.route("/")
def Inicio():
    return render_template("inicio.html")


@app.route("/form")
def Form():
    return render_template("form.html")

@app.route("/Trilladoras/nueva", methods=['POST'])
def nueva_trilladora():
    nombre = request.json['nombre']
    ubicacion = request.json['ubicacion']
    telefono = request.json['telefono']
    horario = request.json['horario']
    print(nombre+" " + ubicacion + " " + telefono + " " + horario)
    if nombre and ubicacion and telefono and horario:
        mongo.db.trilladoras.insert_one({
            "nombre": nombre,
            "ubicacion": ubicacion,
            "telefono": telefono,
            "horario": horario
        })
        res = {
            'res': 'ok'
        }
    else:
        res = {
            'res': 'err'
        }
    return res

@app.route("/Trilladoras/consultar", methods=['GET'])
def consultar_trilladoras():
    consulta = mongo.db.trilladoras.find()
    res = json_util.dumps(consulta)
    return Response(res, mimetype="application/json")

@app.route("/informacion")
def informacion():
    return render_template("informacion.html")

@app.route("/Trilladoras")
def Trilladoras():
    return render_template("Trilladoras.html")

@app.route("/calculo")
def calculo():
    return render_template("calculo.html")

@app.route("/Foro")
def Foro():
    return render_template("Foro.html")

@app.route("/registro", methods=["GET", "POST"])
def registro():
    # if  request.methods == "POST":
    # name = request.form.get("nombre")
    # username = request.form.get("usuario")
    #   }  password = request.form.get("contraseña")
    # confirm = request.form.get("confirm")
    # secure_password = sha256_crypt.encrypt(str(password))

    # if password == confirm:
    # db.execute("INSERT INTO users(name, username, password) VALUES(:name, :username, :password)",
    #  {"name":name, "username":username, "password":secure_password})
    # bb.comimit()
    # return redirect(url_for("login"))
    # else:
    # return render_template("registro.html")
    return render_template("registro.html")


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response


@app.route("/login")
def loginn():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
