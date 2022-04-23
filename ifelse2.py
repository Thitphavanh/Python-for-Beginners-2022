# ifelse2.py
friends = ['James', 'Noy', 'Tui', 'Ley', 'Jo']

friends2 = {'James': 'ເຈມສ໌', 'Noy': 'ນ້ອຍ', 'Tui': 'ຕຸ້ຍ', 'Ley': 'ເລ້'}

visitor = 'jo'

if visitor in friends or visitor.title() in friends:
    print('ເປັນໝູ່ຂ້ອຍເອງ ເຊີນຂຶ້ນມາໄດ້ເລີຍ')
    if visitor in friends2 or visitor.title() in friends2:
        print('ສະບາຍດີ ' + friends2[visitor.title()])
    else:
        print('ສະບາຍດີ ລູກຄ້າ')
else:
    print('Hey! ເຈົ້າແມ່ນໃຜ ບໍ່ມີຊື່ໃນ Member')
