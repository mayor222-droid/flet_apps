# import the library
import flet as ft

# defining the main function
def main(page: ft.Page):
    page.tittle = "counter App"
    page.theme_mode = "light"

    # creating the text field
    txt_number = ft.TextField(value="0", text_align="counter", width=100)

    page.add(
        ft.Row(
            controls=(
                ft.IconButton(),
                txt_number,
                ft.IconButton()
            )
        )
    )

ft.app(target=main)