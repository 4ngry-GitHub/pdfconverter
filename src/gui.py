import PySimpleGUI as gui

from pdf_handler import process_pdf


gui.theme("Dark")
layout: list = [
    [gui.Text("Welcome to simple PDF TTS converter!")],
    [gui.Text("The program will convert PDF file to a audio MP3 file.")],
    [gui.Text("Choose a file:", font=('Helvetica', 12, 'bold'))],
    [gui.InputText(key="file_path", default_text="Choose a file"), gui.FileBrowse(button_color=("white", "blue"))],
    [gui.Output(size=(45, 3))],
    [gui.Button("Submit", button_color=("white", "green"))],
    [gui.Button("Exit", button_color=("white", "red"))],
]

window = gui.Window("Simple PDF TTS converter", layout)


def start_app() -> None:
    while True:
        event, values = window.read()
        if event == gui.WIN_CLOSED or event == "Exit":
            break
        if event == "Submit":
            process_pdf(values["file_path"])

    window.close()


if __name__ == "__main__":
    try:
        start_app()
    except KeyboardInterrupt:
        exit(0)
