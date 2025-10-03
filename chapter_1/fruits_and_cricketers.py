import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Row(controls=[ft.Text("My favorite fruits\n")]),
        ft.Row(
            controls=[
                ft.Text("Apple"),
                ft.Text("watermelon"),
                ft.Text("mango"),

            ]
        ),
        ft.Column(controls=[ft.Text("  My favorite cricketers\n")]),
        ft.Column(
            controls=[
                ft.Text("Sachin Ten"),
                ft.Text("Virat Kohli"),
                ft.Text("Ms Dhonj"),
            ]
        )
    )

ft.app(target=main)