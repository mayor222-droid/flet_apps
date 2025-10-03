# importing the library
import flet as ft

 # defining the main function
def main(page: ft.Page):

    # setting the page tittle
    page.tittle = "Hello World"

    # flet text control
    text = ft.Text(value="My first flet App!",color="blue")
    

    # appending 4 updating it to the page
    page.controls.append(text)
    page.update()

# startig the app
ft.app(target=main)