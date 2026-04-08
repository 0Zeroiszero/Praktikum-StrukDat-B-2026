history_array = ["google.com", "python.org"]

def tambah_pencarian_array(keyword):
    history_array.append(keyword)
    return history_array

perubahan_history = tambah_pencarian_array("huggingface.com")
print(perubahan_history)