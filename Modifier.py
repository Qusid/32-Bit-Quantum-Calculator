from qiskit import QuantumCircuit

def Modifier(a,b):
  n1,n2 = a,b
  #converting the number into binanry
  Ba, Bb = '{:32b}'.format(n1),'{:32b}'.format(n2)
  Ba.split('1')
  Bb.split('1')
  Ba = Ba.replace(" ", "")
  Bb = Bb.replace(" ", "")
  la = len(Ba)
  lb = len(Bb)
  if la > lb:
    Bb = "0"*(la-lb) + Bb
  else:
    Ba = "0"*(lb-la) + Ba

  l1 = len(Ba)
  l2 = len(Bb)
  ls = l1
  Qc1 = QuantumCircuit(ls*2+1, name = "Bin Transform")

  # for putting in the digits in binaanry as per x gates
  for i in range(ls):
    if Ba[i] == "1":
      Qc1.x(ls-i-1)

  for i in range(ls):
    if Bb[i] == "1":
      Qc1.x(-1-i+ls*2)

  return Qc1,ls
