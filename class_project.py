
class notebook_phon:

	phonbook_list=[]


	def addnumber(self):
		print('      ---------------------------------------      \n')
		self.numberuser=int(input('Please enter the number of members(1,2,..): '))
		print()
		while(self.numberuser>0):
			self.phonbook={}
			self.input()
			self.number=input('Please enter the number : ')
			print()
			self.phonbook["firstname"]=self.firstname
			self.phonbook["lastname"]=self.lastname
			self.phonbook["number"]=self.number
			self.phonbook_list.append(self.phonbook)
			self.numberuser-=1
		print('      ---------------------------------------      ')

	def shownumber(self):
		print('      ---------------------------------------      \n')
		if len(self.phonbook_list)==0:
			print('The phone book is empty, please add a number to it first')
			print('\n      ---------------------------------------      ')
			return
		print("<<Numbers in the phone book>> ")
		for i in range(len(self.phonbook_list)):
			print(f"name :\'{self.phonbook_list[i]['firstname']}\' & lastname :\'{self.phonbook_list[i]['lastname']}\' & number :\'{self.phonbook_list[i]['number']}\' \n")
		print('      ---------------------------------------      ')


	def deletenumber(self):
		print('      ---------------------------------------      \n')
		if len(self.phonbook_list)==0:
			print('The phone book is empty, please add a number to it first')
			print('\n      ---------------------------------------      ')
			return
		self.input()
		print()
		for i in range(len(self.phonbook_list)):
			if self.phonbook_list[i]["firstname"]==self.firstname and self.phonbook_list[i]["lastname"]==self.lastname:
				self.phonbook_list.pop(i)
				print('Removed successfully')
				break
		print('\n      ---------------------------------------      ')



	def serchnumber(self):
		print('      ---------------------------------------      \n')
		if len(self.phonbook_list)==0:
			print('The phone book is empty, please add a number to it first')
			print('\n      ---------------------------------------      ')
			return
		self.input()
		print()
		for i in range(len(self.phonbook_list)):
			if self.phonbook_list[i]["firstname"]==self.firstname and self.phonbook_list[i]["lastname"]==self.lastname:
				print('number -->  ' , end="")
				print(self.phonbook_list[i]["number"])
		print('\n      ---------------------------------------      ')


	def input(self):
		self.firstname=input('please enter the firstname : ')
		self.lastname=input('please enter the lastname : ')


	def fileNumber(self):
		print('      ---------------------------------------      \n')
		if len(self.phonbook_list)==0:
			print('The phone book is empty, please add a number to it first')
			print('\n      ---------------------------------------      ')
			return
		filename=input("Please enter the file name : ")
		print()
		f=open(f"{filename}.txt" , "w")
		for i in range(len(self.phonbook_list)):
			f.write(f"name :\'{self.phonbook_list[i]['firstname']}\' & lastname :\'{self.phonbook_list[i]['lastname']}\' & number :\'{self.phonbook_list[i]['number']}\'\n")
		print("File saved successfully\n")
		print("Note: The location of the created file is next to the executable file of the program")
		f.close()
		print('      ---------------------------------------      ')













