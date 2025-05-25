# Fraud-Detection
Develop a real-time fraud detection system using machine learning to identify fraudulent credit card transactions with high accuracy and minimal false positives.
# Project Structure
fraud-detection-preprocessing/  
├── data/  
│   └── fraud_dataset.csv  
├── notebooks/  
│   └── preprocessing_and_visualization.ipynb  
├── presentation/  
│   └── fraud_preprocessing_presentation.pdf  
├── README.md  
└── requirements.txt  
# Features / Tasks Completed
## Key Tasks Completed

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



