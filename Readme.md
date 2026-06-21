# Case-Based Reasoning (CBR) for KDRT Cases - PN Sleman

## Project Description

This project is developed as an assignment for the Case-Based Reasoning (CBR) course.
The project aims to build a simple CBR system to analyze Domestic Violence (KDRT) court decisions from Pengadilan Negeri Sleman.
The system will retrieve similar previous cases and reuse previous decisions to help predict solutions for new cases.

## Dataset

Source:
https://putusan3.mahkamahagung.go.id

Case domain:
Pidana Khusus KDRT

Court:
Pengadilan Negeri Sleman

Minimum dataset requirement:
30 court decisions

## Project Structure

```
cbr-kdrt-pn-sleman/
data/
├── raw_pdf/
├── raw_txt/
├── processed/
├── eval/
└── results/
notebooks/
scripts/
README.md
.gitignore
```

## Workflow

1. Download court decisions (PDF)
2. Convert PDF to text
3. Clean text data
4. Extract metadata
5. Create structured dataset
6. Build retrieval system
7. Predict solutions
8. Evaluate model performance

## Tools

- Python
- Jupyter Notebook
- pandas
- scikit-learn
- transformers
- requests
- BeautifulSoup

## Team Notes

This repository will be developed incrementally following each stage of the CBR assignment.