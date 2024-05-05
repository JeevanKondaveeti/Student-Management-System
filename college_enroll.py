import flet as ft

"""
Theory: Why do we need User Controls

1)UserControl allows building isolated re-useable components by combaining the existing Flet controls
2)UserControl must implement build() that is called to build the Control's UI
3)build() function should return a single control instance or a list of controls
4)UserControl should call self.update() to push its changes to the Flet page.
5)super().__init__() must be always called in your constructor
"""

class Student(ft.UserControl):
    #def __init__(self,first_name,last_name,date_of_birth,phone_number,address):
    def __init__(self):
        super().__init__()
        #self.first_name =first_name
        #self.last_name = last_name
        #self.date_of_birth = date_of_birth
        #self.phone_number = phone_number
        #self.address = address
    def build(self):
        self.first_name=ft.TextField(label="first_name",hint_text="first_name",width=300)
        self.last_name=ft.TextField(label="last_name",hint_text="last_name",width=300)
        self.date_of_birth=ft.TextField(label="Date of birth",hint_text="Date_of_birth",width=300)
        self.phone_number=ft.TextField(label="Phone_number",hint_text="phone_number",width=300)
        self.address=ft.TextField(label="Address",hint_text="address",width=300)
        self.save_student=ft.ElevatedButton("Save student",on_click=self.add_student)
        #layout= ft.card(ft.Row([ft.Column([self.first_name,self.last_name,self.date_of_birth,self.phone_number,self.address,ft.Container(content=self.save_student,alignment=ft.alignment.center,width=300)])],alignment=ft.MainAxisAlignment.CENTER))
        
        return ft.Row([ft.Column([self.first_name,self.last_name,self.date_of_birth,self.phone_number,self.address,ft.Container(content=self.save_student,alignment=ft.alignment.center,width=300)])],alignment=ft.MainAxisAlignment.CENTER)
    
    def add_student(self,e):
        if not self.first_name.value and not self.last_name and not self.date_of_birth and not self.phone_number and not self.address :
            print("Enter Fields")
        else:
            with open('student.txt','a') as f:
                f.write(self.first_name.value)