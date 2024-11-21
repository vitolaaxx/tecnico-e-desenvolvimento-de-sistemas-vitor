# Definindo a função que verifica se um número é par ou ímpar
def verificar_par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


numero1 = 7
numero2 = 10

resultado1 = verificar_par_ou_impar(numero1)
resultado2 = verificar_par_ou_impar(numero2)

print(f"O número {numero1} é {resultado1}.")
print(f"O número {numero2} é {resultado2}.")
