from pathlib import Path
import json
from datetime import datetime

# >>> Edite aqui o caminho do seu repositório <<<
REPO_DIR = Path(r"/workspaces/Personal/UnB/2025.2/APC/Questionário - Strings")  # Ex.: r"C:\Users\voce\projeto" ou "/home/voce/projeto"

REPO_DIR.mkdir(parents=True, exist_ok=True)

# Modelo de notebook Jupyter (estrutura JSON)
def notebook_template(n):
    return {
        "cells": [
            {
                "cell_type": "markdown",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [ f'## Questão {n}\n\n### Texto da questão']
            }
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "name": "python",
                "version": "3.x"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    }

created, skipped = 0, 0

for n in range(1, 10):
    fpath = REPO_DIR / f"Q{n}.ipynb"
    if fpath.exists():
        skipped += 1
        continue
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(notebook_template(n), f, indent=2, ensure_ascii=False)
    created += 1

print(f"Notebooks criados: {created} | Já existiam: {skipped} | Pasta: {REPO_DIR}")