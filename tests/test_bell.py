import pytest
from qiskit.quantum_info import Statevector
import numpy as np

from src.qiskit_helpers.bell import create_bell_state

def test_phi_plus_statevector():
    qc = create_bell_state("phi_plus")
    sv = Statevector.from_instruction(qc)
    
    # Expected: 1/sqrt(2) * (|00> + |11>)
    expected_sv = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
    assert np.allclose(sv.data, expected_sv)

def test_invalid_state_type():
    with pytest.raises(ValueError):
        create_bell_state("invalid_type")
