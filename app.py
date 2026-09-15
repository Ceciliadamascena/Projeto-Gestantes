from flask import Flask, render_template, url_for, redirect, request
# from flask import criar_tabela, inserir, listar, buscar_por_id, atualizar, excluir
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy()
db.init_app(app)
# migrate = Migrate(app,db)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")
   
class Gestante(db.Model):

    __tablename__ = "gestantes"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    cpf = db.Column(db.String(14), nullable=False)
    peso = db.Column(db.Float, nullable=False)
    altura = db.Column(db.Float, nullable=False)
    inicio_gestacao = db.Column(db.String(10), nullable=False)
    prenatal = db.Column(db.String(3), nullable=False)
    email = db.Column(db.String(100), nullable=False)

@app.route('/adicionar', methods=['GET','POST'])
def adicionar():
    if request.method == "POST":
        nome= request.form('nomeForm')
        numero= request.form('numeroForm')
        email= request.form('emailForm')
        cpf= request.form('cpfForm')
        idade= request.form('idadeForm')
        peso= request.form('pesoForm')
        altura= request.form('alturaForm')
        inicio_gestacao= request.form('inicio_gestacaoForm')
        prenatal= request.form('prenatalForm')

    gestante= Gestante(
        nome=nome,
        numero=numero,
        email=email,
        cpf=cpf,
        idade=idade,
        peso=peso,
        altura=altura,
        inicio_gestacao= inicio_gestacao,
        prenatal=prenatal
        )
    db.session.add(gestante)
    db.sesion.commit()
    return redirect(url_for("index"))
    return render_template("cadastrar.html")



# # def inserir(nome, telefone, cpf, peso, altura,
#             inicio_gestacao, prenatal, email):

#     conexao = conectar()
#     cursor = conexao.cursor()

#     cursor.execute("""
#         INSERT INTO gestantes
#         (nome, telefone, cpf, peso, altura,
#          inicio_gestacao, prenatal, email)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     """, (
#         nome,
#         telefone,
#         cpf,
#         peso,
#         altura,
#         inicio_gestacao,
#         prenatal,
#         email
#     ))

#     conexao.commit()
#     conexao.close()
# @app.route("/adicionar", methods=["GET", "POST"])
# def adicionar():

#     if request.method == "POST":

#         nome = request.form["nome"]
#         telefone = request.form["telefone"]
#         cpf = request.form["cpf"]
#         peso = request.form["peso"]
#         altura = request.form["altura"]
#         inicio_gestacao = request.form["inicio_gestacao"]
#         prenatal = request.form["prenatal"]
#         email = request.form["email"]

#         inserir(
#             nome,
#             telefone,
#             cpf,
#             peso,
#             altura,
#             inicio_gestacao,
#             prenatal,
#             email
#         )

#         return redirect("/listar")

#     return render_template("adicionar.html")

# @app.route("/cadastro")
# def cadastro():
#     return render_template("cadastro.html")

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug=True)
