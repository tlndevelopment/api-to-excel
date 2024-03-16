import requests
import openpyxl

response = requests.get("http://3.144.19.115:8080/GamecenterAPI/gamecenter/produtos").json()

excel = openpyxl.Workbook()
comunidades = excel['Sheet']
comunidades.title = 'Produtos'
comunidades.append(['Produto', "Descrição", "Valor", "Frete", "Vendedor", "Produto Vendido", "Nota da Venda"])

for item in response:
    comunidades.append([item['nome'], item['descricao'], item['valor'], item['frete'], item['nickVendedor'], "Sim" if item['vendido'] else "Não", item['notaVenda']])

excel.save("catalogo.xlsx")