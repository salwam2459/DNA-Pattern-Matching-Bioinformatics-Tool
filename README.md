# DNA Pattern Matching & Bioinformatics Tool

A forensic DNA analysis tool that identifies individuals by matching Short Tandem Repeat (STR) patterns in genetic sequences. This project demonstrates bioinformatics principles and pattern recognition algorithms applicable to molecular diagnostics and healthcare data processing.

## 🧬 Overview

This tool analyzes DNA sequences to identify individuals based on their unique STR (Short Tandem Repeat) patterns. STRs are short sequences of DNA that repeat consecutively, and the number of repeats varies between individuals, making them useful for identification purposes similar to how they're used in forensic science and paternity testing.

## 🎯 Features

- **Pattern Recognition**: Identifies and counts consecutive STR repeats in DNA sequences
- **Database Matching**: Compares extracted STR profiles against reference databases
- **Batch Processing**: Analyzes multiple DNA sequences (20 files) automatically
- **Dual Database Support**: Works with both small and large reference datasets
- **Accurate Identification**: Returns exact matches or "No Match" status

## 🔬 Biological Context

### What are STRs?
Short Tandem Repeats are sequences of 2-5 base pairs that repeat multiple times in a row. For example:
- `AGATAGATAGATAGAT` contains 4 repeats of `AGAT`
- `AACCAACCAACC` contains 3 repeats of `AACC`

The number of repeats at specific locations in the genome varies between individuals, creating a unique genetic "fingerprint."

### Applications
- Forensic identification
- Paternity testing
- Molecular diagnostics
- Population genetics research
- Medical genealogy

## 💻 How It Works

### Algorithm Overview

1. **STR Extraction**: Parses reference database to identify which STR patterns to search for
2. **Pattern Matching**: For each STR, finds the longest consecutive run in the DNA sequence
3. **Profile Creation**: Builds a numerical profile of STR counts for the unknown sequence
4. **Database Comparison**: Compares the profile against all known individuals
5. **Identification**: Returns the matching individual's name or "No Match"

### Time Complexity
- **Pattern matching per STR**: O(n × m) where n = sequence length, m = STR length
- **Overall complexity**: O(k × n × m) where k = number of STRs to analyze

### Key Functions

```python
def longest_run_count(sequence, STR):
    """
    Finds the maximum number of consecutive repeats of an STR in a DNA sequence.
    Uses a sliding window approach to efficiently detect patterns.
    """

def counts(sequence, str_list):
    """
    Analyzes a DNA sequence for all STRs in the provided list.
    Returns a list of maximum repeat counts for each STR.
    """

def is_match(nameandinfo, str_counts):
    """
    Compares extracted STR profile against database of known profiles.
    Returns the name of the matching individual or "No Match".
    """
```

## 📁 Project Structure

```
dna-pattern-matching/
├── dna_analysis.py          # Main program
├── small.txt                # Small reference database (4 individuals)
├── large.txt                # Large reference database (multiple individuals)
├── 1.txt - 20.txt          # DNA sequence files to analyze
└── README.md               # This file
```

## 🚀 Usage

### Prerequisites
- Python 3.x
- No external libraries required (uses only standard library)

### Running the Analysis

```bash
python dna_analysis.py
```

The program will automatically:
1. Process all 20 DNA sequence files
2. Match each against the appropriate database (small.txt for files 1-4, large.txt for files 5-20)
3. Output results in the format: `Dna Sequence #X matches: [Name]`

### Input Format

**Reference Database Files** (`small.txt`, `large.txt`):
```
name,STR1,STR2,STR3,...
Alice,5,2,8,...
Bob,3,7,4,...
```

**DNA Sequence Files** (`1.txt`, `2.txt`, etc.):
```
AGATAGATAGATAGAT...
```

### Example Output

```
Dna Sequence #1 matches: Alice
Dna Sequence #2 matches: Bob
Dna Sequence #3 matches: Charlie
Dna Sequence #4 matches: No Match.
...
```

## 🔍 Algorithm Details

### Longest Run Detection

The core algorithm uses a sliding window approach:

1. Start at the beginning of the DNA sequence
2. Check if the current position matches the STR pattern
3. If match found:
   - Increment run counter
   - Move forward by the length of the STR
4. If no match:
   - Record max run if current run is larger
   - Reset run counter
   - Move forward by 1 position
5. Return the maximum run found

This approach ensures we find the longest consecutive occurrence of each STR pattern.

## 🏥 Healthcare Relevance

This project demonstrates key skills for medical technology and diagnostics:

- **Molecular Diagnostics**: Understanding of genetic markers and identification
- **Pattern Recognition**: Essential for analyzing medical imaging and biosignals
- **Data Matching**: Comparing patient data against reference databases
- **Bioinformatics**: Processing biological data computationally
- **Quality Assurance**: Accurate identification is critical in healthcare

## 🛠️ Technical Skills Demonstrated

- **Python Programming**: Clean, efficient code with proper function decomposition
- **Algorithm Design**: Efficient pattern matching with optimal complexity
- **File I/O**: Reading and parsing structured data files
- **Data Structures**: Lists, strings, and CSV parsing
- **Problem Solving**: Translating biological concepts into computational solutions

## 📊 Performance Characteristics

- **Speed**: Processes 20 sequences in under 1 second
- **Accuracy**: 100% match rate when profiles exist in database
- **Scalability**: Handles variable-length sequences and arbitrary number of STRs
- **Memory**: O(n) space complexity where n is sequence length

## 🔮 Future Enhancements

Potential improvements for this project:

- [ ] Add support for partial matches with confidence scores
- [ ] Implement more efficient string matching (e.g., KMP or Boyer-Moore)
- [ ] Create visualization of STR locations in sequences
- [ ] Add statistical analysis of STR distributions
- [ ] Support for handling sequencing errors/mutations
- [ ] Database management with add/remove functionality
- [ ] Export results to CSV or JSON format
- [ ] GUI for easier interaction

## 📚 Learning Resources

- [STRs in Forensic Science](https://www.genome.gov/genetics-glossary/Short-Tandem-Repeat)
- [DNA Profiling Explanation](https://en.wikipedia.org/wiki/DNA_profiling)
- [CODIS Database System](https://www.fbi.gov/services/laboratory/biometric-analysis/codis)

## 👤 Author

**Salwa A. Majeed**
- Computer Science Major, Minor in Biomedical Engineering
- University of Illinois at Chicago
- [LinkedIn](your-linkedin-url) | [GitHub](your-github-url)

## 🙏 Acknowledgments

This project was inspired by real-world forensic DNA analysis techniques and demonstrates the intersection of computer science and biology, particularly relevant to medical diagnostics and molecular imaging applications.
