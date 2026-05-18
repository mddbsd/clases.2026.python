#Los operadores lógicos se utilizan para combinar 2 o mas expresiones lógicas
#Vamos a estudiar 3 de estos operadores, AND, OR, NOT

#El operador AND requiere que una de las expresiones logicas sea verdadera para que 
#la salida de como resultado verdadero.

x = 10

print(x > 0 and x < 20)
print(x == 8 and x > 5)

#El operador OR requiere que solo una de las expresiones
#sea verdadera para que su resultado sea verdadero

print(x == 10 or x < 8)
print(x < 3 or x == 9)

#El operador not niega la expresion logica, cuando esta es verdadera
#el not devuelve falso y viceversa

print(not(x == 10))

#podemos combinar multiples expresiones logicas con distintos operadores logicos

a = 10
b = 12
c = 13
d = 10

print(((a > b) or (a < c)) and ((a == c) or (a >= b)))

print(((a >= b) or (a < d)) and ((a >= d) and (c > d)))

print(not(a == c) and (c > b))

m = 8, n = 9, r = 5, s = 5
t = 4, v = 7

not(( m > n and r > s) or (not(t > v and s > m)))

print((3 >= 3 or 5 != 5) and not(15 / 5 + 2 != 5))

print((3 >= 4 and 5  > 3 and 3 > 3) or not(4 <= 4 or 5 > 4 or 6 >= 7))