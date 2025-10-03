import flet as ft
hero_section= ft.Row(
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
                        ft.Row(height=70,), 
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
                                            size=20,
                                            weight='bold'

                                        ),
                                        padding=ft.Padding(left=20,top=20,right=20,bottom=20),
                                        bgcolor=ft.Colors.BLUE_900,
                                        
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
                                        side=ft.BorderSide(width=2,color='black')


                                    )

                                    ),
                            ]
                            
                        ),
                        ft.Row(height=100),                 
                        ft.Row(
                            controls=[
                                # ft.Text(
                                #     'Secure Trasactions'
                                # )
                                ft.Container(
                                    content=ft.Row(
                                       controls=[
                                           ft.Icon(
                                               name=ft.Icons.ARROW_CIRCLE_RIGHT_ROUNDED,
                                           ),
                                           ft.Text(
                                    'Secure Trasactions'
                                )
   
                                       ] 
                                    ),
                                    bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,top=5,right=10,bottom=5),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                       controls=[
                                           ft.Icon(
                                               name=ft.Icons.CHECK_BOX_OUTLINE_BLANK_ROUNDED,
                                           ),
                                           ft.Text(
                                    'Real-time Rates'
                                )
   
                                       ] 
                                    ),
                                    bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,top=5,right=10,bottom=5),
                                ),
                                ft.Container(
                                    content=ft.Row(
                                       controls=[
                                           ft.Icon(
                                               name=ft.Icons.CONTROL_POINT_SHARP,
                                           ),
                                           ft.Text(
                                    'User-Focused Platform'
                                )
   
                                       ] 
                                    ),
                                    bgcolor='black',
                                    border_radius=50,
                                    padding=ft.Padding(left=10,top=5,right=10,bottom=5),
                                ),
                                    
                                    ft.Row(
                                        [
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        'Powerful Features for Modern DeFi',size=60,weight=ft.FontWeight.BOLD
                                                        ),
                                                ]
                                            )
                                        ]
                                    )
                                

                            ],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                    ],
                    
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=-25

                    
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
 