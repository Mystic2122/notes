import subprocess
import os

file_name = input("Enter LaTeX file name: ")

subprocess.run(f"pdflatex {file_name}")

keep_log = input("Type yes to keep log file: ")

if keep_log == "yes":
    file_base, ext = os.path.split(file_name)
    os.remove(f"{file_base}.aux")
else:
    file_base, ext = os.path.splitext(file_name)
    os.remove(f"{file_base}.aux")
    os.remove(f"{file_base}.log")

if os.path.exists("texput.log"):
    os.remove("texput.log")

    
print("\nOutput Done!")