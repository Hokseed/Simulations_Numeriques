import random

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def chiffrementRSA(p, q, message): #p,q sont des nombres premiers non egaux
  # générer les paires p,q
  n = p * q
  phi = (p-1) * (q-1) #indicatrice de n
  e = random.randrange(1, phi) #e aléatoire tel que e et phi(n) sont premiers entre eux

  #Utilisation de l'algo d'Euclide pour le verifier
  g = pgcd(e, phi)
  while g != 1:
    e = random.randrange(1, phi)
    g = pgcd(e, phi)

  #Utilisation de l'algo d'Euclide étendu pour générer une clé privée
  #On cherche l'inverse de e et de phi (bout de code issu de openclassrooms)
  d,x1,x2,y1,temp_phi = 0,0,1,1,phi
  while e > 0:
    temp1 = temp_phi/e
    temp2 = temp_phi - temp1 * e
    temp_phi,e = e,temp2
    x,y = x2- temp1* x1, d - temp1 * y1
    x2,x1,d,y1 = x1,x,y1,y
  if temp_phi == 1:
    d = d + phi
  cleprivee = (d, n)

  #chiffrement du message
  key, n = cleprivee #décomposition de la clé privée
  #conversion du message en nombre en fct de chaque lettre en utilisant a^b % m
  meschiffre = [(ord(char) ** key) % n for char in message]
  #affichage du message chiffré
  print("Message chiffré:",''.join(map(lambda x: str(x), meschiffre)))

chiffrementRSA(17,19,'Bonjour le monde')
