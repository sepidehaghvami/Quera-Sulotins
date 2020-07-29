w = float(input())
h = float(input())
bmi = w / (h ** 2)
print('%0.2f' % bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Overweight")
else:
    print("Obese")
