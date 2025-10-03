
import flet as ft
from .components.hero import hero_section

def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
       
    page.add(hero_section)
    feature_section= ft.Container(

    )
    page.add(feature_section)
        

ft.app(main)