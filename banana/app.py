import csv
from flask import Flask , render_template , request, redirect, url_for
from validate_docbr import CPF, CNPJ
app = Flask(__name__)
def load_products_from_csv():
    lista_produtos = []
    with open('produtos.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            lista_produtos.append(row)
    return lista_produtos
@app.route("/home")
def home(): 
    return '<h1>Home</h1>'

@app.route("/contato")
def contato(): 
    return '<h1>Contato</h1>'



# Save products to CSV file
def save_products_to_csv(lista_produtos):
    with open('produtos.csv', 'w', newline='') as csvfile:
        fieldnames = ['nome', 'descricao', 'preco', 'imagem']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for produto in lista_produtos:
            writer.writerow(produto)

# Initial load of products
lista_produtos = load_products_from_csv()

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=lista_produtos)

@app.route("/produtos/cadastro")
def cadastro_produto():
    return render_template("cadastro-produto.html")

@app.route("/produtos", methods=["POST"])
def salvar_produto():
    nome = request.form["nome"]
    descricao = request.form["descricao"]
    preco = request.form["preco"]
    imagem = request.form["imagem"]
    produto = {"nome": nome, "descricao": descricao, "preco": preco, "imagem": imagem}
    lista_produtos.append(produto)
    save_products_to_csv(lista_produtos)
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