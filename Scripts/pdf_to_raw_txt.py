from __future__ import annotations

import argparse
import re
from pathlib import Path
from typing import List

from pypdf import PdfReader
import pdfplumber


def normalize_text(text: str) -> str:
    """Clean extracted PDF text for downstream NLP and CBR processing."""
    if not text:
        return ""

    text = text.replace("\x00", "")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?<!\n)\n(?!\n)", " ", text)
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s*([.,;:!?])", r"\1", text)
    text = re.sub(r"(?<=\w)\s(?=[.,;:!?])", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from PDF using pypdf, with a fallback to pdfplumber."""
    try:
        reader = PdfReader(str(pdf_path))
        pages = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            if page_text:
                pages.append(page_text)
        if pages:
            return "\n\n".join(pages)
    except Exception as exc:
        print(f"[warning] pypdf failed for {pdf_path.name}: {exc}")

    try:
        with pdfplumber.open(str(pdf_path)) as pdf:
            pages = []
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                if page_text:
                    pages.append(page_text)
            if pages:
                return "\n\n".join(pages)
    except Exception as exc:
        print(f"[warning] pdfplumber failed for {pdf_path.name}: {exc}")

    return ""


def convert_pdfs(input_dir: Path, output_dir: Path, overwrite: bool = False) -> List[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    converted_files: List[Path] = []

    pdf_files = sorted(input_dir.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return converted_files

    for pdf_path in pdf_files:
        output_path = output_dir / f"{pdf_path.stem}.txt"
        if output_path.exists() and not overwrite:
            print(f"[skip] {output_path.name} already exists")
            converted_files.append(output_path)
            continue

        text = extract_text_from_pdf(pdf_path)
        cleaned_text = normalize_text(text)
        output_path.write_text(cleaned_text, encoding="utf-8")
        converted_files.append(output_path)
        print(f"[saved] {output_path.name} ({len(cleaned_text)} chars)")

    return converted_files


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert PDF court decisions to cleaned raw text files")
    parser.add_argument("--input-dir", type=Path, default=Path("Data/Raw_PDF"), help="Directory containing source PDFs")
    parser.add_argument("--output-dir", type=Path, default=Path("Data/Raw_Txt"), help="Directory for cleaned text files")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing output files")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    input_dir = (repo_root / args.input_dir).resolve() if not args.input_dir.is_absolute() else args.input_dir
    output_dir = (repo_root / args.output_dir).resolve() if not args.output_dir.is_absolute() else args.output_dir

    converted_files = convert_pdfs(input_dir, output_dir, overwrite=args.overwrite)
    print(f"Processed {len(converted_files)} files")


if __name__ == "__main__":
    main()
