# Bell State Generator & NISQ Hardware Benchmark

This project demonstrates the creation of maximally entangled two-qubit Bell states using Qiskit. It compares ideal classical simulation against real hardware execution on an IBM Quantum superconducting processor.

## 🚀 Key Features

* **Modular Circuit Generator:** Implements a Python function to dynamically build quantum circuits for any of the four Bell states ($|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle$).
* **Ideal Statevector Analysis:** Calculates exact mathematical statevectors and theoretical probability distributions.
* **Hardware-Aware Transpilation:** Optimizes abstract quantum circuits into backend-native gates using Qiskit's `preset_pass_manager` (Optimization Level 3).
* **QPU Hardware Execution:** Runs jobs on physical quantum hardware (`ibm_fez`) via `qiskit-ibm-runtime` (`SamplerV2`) to analyze real-world noise and fidelity loss.

---

## 📊 Summary of Results

Executing the $|\Psi^+\rangle$ state for 1,024 shots yielded the following performance:

| Execution Mode | Target States ($|01\rangle + |10\rangle$) | Noise Artifacts ($|00\rangle + |11\rangle$) | Target Accuracy |
| :--- | :--- | :--- | :--- |
| **Ideal Simulator** | 100% (1,024 shots) | 0.0% (0 shots) | **100.0%** |
| **IBM QPU (`ibm_fez`)** | 97.0% (993 shots) | 3.0% (31 shots) | **96.97%** |

### Key Takeaway
The QPU physical run achieved **~97% target state accuracy**, closely matching the theoretical 50/50 superposition. The ~3% error rate reflects real-world hardware noise, including control gate inaccuracies, environmental interaction, and readout errors.

---

## 📄 Notebook Link

For full code, mathematical step-by-step explanations, circuit drawings, and histogram visualizations, see the primary notebook:
* **[View `bell_state_generator.ipynb`](./bell_state_generator.ipynb)**
