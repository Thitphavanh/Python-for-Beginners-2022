class Student:

	def __init__(self, name, age, gender):
		self.name = name
		self.age = age
		self.gender = gender

	def study(self):
		print(f'{self.name} is learning...')

	def sabaiydee(self):
		if self.gender == 'men':
			tail = 'ໂດຍ'
			callme = 'ເຈົ້າ'
		else:
			tail = 'ຈາ'
			callme = 'ໂດຍ ຂະນ້ອຍ'
		print(f'ສະບາຍດີ {tail} {callme} name {self.name} ')


class SpeialStudent(Student):

	def __init__(self, name, age, gender, parent):
		super().__init__(name, age, gender)
		self.parent = parent

	def hello(self, person='friend'):
		if person == 'friend':
			print("Hey!!!, What's up")
		else:
			print('Shut up')

	def sabaiydee(self):
		print('Hello!, name {self.name}')

	def myfather(self):
		print('You know ?, who is myfather')
		print(f'My father is {self.parent}')


class Teacher:

	def __init__(self, name, gender, subject):
		self.name = name
		self.gender = gender
		self.subject = subject

	def teach(self):
		print('Teacher {} is teaching {} course'.format(self.name, self.subject))


if __name__ == '__main__':
	student1 = Student('Robert', 15, 'men')
	student2 = Student('Zara', 15, 'women')
	speial_student = SpeialStudent('Frank', 16, 'men', 'Big boss')

	teach1 = Teacher('David', 'men', 'Englist')
	print(teach1.name)
	print(teach1.subject)

	print('-------8:00------')
	student1.sabaiydee()
	student2.sabaiydee()
	teach1.teach()
	student1.study()
	student2.study()
	print('-------8:30------')
	speial_student.sabaiydee()
	print('go to his tabel')
	speial_student.hello()
	print(f'teacher {teach1.name} ! can you give me higth score')
	speial_student.myfather()
