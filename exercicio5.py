# EXERCÍCIO 5

# Definindo a string ou solicitando a entrada do usuário
entrada = input("Informe uma string para inverter: ")

# Função para inverter a string sem usar funções prontas
def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida  # Adiciona o caractere no início
    return string_invertida

# Invertendo a string
resultado = inverter_string(entrada)

# Exibindo o resultado
print(f"String invertida: {resultado}")