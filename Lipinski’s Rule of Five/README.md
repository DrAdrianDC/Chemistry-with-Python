🧪 # Drug-Likeness Predictor Using Lipinski's Rule of Five

🔍 # Project Description

This project provides a simple yet effective way to assess whether a compound is "drug-like" using Lipinski’s Rule of Five, a widely accepted rule of thumb in drug discovery. Given a set of SMILES strings, the script uses RDKit to compute molecular descriptors and determines if each compound satisfies the criteria commonly associated with orally active drugs.

    ✅ # Lipinski’s Rule of Five states that a molecule is more likely to be orally bioavailable if:

      * Molecular weight ≤ 500 Daltons
      * LogP ≤ 5
      * Hydrogen bond donors ≤ 5
      * Hydrogen bond acceptors ≤ 10
