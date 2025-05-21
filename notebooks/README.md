## Task 3: Cross-Country Comparison - Documentation

## Objective

Compare solar potential across Benin, Sierra Leone, and Togo using cleaned datasets to identify optimal regions for solar energy deployment.

## Methodology

1. Data Loading

### 2. Summary Statistics Table

### 3. Statistical Testing

- **Test**: Kruskal–Wallis H-test (non-parametric ANOVA)
- **Purpose**: Test whether median GHI values significantly differ between the three countries.

# Key Observations

- Togo shows the **highest average GHI**, suggesting greater solar potential.
- Sierra Leone has the **lowest median DNI**, likely due to more frequent cloud cover.
- Benin displays **higher variability in DHI**, possibly due to local weather fluctuations.

## Folder Structure

├── data/
│ ├── benin_clean.csv
│ ├── sierra_leone_clean.csv
│ └── togo_clean.csv
├── notebooks/
│ └── compare_countries.ipynb
└── dashboard_screenshots/
└── ghi_bar_chart.png

# 📁 Output Files

- Notebook: `notebooks/compare_countries.ipynb`
- Cleaned Data Files: Located in `data/` folder (ignored in Git).
- Charts: All plots are embedded in the notebook.
- Screenshot: Added under `dashboard_screenshots/`

## Key Performance Indicators (KPIs)

| KPI                                     | Status    |
| --------------------------------------- | --------- |
| Inclusion of all countries in each plot | Completed |
| Summary statistics (mean, median, SD)   | Completed |
| Statistical test on GHI (p-value noted) | Completed |
| Key observations in markdown            | Completed |
| Bonus visual summary (bar chart)        | Completed |

## 🧠 Insights & Next Steps

- These insights help identify **priority countries for solar project investments**.
- Can be expanded by integrating location-based analysis or including seasonal trends.

## 🧪 Requirements

- Python 3.9+
- pandas, seaborn, matplotlib, scipy

pip install pandas matplotlib seaborn scipy
