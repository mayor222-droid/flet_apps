
import flet as ft

def main(page:ft.Page):
    page.vertical_alignment=ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Row(
            [
                ft.Column(
                    controls=[
                        ft.Text('Discover Atlantian Crown ',size=60,weight=ft.FontWeight.BOLD, ),
                        ft.Text(
                            spans=[
                                ft.TextSpan('Currency '),
                                ft.TextSpan('(ATC)',style=ft.TextStyle(color='blue', )),
                                ft.TextSpan(': The'),
                                ],
                                size=60,
                                weight='bold',
                            ),

                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                   text= 'Future of '
                                ),
                                ft.TextSpan(
                                   text= 'Digital Currency',
                                   style=ft.TextStyle(color='blue')
                                ),

                            ],
                            size=60,
                            weight='bold'
                        ),
                        ft.Row(height=50),
                        ft.Text(
                            'Experience secure transactions, real-time rates, and a user-focused platform with Atlantian \n Crown (ATC). Join the UKA Decentralized E-currency revolution today.',
                            text_align=ft.TextAlign.CENTER,
                            size=17.2,
                            weight=ft.FontWeight.W_600,
                            color='grey'
                        ),
                        ft.Row(height=70,), # to bring the btn rows down 
                        ########################## buttons #######################
                        ft.Row(
                            controls=[
                            
                                ft.Button(
                                    content=ft.Row(
                                        [
                                            ft.Text(
                                               'Register', 
                                            ),
                                            ft.Icon(
                                                name=ft.Icons.ARROW_FORWARD,
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        text_style=ft.TextStyle(
                                            size=25,
                                            weight='bold'

                                        ),
                                        padding=ft.Padding(left=10,top=20,right=10,bottom=20),
                                        bgcolor=ft.Colors.BLUE_600,
                                        
                                    )
                                    


                                ),
                                ft.OutlinedButton(
                                    'Login',
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight=ft.FontWeight.W_400
                                        ),
                                        padding=ft.Padding(left=30,top=20,right=30,bottom=20),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(width=1,color='blue') #border styling


                                    )

                                    ),
                                    
                                    

                            ]
                        )
                    ],
                    
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=-25

                    
                ),
            ],
            # vertical_alignment=ft.MainAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(main)