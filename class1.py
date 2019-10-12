class Students:
	def __init__(self,first,last):
		self.first=first
		self.last=last
		self.email=first+'.'+last+'@college.edu'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

std1= Students('prakriti','anand')

print(std1.fullname())
