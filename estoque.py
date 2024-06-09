estoque = ["camiseta", "calça", "sapato", "boné"]

def verificar_estoque(item):
    if item in estoque:
        return True
    else:
        return False

# Exemplo de uso da função
item_desejado = "sapato"
if verificar_estoque(item_desejado):
    print(f"O item {item_desejado} está em estoque.")
else:
    print(f"O item {item_desejado} não está em estoque.")