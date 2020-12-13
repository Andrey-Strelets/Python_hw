student_list = {'Ivanov Ivan':['Python', 'Java'],
                'Stepanov Stepan':['Java'],
                'Petrov Petr': ['FrontEnd'],
                'Semenov Semen':['FullStek'],
                'Sidorov Anton':['Python'],
                'Ivanova Anna':['FrontEnd', 'Java']}
for key, values in student_list.items():
	if len(values) >= 2:
		print("Cтудент", key, "учится в двух и более группах")
print()
for key, values in student_list.items():
	if "Java" in values and "Python" in values:
		print("Студент", key, "изучает Python и Java")
	elif "Java" in values:
		print("Студент", key, "изучает Java")
	elif "Python" in values:
		print("Студент", key, "изучает Python")
print()
for key, values in student_list.items():
	# for group in values:
	if not "FrontEnd" in values:
		print("Студент", key, "не изучает фронтенд")
