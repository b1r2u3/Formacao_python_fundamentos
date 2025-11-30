def calcular(operacao):
    def somar(a, b):
        return a + b
    
    def sub(a, b):
        return a - b
    
    def mult(a, b):
        return a * b
    
    def div(a, b):
        return a / b
    
    match operacao:
        case "+":
            return somar
        case "-":
            return sub
        case "*":
            return mult
        case "/":
            return div
    
op = calcular("+")
print(op(2, 2))
op = calcular("-")
print(op(2, 2))
op = calcular("*")
print(op(2, 2))
op = calcular("/")
print(op(2, 2))