

## Drug Toxicity Prediction using Neural Networks and RDKit


 ![red text](https://img.shields.io/badge/WIP-red)

### Overview

The main goal of the present work is to present a pathway for implementing a neural network model for toxicity prediction.

This project predicts **molecular toxicity** from **SMILES** strings using **RDKit** to generate molecular fingerprints and a **deep neural network** built with TensorFlow/Keras.

---

### Features
- Converts SMILES strings to Morgan fingerprints (ECFP).
- Trains a feed-forward neural network for toxicity prediction.
- Saves the trained model, scaler, and performance plots.
- Provides a **Streamlit web app** for real-time molecular toxicity predictions.

---

### Project Structure

``` bash
drug-toxicity-prediction/
├── data/
│   └── dataset.csv
├── results/          # Will contain model, scaler, plots after training
├── toxicity_model.py
├── app.py
├── README.md
└── requirements.txt

```
