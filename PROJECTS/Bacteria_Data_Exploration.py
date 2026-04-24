# ============================================================
# Bacteria Data Exploration — Pandas Task
# Name:        Team Phenylalanin
# Affiliation: Nigerian institute of Medical Research
# Fav gene:    pfcrt  (Key marker for chloroquine resistance)
# Organism:    Plasmodium falciparum
# ============================================================

import pandas as pd
import numpy as np

# -- Identity print (rubric requirement) --
print("Name:        Team Phenylalanin")
print("Affiliation: Nigerian institute of Medical Research")
print("Fav gene:    pfcrt")
print("Organism:    Plasmodium falciparum")
print()

# -- Synthetic bacteria dataset --
np.random.seed(42)
n = 50

bacteria_data = pd.DataFrame({
    'species':          np.random.choice(
                            ['E. coli', 'S. aureus', 'P. aeruginosa',
                             'K. pneumoniae', 'A. baumannii'], n),
    'Isolation Origin': np.random.choice(
                            ['Blood', 'Urine', 'Wound', 'Sputum', 'CSF'], n),
    'Phenotype':        np.random.choice(
                            ['Resistant', 'Susceptible', 'Intermediate'], n),
    'label':            np.random.choice(['GroupA', 'GroupB', 'GroupC'], n),
    'cipro_fit':        np.random.uniform(0, 1, n),
    'carb_fit':         np.random.uniform(0, 1, n),
    'BSL':              np.random.randint(1, 4, n),
    'C1':               np.random.randn(n),
    'C2':               np.random.randn(n),
})

# ============================================================
# PART 1: Basic Data Inspection
# ============================================================
print("=" * 60)
print("PART 1: Basic Data Inspection")
print("=" * 60)

print(f"Shape: {bacteria_data.shape}")
print(f"Columns: {bacteria_data.columns.tolist()}")

# ============================================================
# PART 2: Data Selection
# ============================================================
print("\n" + "=" * 60)
print("PART 2: Data Selection")
print("=" * 60)

print("\nRow 15 (using .iloc):")
print(bacteria_data.iloc[15])

print("\nColumn 'species':")
print(bacteria_data['species'])

print("\nValue at row 15, column 'Isolation Origin':")
print(bacteria_data.iloc[15]['Isolation Origin'])

# ============================================================
# PART 3: Data Filtering
# ============================================================
print("\n" + "=" * 60)
print("PART 3: Filter — carb_fit > 0.5")
print("=" * 60)

filtered = bacteria_data[bacteria_data['carb_fit'] > 0.5]
print(f"Rows with carb_fit > 0.5: {len(filtered)}")
print(filtered)

# ============================================================
# PART 4: Handling Missing Data
# ============================================================
print("\n" + "=" * 60)
print("PART 4: Handling Missing Data")
print("=" * 60)

# Create a copy and introduce missing values
bacteria_data_missing = bacteria_data.copy()
idx  = np.random.choice(bacteria_data_missing.index, 10, replace=False)
cols = np.random.choice(['cipro_fit', 'carb_fit', 'BSL'], 10)
for i, c in zip(idx, cols):
    bacteria_data_missing.at[i, c] = np.nan

# 1. Count missing values per row
print("\nMissing values per row:")
missing_per_row = bacteria_data_missing.isnull().sum(axis=1)
print(missing_per_row[missing_per_row > 0])

# 2. Fill missing values with 1 — store in new variable
filled_with_1 = bacteria_data_missing.fillna(1)
print(f"\nfilled_with_1 — missing values remaining: "
      f"{filled_with_1.isnull().sum().sum()}")
print(filled_with_1)

# 3. Drop columns that contain missing values — store in new variable
dropped_cols = bacteria_data_missing.dropna(axis=1)
print(f"\ndropped_cols — columns remaining: {dropped_cols.columns.tolist()}")
print(dropped_cols)

# bacteria_data_missing is NOT overwritten:
print(f"\nbacteria_data_missing still has "
      f"{bacteria_data_missing.isnull().sum().sum()} missing values (unchanged).")

# ============================================================
# PART 5: Checking Missing Data in Main Dataset
# ============================================================
print("\n" + "=" * 60)
print("PART 5: Missing Values in bacteria_data (original)")
print("=" * 60)

total_missing = bacteria_data.isnull().sum().sum()
print(f"Total missing values: {total_missing}")
if total_missing > 0:
    print("Missing values per column:")
    print(bacteria_data.isnull().sum())
else:
    print("No missing values found in bacteria_data.")

# ============================================================
# PART 6: Column Renaming
# ============================================================
print("\n" + "=" * 60)
print("PART 6: Column Renaming")
print("=" * 60)

bacteria_data.rename(columns={'C1': 'UMAP1', 'C2': 'UMAP2'}, inplace=True)
print(f"Columns after rename: {bacteria_data.columns.tolist()}")

# ============================================================
# PART 7: Sorting
# ============================================================
print("\n" + "=" * 60)
print("PART 7: Sort by BSL (descending)")
print("=" * 60)

sorted_df = bacteria_data.sort_values(by='BSL', ascending=False)
print(sorted_df[['species', 'BSL']])

# ============================================================
# PART 8: Grouped Analysis
# ============================================================
print("\n" + "=" * 60)
print("PART 8: Grouped Analysis")
print("=" * 60)

print("\nMean of cipro_fit and carb_fit grouped by label:")
print(bacteria_data.groupby('label')[['cipro_fit', 'carb_fit']].mean())

print("\nMaximum of cipro_fit and carb_fit grouped by label:")
print(bacteria_data.groupby('label')[['cipro_fit', 'carb_fit']].max())

print("\nRow count by Phenotype:")
print(bacteria_data['Phenotype'].value_counts())
