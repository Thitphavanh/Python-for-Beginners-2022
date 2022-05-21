# class PublicEmp:
# 	def __init__(self, salary):
# 		self.salary = salary


# class ProtectedEmp:
# 	def __init__(self, salary):
# 		self._salary = salary


# class Emp(ProtectedEmp):
# 	def getsalary(self):
# 		return self._salary


# class PrivateEmp:
# 	def __init__(self, salary):
# 		self._salary = salary

# 	def getsalary(self):
# 		return self._salary


# myEmp1 = PublicEmp(1800000)
# print('PublicEmp salary = {0:,.2f} LAK'.format(myEmp1.salary))


# myEmp2 = PublicEmp(2800000)
# print('ProtectedEmp salary = {0:,.2f} LAK'.format(myEmp2.salary))

# myEmp3 = PublicEmp(2500000)
# print('PrivateEmp salary = {0:,.2f} LAK'.format(myEmp3.salary))


class Employee:
	minSalary = 2800000
	maxSalary = 4000000
	_companyName = "Anitocorn"

	def __init__(self, name, salary, department):
		self.name = name
		self.salary = salary
		self.department = department

	def _showData(self):
		print("ຊື່ພະນັກງານ = {}".format(self.name))
		print("ເງິນເດືອນ = {0:,.2f}".format(self.salary))
		print("ຕຳແໜ່ງ = {}".format(self.department))

	def _getIncome(self):
		return self.salary * 12

	def __str__(self):
		return ("ຊື່ພະນັກງານ = {} , ເງິນເດືອນ = {} , ຕຳແໜ່ງ = {}".format(self.name, self.salary, self.department))


class Accounting(Employee):
	__departmentName = "ພະແນກບັນຊີ"

	def __init__(self, name, salary):
		super().__init__(name, salary, self.__departmentName)


class Programmer(Employee):
	__departmentName = "ໂປຣແກຣມເມີຣ໌"

	def __init__(self, name, salary, experience):
		super().__init__(name, salary, self.__departmentName)
		self.exp = experience

	def __str__(self):
		return (super().__str__()+" , ປະສົບການເຮັດວຽກ = {} ປີ".format(self.exp))


programmer = Programmer("James", 4000000, 2)
print(programmer.__str__())
print("ລາຍໄດ້ຕໍ່ປີ = {}".format(programmer._getIncome()))
