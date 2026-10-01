import flet as ft

def main(page: ft.Page):
    page.title = "Test FilePicker Flet 1.0.1"
    page.alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Testo per mostrare l'esito della selezione
    testo_esito = ft.Text("Nessun file selezionato", size=16)

    # Callback eseguita al termine della selezione
    def al_selezionare_file(e: ft.FilePickerResultEvent):
        if e.files and len(e.files) > 0:
            testo_esito.value = f"Selezionato: {e.files[0].name}"
            testo_esito.color = ft.Colors.GREEN
        else:
            testo_esito.value = "Selezione annullata"
            testo_esito.color = ft.Colors.ORANGE
        page.update()

    # Inizializzazione FilePicker
    picker = ft.FilePicker(on_result=al_selezionare_file)
    
    # REGOLA FONDAMENTALE: Va Aggiunto solo in overlay
    page.overlay.append(picker)

    # Layout dell'interfaccia
    page.add(
        ft.Column(
            [
                ft.ElevatedButton(
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
