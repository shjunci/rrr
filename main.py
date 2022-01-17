teksts = input("Ievadit tekstu:"  )

def countNumbers(teksts):
  summa = 0
  for simbols in teksts:
    summa = summa + int(simbols)
  return summa
  
print(countNumbers(teksts))
                      