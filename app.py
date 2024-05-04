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
                    ft.AppBar(title=ft.Text("Student Management Application"),
                              center_title=True,
                              elevation=5,),
                    Student()
                ]
            )
        )
        page.update()

    mybutton1 = ft.ElevatedButton("Enroll student",
                                  icon=ft.icons.PERSON_2_SHARP,
                                  on_click=lambda _: page.go('/'))
    page.add(mybutton1)
    page.on_route_change=routed

    #page.go(page.route)
ft.app(target=main)