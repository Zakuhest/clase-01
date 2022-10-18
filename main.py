def sumar(a, b):
    resultado = a + b
    print("\nEl resultado de", a, "+", b, "es:", resultado)


def restar(a, b):
    resultado = a - b
    print("\nEl resultado de", a, "-", b, "es:", resultado)


def multiplicar(a, b):
    resultado = a * b
    print("\nEl resultado de", a, "*", b, "es:", resultado)


def dividir(a, b):
    resultado = a / b
    print("\nEl resultado de", a, "/", b, "es:", resultado)


def potenciar(a, b):
    resultado = a ** b
    print("\nEl resultado de", a, "**", b, "es:", resultado)


def potencia_recursiva(a, b):
    if b < 0:
        return -1

    if b == 0:
        return 1

    return potencia_recursiva(a, b - 1) * a


start = True
resultado = 0

print("""
|==================|
|Calculadora básica|
|==================|"""
      )

while start:

  try:
  
      print("""
    ============
    OPERACIONES:
    ============
    -> Sumar (+)
    -> Restar (-)
    -> Multiplicar (*)
    -> Dividir (/)
    -> Potenciar (**)
    -> Potencia Recursiva (recursiva)
    """
            )
  
      a = int(input("\nIngresar el primer número: "))
  
      b = int(input("Ingresar el segundo número: "))
  
      op = input("Escribir la operación a realizar (nombre/signo)): ").lower()
  
      while op not in ("sumar", "+", "restar", "-", "multiplicar", "*", "dividir", "/",
                       "potenciar", "**", "potencia recursiva", "recursiva", "recursivo"):
  
          op = input("Escribir nuevamente la operación a realizar (nombre/signo)): ").lower()
  
      if op == "sumar" or op == "+":
          sumar(a, b)
  
      if op == "restar" or op == "-":
          restar(a, b)
  
      if op == "multiplicar" or op == "*":
          multiplicar(a, b)
  
      if op == "dividir" or op == "/":
          dividir(a, b)
  
      if op == "potenciar" or op == "**":
          potenciar(a, b)
  
      if op == "potencia recursiva" or op == "recursiva" or op == "recursivo":
          print("\nEl resultado recursivo es:", potencia_recursiva(a, b))
  
      q = input("\nDesea realizar otra operación? (y/n): ").lower()
  
      if q == "y":
          start = True
      else:
          start = False
          print("\nTerminado con éxito.")
  except:
      print("\nError. Vuelva a ejecutar el programa.")
