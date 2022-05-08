# while1.py

money = 100000
transfer = 1000000

print('Check : ', money < transfer)

while money < transfer:
	print('ກະລຸນາຕື່ມໂຕເລກໂອນໃໝ່ເຈົ້າ')
	transfer = int(input('new transfer : '))
	if transfer > 10000000:
		print('ເອີ່ນຜູ້ຈັດການມາ ຂໍເຄລຍຣ໌ກ່ອນຈຶ່ງຈະໂອນໄດ້')
		break

print('ໂອນໄດ້ຖ້າຜູ້ຈັດການອະນຸຍາດສຳຫຼັບກໍລະນີເປັນ VIP')
