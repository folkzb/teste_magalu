from pymongo import MongoClient

url_con = 'mongodb+srv://bruno:canela@gama.9tcj4nl.mongodb.net/test'
collection = 'magalu'

def obter_colecao_mongodb(url_conexao, colecao):
    conn = MongoClient(url_conexao)
    db = conn[colecao]
    query = db.teste_div.find_one({'produto':'banana'})
    print(query)
    
obter_colecao_mongodb(url_con,collection)
