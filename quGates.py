from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt

def create_and_measure_circuit(gate_name, gate_function):
    # Create circuit with 1 qubit and 1 classical bit
    qc = QuantumCircuit(1, 1)
    
    # Apply the specified gate
    gate_function(qc)
    
    # Measure
    qc.measure(0, 0)
    
    # Simulate and get results
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    # Plot results
    plt.figure(figsize=(5, 4))
    plot_histogram(counts)
    plt.title(f'{gate_name} Gate Results')
    plt.show()
    
    # Show state before measurement (using statevector simulator)
    qc_state = QuantumCircuit(1)
    gate_function(qc_state)
    state = Statevector.from_instruction(qc_state)
    plot_bloch_multivector(state)
    plt.title(f'{gate_name} Gate Bloch Sphere')
    plt.show()

# Define gate applications
def apply_x(qc):
    qc.x(0)  # Pauli-X (NOT gate)

def apply_h(qc):
    qc.h(0)  # Hadamard

def apply_z(qc):
    qc.z(0)  # Pauli-Z

def apply_y(qc):
    qc.y(0)  # Pauli-Y

# Demonstrate CNOT (requires 2 qubits)
def demonstrate_cnot():
    qc = QuantumCircuit(2, 2)
    
    # Put first qubit in superposition
    qc.h(0)
    
    # Apply CNOT (control=qubit 0, target=qubit 1)
    qc.cx(0, 1)

    # First, let's show the statevector
    qc_state = QuantumCircuit(2)
    qc_state.h(0)
    qc_state.cx(0, 1)
    state = Statevector.from_instruction(qc_state)
    
    # Plot the state vector (this will show individual qubit states)
    plot_bloch_multivector(state)
    plt.title('CNOT Gate Bloch Sphere (Individual Qubit States)')
    plt.show()
    
    # Measure both qubits
    qc.measure([0, 1], [0, 1])
    
    # Simulate and get results
    simulator = Aer.get_backend('qasm_simulator')
    job = simulator.run(qc, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    
    plt.figure(figsize=(5, 4))
    plot_histogram(counts)
    plt.title('CNOT Gate Results')
    plt.show()

# Test each single-qubit gate
gates = [
    ("Pauli-X", apply_x),
    ("Hadamard", apply_h),
    ("Pauli-Z", apply_z),
    ("Pauli-Y", apply_y)
]

for gate_name, gate_function in gates:
    print(f"\nDemonstrating {gate_name} Gate:")
    create_and_measure_circuit(gate_name, gate_function)

# Demonstrate CNOT
print("\nDemonstrating CNOT Gate:")
demonstrate_cnot()