# Создать словарь оценок предполагаемых студентов (Ключ - ФИ студента, значение - список оценок студентов). 
# Найти самого успешного и самого отстающего по среднему баллу.

student_list = {'Ivanov Ivan':[5, 5, 3, 4,5],
                'Stepanov Stepan':[3, 4, 5, 3, 4],
                'Petrov Petr': [5, 5, 5, 5, 5],
                'Semenov Semen':[3,4,3,3,4]}
medium_mark = {key:sum(val)/len(val) for key,val in student_list.items()}
maxs_mark = max(medium_mark.values())
min_mark = min(medium_mark.values())
reversed_list = {value : key for (key, value)in medium_mark.items()}
print("Самый успешный студент:", reversed_list.get(maxs_mark), "с средним балом =", maxs_mark)
print("Самый отстающий студент:", reversed_list.get(min_mark), "с средним балом =", min_mark)


