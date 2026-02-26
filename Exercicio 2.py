print("\n\n---------------------------------------------------------\n-----------Simulador de Análise Numérica (Ex.2)----------\n---------------------------------------------------------\nVocê deverá inserir 3 valores inteiros diferentes para serem analisados e colocados em ordem decrescente.\n")
v1=float(input("Insira o primeiro valor: "))
v2=float(input("Insira o segundo valor: "))
v3=float(input("Insira o terceiro valor: "))
v1=int(v1)
v2=int(v2)
v3=int(v3)
print("-------------------------------------------------------")
if v1 >= v2 and v1 >= v3:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v1,v2,v3))
elif v1 >= v3 >= v2:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v1,v3,v2))
elif v2 >= v1 >= v3:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v2,v1,v3))
elif v2 >= v3 >= v1:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v2,v3,v1))
elif v3 >= v1 >= v2:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v3,v1,v2))
elif v3 >= v2 >= v1:
    print("A ordem numérica em forma decrescente é: %d / %d / %d" % (v3,v2,v1))
else:
    print("Erro")
print("\n")