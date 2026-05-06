# 🧠 EEG Signal Analysis & Classification

Projet complet d'analyse et classification de signaux EEG (Electroencéphalographie) pour détection d'états mentaux et physiologiques.

## 📋 Vue d'ensemble

Ce projet explore le traitement et l'analyse de signaux EEG, en comparant plusieurs approches de Machine Learning pour classifier différents états mentaux/physiologiques à partir des données brutes d'EEG.

## 🎯 Objectifs

1. **Exploration des Données** 📊
   - Charger et visualiser les données EEG brutes
   - Comprendre la structure et les caractéristiques
   - Analyser la distribution des classes

2. **Prétraitement du Signal** 🔧
   - Filtrage (Butterworth, Chebyshev)
   - Suppression des artefacts (eye movements, muscle)
   - Normalisation et standardisation

3. **Feature Engineering** ⚙️
   - Extraction de la puissance spectrale (PSD)
   - Calcul des bandes de fréquence (Delta, Theta, Alpha, Beta, Gamma)
   - Statistiques temporelles (mean, std, entropy)
   - Wavelet features

4. **Entraînement de Modèles** 🤖
   - Support Vector Machine (SVM)
   - Random Forest
   - Multi-Layer Perceptron (MLP)
   - Comparaison des performances

5. **Visualisation & Reporting** 📈
   - Graphiques de confusion matrix
   - Courbes ROC & AUC
   - Feature importance
   - Comparaisons visuelles des états

## 📁 Structure du Projet

```
projet_eeg_alpha/
├── README.md                          # Ce fichier
├── requirements.txt                   # Dépendances Python
├── doc.txt                           # Documentation techniques
│
├── notebooks/
│   └── 01-Data-Exploration.ipynb     # Exploration interactive des données
│
├── src/
│   ├── __init__.py
│   ├── data_processing.py            # Chargement & prétraitement
│   ├── feature_engineering.py        # Extraction de features
│   ├── model_training.py             # Entraînement des modèles
│   ├── plotting.py                   # Visualisations
│   └── __pycache__/
│
├── data/                             # Données EEG (gitignored)
│   ├── raw/                          # Données brutes
│   └── processed/                    # Données prétraitées
│
└── reports/
    ├── arousal_comparison.png
    ├── des_composite_comparison.png
    ├── funnel_chart_selection.png
    ├── panas_affect_comparison.png
    └── protocol_flowchart.png
```

## 🚀 Installation & Setup

### Prérequis
- Python 3.8+
- pip ou conda
- Jupyter Notebook/Lab (pour les notebooks)

### Installation

```bash
# 1. Cloner le repository
git clone https://github.com/iz235/machine-learning.git
cd machine-learning/Dispo_Medicaux/projet_eeg_alpha

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate      # Linux/Mac
# ou
venv\Scripts\activate         # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer Jupyter Lab
jupyter lab notebooks/
```

## 📦 Dépendances

```
numpy              # Calculs numériques
pandas             # Manipulation de données
scipy              # Traitement du signal
scikit-learn       # Machine Learning
matplotlib         # Visualisation statique
seaborn           # Visualisation statistique
jupyterlab        # Environnement interactif
```

## 💻 Utilisation

### 1. Exploration des Données
```python
from src.data_processing import load_eeg_data, preprocess_signal

# Charger les données
X, y = load_eeg_data('data/raw/')

# Prétraiter
X_clean = preprocess_signal(X, sampling_rate=250)
```

### 2. Feature Engineering
```python
from src.feature_engineering import extract_spectral_features

# Extraire les features spectrales
features = extract_spectral_features(X_clean, fs=250)
```

### 3. Entraînement
```python
from src.model_training import train_models

# Entraîner les modèles
results = train_models(features, y)
```

### 4. Visualisation
```python
from src.plotting import plot_confusion_matrix, plot_roc

# Générer les graphiques
plot_confusion_matrix(results['predictions'], y)
plot_roc(results['probabilities'], y)
```

## 📊 Résultats Attendus

### Performances des Modèles (État de base)
| Modèle | Accuracy | Precision | Recall | F1-Score |
|--------|----------|-----------|--------|----------|
| SVM    | 78%      | 0.78      | 0.77   | 0.77     |
| Random Forest | 82% | 0.82   | 0.81   | 0.81     |
| MLP    | 84%      | 0.85      | 0.84   | 0.84     |

### Visualisations Générées
- **Confusion Matrix:** Matrice de confusion pour chaque modèle
- **ROC Curves:** Courbes ROC avec AUC scores
- **Feature Importance:** Importance relative des features
- **Signal Samples:** Représentation temporelle et spectrale

## 🔍 Détails Techniques

### Bandes de Fréquence EEG
- **Delta (0.5-4 Hz):** Sommeil profond, inconscience
- **Theta (4-8 Hz):** Méditation, relaxation
- **Alpha (8-12 Hz):** État de veille relaxé
- **Beta (12-30 Hz):** Activité mentale, concentration
- **Gamma (30-100 Hz):** Traitement cognitif haut niveau

### Filtres Utilisés
- **Butterworth (ordre 4):** Lissage général
- **Chebyshev:** Atténuation d'ondulation minimale
- **Notch (50/60 Hz):** Suppression du bruit électrique

### Métriques de Classement
- **PSD (Power Spectral Density):** Via FFT et Welch
- **Entropy:** Shannon entropy des signaux
- **Band Power:** Puissance par bande de fréquence
- **Connectivity:** Corrélation inter-électrodes

## 📝 Fichiers Importants

- `notebooks/01-Data-Exploration.ipynb` - Point de départ recommandé
- `src/data_processing.py` - Cœur du prétraitement
- `src/feature_engineering.py` - Pipeline de features
- `reports/` - Visualisations générées

## 🐛 Troubleshooting

### Problème: "No module named 'scipy'"
```bash
pip install scipy --upgrade
```

### Problème: Les données ne chargeant pas
- Vérifier que le chemin dans `load_eeg_data()` est correct
- Vérifier le format des fichiers (CSV, HDF5, etc.)

### Problème: Mémoire insuffisante
- Réduire la fréquence d'échantillonnage
- Traiter par chunks (voir `data_processing.py`)

## 🔮 Améliorations Futures

- [ ] Intégration de modèles Deep Learning (CNN 1D, LSTM)
- [ ] Analyse multi-canal (10-20 system visualization)
- [ ] Real-time processing capability
- [ ] Artifact removal avec ICA (Independent Component Analysis)
- [ ] Transfer learning avec modèles pré-entrainés
- [ ] API REST pour inférence en temps réel

## 📚 Ressources

- [MNE-Python Documentation](https://mne.tools/)
- [SciPy Signal Processing](https://docs.scipy.org/doc/scipy/reference/signal.html)
- [EEG Signal Processing Guide](https://eeglab.org/tutorials/)
- [Scikit-learn Classification](https://scikit-learn.org/stable/modules/classification.html)

## 👤 Auteur
**Izadine** - Data Scientist & ML Engineer  
Email: massarizzadinealkhali@gmail.com  
GitHub: [@iz235](https://github.com/iz235)

## 📄 Licence
MIT License - Libre d'utilisation

## 🤝 Contribution
Contributions bienvenues! Pour contribuer:
1. Fork le repository
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

---
**État du Projet:** 🟡 En développement  
**Dernière Mise à Jour:** Mai 2026  
**Maintenance:** Active
