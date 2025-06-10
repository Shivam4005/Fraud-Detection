import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Check if file exists
file_path = "Module 5 Datset.csv"
if not os.path.isfile(file_path):
    print(f"❌ ERROR: File '{file_path}' not found.")
    exit()

# Load dataset
df = pd.read_csv(file_path)
df.columns = df.columns.str.strip()  # Strip whitespace
print("📄 Columns in the dataset:", df.columns.tolist())

# Try to detect the fraud column automatically
fraud_col = None
for col in df.columns:
    if 'fraud' in col.lower():
        fraud_col = col
        break

if fraud_col is None:
    print("❌ ERROR: No column related to 'fraud' found.")
    exit()
else:
    print(f"✅ Using '{fraud_col}' as the fraud column.")

# Optional: check if 'amount' column exists
if 'amount' not in df.columns:
    print("❌ ERROR: Column 'amount' not found in dataset.")
    exit()

# 1. Bar Plot
plt.figure(figsize=(6, 4))
sns.countplot(x=fraud_col, data=df, palette='Set2')
plt.title("Fraud vs Non-Fraud Count")
plt.xlabel("Is Fraud")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("fraud_count.png")
plt.show()

# 2. Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="amount", hue=fraud_col, bins=50, kde=True)
plt.title("Transaction Amount Distribution by Fraud Status")
plt.xlabel("Transaction Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("amount_distribution.png")
plt.show()

# 3. Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(x=fraud_col, y="amount", data=df)
plt.title("Boxplot: Amount by Fraud Status")
plt.xlabel("Is Fraud")
plt.ylabel("Amount")
plt.tight_layout()
plt.savefig("amount_boxplot.png")
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# 5. Pie Chart
fraud_counts = df[fraud_col].value_counts()
plt.figure(figsize=(5, 5))
fraud_counts.plot.pie(autopct='%1.1f%%', colors=['skyblue', 'salmon'])
plt.title("Fraud vs Non-Fraud (Pie Chart)")
plt.ylabel("")
plt.tight_layout()
plt.savefig("fraud_piechart.png")
plt.show()
