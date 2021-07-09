import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session


# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///lobo.db")

@app.route("/", methods=["GET", "POST"])
def index():

    cliente = request.form.get("cliente")
    impressao = request.form.get("impressao")
    descricao = request.form.get("descricao")
    custo = request.form.get("custo")
    valor = request.form.get("valor")
    data = request.form.get("data")
    filamento = request.form.get("filamento")

    if request.method == "POST" and not cliente and not impressao and not descricao and not custo and not valor and not data and not filamento:

        return redirect("/")

    elif request.method == "POST":

        db.execute("INSERT INTO lobo (nome, impressao, descricao, custo, valor, data, filamento) VALUES (?,?,?,?,?,?,?)", cliente, impressao, descricao, custo, valor, data, filamento)
        return redirect("/")


    else:
        # TODO: Display the entries in the database on index.html
        display = db.execute("SELECT * FROM lobo")
        return render_template("index.html", display = display)


@app.route("/redirect_apagar", methods = ["GET", 'POST'])
def redirect_apagar():

    if request.method == 'POST':

        id = request.form.get("apagar")
        display = db.execute("SELECT * FROM lobo WHERE id = ?", id)
        return render_template("/apagar.html", display = display)

    return redirect("/")


@app.route("/apagar", methods = ['GET', 'POST'])
def apagar():

    if request.method == 'POST':

        id = request.form.get("id")
        db.execute("DELETE FROM lobo WHERE id = ?", id)
        return redirect("/")

    return redirect("/")


@app.route("/redirect_editar", methods = ["GET", "POST"])
def redirect_editar():

     if request.method == 'POST':
        id = request.form.get("editar")
        display = db.execute("SELECT * FROM lobo WHERE id = ?", id)
        return render_template("/editar.html", display = display)




@app.route("/editar", methods = ["GET", "POST"])
def editar():

     cliente = request.form.get("cliente")
     impressao = request.form.get("impressao")
     descricao = request.form.get("descricao")
     custo = request.form.get("custo")
     valor = request.form.get("valor")
     data = request.form.get("data")
     filamento = request.form.get("filamento")
     id = request.form.get("id")


     if request.method == "POST":

        db.execute("UPDATE lobo SET nome = ? WHERE id = ?", cliente, id)
        db.execute("UPDATE lobo SET impressao = ? WHERE id = ?", impressao, id)
        db.execute("UPDATE lobo SET descricao = ? WHERE id = ?", descricao, id)
        db.execute("UPDATE lobo SET custo = ? WHERE id = ?", custo, id)
        db.execute("UPDATE lobo SET valor = ? WHERE id = ?", valor, id)
        db.execute("UPDATE lobo SET data = ? WHERE id = ?", data, id)
        db.execute("UPDATE lobo SET filamento = ? WHERE id = ?", filamento, id)

        return redirect("/")

     return  redirect("/")