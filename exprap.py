def exprap(x,n):
  if n == 0: # si l'exp vaut 0
    # retourne x^0 = 1
    return 1
  elif (n % 2 == 0): # si l’exp est paire
    # récupere le resultat d’un appel récursif x^(n/2)
    a = exprap(x, n/2)
    # retourne x^(n/2) * x^(n/2)
    return a*a
  else: # sinon
    # retourne le produit de x et de x^(n-1) car x^n = x*x^(n-1)
    # permet de se retrouver dans le elif lors de l'appel recursif
    return x * exprap(x, n - 1)

print(exprap(10, 4))
