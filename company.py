class Member:
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age

	def display(self):
		print(f"Member: {self.first_name} {self.last_name}, age {self.age}")

	def update_first_name(self, new_first_name):
		self.first_name = new_first_name

	def update_last_name(self, new_last_name):
		self.last_name = new_last_name

	def update_age(self, new_age):
		self.age = new_age

class Executives(Member):
	pass


class Employee(Member):
	salary = 1000
	vacation_status = False

	def display(self):
		print(f"Employee: {self.first_name} {self.last_name}, age {self.age}")

	def show_salary(self):
		print(f"{self.first_name} {self.last_name}'s Salary is {self.salary} USD")

	def update_salary(self, new_salary):
		self.salary = new_salary

	def send_on_vacation(self):
		self.vacation_status = True

	def return_from_vacation(self):
		self.vacation_status = False

class Sponsors:
	pass


#additional method to display information on everyone

general_member = Member("david", "Keen", 52)

general_member.display()
general_member.update_first_name("george")
general_member.update_last_name("michaels")
general_member.update_age(19)
general_member.display()

employee1 = Employee("Cool", "Guy", 52)
employee1.display()
employee1.update_last_name("Neon")
employee1.display()
employee1.show_salary()
employee1.update_salary(1200)
employee1.show_salary()
employee1.send_on_vacation()
print(employee1.vacation_status)
employee1.return_from_vacation()
print(employee1.vacation_status)
