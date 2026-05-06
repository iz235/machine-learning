# src/feature_engineering.py
import numpy as np
import pandas as pd
from scipy.signal import welch
from pathlib import Path
from .data_processing import FS, POSTERIOR_MAP

def welch_psd(seg: np.ndarray, fs: int = FS):
    """Welch par segment (250xNch) -> (f, Pxx[Nf x Nch])."""
    f, Pxx = welch(seg, fs=fs, nperseg=fs, axis=0)
    return f, Pxx

def band_power(psd: np.ndarray, freqs: np.ndarray, fmin: float, fmax: float):
    idx = (freqs >= fmin) & (freqs < fmax)
    return np.trapz(psd[:, idx, :], freqs[idx], axis=1)  # (n_seg, n_ch)

def rel_band_powers(segments: np.ndarray):
    """Renvoie dict {alpha_rel, theta_rel} moyens sur O1/O2/P3/P4."""
    freqs = None; stack = []
    for seg in segments:
        f, Pxx = welch_psd(seg)
        if freqs is None: freqs = f
        stack.append(Pxx)
    psd = np.stack(stack, axis=0)  # (n_seg, Nf, Nch)

    theta = band_power(psd, freqs, 4.0, 8.0)
    alpha = band_power(psd, freqs, 8.0, 12.0)
    total = band_power(psd, freqs, 4.0, 60.0)
    rel_theta = theta / np.maximum(total, 1e-12)
    rel_alpha = alpha / np.maximum(total, 1e-12)
    # moyenne sur canaux postérieurs (indices à fournir à l'appel)
    return freqs, rel_alpha, rel_theta

def make_labels_L300() -> np.ndarray:
    """Labels sur 300 s (0=open, 1=closed) selon l’organisation de l’acquisition.
    0–30 s: préparation (open) -> on peut l’ignorer plus tard.
    Puis alternance toutes les 30 s. (cf. Organisation_acquisition.txt)
    """
    y = np.zeros(300, dtype=int)
    for s, e, lab in [(30,60,1),(60,90,0),(90,120,1),(120,150,0),
                      (150,180,1),(180,210,0),(210,240,1),(240,270,0),(270,300,0)]:
        y[s:e] = lab
    return y
