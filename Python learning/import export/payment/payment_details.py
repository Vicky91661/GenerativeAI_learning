import os, sys
from os.path import dirname,join,abspath
sys.path.insert(0,abspath(join(dirname(__file__),'..')))



from course import course_deatils
def payment():
    print("this is payment")
course_deatils.course()