# ifelse.py
money = 80000

if money >= 100000:
    print('ໄປກິນຊີ້ນດາດເກົາຫຼີ')
elif money >= 30000:
    print('ໄປກິນເຂົ້າລາດໜ້າ')
elif money >= 0 and money < 30000:
    print('ກັບໄປກິນເຂົ້າຢູ່ເຮືອນ')
else:
    print('ໃສ່ຂໍ້ມູນບໍ່ຖືກຕ້ອງ ກະລຸນາໃສ່ຈຳນວນຫຼາຍກວ່າ 0 ຂຶ້ນໄປ')

print('ກັບມາ Python ຕໍ່')

# elif money >= 60000:
#     pass