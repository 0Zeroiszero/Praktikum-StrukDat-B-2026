from node import BinaryTree


def main():
    print('SISTEM AUDIT DISTRIBUSI "CEPAT SAMPAI"')
    print("=" * 55)
    pohon = BinaryTree()
    pohon.insert_manual()

    print("HASIL AUDIT:")
    print("1. Pre-Order   : " + " - ".join(pohon.traverse_preorder()))
    print("2. In-Order    : " + " - ".join(pohon.traverse_inorder()))
    print("3. Post-Order  : " + " - ".join(pohon.traverse_postorder()))

    print("\n[DATA] Gudang Ujung (Leaf Nodes): " + ", ".join(pohon.get_leaf_nodes()))
    print("=" * 55)
    print("Audit Selesai!")


if __name__ == "__main__":
    main()
