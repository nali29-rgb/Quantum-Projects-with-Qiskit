from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

def create_bell_state(state_type: str = "phi_plus") -> QuantumCircuit:
    """
    Generates a QuantumCircuit for the specified Bell State.
    Supported types: 'phi_plus', 'phi_minus', 'psi_plus', 'psi_minus'
    """
    qc = QuantumCircuit(2)
    
    if state_type == "phi_plus":
        qc.h(0)
        qc.cx(0, 1)
    elif state_type == "phi_minus":
        qc.x(0)
        qc.h(0)
        qc.cx(0, 1)
    elif state_type == "psi_plus":
        qc.h(0)
        qc.x(1)
        qc.cx(0, 1)
    elif state_type == "psi_minus":
        qc.x(0)
        qc.h(0)
        qc.x(1)
        qc.cx(0, 1)
    else:
        raise ValueError(f"Unknown Bell state type: {state_type}")
        
    return qc
