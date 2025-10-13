import flet as ft

feature_section= ft.Container(
    content= ft.Column(
        [
            ft.Row(
                [
                    ft.Container(
                        bgcolor='white',
                        height=250,
                        width=350,
                        # border=ft.Border.all(1, 'black')
                        padding=20,

                        border_radius=20,
                        content=ft.Column(
                            [
                                ft.Icon(ft.Icons.SECURITY, size=50, color='black'),
                                ft.Text('Secure Wallet', size=30, weight=ft.FontWeight.BOLD, color='black'),
                                ft.Text('Protect your digital assets with our state-of-the-art security features,\n including multi-signature support')
                            ],
                            
                        ),

                    ),
                    ft.Container(
                        bgcolor='white',
                        height=250,
                        width=350

                        
                    ),
                    ft.Container(
                        bgcolor='white',
                        height=250,
                        width=350
                        
                    ),
                    
                ],
                run_alignment=ft.MainAxisAlignment.SPACE_EVENLY,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=50,
            ),
            ft.Row(
                [
                    ft.Container(
                        bgcolor='green',
                        width=100,
                        height=100,


                    )
                ]
            ),

        ],
        col=2,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,

    ),
    bgcolor='#040A10'
)
