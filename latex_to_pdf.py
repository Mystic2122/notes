import subprocess
import os

file_name = input("Enter LaTeX file name: ")

full_path = None

for root, dirs, files in os.walk("."):
    if file_name in files:
        full_path = os.path.join(root, file_name)
        break

dir_name, base_name = os.path.split(full_path)
file_base, _ = os.path.splitext(base_name)

result = subprocess.run(
    ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", base_name],
    cwd=dir_name
)

pdf_name = f"{file_base}.pdf"
pdf_path = os.path.join(dir_name, pdf_name)

parent_dir = os.path.dirname(dir_name)
new_pdf_path = os.path.join(parent_dir, pdf_name)

# Only move if the PDF exists
if os.path.exists(pdf_path):
    os.replace(pdf_path, new_pdf_path)




keep_log = input("Type yes to keep log file: ").strip().lower()


def rm(ext):
    # Use file_base (no .tex), so we get factorial_design.aux etc.
    path = os.path.join(dir_name, f"{file_base}{ext}")
    if os.path.exists(path):
        os.remove(path)

# Always remove these
rm(".aux")
rm(".fdb_latexmk")
rm(".fls")
rm(".synctex.gz")

# Remove .log unless user wants to keep it
if keep_log != "yes":
    rm(".log")

# Remove stray texput.log in the directory where you ran the script
if os.path.exists("texput.log"):
    os.remove("texput.log")

print("\nOutput Done!")