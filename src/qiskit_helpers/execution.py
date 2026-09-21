"""
execution.py: Helper functions for executing Qiskit circuits on hardware 
and calculating error mitigation metrics.
"""

import numpy as np
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.quantum_info import hellinger_fidelity

def run_with_resilience(qc, backend, resilience_level: int = 1, shots: int = 4096) -> dict:
    """
    Executes a QuantumCircuit on an IBM QPU backend with a specified resilience level (explanation listed).
    Resilience Level 0 = Raw Unmitigated
    Resilience Level 1 = Readout Error Mitigation (M3/TREX)
    """
    sampler = Sampler(mode=backend)
    sampler.options.resilience_level = resilience_level
    
    job = sampler.run([qc], shots=shots)
    pub_result = job.result()[0]
    
    # Extract counts dictionary from bitstring data
    counts = pub_result.data.meas.get_counts()
    return counts

def calculate_bell_fidelity(counts: dict, ideal_counts: dict) -> float:
    """
    Calculates Hellinger Fidelity between experimental counts and theoretical ideal counts.
    """
    return hellinger_fidelity(counts, ideal_counts)
