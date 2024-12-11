# Quantum Gates Visualization

## Overview

This project provides a comprehensive visualization of fundamental quantum gates using Qiskit, a popular open-source framework for quantum computing. The script demonstrates the behavior of single-qubit gates (Pauli-X, Hadamard, Pauli-Z, and Pauli-Y) and the two-qubit CNOT gate through interactive visualizations.

## Features

- Visualize the effects of single-qubit gates on the Bloch sphere
- Generate measurement histograms for quantum gates
- Demonstrate the CNOT (Controlled-NOT) gate behavior
- Use Qiskit's quantum circuit simulation capabilities

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.7+
- Qiskit
- Qiskit Aer
- Matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tyler-Beck/QuantumGates.git
   ```

2. Install required dependencies:
   ```bash
   pip install qiskit qiskit-aer matplotlib
   ```

## Usage

Run the script to visualize quantum gates:

```bash
python quGates.py
```

The script will generate:
- Measurement histograms for each gate
- Bloch sphere representations
- CNOT gate visualization

## Quantum Gates Demonstrated

1. **Pauli-X Gate (NOT Gate)**
   - Rotates the qubit state by 180 degrees around the X-axis
   - Equivalent to a classical NOT operation

2. **Hadamard Gate**
   - Creates superposition by rotating the qubit state to the XY plane
   - Transforms basis states to equal superpositions

3. **Pauli-Z Gate**
   - Rotates the qubit state by 180 degrees around the Z-axis
   - Applies a phase shift to the quantum state

4. **Pauli-Y Gate**
   - Rotates the qubit state by 180 degrees around the Y-axis
   - Involves both amplitude and phase changes

5. **CNOT (Controlled-NOT) Gate**
   - Two-qubit gate demonstrating quantum entanglement
   - Flips the target qubit based on the control qubit's state

## Visualization Details

- **Measurement Histograms**: Show the probability distribution of qubit states
- **Bloch Sphere Representations**: Illustrate the geometric transformation of qubit states

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Acknowledgments

- [Qiskit](https://qiskit.org/) - Quantum computing framework
- [Matplotlib](https://matplotlib.org/) - Visualization library
