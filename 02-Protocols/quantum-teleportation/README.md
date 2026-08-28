# Quantum Teleportation Protocol Implementation

A Qiskit implementation of the **Quantum Teleportation Protocol** featuring dynamic conditional corrections and state verification via uncomputation ($U^\dagger$).

---

## Overview

Quantum teleportation enables the transfer of an arbitrary quantum state $|\psi\rangle$ from a sender (Alice) to a receiver (Bob) using a shared entangled Bell pair and two bits of classical communication. 

This repository demonstrates the state-agnostic nature of the protocol by preparing an arbitrary single-qubit state using parameterizable rotation gates ($R_y, R_z$), executing the teleportation circuit, and proving 100% state transfer fidelity via uncomputation.

---

## Circuit Architecture

| Phase | Target Qubits | Description |
| :--- | :--- | :--- |
| **1. Register Setup** | $q_0, q_1, q_2$ | Allocate 3 qubits ($q_0$: payload, $q_1$: Alice, $q_2$: Bob) and 3 classical bits ($c_0, c_1, c_2$). |
| **2. State Preparation ($U$)** | $q_0$ | Initialize payload state $|\psi\rangle = R_z(\phi) R_y(\theta)|0\rangle$. |
| **3. Entanglement Channel** | $q_1, q_2$ | Create Bell state $|\Phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ using $H$ and $CNOT$. |
| **4. Alice's Measurement** | $q_0, q_1$ | Rotate into the Bell basis ($CNOT$ + $H$) and measure into $c_0, c_1$. |
| **5. Dynamic Corrections** | $q_2$ | Apply conditional $X$ and $Z$ gates on Bob's qubit based on $(c_1, c_0)$. |
| **6. Uncomputation ($U^\dagger$)** | $q_2$ | Apply $U^\dagger = R_y(-\theta) R_z(-\phi)$ to collapse $q_2$ back to $|0\rangle$ for verification. |
| **7. Measurement** | $q_2 \to c_2$ | Measure Bob's verification bit. |

---

## Verification & Output Analysis

Qiskit orders classical bitstrings in reverse index format: **`c2 c1 c0`**.

* **Alice's Measurement (`c1 c0`):** Fluctuate uniformly across `00`, `01`, `10`, and `11` ($\approx 25\%$ probability each) due to wave-function collapse in the Bell basis.
* **Bob's Verification (`c2`):** Always evaluates to **`0` for 100% of simulator shots**.

### Mathematical Proof of Success

After conditional corrections, Bob holds $q_2 = |\psi\rangle = U|0\rangle$. Applying $U^\dagger$ yields:

$$U^\dagger |\psi\rangle = U^\dagger (U |0\rangle) = (U^\dagger U) |0\rangle = I |0\rangle = |0\rangle$$

Measuring $|0\rangle$ deterministically yields `0`, proving exact state reconstruction without full state tomography.

---

## Key Takeaways

* **State-Agnostic Engine:** Replacing $R_y/R_z$ with any unitary $U \in SU(2)$ leaves the core teleportation steps (3–5) completely unchanged.
* **No-Cloning Preserved:** Measuring $q_0$ destroys Alice's local state, transferring the quantum information rather than copying it.
* **Classical Speed Limit:** Bob cannot recover $|\psi\rangle$ until Alice transmits her measurement outcomes over a classical channel.

---

## Quickstart

### Prerequisites

* Python 3.9+
* Qiskit 1.0+
* Qiskit Aer

### Installation

```bash
git clone [https://github.com/YOUR_USERNAME/quantum-teleportation-qiskit.git](https://github.com/YOUR_USERNAME/quantum-teleportation-qiskit.git)
cd quantum-teleportation-qiskit
pip install qiskit qiskit-aer matplotlib
