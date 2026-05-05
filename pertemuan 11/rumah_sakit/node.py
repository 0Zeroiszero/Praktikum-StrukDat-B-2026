class Node:
    """Node untuk data pasien dan keluhan, serta pasien berikutnya"""

    def __init__(self, nama, keluhan):
        self.nama = nama
        self.keluhan = keluhan
        self.next = None