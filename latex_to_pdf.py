import subprocess
import os

file_name = input("Enter LaTeX file name: ")

subprocess.run(f"pdflatex {file_name}")

keep_log = input("Type yes to keep log file: ")

if keep_log == "yes":
    file_base, ext = os.path.split(file_name)
    if os.path.exists(f"{file_base}.aux"): 
        os.remove(f"{file_base}.aux") 
    if os.path.exists(f"{file_base}.fdb_latexmk"): 
        os.remove(f"{file_base}.fdb_latexmk")
    if os.path.exists(f"{file_base}.fls"):
        os.remove(f"{file_base}.fls")
    if os.path.exists(f"{file_base}.synctex.gz/{file_base}"):
        os.remove(f"{file_base}.synctex.gz/{file_base}.synctex")
    if os.path.exists(f"{file_base}.synctex.gz"):
        os.remove(f"{file_base}.synctex.gz")
else:
    file_base, ext = os.path.splitext(file_name)
    if os.path.exists(f"{file_base}.log"):
        os.remove(f"{file_base}.log")
    if os.path.exists(f"{file_base}.aux"): 
        os.remove(f"{file_base}.aux") 
    if os.path.exists(f"{file_base}.fdb_latexmk"): 
        os.remove(f"{file_base}.fdb_latexmk")
    if os.path.exists(f"{file_base}.fls"):
        os.remove(f"{file_base}.fls")
    if os.path.exists(f"{file_base}.synctex.gz/{file_base}"):
        os.remove(f"{file_base}.synctex.gz/{file_base}.synctex")
    if os.path.exists(f"{file_base}.synctex.gz"):
        os.remove(f"{file_base}.synctex.gz")


if os.path.exists("texput.log"):
    os.remove("texput.log")

    
print("\nOutput Done!")