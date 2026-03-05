print("\n\n---------------------------------------------------------\n--------------Simulador de Somatória (Ex.4)--------------\n---------------------------------------------------------")
i = 1
acumulo = 0
while i<10:

    valor = int(input("Digite o número: "))
    acumulo = acumulo + valor
    i = i+1
    
print("%d" % acumulo)