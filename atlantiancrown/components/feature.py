import flet as ft


feature_section= ft.Container(
    content= ft.Row(
        [
            ft.Column(
                controls=[
                    ft.Row(height=50),
                    ft.Text(
                        'Powerful Features For Modern DeFi',size=65, weight=ft.FontWeight.BOLD
                    ),
                    ft.Text(
                        'Everything you need to navigate the decentralized finance ecosystem\n with confidence and ease',
                        text_align=ft.TextAlign.CENTER,
                        size=25,
                        weight=ft.FontWeight.W_600,
                        color='grey',
                    ),
                    ft.OutlinedButton(
                                    'Token Management\n Seamlessly manage your digital assests with advanced potfolio\n tracking and analytic',
                                    
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight=ft.FontWeight.W_400
                                        ),
                                        padding=ft.Padding(left=30,top=20,right=30,bottom=20),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        


                                    )

                                    ),
                    ft.OutlinedButton(
                                    'Stacking resources  \n Earn passive income by stacking your tokens with competitive APY\n rates.',
                                    
                                    style=ft.ButtonStyle(
                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight=ft.FontWeight.W_400
                                        ),
                                        padding=ft.Padding(left=30,top=20,right=30,bottom=20),
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        


                                    )

                                    ),

                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),

        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    bgcolor='#040A10'
)
