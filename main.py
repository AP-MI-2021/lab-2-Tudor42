#problema 3, 4, 5

def is_prime(n):
  """
  input:
    n - numarul verificat
  output:
    True  - n este prim
    False - n nu este prim
  """
  if n == 2:
    return True

  if n < 2 or not n % 2:
    return False

  for i in range(3, n//2 + 1, 2):
    if n % i == 0:
      return False
  return True


def get_goldbach(n):
  """
  input:
    n - numarul pentru care se genereaza p1 si p2
      astfel incat n = p1 + p2
  output:
    [p1, p2] - daca p1 si p2 exista
    None - in caz contrar
  """
  if n < 4: #numerele mai mici de 4 nu pot fi
    # reprezenteate ca suma de 2 numere prime
    return None

  if n == 4:
    return [2, 2]

  if n % 2: # daca n este impar atunci p1 e 2
    j = n - 2
    if is_prime(j):
      return [2, j]
    return None

  for i in range(3, n//2 + 1, 2): # daca n este par
    if is_prime(i):
      j = n - i
      if is_prime(j):
        return [i, j]

  return None

def test_get_goldbach():
  print("Test 1")
  assert get_goldbach(1) is None, "should be None"
  print("Test 15")
  assert get_goldbach(15) == [2, 13], "should be [2, 13]"
  print("Test 21")
  assert get_goldbach(21) == [2, 19], "should be [2, 19]"
  print("Test 24")
  assert get_goldbach(24) == [5, 19], "should be [5, 19]"
  print("Test 28")
  assert get_goldbach(28) == [5, 23], "should be [5, 23]"
  print("Test 97")
  assert get_goldbach(97) is None, "should be None"
  print("Test 100")
  assert get_goldbach(100) == [3, 97], "should be [3, 97]"
  print("Test 10000")
  assert get_goldbach(10000)      == [59, 9941], "should be [59, 9941]"
  print("Test 80000")
  assert get_goldbach(80000)      == [3, 79997], "should be [3, 79997]"
  print("Test 100000000")
  assert get_goldbach(100000000) == [11, 99999989], "should be [71, 999999929]"
  print("Everything passed")
  

def get_newton_sqrt(n, steps):
  """
  input:
    n - numarul
    steps - numarul de aproximari
  output:
    radical din n
  """
  if n < 0 or steps < 0:
    return None
  x0 = 2
  while steps:
    x0 = 0.5 * (x0 + n/x0)
    steps -= 1
  return x0


def test_get_newton_sqrt():
  print("Test sqrt of -1 with 2 aproximations")
  assert get_newton_sqrt(-1, 2) == None
  print("Test sqrt of 0 with 15 aproximations")
  assert round(get_newton_sqrt(0, 15), 3) == 0.0
  print("Test sqrt of 2 with 5 aproximations")
  assert round(get_newton_sqrt(2, 5), 8) == 1.41421356
  print("Test sqrt of 10 with 6 aproximations")
  assert round(get_newton_sqrt(10, 6), 8) == 3.16227766
  print("Test sqrt of 16 with 6 aproximations")
  assert get_newton_sqrt(16, 6) == 4.0
  print("Test sqrt of 32 with 6 aproximations")
  assert round(get_newton_sqrt(32, 6), 8) == 5.65685425
  print("Test sqrt of 1024 with 9 aproximations")
  assert get_newton_sqrt(1024, 9) == 32.0
  print("Test sqrt of 50000 with 11 aproximations")
  assert round(get_newton_sqrt(50000, 11), 6) == 223.606798
  print("Everything passed")

def is_palindrome(n) -> bool:
  n = str(n)
  m = n[-1::-1]
  if m == n:
    return True
  return False

def test_is_palindrome():
  print('Test 0')
  assert is_palindrome(0) is True
  print('Test 54')
  assert is_palindrome(54) is False
  print('Test 131')
  assert is_palindrome(131) is True
  print('Test 109312')
  assert is_palindrome(109312) is False
  print('Test 199979991')
  assert is_palindrome(199979991) is True
  print('Everything passed')

def main():
  print('###')
  print('Se testeaza get_newton_sqrt:')
  test_get_newton_sqrt()
  print('###')
  print('Se testeaza get_goldbach')
  test_get_goldbach()
  print('###')
  print('Se testeaza is_palindrome')
  test_is_palindrome()
  print()
  print('Scrie help pentru a vedea lista de comenzi')
  while True:
    command = input('$').split()
    if command[0] == 'help':
      print('get_goldbach [n]            - genereaza p1 si p2 prime astfel incat n = p1 + p2')
      print('get_newton_sqrt [n] [steps] - calculeaza radicalul lui n dupa algoritmul lui newton')
      print('is_palindrome [n]           - verifica daca un numar este palindrom')
      print('quit                        - opreste programul')
    if command[0] == 'get_newton_sqrt':
      if len(command) < 3:
        print('prea putini argumenti')
        continue
      try:
        steps = int(command[2])
      except:
        print("numarul de pasi trebuie sa fie un numar intreg")
        continue
      try:
        print(get_newton_sqrt(float(command[1]), steps))
      except:
        print('n trebuie sa fie un numar')
    if command[0] == 'get_goldbach':
      if len(command) < 2:
        print('prea putini argumenti')
      try:
        print(get_goldbach(int(command[1])))
      except:
        print('argumentul trebuie sa fie numar intreg')
    if command[0] == 'is_palindrome':
      if len(command) < 2:
        print('prea putini argumenti')
        continue
      print(is_palindrome(command[1]))

    if command[0] == 'quit':
      break

if __name__ == '__main__':
  main()
