# Programa para realizar los operadores, usando las diferentes formulas

print("-------------------------------------")
print("El resultado de las operaciones son:-")
print("-------------------------------------")

# input
nc = int(input("Digite el valor de la nota cognitiva: "))
np = int(input("Digite el valor de la nota procedimental: "))
na = int(input("Digite el valor de la nota actitudinal: "))
au = int(input("Digite el valor de la autoevaluación: "))
bi = int(input("Digite el valor de la nota bimestral: "))

# processing

nd = (0.3*nc) + (0.3*np) + (0.1*na) + (0.1*au) + (0.2*bi)

# output 

print("-----------------------------")
print("resultados de las operaciones")
print("-----------------------------")

print("nota definitiva " + str(nd))