# 32-Bit Quantum Calculator

A small Python calculator that does addition, subtraction, and multiplication with quantum circuits built in [Qiskit](https://www.ibm.com/quantum/qiskit) and run on the Qiskit Aer simulator. It comes with a command-line interface and a Tkinter GUI that can show the circuit behind each result.

It's meant as an educational example of quantum arithmetic, not a fast way to do math.

## How it works

1. **Encoding** (`Modifier.py`): both inputs are written in binary, padded to the same width `n`, and loaded into qubits with X gates.
2. **Addition** (`Upto32BitAdder.py`): Qiskit's `CDKMRippleCarryAdder` (the Cuccaro–Draper–Kutin–Moulton ripple-carry adder) adds the two registers on `2n + 2` qubits.
3. **Subtraction** (`Upto32Subtractor.py`): the inverse of the same adder circuit computes the difference.
4. **Multiplication** (`Upto32BitMultiplier.py`): shift-and-add, using a controlled half-adder for each bit of the first number, on `4n + 1` qubits.
5. **Readout**: the circuit is measured once with the Aer `Sampler` and the bitstring is converted back to an integer.

Each function returns `(result, circuit)` so you can inspect the circuit that produced the answer.

## Getting started

### Requirements

- Python 3.9+
- Tkinter (bundled with most Python installs; only needed for the GUI)

### Install

```bash
git clone https://github.com/Qusid/32-Bit-Quantum-Calculator.git
cd 32-Bit-Quantum-Calculator
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r Requirements.txt
```

Tested with Qiskit 1.4 and Qiskit Aer 0.17. The code uses the V1 `Sampler` from `qiskit_aer.primitives`, so newer versions may emit deprecation warnings or need small changes.

## Usage

### Command line

```bash
python Calculator.py
```

```
Select operation.
1.Add
2.Subtract
3.Multiply
Enter choice(1/2/3): 1
Enter first number: 4
Enter second number: 6
4.0 + 6.0 = (10, <qiskit.circuit.quantumcircuit.QuantumCircuit object at 0x...>)
Let's do next calculation? (yes/no): no
```

### GUI

```bash
python Gui.py
```

Enter two integers, choose **Add**, **Subtract**, or **Multiply**, and click **Calculate**. After a calculation, **Show Circuit** opens a window with a text drawing of the quantum circuit used.

### From Python

```python
from Upto32BitAdder import Adder
from Upto32BitMultiplier import Multiply

result, circuit = Adder(4, 6)      # 10
result, circuit = Multiply(5, 4)   # 20
print(circuit.draw())
```

## Limitations

The "32-bit" in the name is the circuits' design width. In practice, the size you can run is limited by the simulator: Aer's default statevector method needs memory that doubles with every extra qubit.

- **Add / subtract** use `2n + 2` qubits. Inputs up to about 10 bits (around 1,000) run in under a second. 15-bit inputs already need about 64 GB of memory.
- **Multiply** uses `4n + 1` qubits. Inputs up to 5 bits (31) run in about a second, and larger inputs slow down quickly.
- Inputs should be non-negative integers.

## Project structure

```
32-Bit-Quantum-Calculator/
├── Calculator.py            # Command-line interface
├── Gui.py                   # Tkinter GUI with circuit viewer
├── Modifier.py              # Encodes the two inputs into qubits
├── Upto32BitAdder.py        # Adder(a, b)
├── Upto32Subtractor.py      # Sub(a, b)
├── Upto32BitMultiplier.py   # Multiply(a, b)
├── Requirements.txt         # Python dependencies
└── LICENSE
```

## Contributing

Issues and pull requests are welcome, for example for division, newer Qiskit primitives, or larger inputs through other simulation methods.

## License

Released under the [MIT License](LICENSE). Copyright (c) 2024 Siddhant Gupta.

If you use or adapt this code, please credit **Siddhant Gupta** and the **32-Bit Quantum Calculator** project (https://github.com/Qusid/32-Bit-Quantum-Calculator).

Qiskit and Qiskit Aer are separate projects under the Apache License 2.0.

## Acknowledgements

- [Qiskit](https://github.com/Qiskit/qiskit) for the `CDKMRippleCarryAdder` circuit and the SDK.
- [Qiskit Aer](https://github.com/Qiskit/qiskit-aer) for the simulator.
