import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_total(alpha_rel, theta_rel, title="Total", smooth=5):
    """Affiche Alpha et Theta avec un léger lissage (look du prof)."""
    # Lissage par moyenne glissante
    a_s = pd.Series(alpha_rel).rolling(window=smooth, center=True, min_periods=1).mean()
    t_s = pd.Series(theta_rel).rolling(window=smooth, center=True, min_periods=1).mean()

    plt.figure(figsize=(6,4))
    plt.plot(a_s, label="Alpha", color="#1f77b4", linewidth=1.8)
    plt.plot(t_s, label="Theta", color="#ff7f0e", linewidth=1.8)
    plt.title(title, fontsize=12)
    plt.xlabel("# of points")
    plt.ylabel("Relative Power")
    plt.ylim(0, 1)
    plt.legend()
    plt.grid(False)
    plt.tight_layout()
    plt.show()
