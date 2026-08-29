# Quantum Superdense Coding Protocol

An implementation of the **Superdense Coding** quantum communication protocol built with **Qiskit** and executed using the **Qiskit Aer Simulator**. 

This repository demonstrates how pre-shared quantum entanglement allows Alice to transmit **2 classical bits** of information to Bob by physically transferring only **1 qubit**.

---

## 📌 Overview

Superdense coding is a fundamental algorithm in quantum information theory that highlights the operational value of entanglement as a communication resource. According to Holevo's bound, an isolated single qubit can carry at most 1 bit of classical information upon measurement. By utilizing a shared entangled Bell state ($\vert\Phi^+\rangle$), Superdense Coding doubles this classical channel capacity.

### Protocol Comparison
* **Superdense Coding:** 1 Shared EPR Pair + 1 Physical Qubit $\rightarrow$ Transmits **2 Classical Bits**
* **Quantum Teleportation:** 1 Shared EPR Pair + 2 Classical Bits $\rightarrow$ Transmits **1 Quantum State**

---

## 🧠 How It Works

The protocol runs in 4 main phases:

1. **Entanglement Channel Setup:** Alice and Bob share an entangled Bell state $\vert\Phi^+\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle)$.
2. **Alice's Local Encoding:** Alice applies single-qubit Pauli operations ($I, X, Z, XZ$) exclusively to her qubit ($q_0$) based on her desired 2-bit classical message. This steers the shared system into one of four orthogonal Bell states.
3. **Bob's Decoding:** Bob receives $q_0$ and performs a Bell-basis transformation ($CNOT \rightarrow H$) to map the joint state back to the computational basis.
4. **Measurement:** Bob measures both qubits to recover Alice's exact 2-bit message deterministically.

### State Mapping Table

| Input Message | Alice's Gate | Encoded Bell State | Bob's Decoded Measurement |
| :--- | :--- | :--- | :--- |
| `'00'` | Identity ($I$) | $\vert\Phi^+\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle + \vert 11\rangle)$ | `00` |
| `'01'` | Pauli-$X$ | $\vert\Psi^+\rangle = \frac{1}{\sqrt{2}}(\vert 01\rangle + \vert 10\rangle)$ | `01` |
| `'10'` | Pauli-$Z$ | $\vert\Phi^-\rangle = \frac{1}{\sqrt{2}}(\vert 00\rangle - \vert 11\rangle)$ | `10` |
| `'11'` | Pauli-$Z \cdot X$ | $\vert\Psi^-\rangle = \frac{1}{\sqrt{2}}(\vert 01\rangle - \vert 10\rangle)$ | `11` |

---

## 🛠️ Prerequisites & Installation

### Requirements
* Python 3.9+
* Qiskit 1.0+
* Qiskit Aer

### Setup Environment

```bash
# Clone the repository
git clone [https://github.com/your-username/quantum-superdense-coding.git](https://github.com/your-username/quantum-superdense-coding.git)
cd quantum-superdense-coding

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install qiskit qiskit-aer ipykernel
```

---

## 💻 Code Structure & Usage

The notebook is organized into modular functions for circuit generation and automated simulation testing.

```python
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def create_superdense_circuit(message: str) -> QuantumCircuit:
    qc = QuantumCircuit(2, 2)
    
    # Phase 1: Create Bell Pair |Phi+>
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()
    
    # Phase 2: Alice's Encoding
    if message == "01":
        qc.x(0)
    elif message == "10":
        qc.z(0)
    elif message == "11":
        qc.z(0)
        qc.x(0)
    qc.barrier()
    
    # Phase 3: Bob's Decoding
    qc.cx(0, 1)
    qc.h(0)
    
    # Phase 4: Measurement
    qc.measure(0, 0)
    qc.measure(1, 1)
    
    return qc
```

To run the automated test suite across all four message variants:

```python
# Run verification script inside Jupyter Notebook or Python script
test_all_superdense_messages()
```

---

## 📊 Results

Executing the test harness on `AerSimulator` (1024 shots) confirms 100% deterministic classical bit recovery for all four message configurations:

```text
--- Running Superdense Coding Verification ---
Sent: 00  |  Measured Counts: {'00': 1024}
Sent: 01  |  Measured Counts: {'01': 1024}
Sent: 10  |  Measured Counts: {'10': 1024}
Sent: 11  |  Measured Counts: {'11': 1024}
```

---

## 📁 Repository Structure

```text
.
├── superdense_coding.ipynb    # Main Jupyter Notebook containing step-by-step code & markdown
└── README.md                  # Project overview and documentation
```

---
