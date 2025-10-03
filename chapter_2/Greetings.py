# importing the libraries
import flet as ft

# defining the main function
def main(page: ft.Page):

    # setting the page tittle
    page.tittle = "Simple Greeting App!"

    # changing the page theme
    page.theme_mode = "light"

    # taking first name\last name from user
    first_name = ft.Ref[ft.TextField]()
    last_name = ft.Ref[ft.TextField]()

    # column for greeting the user
    greetings = ft.Ref[ft.Column]()

    # defining the botton click function
    def btn_click(e):
        greetings.current.controls.append(ft.Text(f"Hello {first_name.current.value} {last_name.current.value}!"))
        first_name.current.value = ""
        last_name.current.value = ""
        first_name.current.focus()
        page.update()


    # Button
    

    page.add(
        ft.TextField(ref=first_name, label="first name", autofocus=True),
        ft.TextField(ref=last_name, label="last name"),
        ft.ElevatedButton("Say hello", on_click=btn_click),
        ft.Column(ref=greetings) 
    )

ft.app(target=main)

...
# NOTE:

# 1 All the first controls have a property know as ref
...