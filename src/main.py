from pathlib import Path

from art import text2art
from gtts import gTTS
import pdfplumber
from termcolor import colored


def read_pdf(file_path: str):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print(colored(text=f"[+] File found. Processing...", color="green"))
        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf_file:
            pages: list = [page.extract_text() for page in pdf_file.pages]

        text: str = ''.join(pages)
        text: str = text.replace('\n', '')

        return text
    print(colored(text=f"Error! File ({file_path}) does`nt exists.\nCheck if path is correct.", color="red"))
    return False


def convert_to_mp3(text: str, file_path: str) -> dict:
    if text is False:
        return {"status": "failure"}
    audio = gTTS(text=text, lang='en', slow=False)
    file_name = Path(file_path).stem
    audio.save(f"{file_name}.mp3")

    print(colored(text=f"[+][Success]: {file_name}.mp3 saved.", color="green"))
    return {"status": "success"}


def main():
    print('-'*115)
    welcome_text: str = text2art("PDF > MP3 CONVERTER")
    print(colored(text=welcome_text, color="red"))
    print('-'*115)
    file_path: str = input('Enter a file`s path: ')
    convert_to_mp3(read_pdf(file_path), file_path)


if __name__ == '__main__':
    main()
