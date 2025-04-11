import os
import subprocess

def convert_docx_to_pdf(docx_path: str, output_dir: str) -> str:
    subprocess.run([
        "soffice",
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_dir,
        docx_path
    ], check=True)
    return os.path.join(output_dir, os.path.basename(docx_path).replace(".docx", ".pdf"))

def warm_up_libreoffice():
    try:
        subprocess.run(["soffice", "--headless", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        print("⚠️ LibreOffice không được tìm thấy trong PATH!")