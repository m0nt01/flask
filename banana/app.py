from flask import Flask , render_template , request, redirect, url_for
from validate_docbr import CPF, CNPJ
lista_produtos = [
        {"nome": "Coca-cola" , "descricao":"Bom" , "preco" : "5,00"},
        {"nome": "Pepsi" , "descricao":"Ruim" , "preco" : "2,50"},
        {"nome": "Dolly" , "descricao":"Custo beneficios" , "preco" : "3,00"},
    ]

app = Flask(__name__)

@app.route("/home")
def home(): 
    return '<h1>Home</h1>'

@app.route("/contato")
def contato(): 
    return "Produto não existe!"
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

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")


@app.route("/produtos", methods=['POST'])
def salvar_produto():
    request.form['nome']
    descricao = request.form['descricao']
    produto = { "nome": nome, "descricao":descricao }
    lista_produtos.append(produto)

    return redirect(url_for("produtos"))

@app.route('/')
def index():
    return render_template('index.html')

@ app.route('/gerar_cpf', methods=['GET'])
def gerar_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return render_template('gerar_cpf.html', cpf_gerado=cpf_gerado)

@ app.route('/gerar_cnpj', methods=['GET'])
def gerar_cnpj():
    cnpj = CNPJ()
    cnpj_gerado = cnpj.generate()
    return render_template('gerar_cnpj.html', cnpj_gerado=cnpj_gerado)

@ app.route('/validar_cpf', methods=['GET', 'POST'])
def validar_cpf():
    if request.method == 'POST':
        cpf = CPF()
        cpf_usuario = request.form['cpf_usuario']
        if cpf.validate(cpf_usuario):
            return render_template('validar_cpf.html', cpf_usuario=cpf_usuario, mensagem='CPF válido')
        else:
            return render_template('validar_cpf.html', cpf_usuario=cpf_usuario, mensagem='CPF inválido')
    return render_template('validar_cpf.html')

@ app.route('/validar_cnpj', methods=['GET', 'POST'])
def validar_cnpj():
    if request.method == 'POST':
        cnpj = CNPJ()
        cnpj_usuario = request.form['cnpj_usuario']
        if cnpj.validate(cnpj_usuario):
            return render_template('validar_cnpj.html', cnpj_usuario=cnpj_usuario, mensagem='CNPJ válido')
        else:
            return render_template('validar_cnpj.html', cnpj_usuario=cnpj_usuario, mensagem='CNPJ inválido')
    return render_template('validar_cnpj.html')

if __name__ == '__main__':
    app.run(debug=True)
app.run(port=5001)