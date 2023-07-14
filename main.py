import flet as ft
import os
import sys
def main(page: ft.Page):
    page.title = "Xrun"#软件标题
    #主界面配置
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        # extended=True,
        min_width=100,
        min_extended_width=400,
        leading=ft.FloatingActionButton(icon=ft.icons.CREATE, text="安装"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.icons.FAVORITE_BORDER, selected_icon=ft.icons.FAVORITE, label="功能"
            ),

            ft.NavigationRailDestination(
                icon=ft.icons.SETTINGS_OUTLINED,
                selected_icon_content=ft.Icon(ft.icons.SETTINGS),
                label_content=ft.Text("设置"),
            ),
        ],
        on_change=lambda e: print("Selected destination:", e.control.selected_index),
    )


    #警告代码
    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, 您使用的不是Linux系统。无法使用该应用。"
        ),
        actions=[
            ft.TextButton("退出",on_click=exit1),
        ],
    )
    #判断系统是否为Linux系统
    if os.name != 'posix':
        page.banner.open = True
        page.update()



    page.add(
        ft.Row(
            [
                rail,
                ft.VerticalDivider(width=1),
                ft.Column([ft.Text("施工中……")], alignment=ft.MainAxisAlignment.START, expand=True),
            ],
            expand=True,
        )
    )
    page.add(ft.Text("欢迎使用Xrun Copyright Allen 2023-2023"))
ft.app(target=main)
