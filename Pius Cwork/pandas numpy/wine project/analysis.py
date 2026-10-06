from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

data_path = Path(__file__).parent / "wine project" / "wine_quality_final.csv"
data = pd.read_csv(data_path)

plt.hist(data["alcohol"], bins=20, edgecolor="black")
plt.title("Distribution of Alcohol Content in Wine")
plt.xlabel("Alcohol (%)")
plt.ylabel("Number of wines")
plt.tight_layout()

plt.savefig(Path(__file__).parent / "wine_alcohol_histogram.png")
plt.show()