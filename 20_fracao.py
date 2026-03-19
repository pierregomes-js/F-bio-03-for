def main():
  n = int(input('N: '))

  somatorio = 0
  for i in range(1, n+1):
    if i % 2 == 0:
        somatorio -= 1/i
    else:
       somatorio += 1/i

  print(f'S = {somatorio:.2f}')


main()