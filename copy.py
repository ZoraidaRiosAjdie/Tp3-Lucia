from sys import argv

foc = open(argv[1],'r')
fe = open("mifile","r")
fs = open("file11","w")
todo = fe.read()
fs.write(todo)

linea = foc.readline().strip()
while linea:
  if linea[len(linea) - 1] != '.':
    linea1 = linea + '.'
  else:
    linea1 = linea
  print(linea1.capitalize())
  linea = foc.readline().strip()
fe.close()
fs.close()