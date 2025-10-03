# import the libraries
import flet as ft

from time import sleep

# defininig the main function
def main(page:ft.Page):
    page.tittle = "Counter App"

    text = ft.Text()

    page.add(text)

    for i in range(1,11):
        text.value = "Count " + str(i)
        page.update()
        sleep(1) # it will make the program sleep for 1 second

ft.app(target=main)



