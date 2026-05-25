import pandas as pd
import matplotlib.pyplot as plt

# أسماء الأعمدة
columns = [
    "Sample Code",
    "Clump Thickness",
    "Cell Size",
    "Cell Shape",
    "Marginal Adhesion",
    "Epithelial Cell Size",
    "Bare Nuclei",
    "Bland Chromatin",
    "Normal Nucleoli",
    "Mitosis",
    "Diagnosis"
]

# قراءة الداتا
df = pd.read_csv("breast-cancer-wisconsin.csv", names=columns)

# عرض أول 5 صفوف
print(df.head())
print(df.info())
# استبدال ? بقيم مفقودة
df.replace("?", pd.NA, inplace=True)
df["Bare Nuclei"] = pd.to_numeric(df["Bare Nuclei"], errors="coerce")
df.dropna(inplace=True)
print(df.info())
df.to_csv("cleaned_breast_cancer.csv", index=False)