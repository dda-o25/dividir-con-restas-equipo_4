"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones
#CONSTANTE = valor


# Entradas
#entrada = int(input(""))
dividendo = int(input("dividendo:"))
divisor = int(input("divisor"))
cociente=0
residuo = dividendo
# Proceso
   
while residuo >= divisor:
    residuo = residuo - divisor
    cociente= cociente + 1

print("cociente",cociente)
print("Residuo:", residuo)

# Salidas
#print(salida)