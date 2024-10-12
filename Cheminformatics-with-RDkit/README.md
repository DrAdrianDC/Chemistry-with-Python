# Cheminformatics with RDkit


## Overview

Cheminformatics can be thought of as the intersection of data science, computer science, and chemistry as a means of better understanding and solving chemical problems. In this small project we will use a popular and versatile Python library known as RDkit.


# Molecular Analysis with RDKit and SELFIES

The following is a step-by-step workflow for analyzing and comparing molecular structures using cheminformatics tools such as RDKit and SELFIES. The primary focus is on the structural comparison of two gold clusters using Morgan fingerprints and Tanimoto similarity. Additionally, the project demonstrates how to convert SMILES strings into SELFIES and analyze their symbolic representation.

## Features

**Molecular Representation:** Converts SMILES strings into RDKit molecule objects.

**Visualization:** Generates molecular structure images using RDKit.

**Substructure Matching:** Detects specific substructures (e.g., 5-membered rings) within molecules.

**Fingerprint Calculation:** Computes Morgan fingerprints to represent molecular environments.

**Similarity Comparison:** Compares two molecular structures using Tanimoto similarity.

**SMILES to SELFIES:** Converts SMILES strings to SELFIES for a more generalized molecular representation.


## Requierements

**Python 3.8.3**

Ensure that the following Python libraries are installed:

 **RDKit**
 
 **NumPy**
 
 **SELFIES**
 

To install RDKit and SELFIES, run:
```bash
pip install rdkit selfies
```

