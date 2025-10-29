import flet as ft

feature_section= ft.Container(
    content= ft.Column(
        [
            ft.Row(height=30),
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Text(
                                spans=[
                                    ft.TextSpan('Powerful'),
                                    ft.TextSpan(' Features', style=ft.TextStyle(color='#2B7FFF')),
                                    ft.TextSpan(' for Modern DeFi'),
                                ],
                                size=55,
                                weight='bold'
                            ),
                        ],
                    ),
                    
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            ft.Row(height=10),
                    ft.Text(
                        'Everything you need to navigate the decentralized finance ecosystem\n with confidence and ease.',
                        text_align=ft.TextAlign.CENTER,
                        size=20,
                        weight=ft.FontWeight.W_600,
                        color='grey'

                    ),
            ft.Row(height=40),
            ft.Row(
                [
                    ft.Container(
                        bgcolor='#111519',
                        height=150,
                        width=450,
                        # border=ft.Border,all(1, 'black')
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY, size=30, color='#5978FF'),
                                ft.Text('Token Management', size=20, weight=ft.FontWeight.BOLD, color='white'),
                                ft.Text('Seamlessly manage your digital assets with advanced portfolio\ntracking and analytics.',size=12,color='grey'),
                            ],
                            
                        ),

                    ),
                    ft.Container(
                        bgcolor='#111519',
                        height=150,
                        width=450,
                        padding=20,

                        border_radius=15,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY,size=30,color='#5978FF'),
                                ft.Text('Staking Rewards',size=20, weight=ft.FontWeight.BOLD, color='white'),
                                ft.Text('Earn passive income by staking your tokens with competitive APY\nrates.',size=12,color='grey'),
                            ],

                        ),

                        
                    ),
                    ft.Container(
                        bgcolor='#111519',
                        height=150,
                        width=450,
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY,size=30,color='#5978FF'),
                                ft.Text('Governance',size=20, weight=ft.FontWeight.BOLD, color='white'),
                                ft.Text('Participate in decentralized governance and shape the future of\nthe protocol.',size=12,color='grey'),
                            ]
                        )
                        
                    ),
                    
                ],
                run_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50,
            ),
            ft.Row(height=20),
            ft.Row(
                [
                    ft.Container(
                        bgcolor='#111519',
                        width=450,
                        height=150,
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY,size=30,color='#394CAC'),
                                ft.Text('Advanced Analytics',size=20,weight=ft.FontWeight.BOLD,color='white'),
                                ft.Text('Real-time market data and comprehensive trading analytics at\nyour fingertips.',size=12,color='grey'),
                            ]

                        )


                    ),
                    ft.Container(
                        bgcolor='#111519',
                        width=450,
                        height=150,
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY,size=30,color='#5978FF'),
                                ft.Text('Security First',size=20,weight=ft.FontWeight.BOLD,color='white'),
                                ft.Text('Multi-layer security protocols to keep your assets safe and\nsecure.',size=12,color='grey'),
                            ]

                        )


                    ),
                    ft.Container(
                        bgcolor='#111519',
                        width=450,
                        height=150,
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY,size=30,color='#5877FF'),
                                ft.Text('Lightning Speed',size=20,weight=ft.FontWeight.BOLD,color='white'),
                                ft.Text('Execute transactions at lightning speed with minimal gas fees.',size=12,color='grey'),
                            ]

                        )


                    )
                ],
                run_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50,

            ),
            ft.Row(height=100),
            ft.Row(
                [
                    ft.Column(
                        controls=[
                            ft.Text(
                                spans=[
                                    ft.TextSpan('What is'),
                                    ft.TextSpan(
                                        text=' GZC',
                                        style=ft.TextStyle(color='#2B7FFF'),
                                    ),
                                    
                                    
                                ],

                                size=40,
                                weight='bold'
                            ),
                    
                                
                            
                        ],
                        
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Text(

                'Golden Zona Coin (GZC) is a digital currency designed to serve as a versatile and innovative asset within the\n evolving landscape of decentralized finance. Positioned as a cutting-edge cryptocurrency, GZC provides a\n secure, efficient, and globally accessible platform for transactions, investments, and digital asset\n management.',
                text_align=ft.TextAlign.CENTER,
                size=18,
                weight=ft.FontWeight.W_600,
                color='grey'
            ),
            ft.Row(height=60),

        ],
        col=2,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,

    ),
    bgcolor='#040A10'
)
