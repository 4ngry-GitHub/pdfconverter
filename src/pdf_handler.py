from pathlib import Path

from gtts import gTTS
import pdfplumber
from tqdm import tqdm as barlib


def read_pdf(file_path: str):
    if Path(file_path).is_file() and Path(file_path).suffix == ".pdf":
        print("File found. Processing...")

        with pdfplumber.PDF(open(file=file_path, mode="rb")) as pdf_file:
            pages: list = [page.extract_text() for page in barlib(pdf_file.pages)]

        text: str = ''.join(pages)
        text: str = text.replace('\n', '')

        return text
    print(f"Error! File ({file_path}) does`nt exists.\nCheck if path is correct.")
    return False


def convert_to_mp3(text: str, file_path: str) -> dict:
    if text is False:
        return {"status": "failure"}
    audio = gTTS(text=text, lang='en', slow=False)
    file_name = Path(file_path).stem
    print("Saving file...")
    audio.save(f"{file_name}.mp3")

    print(f"The file {file_name}.mp3 is saved successfully.")
    return {"status": "success"}


def process_pdf(file_path: str):
    convert_to_mp3(read_pdf(file_path), file_path)
