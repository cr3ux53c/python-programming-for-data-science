class_category = ["A", "B", "C", "D"]
student_category = ["Sam", "Sarah", "Jane", "John"]

class_student_cate = { }
for i in range(len(class_category)):
    class_student_cate[class_category[i]] = student_category[i]
print(class_student_cate)
