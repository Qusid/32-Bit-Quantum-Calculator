from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from qiskit import QuantumRegister, ClassicalRegister
from qiskit.circuit.library import CDKMRippleCarryAdder
from Modifier import Modifier

def Multiply(a,b):

  Qcr,ls = Modifier(a,b)
  a = QuantumRegister(ls, name='a')
  b = QuantumRegister(ls, name='b')
  out = QuantumRegister((ls)*2, name='out')
  helper = QuantumRegister(1, name='helper')

  Qc1 = QuantumCircuit(a,b,out,helper, name = "Multiplier")

  plist = []
  for i in range(ls*2+1): plist.append(i)

  Qc1.append(Qcr,plist)

  gate = CDKMRippleCarryAdder(ls,kind = "half").to_gate().control()


  for i in range(ls):
    xlist = [i]
    for k in range(ls,ls*2):
      xlist.append(k)
    for j in range(ls*2,ls*3+1):
      xlist.append(j+i)

    xlist.append(ls*4)
    Qc1.append(gate, xlist)

  # printing the circuit
  Qc1.measure_all()
  psi = Sampler().run([Qc1], shots=1).result().quasi_dists[0].binary_probabilities()
  results = int(next(iter(psi))[:ls*2+1],2)
  return results
