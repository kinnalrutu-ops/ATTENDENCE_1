import sys
if sys.argv==2:
    classes_held=sys.argv[1]
    classes_attended=sys.argv[2]
attendance = (classes_attended / classes_held) * 100
print("Classes Held:", classes_held)
print("Classes Attended:", classes_attended)
print("Attendance:", round(attendance, 2), "%")
if attendance >= 75:
    print("Status: Eligible for exams")
else:
    print("Status: Not eligible for exams")
