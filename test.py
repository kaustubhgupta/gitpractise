# TODO: Some task for a project like a basic one shown here
import os


class Disp:
    def __init__(self):
        self.name = ''
        self.roll_no = ''

    def show(self, name,roll_no):
        self.name = name
        self.roll_no = roll_no
        return self.name, self.roll_no


a = Disp()
print(a.show(name='Kaustubh', roll_no=12))

# Now I am in new feature branch
