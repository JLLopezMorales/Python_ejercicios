nombre=input("Ingrese su nombre: ")
print("Hola, " + nombre + "! Bienvenido/a al programa, es tu primera vez usando VS Code.")
for i in range(5):
    print("Este es el mensaje número " + str(i+1))
if i == 4:
    print("¡Gracias por usar el programa, " + nombre + "! Esperamos que tengas una excelente experiencia.") 
y=input("¿Deseas continuar usando el programa? (sí/no): ")
if y.lower() == "sí":
    print("¡Genial! Continuemos con el programa.") 