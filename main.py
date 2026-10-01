import flet as ft

def main(page: ft.Page):
    page.title = "Test FilePicker Flet 1.0.1"
    page.alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    testo_esito = ft.Text("Nessun file selezionato", size=16)

    # In Flet 1.0 l'handler è asincrono per attendere l'esito di pick_files()
    async def al_selezionare_file(e: ft.Event[ft.Button]):
        files = await picker.pick_files()
        if files:
            testo_esito.value = f"Selezionato: {files[0].name}"
            testo_esito.color = ft.Colors.GREEN
        else:
            testo_esito.value = "Selezione annullata"
            testo_esito.color = ft.Colors.ORANGE
        page.update()

    # 1. Inizializzazione come Service
    picker = ft.FilePicker()
    
    # 2. Registrazione in page.services (NON page.overlay)
    page.services.append(picker)

    page.add(
        ft.Column(
            [
                ft.Button(
                    content="Scegli un file",
                    icon=ft.Icons.FOLDER_OPEN,
                    on_click=al_selezionare_file,
                ),
                testo_esito,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

if __name__ == "__main__":
    ft.run(main)
