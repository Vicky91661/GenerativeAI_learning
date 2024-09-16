def test(data1,data2):
    return data1+data2
print(test(23,34))
print(test("vicky","kumar"))
print(test([1,2,4,2],[35,342,45]))

# lets make class and object 
class web_dev:
    def syllabus(self):
        print("this is my web dev syllabus")
class python:
    def syllabus(self):
        print("this is my python syllabus")
data_science = python()
web_dev2 = web_dev()
# print(web_dev2.syllabus())
# print(data_science.syllabus())


def class_parser(class_obj):
    for i in class_obj:
        i.syllabus()
class_parser([data_science,web_dev2])