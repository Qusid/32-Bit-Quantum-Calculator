from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit import QuantumRegister, ClassicalRegister
from qiskit.circuit.library import CDKMRippleCarryAdder
from Modifier import Modifier

def Adder(a,b):
    
  Qcr,ls = Modifier(a,b)
  cin = QuantumRegister(1, name='cin')
  a = QuantumRegister(ls, name='a')
  b = QuantumRegister(ls, name='b')
  out = QuantumRegister(1, name='out')

  Qc1 = QuantumCircuit(cin,a,b,out, name = "Modified")

  plist = []
  for i in range((ls*2)+2): plist.append(i)

  Qc1.append(Qcr,plist[1:])
  Qc1.append(CDKMRippleCarryAdder(ls),plist)
  Qc1.measure_all()
  psi = Sampler().run(Qc1, shots=1).result().quasi_dists[0].binary_probabilities()
  results = int(next(iter(psi))[:ls+1],2)
  return results