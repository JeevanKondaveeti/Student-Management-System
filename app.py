import flet as ft
from college_enroll import Student
"""
Theory: Why do we need User Controls

1)UserControl allows building isolated re-useable components by combaining the existing Flet controls
2)UserControl must implement build() that is called to build the Control's UI
3)build() function should return a single control instance or a list of controls
4)UserControl should call self.update() to push its changes to the Flet page.
5)super().__init__() must be always called in your constructor
"""


def main(page:ft.Page):
    page.title= "Student management"
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.scroll= True
    page.appbar = ft.AppBar(
        title=ft.Text("Student Management Application"),
        center_title=True,
        elevation=5,
    )
    def routed(route):
        page.views.clear()
        page.views.append(
            ft.View(
                '/',
                controls=[
                    ft.AppBar(title=ft.Text("Student Management Application"),center_title=True,elevation=5),
                    mycontainer
                ],
                vertical_alignment="center",
                horizontal_alignment="center",
                scroll=True,
            )
        )
        if page.route == '/add_student':
            page.views.append(
            ft.View(
                '/add_student',
                controls=[
                    ft.AppBar(title=ft.Text("Student Management Application"),
                              center_title=True,
                              elevation=5,),
                    Student()
                ]
            )
        )
            
        page.update()
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    mybutton1 = ft.ElevatedButton("Add student",
                                  icon=ft.icons.PERSON_2_SHARP,
                                  width=300,
                                  
                                  on_click=lambda _: page.go('/add_student'))
    mybutton2 = ft.ElevatedButton("Add course",width=300,
                                  icon=ft.icons.PERSON_2_SHARP,
                                  on_click=lambda _: page.go('/add_course'))
    mybutton3 = ft.ElevatedButton("Enroll student to course",width=300,
                                  icon=ft.icons.PERSON_2_SHARP,
                                  on_click=lambda _: page.go('/enroll'))
    mycontainer = ft.Container(ft.Column([mybutton1,mybutton2,mybutton3],alignment=ft.MainAxisAlignment.CENTER),
                               margin=10,
                               padding=10,
                               bgcolor=ft.colors.BLUE_200,
                               border_radius=10,
                               height=500,
                              )
    #page.add(mycontainer)
    page.on_route_change=routed
    page.on_view_pop = view_pop

    page.go(page.route)
ft.app(target=main,view=ft.AppView.WEB_BROWSER)