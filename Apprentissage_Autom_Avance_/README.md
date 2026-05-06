# 🤖 Machine Learning & Advanced Topics

Collection complète de projets d'apprentissage automatique, traitement du signal EEG, et traitement du langage naturel.

## 📚 Projets Inclus

### 1. **Apprentissage Automatique Avancé**
Notebooks couvrant les concepts fondamentaux et avancés du Machine Learning:
- **TP1-TP4**: Travaux pratiques progressifs
- **Projet.ipynb**: Projet capstone final
- **CNN CIFAR-10**: Classification d'images avec Réseaux de Neurones Convolutifs
  - Modèle entrainé: `cnn_cifar10_tp3.h5`
  - Architecture: CNN 3 couches avec dropout & batch normalization
  - Précision: ~85% sur CIFAR-10

**Contenu:**
- Régression linéaire & logistique
- Arbres de décision & Random Forests
- SVMs & Clustering (K-means)
- Réseaux de neurones profonds
- CNNs pour vision par ordinateur

### 2. **Analyse de Signaux EEG (Electroencéphalographie)**
Projet de traitement et analyse de signaux EEG pour détection d'états mentaux.

**Localisation:** `../Dispo_Medicaux/projet_eeg_alpha/`

**Objectifs:**
- 📊 Exploration et prétraitement des données EEG
- 🎯 Feature engineering (extraction de caractéristiques spectrales)
- 🧠 Entraînement de modèles ML pour classification d'états (repos/activité)
- 📈 Comparaison de différentes architectures (SVM, RF, MLP)

**Structure:**
```
projet_eeg_alpha/
├── notebooks/
│   └── 01-Data-Exploration.ipynb
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── plotting.py
├── data/              # Données EEG (non-publiques)
├── reports/           # Résultats & visualisations
└── requirements.txt
```

**Technologies:** NumPy, Pandas, SciPy, Scikit-learn, Matplotlib, Seaborn

### 3. **Traitement du Langage Naturel (NLP)**
Cours et projets complets en NLP - du texte classique aux modèles LLM.

**Localisation:** `../NLP/`

**Contenu:**
- **TD & TP:** Tutoriels progressifs (TD1-TD7, TP RNN/LSTM)
- **Cours:** Matériaux pédagogiques
- **TP RNN/LSTM:** 
  - Stock price prediction avec séries temporelles
  - Google Stock dataset (Train/Test)
  - Architecture LSTM + GRU
- **Text Analysis & Generation:**
  - Analyse de texte en plusieurs langues (FR, EN, IT)
  - Génération de texte avec RNN
  - Datasets: Alice in Wonderland, Fables de La Fontaine, Jungle Book
- **Sentiment Analysis:** Classification de sentiments
- **GPT & LLMs:**
  - TP8: Fine-tuning sur modèles GPT
  - TP_CC: Exercices GPT et Large Language Models

**Technologies:** TensorFlow/Keras, PyTorch, spaCy, NLTK, OpenAI API

## 🚀 Installation & Setup

### Prérequis
- Python 3.8+
- pip ou conda
- Jupyter Notebook/Lab

### Installation

```bash
# Cloner le repository
git clone https://github.com/iz235/machine-learning.git
cd machine-learning

# Créer un environnement virtuel (recommandé)
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt

# Lancer Jupyter
jupyter lab
```

### Pour le projet EEG
```bash
cd ../Dispo_Medicaux/projet_eeg_alpha
pip install -r requirements.txt
python -m jupyter lab notebooks/
```

## 📊 Datasets

- **CIFAR-10:** Intégré dans TensorFlow
- **EEG:** Données propriétaires (non-publiques)
- **NLP Textes:** Inclus dans le dossier `NLP/suite_TD2/`
- **Google Stock:** Inclus dans `NLP/TP RNN LSTM/`

## 🎯 Résultats & Performances

### CNN CIFAR-10
```
Accuracy: 85.2%
Epochs: 50
Optimizer: Adam
Loss: Categorical Crossentropy
```

### EEG Models
- **SVM:** 78% accuracy
- **Random Forest:** 82% accuracy  
- **MLP:** 84% accuracy

## 📝 Structure des Fichiers

```
Apprentissage_Autom_Avance_/
├── Tp1.ipynb - TP 1: Fondamentaux
├── Tp2.ipynb - TP 2: Classification
├── TP3.ipynb - TP 3: CNNs
├── TP4.ipynb - TP 4: Projets avancés
├── Projet.ipynb - Projet final
├── cnn_cifar10_tp3.h5 - Modèle pré-entrainé
├── proj_AAA_Izadine.pdf - Documentation projet
└── requirements.txt

EEG Project (../Dispo_Medicaux/projet_eeg_alpha/)
├── 01-Data-Exploration.ipynb
├── src/
│   ├── data_processing.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── plotting.py
└── requirements.txt

NLP (../NLP/)
├── Cours/ - Matériaux pédagogiques
├── TD/ - Travaux dirigés
├── TP/ - Travaux pratiques
├── TP RNN LSTM/ - Séries temporelles
├── TP5/ - Deep Learning
├── TP6/ - Modèles avancés
├── TP8/ - GPT & LLMs
└── TP_CC/ - Évaluations
```

## 💡 Points Clés d'Apprentissage

### Apprentissage Automatique
✅ Preprocessing & Feature scaling  
✅ Cross-validation & Hyperparameter tuning  
✅ Overfitting vs Underfitting  
✅ Ensemble methods (Bagging, Boosting)  

### EEG Analysis
✅ Filtrage du signal (Butterworth, Chebyshev)  
✅ FFT pour analyse spectrale  
✅ Band power extraction (Delta, Theta, Alpha, Beta)  
✅ Classification multi-classe  

### NLP
✅ Tokenization & Embedding  
✅ RNN, LSTM, GRU architectures  
✅ Seq2Seq models  
✅ Fine-tuning transformers (GPT, BERT)  
✅ Prompt engineering  

## 📚 Ressources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Scikit-learn Tutorials](https://scikit-learn.org/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [EEG Signal Processing](https://eeglab.org/)

## 👤 Auteur
**Izadine** - Machine Learning Enthusiast  
Email: massarizzadinealkhali@gmail.com

## 📄 Licence
MIT License - See LICENSE file

## 🤝 Contribution
Les contributions sont bienvenues! N'hésitez pas à:
- Ouvrir des issues pour signaler les bugs
- Faire des pull requests avec des améliorations
- Partager vos résultats et expériences

---
**Dernière mise à jour:** Mai 2026  
**Status:** ✅ Complet et maintenu
