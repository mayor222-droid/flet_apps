import flet as ft

__init__section=ft.Container(
    content=ft.Column(
        [
            ft.Row(height=50),
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Text(
                                spans=[
                                    ft.TextSpan('Get in'),
                                    ft.TextSpan(
                                        text=' Touch',
                                        style=ft.TextStyle(color='#2B7FFF'),
                                    )
                                ],
                                size=40,
                                weight='bold'
                            )
                        ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(height=20),
            ft.Text(
                'Have questions, feedback, or partnership ideas? We’d love to hear from you.',
                text_align=ft.TextAlign.CENTER,
                size=18,
                weight=ft.FontWeight.W_600,
                color='grey'
            ),
            ft.Row(
                [
                    ft.Container(
                        bgcolor='#111519',
                        height=400,
                        width=700,
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Text('Contact Information',size=30, weight=ft.FontWeight.BOLD, color='white'),
                                ft.Row(height=15),
                                ft.Row(
                                    controls=[
                                        
                                        ft.Button(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                       name=ft.Icons.EMAIL,
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.Padding(left=20,right=20,top=20,bottom=20),
                                                bgcolor='#5978FF',
                                            )
                                        ),
                                        ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                                ft.TextSpan('Email',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.Text('support@gzc.io',weight=ft.FontWeight.BOLD),

                                                    ],
                                                    spacing=2
                                                )
                                            ]
                                        )
                                    
                                    

                                    ],

                                ),
                                ft.Row(height=15),
                                ft.Row(
                                    controls=[
                                        
                                        ft.Button(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                       name=ft.Icons.PHONE,
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.Padding(left=20,right=20,top=20,bottom=20),
                                                bgcolor='#5978FF',
                                            )
                                        ),
                                        ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                            ft.TextSpan('Phone',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.Text('+1 (555) 987-6543',weight=ft.FontWeight.BOLD),

                                                    ],
                                                    spacing=2
                                                )
                                            ]
                                        )
                                    
                                    

                                    ],

                                ),
                                ft.Row(height=15),
                                ft.Row(
                                    controls=[
                                        
                                        ft.Button(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                       name=ft.Icons.EMAIL,
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.Padding(left=20,right=20,top=20,bottom=20),
                                                bgcolor='#5978FF',
                                            )
                                        ),
                                        ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                                ft.TextSpan('Address',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.Text('123 DeFi Street, Blockchain City',weight=ft.FontWeight.BOLD),

                                                    ],
                                                    spacing=2
                                                )
                                            ]
                                        )
                                    
                                    

                                    ],

                                ),
                                ft.Row(height=15),
                                ft.Row(
                                    controls=[
                                        
                                        ft.Button(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                    name=ft.Icons.EMAIL,
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.Padding(left=20,right=20,top=20,bottom=20),
                                                bgcolor='#5978FF',
                                            )
                                        ),
                                        ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                                ft.TextSpan('Working Hours',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.Text('Mon - Fri: 9:00 AM - 6:00 PM',weight=ft.FontWeight.BOLD),

                                                    ],
                                                    spacing=2
                                                )
                                            ]
                                        )
                                    
                                    

                                    ],

                                ),
                                ft.Row(height=15),
                                ft.Row(
                                    controls=[
                                        
                                        ft.Button(
                                            content=ft.Row(
                                                [
                                                    ft.Icon(
                                                       name=ft.Icons.CHAT,
                                                    )
                                                ]
                                            ),
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.Padding(left=20,right=20,top=20,bottom=20),
                                                bgcolor='#5978FF',
                                            )
                                        ),
                                        ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                                ft.TextSpan('Live Chat',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.Text('Available 24/7 for Premium Members',weight=ft.FontWeight.BOLD),

                                                    ],
                                                    spacing=2
                                                )
                                            ]
                                        )
                                    
                                    

                                    ],

                                ),
                            ],
                            spacing=4
                        )
                    ),
                    ft.Container(
                        bgcolor='#111519',
                        height=400,
                        width=700,
                        padding=20,
                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Text('Send us a Message',size=30, weight=ft.FontWeight.BOLD, color='white'),
                                ft.Row(
                                        [
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        spans=[
                                                            ft.TextSpan('First Name',style=ft.TextStyle(color='grey')),
                                                            
                                                        ],
                                                    ),
                                                    ft.OutlinedButton(

                                                        'Omowumi',
                                                        style=ft.ButtonStyle(

                                                            text_style=ft.TextStyle(
                                                                size=15,
                                                                weight=ft.FontWeight.W_400
                                                            ),
                                                            padding=ft.Padding(left=15,top=5,right=300,bottom=5),
                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                            side=ft.BorderSide(width=3,color='grey') 
                                                        ),

                                                    ),

                                                ],
                                                spacing=2
                                            ),
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        spans=[
                                                            ft.TextSpan('First Name',style=ft.TextStyle(color='grey')),
                                                            
                                                        ],
                                                    ),

                                                ],
                                                spacing=2
                                            ),
                                        ]
                                    ),
                                ft.Row(
                                        [
                                            ft.Column(
                                                controls=[
                                                    ft.Text(
                                                        spans=[
                                                            ft.TextSpan('Email',style=ft.TextStyle(color='grey')),
                                                            
                                                        ],
                                                    ),
                                                    ft.OutlinedButton(

                                                        'you@email.com',
                                                        style=ft.ButtonStyle(

                                                            text_style=ft.TextStyle(
                                                                size=15,
                                                                weight=ft.FontWeight.W_400
                                                            ),
                                                            padding=ft.Padding(left=15,top=5,right=500,bottom=5),
                                                            shape=ft.RoundedRectangleBorder(radius=10),
                                                            side=ft.BorderSide(width=3,color='grey') 
                                                        ),

                                                    ),

                                                ],
                                                spacing=2
                                            ),
                                        ]
                                    ),

                                    ft.Row(
                                            [
                                                ft.Column(
                                                    controls=[
                                                        ft.Text(
                                                            spans=[
                                                                ft.TextSpan('Message',style=ft.TextStyle(color='grey')),
                                                                
                                                            ],
                                                        ),
                                                        ft.OutlinedButton(

                                                            'Write your message.......',
                                                            style=ft.ButtonStyle(

                                                                text_style=ft.TextStyle(
                                                                    size=15,
                                                                    weight=ft.FontWeight.W_400
                                                                ),
                                                                padding=ft.Padding(left=15,top=5,right=450,bottom=30),
                                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                                side=ft.BorderSide(width=3,color='grey') 
                                                            ),

                                                        ),

                                                    ],
                                                    spacing=2
                                                ),
                                            ]
                                        ),
                                        ft.Row(
                                            controls=[
                                                ft.Button(
                                                    content=ft.Row(
                                                        [
                                                            ft.Icon(
                                                                name=ft.Icons.MESSAGE,
                                                            ),
                                                            ft.Text(
                                                                'Send Message',
                                                            )
                                                        ],
                                                        alignment=ft.MainAxisAlignment.CENTER
                                                    ),
                                                    style=ft.ButtonStyle(
                                                        shape=ft.RoundedRectangleBorder(radius=10),
                                                        text_style=ft.TextStyle(
                                                            size=15,
                                                            weight='bold'

                                                        ),
                                                        padding=ft.Padding(left=250,top=15,right=250,bottom=15),
                                                        bgcolor='#5978FF',
                                                    )
                                                ),

                                                

                                            ],
                                        ),
                                

                            ]
                        )
                    ),
                     ft.Row(height=50),
                     ft.Row(
                        [
                            ft.Column(
                                controls=[
                                    ft.Text(
                                        spans=[
                                            ft.TextSpan('C'),
                                            ft.TextSpan(
                                                text='Golden Zona Coin',
                                                style=ft.TextStyle(color='#2B7FFF'),
                                            )
                                        ],
                                        size=40,
                                        weight='bold',
                                    ),
                                ]
                            )
                        ],
                        
                    ),
                    ft.Row(height=20),
                    ft.Text(
                        'The future of decentralised finance.Manage,stake,and\n grow your digital assests with our cutting-edge blockchain\n platform.',
                        text_align=ft.TextAlign.CENTER,
                        size=13,
                        weight=ft.FontWeight.W_400,
                        color='grey'
                    ),
                        ]
                    )
                ],

        col=2,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    bgcolor='#090D11'

)