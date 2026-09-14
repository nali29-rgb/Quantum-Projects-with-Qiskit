# Deutsch-Jozsa Algorithm Implementation

An interview-defensible, modular implementation of the Deutsch-Jozsa quantum algorithm constructed in Qiskit 1.0+. This repository serves as a foundational benchmark circuit demonstrating quantum speedup, phase kickback, and constructive/destructive interference.

## Overview

The Deutsch-Jozsa algorithm determines whether a black-box boolean function $f: \{0,1\}^n \rightarrow \{0,1\}$ is **constant** (returns $0$ for all inputs or $1$ for all inputs) or **balanced** (returns $0$ for half the inputs and $1$ for the other half).

* **Classical Query Complexity:** $2^{n-1} + 1$ evaluations (worst-case deterministic)
* **Quantum Query Complexity:** Exactly **1 query** to the oracle $U_f$

## Circuit Architecture

The implementation executes across five distinct physical stages:

1. **Target Qubit Prep:** Flip target qubit to $\vert{}1\rangle$ using an $X$ gate.
2. **Superposition:** Apply $H^{\otimes (n+1)}$ to create an equal superposition across input qubits and set the target qubit to $\vert{}-\rangle$.
3. **Oracle Evaluation:** Apply custom oracle gate $U_f$, leveraging phase kickback to encode function values directly into input register phases:
   $$U_f \vert{}x\rangle \vert{}-\rangle = (-1)^{f(x)} \vert{}x\rangle \vert{}-\rangle$$
4. **Interference Generation:** Apply final Hadamards $H^{\otimes n}$ to the input register to force constructive or destructive interference.
5. **Measurement:** Measure the $n$ input register qubits.

## Results & Analysis

Simulated on `AerSimulator` with $n = 3$ input qubits over 1024 shots:

| Function Type | Oracle Logic | Measured Output | Probability | Physical Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **Constant** | $f(x) = 1$ | `000` | **100%** | Uniform phase $(-1)^1$ creates complete constructive interference at $\vert 000 \rangle$. |
| **Balanced** | $f(x) = x_0 \oplus x_1 \oplus x_2$ | `111` | **100%** | Alternating phase signs $(-1)^{f(x)}$ cause destructive interference at $\vert 000 \rangle$, shifting amplitude to non-zero basis states. |

## Repository Structure

```text
.
├── Deutsch-Jozsa Algorithm.ipynb   # Complete walkthrough notebook with step-by-step circuit code
└── readme.md                    # Project overview and technical documentation
