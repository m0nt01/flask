from flask import Flask , render_template
lista_produtos = [
        {"nome": "Coca-cola" , "descricao":"Bom" },
        {"nome": "Pepsi" , "descricao":"Ruim" },
        {"nome": "Dolly" , "descricao":"Custo beneficios" },
    ]

app = Flask(__name__)

@app.route("/")
def home(): 
    return '<h1>Home</h1>'

@app.route("/contato")
def contato(): 
    return '<h1>Contato</h1>'

@app.route("/produtos")
def lista_produtos():
    return render_template("produtos.html", produtos = lista_produtos)
 
@app.route("/produtos/home/<nome>")
def produto(nome):
    for produto in lista_produtos:
        if produto("nome") == nome:
            return render_template("produto.html", produto=produto)


    return "Produto não existe!"