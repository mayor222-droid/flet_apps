import flet as ft

def main(page:ft.Page):
    page.title = 'Mayor Wumni App'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    page.add(txt_number)

ft.app(target=main)


