# Quantum Calculator using Qiskit

Welcome to the **Quantum Calculator**, a Python-based project utilizing **Qiskit** to perform basic arithmetic operations—addition, subtraction, and multiplication—using quantum circuits. This calculator showcases the power of quantum computing for arithmetic computations and serves as an educational tool for those interested in quantum programming.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Setting Up the Environment](#setting-up-the-environment)
- [Usage](#usage)
  - [Running the Calculator](#running-the-calculator)
  - [Using the GUI](#using-the-gui)
  - [Example Sessions](#example-sessions)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

This project demonstrates how quantum circuits can be used to perform arithmetic operations. By leveraging the capabilities of **Qiskit**, an open-source quantum computing framework, we implement quantum versions of addition, subtraction, and multiplication.

The calculator provides both a command-line interface and a graphical user interface (GUI) where users can select an operation and input numbers to perform calculations using quantum circuits simulated on a classical computer.

## Features

- **Quantum Addition**: Adds two numbers using a quantum ripple-carry adder circuit.
- **Quantum Subtraction**: Subtracts one number from another using the inverse of a quantum adder circuit.
- **Quantum Multiplication**: Multiplies two numbers using controlled addition and quantum gates.
- **Graphical User Interface (GUI)**: A simple and user-friendly GUI built with Tkinter.
- **Circuit Visualization**: Ability to display the quantum circuit used in the calculation.
- **Educational Tool**: Helps users understand how quantum circuits can perform arithmetic operations.
- **Modular Codebase**: Organized code with modular functions for each arithmetic operation.

## Getting Started

Follow these instructions to set up the project on your local machine.

### Prerequisites

- **Python 3.8 or higher**: Ensure you have Python installed. You can download it from the [official website](https://www.python.org/downloads/).
- **pip**: Python package installer, which usually comes with Python.
- **Virtual Environment (optional but recommended)**: To manage dependencies without affecting system-wide packages.
- **Tkinter**: The standard Python interface to the Tk GUI toolkit (usually included with Python).
- **Qiskit**: Quantum computing framework for Python.

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/quantum-calculator.git
   cd quantum-calculator
   ```

2. **Set Up a Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   source venv/bin/activate       # On Unix or MacOS
   venv\Scripts\activate          # On Windows
   ```

3. **Install Dependencies**

   Use the `requirements.txt` file to install all necessary packages:

   ```bash
   pip install -r requirements.txt
   ```

   **Contents of `requirements.txt`:**

   ```txt
   qiskit==0.45.0
   numpy>=1.21.0
   ```

   *Note: Adjust the versions if necessary based on your environment.*

### Setting Up the Environment

Ensure that Qiskit is correctly installed by running:

```bash
python -c "import qiskit; print(qiskit.__qiskit_version__)"
```

This should display the versions of Qiskit's components without errors.

## Usage

### Running the Calculator

You can use the calculator in two ways:

1. **Command-Line Interface (CLI)**
2. **Graphical User Interface (GUI)**

### Using the Command-Line Interface

To start the calculator using the command-line interface, run the `calculator.py` script:

```bash
python calculator.py
```

### Using the GUI

To launch the graphical user interface, run the `quantum_calculator_gui.py` script:

```bash
python quantum_calculator_gui.py
```

#### Steps:

1. **Enter the First Number**: Input the first integer in the provided field.
2. **Enter the Second Number**: Input the second integer.
3. **Select the Operation**: Choose from Add, Subtract, or Multiply.
4. **Calculate**: Click the **Calculate** button to perform the operation.
5. **View Result**: The result will be displayed on the screen.
6. **Show Circuit**: Click the **Show Circuit** button to view the quantum circuit used in the calculation.

#### GUI Features:

- **User-Friendly Interface**: Simple layout for easy interaction.
- **Error Handling**: Validates input and displays error messages for invalid data.
- **Circuit Visualization**: Displays the quantum circuit in a new window for educational purposes.

### Example Sessions

#### Using the GUI

1. **Addition Example**

   - Enter `4` as the first number.
   - Enter `6` as the second number.
   - Select **Add**.
   - Click **Calculate**.
   - Result displayed: `4 + 6 = 10`.
   - Click **Show Circuit** to view the quantum circuit.

2. **Subtraction Example**

   - Enter `10` as the first number.
   - Enter `3` as the second number.
   - Select **Subtract**.
   - Click **Calculate**.
   - Result displayed: `10 - 3 = 7`.
   - Click **Show Circuit** to view the quantum circuit.

3. **Multiplication Example**

   - Enter `5` as the first number.
   - Enter `4` as the second number.
   - Select **Multiply**.
   - Click **Calculate**.
   - Result displayed: `5 * 4 = 20`.
   - Click **Show Circuit** to view the quantum circuit.

#### Using the Command-Line Interface

```
Select operation.
1.Add
2.Subtract
3.Multiply
Enter choice(1/2/3): 1
Enter first number: 4
Enter second number: 6
4.0 + 6.0 = 10
Let's do next calculation? (yes/no): yes
```

## Project Structure

```
quantum-calculator/
├── calculator.py                # Command-line calculator script
├── quantum_calculator_gui.py    # GUI application script
├── adder.py                     # Contains the Adder function
├── subtractor.py                # Contains the Sub function
├── multiplier.py                # Contains the Multiply function
├── modifier.py                  # Contains the Modifier function
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

### Description of Files

- **calculator.py**: Main script that provides the command-line user interface.
- **quantum_calculator_gui.py**: GUI application script using Tkinter.
- **adder.py**: Implements the quantum addition operation.
- **subtractor.py**: Implements the quantum subtraction operation.
- **multiplier.py**: Implements the quantum multiplication operation.
- **modifier.py**: Utility functions for initializing quantum circuits.
- **requirements.txt**: Lists all Python packages required.
- **README.md**: Documentation for the project.

## Contributing

Contributions are welcome! If you'd like to enhance the calculator (e.g., add division or other operations), please follow these steps:

1. **Fork the Repository**

   Click the "Fork" button on the top right to create a copy of the repository on your GitHub account.

2. **Clone Your Fork**

   ```bash
   git clone https://github.com/your-username/quantum-calculator.git
   cd quantum-calculator
   ```

3. **Create a Feature Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**

   - Implement your feature or fix.
   - Ensure code follows the existing style.
   - Test your changes thoroughly.

5. **Commit and Push**

   ```bash
   git add .
   git commit -m "Add your commit message here"
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**

   Go to the original repository and click on "Pull Requests" to submit your changes for review.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Qiskit**: [Qiskit](https://qiskit.org/) is an open-source SDK for working with quantum computers at the level of pulses, circuits, and application modules.
- **IBM Quantum**: For providing access to quantum computing resources and educational materials.
- **Contributors**: Thanks to everyone who has contributed to this project.

---

*This project is intended for educational purposes to demonstrate quantum computing concepts. The quantum circuits are simulated on classical hardware using Qiskit's simulators.*

---

# Changes and Updates

## Added GUI Application

- Introduced `quantum_calculator_gui.py` script for the graphical user interface.
- The GUI allows users to input numbers, select operations, and perform calculations.
- Users can view the quantum circuit used in each calculation by clicking the **Show Circuit** button.

## Updated Features Section

- Added details about the GUI and circuit visualization features.

## Updated Usage Instructions

- Provided instructions on how to run and use the GUI application.
- Included steps for performing calculations and viewing circuits in the GUI.

## Updated Project Structure

- Included `quantum_calculator_gui.py` in the project structure.
- Provided descriptions for the GUI script.

## Notes on Running the GUI

- Ensure all dependencies are installed, including `tkinter` and `qiskit`.
- The GUI uses the same quantum functions (`Adder`, `Sub`, `Multiply`) as the command-line version.

## Final Remarks

Feel free to explore the code, experiment with the quantum circuits, and enhance the calculator with additional features. The GUI provides a more interactive way to engage with quantum computing concepts and visualize the underlying circuits.

If you encounter any issues or have suggestions, please open an issue on GitHub or contribute through a pull request.

Happy computing!
