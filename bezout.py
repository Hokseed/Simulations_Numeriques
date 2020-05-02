def bezout(a, b):
  if b == 0: # si b est nul
    # retourne (u,v) = (1,0) et pgcd=a
    return a, 1, 0
  # division euclidienne: q=a/b+r
  q, r = divmod(a, b)
  # appel recursif pgcd = ub + vr
  d, u, v = bezout(b, r)
  # on veut pgcd = ua + vb donc
  # pgcd = ub+vr = ub + v(a-qb) = va + (U-qv)b
  # donc on retourne (u,v) = (v,u-q*v)
  return d, v, u-q*v

print(bezout(10,4))
