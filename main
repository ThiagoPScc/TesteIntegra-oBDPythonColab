import pymongo

uri = ""
client = pymongo.MongoClient(uri)


db = client["meu_projeto"]        
colecao = db["usuarios"]         


def inserir_usuario(nome, idade, curso):
    documento = {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }
    resultado = colecao.insert_one(documento)
    print(f"Dado inserido com ID: {resultado.inserted_id}")


def buscar_usuarios():
    print("\n Consultando dados:")
    for doc in colecao.find():
        print(doc)


def deletar_por_nome(nome):
    resultado = colecao.delete_one({"nome": nome})
    if resultado.deleted_count > 0:
        print(f"Registro de '{nome}' removido com sucesso.")
    else:
        print("Nenhum registro encontrado para deletar.")


try:
  
    inserir_usuario("Thiago", 22, "Ciência da Computação")
    
  
    buscar_usuarios()
    
    

except Exception as e:
    print(f"Erro na conexão: {e}")
