import math
def areaCirculo(r):
    return math.pi * pow(r,2)

def perimetroCirculo(r):
    return 2 * math.pi * r

def areaRectangulo(b, a):
    return b * a

def perimetroRectangulo(b, a):
    return (b * 2) + (a * 2)

def tipoTriangulo(l1, l2 ,l3):
    if l1 <= 0 or l2 <= 0 or l3 <= 0:
        print("No se puede calcular")
    elif l1 == l2 and l1 == l3 and l2 == l3:
        print("Es equilatero")
    elif (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l2 != l1):
        print("Es iscoceles")
    elif (l1 != l2 and l1 != l3 and l2 !=l3):
        print("Es escaleno")