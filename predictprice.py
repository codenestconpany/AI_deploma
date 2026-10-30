import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. بيانات تجريبية (المساحة بـ متر مربع، عدد الغرف، السعر)
# [المساحة، عدد الغرف]
X = np.array([
    [120, 2],
    [150, 3],
    [200, 4],
    [80, 1],
    [220, 4],
    [100, 2],
    [180, 3]
])
# السعر (بالآلاف )
y = np.array([150, 200, 280, 100, 300, 130, 250])

# 2. تقسيم البيانات إلى بيانات تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. بناء وتدريب الموديل
model = LinearRegression()
model.fit(X_train, y_train)

# 4. اختبار الموديل وتوقع الأسعار
y_pred = model.predict(X_test)

# 5. حساب الدقة
print("R2 Score (دقة الموديل):", r2_score(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# 6. رسم النتائج بشكل أنيق ومنظم
plt.figure(figsize=(8, 5)) # تحديد حجم نافذة الرسم
plt.scatter(X[:, 0], y, color='blue', s=60, label='البيانات الحقيقية (Actual)') # تكبير النقاط قليلاً
plt.plot(X[:, 0], model.predict(X), color='red', linewidth=2.5, label='خط التوقع (Prediction)') # جعل الخط أكثر وضوحاً

# إضافة العنوان والمسميات مع تنسيقها
plt.title('توقع سعر المنزل بناءً على المساحة', fontsize=14, pad=15)
plt.xlabel('المساحة (متر مربع)', fontsize=12)
plt.ylabel('السعر (بالألف)', fontsize=12)

# إضافة شبكة خلفية لتسهيل قراءة القيم
plt.grid(True, linestyle='--', alpha=0.6)

# إضافة إطار ومفتاح التوضيح
plt.legend(fontsize=11)
plt.tight_layout()

plt.show()