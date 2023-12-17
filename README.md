
# Compound Word Finder

This Python script identifies compound words from a list of words provided in text files. It offers two different approaches to identify compound words and find the longest and second-longest compound words within the given list.

## Getting Started

### Prerequisites
- Python 3.x

### Installation
1. Clone the repository or download the compound_word_finder.py file.

### Usage
1. Prepare input files (Input_01.txt, Input_02.txt, etc.) containing lists of words separated by newlines.
2. Update the file paths (file_01, file_02, etc.) in the script to match the paths of your input files.
3. Run the Python script in your terminal or IDE.

```bash
python compound_word_finder.py

## Overview

The script identifies compound words within text files, displaying the longest and second-longest compound words along with processing times.

## Design Decisions and Approach

### Design
The program is divided into key components:
- File Reading
- Compound Word Identification
- Finding Longest Compounds
- Processing Input Files

### Functionality Breakdown:
- *File Reading*: Reads a text file with word lists, returning them as lists.
- *Compound Word Identification*: Divides words into prefixes and suffixes, checking their existence in a set of words.
- *Finding Longest Compounds*: Identifies the two longest compound words from a list of identified compounds.
- *Processing Input Files*: Reads input files, identifies compound words, finds the longest and second-longest compound words, and measures processing time.

### Approach:
- *Two Methods*: Offers Trie-based and Set-based approaches for compound word identification.
- *Efficiency*: Utilizes recursion and data structure optimization for quicker lookups.

### Further Improvements:
- Enhancements using multithreading/multiprocessing for larger datasets.
- Experimentation with different data structures/algorithms for better efficiency.

This script serves as a foundation for identifying compound words within a list and can be extended or optimized based on specific requirements or larger datasets.

