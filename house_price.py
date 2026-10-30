
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

# 1. بيانات المنازل: المساحة، الموقع، عدد الغرف
X = np.array([
    [50, 1, 2],
    [70, 2, 3],
    [90, 3, 3],
    [100, 2, 4],
    [120, 3, 4],
    [60, 1, 2],
    [80, 2, 3],
    [150, 3, 5],
    [110, 2, 3],
    [130, 3, 4],
    [75, 1, 3],
    [95, 2, 3],
    [140, 3, 5],
    [85, 1, 3],
    [105, 2, 4],
    [160, 3, 5]
])

# 2. أسعار المنازل الحقيقية (بالدولار)
y = np.array([
    55000, 85000, 120000, 105000,
    140000, 58000, 88000, 175000,
    108000, 150000, 73000, 100000,
    165000, 80000, 115000, 190000
])

# 3. تقسيم البيانات إلى تدريب واختبار
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# 4. إنشاء المودل وتدريبه
model = LinearRegression()
model.fit(X_train, y_train)

# 5. اختبار المودل
y_pred = model.predict(X_test)

# 6. حساب مقاييس الأداء
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("real prices:", y_test)
print("Expected prices:", np.round(y_pred, 2))
print("Average error in dollars :", round(mae, 2))
print("R2 Selection Coefficient:", round(r2, 3))

# 7. توقع سعر منزل جديد
new_house = np.array([[100, 2, 3]])
price = model.predict(new_house)

print("The expected new home price :", round(price[0], 2), "$")

# 8. رسم الأسعار الحقيقية والمتوقعة
plt.plot(y_test, marker="o", label="Actual Prices")
plt.plot(y_pred, marker="x", label="Predicted Prices")
plt.xlabel("Test House")
plt.ylabel("Price in Dollars")
plt.title("Actual vs Predicted House Prices")
plt.legend()
plt.show()
