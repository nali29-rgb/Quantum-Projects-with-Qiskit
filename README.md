# Quantum Projects with Qiskit

A growing portfolio of hands-on quantum computing projects built with **Qiskit**, exploring quantum information, quantum protocols, algorithms, and execution on real IBM Quantum hardware.

My goal with this repository is to develop a practical understanding of quantum computing by connecting **theory → circuit construction → simulation → real-hardware execution → experimental analysis**.

---

## 🧭 Projects

### 01 — Fundamentals

#### [Bell State Generator](./01-Fundamentals/Bell-State-Generator/)

A modular implementation for generating all four Bell states:

- $|\Phi^+\rangle$
- $|\Phi^-\rangle$
- $|\Psi^+\rangle$
- $|\Psi^-\rangle$

The project compares ideal statevector probability distributions with measurement results obtained from an IBM Quantum processor, including hardware-aware transpilation.

**Concepts:** quantum states · superposition · entanglement · measurement · quantum circuits · transpilation

---

### 02 — Quantum Protocols

#### Quantum Teleportation

Implementation of the quantum teleportation protocol, exploring how an unknown quantum state can be transmitted using shared entanglement and classical communication.

**Concepts:** entanglement · measurement · classical communication · state transfer

#### Superdense Coding

Implementation of superdense coding, demonstrating how shared entanglement can be used to transmit two classical bits of information through the transmission of a single qubit.

**Concepts:** entanglement · quantum communication · Pauli gates · measurement

#### CHSH Game

Implementation of the CHSH game to explore quantum correlations and the violation of the classical CHSH bound.

**Concepts:** Bell inequalities · quantum correlations · entanglement · measurement

---

### 03 — Quantum Algorithms

*In progress*

This section will contain implementations and experiments involving foundational quantum algorithms, beginning with:

- Deutsch–Jozsa Algorithm
- Grover's Search Algorithm
- Additional algorithms as my studies progress

The emphasis will be on understanding the underlying mathematics and quantum advantage, rather than simply reproducing circuit implementations.

---

## 🔬 Project Philosophy

For each project, I aim to go beyond simply constructing a circuit.

Where appropriate, projects explore:

1. **The underlying quantum information concepts**
2. **Mathematical intuition**
3. **Circuit construction**
4. **Qiskit implementation**
5. **Ideal simulation**
6. **Noise and hardware effects**
7. **Execution on real quantum processors**
8. **Analysis of experimental results**

As the repository develops, I plan to investigate how ideal theoretical predictions compare with the behavior of real quantum hardware.

---

## 🛠️ Technologies

- **Python**
- **Qiskit**
- **Qiskit IBM Runtime**
- **IBM Quantum**
- **Matplotlib**
- **Jupyter / IPython**

---

## 📚 Learning

These projects are part of my ongoing study of quantum computing and quantum information, including material from:

- IBM Quantum learning resources
- Qiskit Global Summer School 2026
- Formal coursework in Quantum Information Science
- Independent study and research in quantum computing

---

## 🚀 Roadmap

### Completed

- [x] Bell State Generator
- [x] Quantum Teleportation
- [x] Superdense Coding
- [x] CHSH Game

### In Progress

- [ ] Deutsch–Jozsa Algorithm
- [ ] Grover's Search Algorithm
- [ ] Additional quantum algorithms
- [ ] More experiments involving noisy simulation and real quantum hardware

### Longer Term

- [ ] Deeper investigation of quantum noise and hardware performance
- [ ] More advanced quantum algorithms
- [ ] Research-driven quantum computing projects
- [ ] Contributions to the broader Qiskit ecosystem

---

## 🎯 About This Repository

This repository is a record of my progression from learning the fundamentals of quantum information to developing the ability to independently implement, test, and investigate quantum algorithms and experiments.

I am particularly interested in the intersection of **quantum computing, software engineering, and experimental quantum information**.

More projects will be added as I continue learning and conducting research in quantum computing.
