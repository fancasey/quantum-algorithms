import pennylane as qml
import numpy as np

# NOTE: NOT DONE AT ALL!

def _equal_superposition(wires):
    for wire in wires:
        qml.Hadamard(wires=wire)

def _oracle(wires, omega):
    qml.FlipSign(omega, wires=wires)

def _grovers(omega, nq):
    m = len(omega)
    n = 2 ** nq;
    wires = list(range(nq))
    iterations = int(np.round(np.sqrt(n / m)) * np.pi / 4)

    # Initial superposition
    _equal_superposition(wires)

    # Grover's iteration
    for _ in range(iterations):
        for omg in omega:
            _oracle(wires, omg)
        qml.templates.GroverOperator(wires)

    return qml.probs(wires=wires)

# TODO: Translate classical search space to quantum one (O(n), hopefully); need to figure out how to structure this

def search(search_space, item):
    # TODO: this doesn't make sense right now
    # TODO: this should search and find the answer(s) in O(sqrt(n)) time
    pass