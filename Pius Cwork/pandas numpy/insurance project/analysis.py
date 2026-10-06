from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

project_dir = Path(__file__).parent
data = pd.read_csv(project_dir / "insurance.csv")

for smoker_status, group in data.groupby("smoker"):
    plt.scatter(
        group["age"],
        group["charges"],
        label=f"Smoker: {smoker_status}",
        alpha=0.6,
    )

plt.title("Insurance Charges by Age")
plt.xlabel("Age (years)")
plt.ylabel("Insurance charges")
plt.legend()
plt.tight_layout()
plt.savefig(project_dir / "insurance_charges_by_age.png", dpi=150)
plt.show()