import numpy as np
import matplotlib.pyplot as plt

data = np.array([10,12,23,34,45,56,67,78,89,91])
mean = data.mean()
std = data.std()

plt.figure(figsize=(10,5))

# نقاط البيانات
plt.scatter(range(len(data)), data, color='blue', s=100, label='Data Points')

# خط المتوسط
plt.axhline(mean, color='green', linestyle='--', label=f'Mean = {mean}')

# خطوط الانحراف (positive and negative)
for i, y in enumerate(data):
    plt.plot([i, i], [mean, y], color='gray', linestyle=':', alpha=0.7)
    plt.text(i, (mean+y)/2, f'{y-mean:+}', ha='center', va='center', color='black')
    
plt.fill_between(range(len(data)), mean-std, mean+std, color='red', alpha=0.3, label=f'±1 Std ≈ {std:.2f}')


plt.title("Why We Square Deviations for Variance/Std")
plt.ylabel("Value")
plt.xlabel("Index")
plt.legend()
plt.show()
