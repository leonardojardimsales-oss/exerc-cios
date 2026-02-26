print("\n\n---------------------------------------------------------\n-------Simulador de Análise de Procedência (Ex.1)--------\n---------------------------------------------------------")

valor = float(input("\nInsira o código de origem do produto: "))
valor = int(valor)
print("-------------------------------------\nCódigo de origem #%d" % valor)
if valor==1:
    print("Esse produto provém da região Sul")
elif valor==2:
    print("Esse produto provém da região Norte")
elif valor==3:
    print("Esse produto provém da região Leste")
elif valor==4:
    print("Esse produto provém da região Oeste")
elif valor==5 or valor==6:
    print("Esse produto provém da região Nordeste")
elif 7>=valor>=9:
    print("Esse produto provém da região Sudeste")
elif 10>=valor>=20:
    print("Esse produto provém da região Centro-Oeste")
elif 25>=valor>=30:
    print("Esse produto provém da região Nordeste")
else:
    print("Esse produto é importado")
print("\n")