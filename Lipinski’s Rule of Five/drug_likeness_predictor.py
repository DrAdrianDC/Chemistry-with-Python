

# Lipinski’s Rule of Fives using Python

print("*************************************") 
print("**                                 **") 
print("**                                 **") 
print("**   Lipinski’s Rule of Five       **")
print("**                                 **") 
print("**                                 **") 
print("*************************************") 


from rdkit import Chem
from rdkit.Chem import Descriptors
import pandas as pd

def compute_descriptors(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return {
        'MolWt': Descriptors.MolWt(mol),
        'LogP': Descriptors.MolLogP(mol),
        'HBD': Descriptors.NumHDonors(mol),
        'HBA': Descriptors.NumHAcceptors(mol)
    }

def passes_lipinski(desc):
    return all([
        desc['MolWt'] <= 500,
        desc['LogP'] <= 5,
        desc['HBD'] <= 5,
        desc['HBA'] <= 10
    ])

def analyze_smiles_file(file_path):
    with open(file_path, 'r') as f:
        smiles_list = [line.strip() for line in f if line.strip()]
    
    results = []
    for smiles in smiles_list:
        desc = compute_descriptors(smiles)
        if desc:
            desc['SMILES'] = smiles
            desc['Lipinski_Pass'] = passes_lipinski(desc)
            results.append(desc)
        else:
            results.append({
                'SMILES': smiles,
                'MolWt': None,
                'LogP': None,
                'HBD': None,
                'HBA': None,
                'Lipinski_Pass': 'Invalid SMILES'
            })
    
    df = pd.DataFrame(results)
    df.to_csv('lipinski_results.csv', index=False)
    print("Analysis complete. Results saved to lipinski_results.csv")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python drug_likeness_predictor.py example_smiles.txt")
    else:
        analyze_smiles_file(sys.argv[1])


