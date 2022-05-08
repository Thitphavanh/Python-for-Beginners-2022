# forloop1.py

# loop ຕາມຈຳນວນ
for i in range(10):
    print('Hello :', i)

print('--------Loop in list--------')
friends = ['James', 'Noy', 'Tui', 'Ley', 'Jo']

for f in friends:
    print(f)
    if f == 'James':
        print('ສະບາຍດີ ເຈມສ໌')
    else:
        print('ສະບາຍດີ ລູກຄ້າ')
print('--------Loop in Dictionary--------')
friends2 = {'James': 'ເຈມສ໌', 'Noy': 'ນ້ອຍ', 'Tui': 'ຕຸ້ຍ', 'Ley': 'ເລ້'}

# Show key
for f in friends2:
    print(f)

# Show items
for k, v in friends2.items():
    print('keys :', k)
    print('values :', v)

# Show key only
for f in friends2.keys():
    print(f)

# Show vulues only
for f in friends2.values():
    print(f)

# ຕ້ອງການລຳດັບ
for i, f in enumerate(friends, start=1000):
    print(i, f)

# ຕ້ອງການລຳດັບສຳຫຼັບ Dictionary
for i, f in enumerate(friends2.items()):
    print(i, f)

# ຕ້ອງການລຳດັບສຳຫຼັບ Dictionary ແຍກ keys
for i, (k, v) in enumerate(friends2.items()):
    print(i, k, v)
