class Node:
    nama: str
    keluhan: str
    next: Node | None

    def __init__(self, nama: str, keluhan: str) -> None: ...
