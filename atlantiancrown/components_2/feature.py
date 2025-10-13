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
                        'Everything you need to negative the decentralised finance ecosystem \n with confidence and ease',
                        text_align=ft.TextAlign.CENTER,
                        size=30,
                        weight=ft.FontWeight.W_600,
                        color='grey',
                    ),
                    ft.OutlinedButton(
                        'Token Management\n Seamlessly Manage your digital'
                    ),
    ],

                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
                                    ft.Row(height=80,), # to bring the btn rows down
                        ########################## buttons ##################
                        ft.Row(
                            controls=[
                                ft.Button(
                                    content=ft.Column(
                                        [
                                            ft.Text(
                                                'Seamlessly Manage your digital assets with\n advanced portfolio tracking and analytics',
                        
                                            ),
                                            ft.Icon(
                                                name=ft.Icon.animate_position
                                            )
                                        ],
                                        alignment=ft.MainAxisAlignment.CENTER
                                    ),
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=30),
                                        text_style=ft.TextStyle(
                                            size=20,
                                            weight='bold'
                                        )
                                    )
                                )
                            ]
                        )

        ],
        alignment=ft.MainAxisAlignment.CENTER,
    ),
    bgcolor='#040A10'
)


