period = int(input())

treated_patients = 0
untreated_patients = 0
count_of_doctors = 7


for i in range(1, period+1):
    current_patients = int(input())

    if period % 3 == 0 and untreated_patients > treated_patients:
        count_of_doctors += 1

    if current_patients > count_of_doctors:
        treated_patients += count_of_doctors
        untreated_patients += current_patients - count_of_doctors

    else:
        treated_patients += current_patients

print(treated_patients)
print(untreated_patients)
