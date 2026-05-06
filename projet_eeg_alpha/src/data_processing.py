# src/data_processing.py
from pathlib import Path
import re
import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, iirnotch

FS = 250  # OpenBCI Cyton (et consigne: 250 pts = 1 s)

POSTERIOR_MAP = {  # mapping électrodes (cf. Organisation_acquisition.txt)
    "EXG Channel 0": "O1",  # channel1
    "EXG Channel 1": "O2",  # channel2
    "EXG Channel 3": "P4",  # channel4
    "EXG Channel 4": "P3",  # channel5
}

def read_openbci_csv(path: Path) -> pd.DataFrame:
    """Lit un CSV OpenBCI et renvoie uniquement les colonnes EEG (8 canaux EXG)."""
    # trouver la ligne d'en-tête contenant "EXG Channel"
    header_idx = 0
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for i, line in enumerate(f):
            if "EXG Channel" in line or "Sample Index" in line:
                header_idx = i
                break

    df = pd.read_csv(path, skiprows=header_idx, engine="python")

    # --- Nettoyage des noms de colonnes ---
    df.columns = [c.strip() for c in df.columns]

    # --- Sélection robuste des canaux EEG ---
    exg_cols = [c for c in df.columns if "EXG" in c and "Channel" in c]
    if not exg_cols:
        # Essayer d'autres formats (par ex. "Channel 1", "ch1", etc.)
        exg_cols = [c for c in df.columns if c.lower().startswith(("channel", "ch"))]
    if not exg_cols:
        # En dernier recours, garder les 8 premières colonnes numériques après l'index
        num_cols = [c for c in df.columns if df[c].dtype in [float, int]]
        exg_cols = num_cols[:8]
    if not exg_cols:
        raise KeyError(
            f"Aucune colonne EEG trouvée dans {path.name}. Colonnes disponibles: {df.columns[:15].tolist()}"
        )

    out = df[exg_cols].copy()
    out.columns = [c.strip() for c in out.columns]
    return out.astype(float)


def bandpass_notch(x: np.ndarray, fs: int = FS,
                   low=4.0, high=60.0, notch=50.0, q=30.0) -> np.ndarray:
    """Filtre passe-bande 4–60 Hz + notch 50 Hz (filtrage zéro-phase)."""
    b, a = butter(4, [low/(fs/2), high/(fs/2)], btype="band")
    y = filtfilt(b, a, x, axis=0)
    b2, a2 = iirnotch(notch/(fs/2), q)
    y = filtfilt(b2, a2, y, axis=0)
    return y

def segment_seconds(x: np.ndarray, fs: int = FS) -> np.ndarray:
    """Découpe en segments de 1 s (250 points). Renvoie (n_seg, 250, n_ch)."""
    n = (len(x) // fs) * fs
    return x[:n].reshape(-1, fs, x.shape[1])
