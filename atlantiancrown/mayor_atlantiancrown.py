import flet as ft
from .components.hero import hero_section
from .components.feature import feature_section
from .components.__init__ import __init__section
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.CrossAxisAlignment.CENTER
    page.scroll=ft.ScrollMode.ALWAYS
    main_column= ft.Column(
        controls=[
            hero_section,
            feature_section,
            __init__section
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        height=1000,
        width=1920,
        scroll=ft.ScrollMode.AUTO,
    )
    page.add(main_column)
    
ft.app(main)    