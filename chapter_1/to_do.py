import flet as ft

def main(page: ft.Page):
    # setting up the page tittle
    page.tittle = "To-DO App"
    page.theme_mode= "light"



    # taking input from the user 
    input_text = ft.TextField(hint_text="what do you want to do today......")

    def button_clicked(e):
        page.add(ft.Checkbox(label=input_text.value))
      

    # aligning the import text and botton in a row
    page.add(
        ft.Row(
            [
                input_text,
                ft.ElevatedButton(text="Add, on_click=button_clicked")
            ]
        )
    )

    ft.app(target=main)
