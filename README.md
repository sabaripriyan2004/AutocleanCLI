# AutocleanCLI

# 🚀 CleanMyData CLI

> Intelligent Command-Line Tool for Automated Data Cleaning

---

## 📌 Overview

**CleanMyData** is a lightweight CLI tool that automatically cleans messy datasets using smart heuristics.

It handles:
- Missing values
- Duplicate rows
- Data type understanding
- Intelligent filling strategies (mean / median / mode)

👉 Built for **data scientists, analysts, and beginners** who want fast preprocessing.

---

## ⚡ Features

✅ Automatic missing value handling  
✅ Intelligent decision engine (mean / median / mode)  
✅ Duplicate row removal  
✅ Column-wise analysis report  
✅ Confidence-based cleaning summary  
✅ Simple CLI usage  

---

## 🧠 How It Works

1. **Load Data**
   - Reads CSV file using pandas

2. **Analyze Data**
   - Detects:
     - Missing values
     - Data types
     - Unique values

3. **Decision Engine**
   - Chooses best strategy:
     - Numeric → mean / median
     - Categorical → mode
     - High missing → drop

4. **Cleaner**
   - Applies transformations
   - Removes duplicates

5. **Scorer**
   - Assigns confidence score to each decision

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| **Python** | Core programming |
| **pandas** | Data handling |
| **numpy** | Numerical operations |
| **typer** | CLI interface |
| **rich** | Styled terminal output |

---

## 📦 Installation

Clone the repository:

git clone git clone https://github.com/YOUR_USERNAME/AutoCleanCLI.git
cd AutocleanCLI

Install dependencies:

pip install -r requirements.txt
```bash

## 📊 Sample Output

Cleaning data (intelligent mode)...

name: filled missing with mode  
age: filled missing with median  
salary: filled missing with median  
city: filled missing with mode  

Removed 1 duplicate rows  

Cleaning Summary:  
name -> mode (confidence=0.7)  
age -> median (confidence=0.8)  
salary -> median (confidence=0.8)  
city -> mode (confidence=0.7)  

Cleaning complete ✅

Run this command:

python -m cleanmydata.cli data/sample.csv
