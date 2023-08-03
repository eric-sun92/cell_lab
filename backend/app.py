from flask import Flask, request, jsonify, session, g
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def get_user_gene_list():
    if 'user_genes' not in g:
        g.user_genes = []
    return g.user_genes

@app.route('/add_gene', methods=['POST'])
def add_gene():
    data = request.get_json()
    gene_name = data.get('gene_name')
    if gene_name:
        user_genes = get_user_gene_list()
        user_genes.append(gene_name)
        return jsonify({"message": "Gene name added successfully!"})
    else:
        return jsonify({"error": "Invalid gene name."}), 400

@app.route('/get_user_genes', methods=['GET'])
def get_user_genes():
    user_genes = get_user_gene_list()
    return jsonify({"user_genes": user_genes})
