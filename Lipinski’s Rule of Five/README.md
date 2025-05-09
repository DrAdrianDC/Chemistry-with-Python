
# 🧪 Drug-Likeness Predictor Using Lipinski's Rule of Five

This project evaluates chemical compounds for oral drug-likeness based on **Lipinski's Rule of Five** using SMILES input strings and RDKit for molecular descriptor computation.

##    ✅  Lipinski’s Rule of Five states that a molecule is more likely to be orally bioavailable if:

             * Molecular weight ≤ 500 Daltons
             * LogP ≤ 5
             * Hydrogen bond donors ≤ 5
             * Hydrogen bond acceptors ≤ 10


##    📁 File Structure

            Lipinski’s Rule of Five/
                │
                ├── drug_likeness_predictor.py      # Main Python script
                ├── example_smiles.txt              # Example input file with SMILES
                └── README.md                       # Project description and usage

## 🚀 How It Works

- Parses SMILES strings from a text file.
- Computes molecular weight, LogP, hydrogen bond donors (HBD), and acceptors (HBA).
- Applies Lipinski’s rules to each compound.
- Saves the results to `lipinski_results.csv`.


## 📂 Usage

Run the script with a SMILES input file:
```bash
python drug_likeness_predictor.py example_smiles.txt
```

The output will be a CSV file named lipinski_results.csv containing molecular weight, LogP, H-bond donors, H-bond acceptors, and Lipinski rule evaluation.

## 🛠️ Requirements

Install dependencies:

```bash
pip install pandas rdkit-pypi


