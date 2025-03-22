from typing import Optional

class Node:
    def __init__(self, cancion: str) -> None:
        self.cancion = cancion
        self.next: Optional["Node"] = None

class Reproductor:
    def __init__(self) -> None:
        self.head = Optional["Node"] = None
        self.tail = Optional["Node"] = None
        self.current = Optional["Node"] = None 

    def agregar(self, cancion: str) -> None:
        nodo: Node = Node(cancion)
        if self.head is None:
            self.head = nodo
            self.tail = nodo
            self.current = nodo
        else: 
            