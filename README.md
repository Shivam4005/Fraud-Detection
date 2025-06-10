# Fraud-Detection
Develop a real-time fraud detection system using machine learning to identify fraudulent credit card transactions with high accuracy and minimal false positives.
# Project Structure
Fraud-Detection/
├── Dashboard/
│ └── app.py
├── data/
│ └── fraud_dataset.csv
├── images/
│ ├── correlation_matrix.png
│ ├── Correlation heatmap.png
│ ├── Income distribution across professions.png
│ ├── Income distribution by fraud status.png
│ └── fraud_vs_nonfraud.png
├── notebooks/
│ ├── Visualizing Fraud Detection.ipynb
│ └── fraud-detection.ipynb
├── presentation/
│ ├── fraud_preprocessing_presentation.pdf
│ └── Visualizing-Fraud-Detection-Insights.pdf
├── README.md
└── requirements.txt 
# Features / Tasks Completed
## Key Tasks Completed

- ✅ To interact with the dashboard you can download the pbix file from the repository and open it in Power BI Desktop locally.
- ✅ Cleaned dataset (removed duplicates, standardized formats)
- ✅ Handled missing values (mean/mode imputation)
- ✅ Performed feature selection using correlation matrix and domain logic
- ✅ Created new features like `transaction_hour`, `is_weekend`
- ✅ Transformed skewed features using log normalization
- ✅ Handled outliers using IQR and Z-score methods
- ✅ Visualized insights using heatmaps, histograms, and boxplots
# Summary Statistics & Visuals
## 📊 Summary Statistics & Visuals

- Class distribution (fraud vs. non-fraud)
- Correlation matrix heatmap
- Boxplots of numerical features
- Distribution plots before/after transformation
- Summary tables with mean, median, std dev
# How to Run the Project
## 🧪 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Shivam4005/Fraud-Detection
   cd fraud-detection-preprocessing
2. required packages:
# Core libraries
pandas==2.2.2
numpy==1.26.4

# Visualization
matplotlib==3.8.4
seaborn==0.13.2

# Machine Learning and preprocessing
scikit-learn==1.4.2

# Jupyter Notebook support
jupyter==1.0.0

# Optional: For progress bars or enhanced terminal outputs
tqdm==4.66.2
3. Launch Jupyter Notebook:
jupyter notebook notebooks/fraud-detection.ipynb
# Fraud Detection - Data Visualization (Review 2)

This repository contains visual analysis of a fraud detection dataset as part of Review 2. The project demonstrates various data visualization techniques using Python libraries like `pandas`, `seaborn`, and `matplotlib`.

---

## 📁 Files Included

- `visualization.ipynb` – Jupyter Notebook containing all visualization code
- `Module 5 Dataset.csv` – Dataset used for analysis
- `fraud_count.png` – Bar chart: Count of fraud vs non-fraud transactions
- `amount_distribution.png` – Histogram: Distribution of transaction amounts
- `amount_boxplot.png` – Boxplot: Amount by fraud status
- `correlation_heatmap.png` – Correlation heatmap for numerical features
- `fraud_piechart.png` – Pie chart showing fraud vs non-fraud percentage

---

## 📊 Visualizations Created

1. **Bar Plot** – Number of fraud and non-fraud cases
2. **Histogram** – Distribution of transaction amounts by fraud status
3. **Box Plot** – Comparison of transaction amount range (fraud vs non-fraud)
4. **Heatmap** – Correlation between numerical columns
5. **Pie Chart** – Percentage of fraud vs non-fraud

---

## 📦 Dependencies

Install required packages:

```bash
pip install pandas seaborn matplotlib




