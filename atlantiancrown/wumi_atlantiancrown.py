
import flet as ft
from .components_2.hero import hero_section
from .components_2.feature import feature_section
def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment=ft.MainAxisAlignment.CENTER


    page.add(hero_section)

    page.add(feature_section)

ft.app(main)