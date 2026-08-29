# CHSH Game: Proving Quantum Non-Locality

This repository contains a Qiskit implementation of the **Clauser-Horne-Shimony-Holt (CHSH) game**, a fundamental quantum protocol used to test local hidden-variable theories and empirically demonstrate quantum non-locality by violating Bell's inequality.

---

**Overview & Objective**

The CHSH game is a non-local game played by two players, Alice and Bob, who share an entangled qubit pair but cannot communicate once the game begins. A referee randomly assigns each player an input bit ($x$ for Alice, $y$ for Bob). They must return measurement output bits ($a$ for Alice, $b$ for Bob) to satisfy the win condition:

$$a \oplus b = x \cdot y$$

* **Classical Limit:** Local Realism bounds any classical deterministic or probabilistic strategy to a maximum win rate of **75%**.
* **Quantum Limit:** Using a shared maximally entangled Bell state $\vert{}\Phi^+\rangle$ and non-orthogonal measurement basis rotations, players reach **Tsirelson's Bound** of $\cos^2(\pi/8) \approx \mathbf{85.35\%}$.

---

**Protocol Mechanics**

| Input ($x, y$) | Target Condition | Alice Rotation ($q_0$) | Bob Rotation ($q_1$) | Basis |
| :--- | :--- | :--- | :--- | :--- |
| **$(0, 0)$** | $a = b$ | $R_y(0)$ | $R_y(\pi/4)$ | $Z$ vs $W$ |
| **$(0, 1)$** | $a = b$ | $R_y(0)$ | $R_y(-\pi/4)$ | $Z$ vs $V$ |
| **$(1, 0)$** | $a = b$ | $R_y(\pi/2)$ | $R_y(\pi/4)$ | $X$ vs $W$ |
| **$(1, 1)$** | $a \neq b$ | $R_y(\pi/2)$ | $R_y(-\pi/4)$ | $X$ vs $V$ |

---

**Repository Structure**

```text
chsh-game/
├── README.md           # Project documentation
└── chsh_game.ipynb     # Interactive Jupyter notebook

## Quickstart

### Prerequisites
* **Python:** Version 3.10 or higher
* **Git:** Installed on your machine

### Installation & Setup
```bash
git clone [https://github.com/nali29-rgb/Quantum-Projects-with-Qiskit.git](https://github.com/nali29-rgb/Quantum-Projects-with-Qiskit.git)
cd Quantum-Projects-with-Qiskit
pip install -r requirements.txt
```
