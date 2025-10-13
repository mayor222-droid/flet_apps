
import flet as ft
hero_section=ft.Row(
            [
                ft.Column(
                    controls=[
                        ft.Text('Discover Golden Zona',size=70,weight=ft.FontWeight.BOLD, ),
                        ft.Text(
                            spans=[
                                ft.TextSpan('coin currency '),
                                ft.TextSpan('(GZC)',style=ft.TextStyle(color='#2B7FFF',)),
                                ft.TextSpan(': The'),
                            ],
                            size=70,
                            weight='bold',
                        ),
                        ft.Text(
                            spans=[
                                ft.TextSpan(
                                    text=' future of '

                                ),
                                ft.TextSpan(
                                    text='Digital Currency',
                                    style=ft.TextStyle(color='#2B7FFF')
                                ),

                            ],
                            size=70,
                            weight='bold'
                        ),
                        ft.Row(height=80),
                        ft.Text(
                            'Experience secure transactions, real-time rate, and a user focused platform with Golden \n Zona (GZC).Join the UKA Decentralized E-currency revolution today.',
                            text_align=ft.TextAlign.CENTER,
                            size=20.5,
                            weight=ft.FontWeight.W_400,
                            color='grey'
                        ),
                        ft.Row(height=80,), # to bring the btn rows down
                        ########################## buttons ##################
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
                                        shape=ft.RoundedRectangleBorder(radius=15),
                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight='bold'

                                        ),
                                        padding=ft.Padding(left=30,top=25,right=32,bottom=20),
                                        bgcolor='#155DFC',
                                    )
                                ),
                                ft.OutlinedButton(
                                    'connect wallet',
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=20),
                                        text_style=ft.TextStyle(
                                            size=30,
                                            weight=ft.FontWeight.W_600
                                        ),
                                        padding=ft.Padding(left=40,top=30,right=30,bottom=40),
                                        bgcolor='#155DFC',
                                    )
                                ),

                                ft.OutlinedButton(
                                    'login',
                                    style=ft.ButtonStyle(

                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight=ft.FontWeight.W_400
                                        ),
                                        padding=ft.Padding(left=30,top=20,right=30,bottom=20),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        side=ft.BorderSide(width=3,color='blue' ) #border styling
                                    ),

                                ),

                            ],
                        ),
                        ft.Row(height=100),
                        ft.Row(
                            controls=[
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.ARROW_DROP_UP,
                                            ),
                                            ft.Text(
                                                'Secure Trasactions'
                                            )
                                        ]
                                    ),bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,right=10,top=5,bottom=5),
                                ),                                
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.CHECK_BOX_OUTLINE_BLANK_ROUNDED,
                                            ),
                                            ft.Text(
                                                'Real-time Rates'
                                            ),
                                        ]
                                    ),bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,right=10,top=5,bottom=5),
                                ),                                
                                ft.Container(
                                    content=ft.Row(
                                        controls=[
                                            ft.Icon(
                                                name=ft.Icons.CONTROL_POINT_SHARP,
                                            ),
                                            ft.Text(
                                                'User-Focused Platform '
                                            )
                                        ]
                                    ),bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,right=10,top=5,bottom=5),
                                ),                                

                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],

                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing= -30


                    
                ),
            ],
            # vertical_alignment=ft.mainAxisalignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER
        )
        