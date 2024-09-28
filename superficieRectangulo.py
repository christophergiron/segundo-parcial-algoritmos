a = float(input("ingrese el primer lado de su rectangulo:"))
b = float(input("ingrese el segundo lado de su rectangulo:"))
superficie1 = (a*b)
print("la superficie de su rectangulo es de:", superficie1)

c = float(input("ingrese el lado de su segundo rectangulo:"))
d = float(input("ingrese el segundo lado de su segundo rectangulo:")) 
superficie2 = (c*d)
print("la superficie de su rectangulo es de:", superficie2)
def comparacion_de_Rectangulos():
    if superficie1 > superficie2:
        print("el primer rectangulo tiene una mayor superficie")
    elif superficie2 > superficie1:
        print("el segundo rectangulo tiene mayor superficie")
    else:
        print("los rectangulos tienen la misma superficie")
        
#primer bloque 
comparacion_de_Rectangulos()