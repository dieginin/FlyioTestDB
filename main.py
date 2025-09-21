import flet as ft


def main(page: ft.Page):
    # Configuración básica
    page.title = "HubSync"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    count = int(page.client_storage.get("count") or 0)

    txt_number = ft.TextField(
        value=str(count), text_align=ft.TextAlign.RIGHT, width=100
    )

    def minus_click(e):
        txt_number.value = str(int(txt_number.value or 0) - 1)
        page.client_storage.set("count", txt_number.value)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value or 0) + 1)
        page.client_storage.set("count", txt_number.value)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.Icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


if __name__ == "__main__":
    # Configurar la aplicación para servir archivos estáticos
    ft.app(
        target=main,
        assets_dir="assets",  # Directorio de assets
        web_renderer=ft.WebRenderer.HTML,  # Usar HTML renderer para mejor compatibilidad PWA
    )
