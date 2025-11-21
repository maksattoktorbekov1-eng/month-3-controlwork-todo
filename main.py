import flet as ft
from db import main_db

def main(page: ft.Page):
    page.title = "Список покупок"
    page.theme_mode = ft.ThemeMode.LIGHT

    item_list = ft.Column(spacing=10)

    def load_items():
        item_list.controls.clear()
        for item_id, item_text, completed in main_db.get_items():
            checkbox = ft.Checkbox(label=item_text,value=bool(completed),on_change=lambda e, id=item_id: toggle_complete(id, e.control.value))
            delete_btn = ft.IconButton(icon=ft.Icons.DELETE,on_click=lambda e, id=item_id: remove_item(id))
            item_list.controls.append(ft.Row([checkbox, delete_btn]))
        page.update()

    def add_new_item(e):
        if input_field.value.strip():
            main_db.add_item(input_field.value)
            input_field.value = ""
            load_items()

    def toggle_complete(item_id, completed):
        main_db.update_item(item_id, completed)
        load_items()

    def remove_item(item_id):
        main_db.delete_item(item_id)
        load_items()

    input_field = ft.TextField(hint_text="Добавить покупку", expand=True)
    add_btn = ft.IconButton(icon=ft.Icons.ADD, on_click=add_new_item)

    page.add(ft.Row([input_field, add_btn]),item_list)

    main_db.init_db()
    load_items()

ft.app(target=main)

