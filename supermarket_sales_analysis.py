
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# إنشاء مجلد لحفظ النتائج
output_dir = "outputs"
os.makedirs(output_dir, exist_ok=True)

# تحميل البيانات من ملف محلي
df = pd.read_csv("supermarket_sales.csv")

# تنظيف الأعمدة
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df['date'] = pd.to_datetime(df['date'])
df['total'] = df['total'].astype(float)

# تحليل الأداء حسب نوع المنتج
product_perf = df.groupby('product_line')['total'].sum().sort_values(ascending=False)

# تحليل الاتجاهات الزمنية
daily_sales = df.groupby('date')['total'].sum()

# تحليل حسب نوع العميل
customer_sales = df.groupby('customer_type')['total'].sum()

# رسم أداء المنتجات
plt.figure(figsize=(10,6))
sns.barplot(x=product_perf.values, y=product_perf.index, palette="viridis")
plt.title("Total Sales by Product Line")
plt.xlabel("Total Sales")
plt.ylabel("Product Line")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "product_performance.png"))
plt.close()

# رسم الاتجاهات الزمنية
plt.figure(figsize=(12,6))
sns.lineplot(x=daily_sales.index, y=daily_sales.values)
plt.title("Daily Sales Trend")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "sales_trend.png"))
plt.close()

# رسم خريطة حرارية للعلاقات
plt.figure(figsize=(10,6))
corr = df.select_dtypes(include='number').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "correlation_heatmap.png"))
plt.close()

# حفظ البيانات النظيفة
df.to_csv(os.path.join(output_dir, "cleaned_supermarket_sales.csv"), index=False)

print("✅ التحليل والرسم تم بنجاح. النتائج محفوظة في مجلد 'outputs'")
