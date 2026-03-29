list1 = []
count = 0
while count != 10:
    try:
        grade = int(input('Enter grade: '))
    except (ValueError, TypeError) as e :
        print('Please enter a valid number')
    else:
        if grade == -999:
            print('Need at least 10 valid grades, keep entering.')
            continue
        if grade <= 0 or grade >= 100:
            print('Please enter a valid grade')
            continue
        count += 1
        list1.append(grade)

avg = sum(list1) / count
max_grade = max(list1)
print(f"number of valid grades: {count}\nAverage: {avg:.2f}\nMax: {max_grade}")

