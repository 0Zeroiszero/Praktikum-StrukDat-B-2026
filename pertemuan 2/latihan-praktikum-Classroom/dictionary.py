# Konstruktor
empty_dict = dict()
dict_from_kwargs = dict(a=1, b=2)
dict_from_mapping = dict({"x": 10, "y": 20})
dict_from_iterable = dict([("p", 1), ("q", 2)])

# clear() - Menghapus semua item
temp_dict = {"a": 1, "b": 2}
temp_dict.clear()

# copy() - Membuat shallow copy
original_dict = {"a": 1, "b": 2}
copied_dict = original_dict.copy()

# get() - Mengambil value dengan default opsional
get_dict = {"name": "John", "age": 25}
name = get_dict.get("name")
missing = get_dict.get("city", "Unknown")

# items() - Return view object pasangan (key, value)
items_view = {"a": 1, "b": 2}.items()

# keys() - Return view object keys
keys_view = {"a": 1, "b": 2}.keys()

# values() - Return view object values
values_view = {"a": 1, "b": 2}.values()

# pop() - Hapus dan return value dengan default opsional
pop_dict = {"x": 1, "y": 2, "z": 3}
popped_value = pop_dict.pop("y")
missing_pop = pop_dict.pop("w", "default")

# popitem() - Hapus dan return item terakhir
popitem_dict = {"a": 1, "b": 2}
last_item = popitem_dict.popitem()

# setdefault() - Return value, set default jika key tidak ada
setdefault_dict = {"a": 1}
existing = setdefault_dict.setdefault("a", 100)
new = setdefault_dict.setdefault("b", 200)

# update() - Update dict dengan pasangan key-value
update_dict = {"a": 1, "b": 2}
update_dict.update({"c": 3, "d": 4})

# Menampilkan hasil
print("Hasil implementasi method dictionary:")
print(f"Dict dari kwargs: {dict_from_kwargs}")
print(f"Dict dari mapping: {dict_from_mapping}")
print(f"Dict dari iterable: {dict_from_iterable}")
print(f"Get 'name': {name}, Get 'city' dengan default: {missing}")
print(f"Items: {list(items_view)}")
print(f"Keys: {list(keys_view)}")
print(f"Values: {list(values_view)}")
print(f"Pop 'y': {popped_value}, Pop 'w' dengan default: {missing_pop}")
print(f"Popitem: {last_item}")
print(f"Setdefault (key ada): {existing}, (key baru): {new}")
print(f"Dict setelah update: {update_dict}")
