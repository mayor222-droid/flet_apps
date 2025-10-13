import flet as ft
hero_section= ft.Row(
            [
                ft.Column(
                    controls=[
                        ft.Text('Discover Golden Zona ',size=60,weight=ft.FontWeight.BOLD, ),
                        ft.Text(
                            spans=[
                                ft.TextSpan(' Coin'),
                                ft.TextSpan(' Currency '),
                                ft.TextSpan('(GZC)',style=ft.TextStyle(color='#2B7FFF',)),
                                ft.TextSpan(': The')
                                ],
                                size=65,
                                weight='bold',
                            ),

                        ft.Text(
                            spans=[
                                ft.TextSpan('Future of'),
                                ft.TextSpan(
                                    text=' Digital Currency',
                                    style=ft.TextStyle(color='#2B7FFF'),
                                )
                            ],
                            size=65,
                            weight='bold'
                            
                        ),
                        ft.Row(height=50),
                        ft.Text(
                            'Experience secure transactions, real-time rates, and a user-focused platform with Golden\n Zona Coin (GZC). Join the UKA Decentralized E-currency revolution today.',
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
                                        bgcolor='#155DFC',
                                        
                                    ),
                                    


                                ),
                                ft.Button(
                                  content=ft.Row(
                                        [
                                            ft.Icon(
                                                name=ft.Icons.ARROW_FORWARD,
                                            ),
                                            ft.Text(
                                               'Connect Wallet', 
                                            ),
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=40),
                                        text_style=ft.TextStyle(
                                            size=40,
                                            weight='bold'

                                        ),
                                        padding=ft.Padding(left=50,top=40,right=50,bottom=40),
                                        bgcolor='#155DFC',
                                        
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
                                        side=ft.BorderSide(width=2,color='#05111A')


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
                                    padding=ft.Padding(left=15,top=10,right=15,bottom=10),
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
                                    padding=ft.Padding(left=15,top=10,right=15,bottom=10),
                                ),
                                    
                                   
                                

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
 