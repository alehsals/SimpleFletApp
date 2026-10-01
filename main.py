import flet as ft

def main(page: ft.Page):
    page.title = "Test FilePicker Flet 1.0.1"
    page.alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    testo_esito = ft.Text("Nessun file selezionato", size=16)

    def al_selezionare_file(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            testo_esito.value = f"Selezionato: {e.files[0].name}"
            testo_esito.color = ft.Colors.GREEN
        else:
            testo_esito.value = "Selezione annullata"
            testo_esito.color = ft.Colors.ORANGE
        page.update()

    # Inizializzazione e registrazione in page.overlay
    picker = ft.FilePicker(on_result=al_selezionare_file)
    page.overlay.append(picker)

    page.add(
        ft.Column(
            [
                ft.Button(
                    "Scegli un file",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=lambda _: picker.pick_files(),
                ),
                testo_esito,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

if __name__ == "__main__":
    ft.run(main)
