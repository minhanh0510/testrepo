#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data = pd.read_csv('diem_thi_thpt_2022.csv')

print("a) Hiển thị 10 dòng đầu tiên và 10 dòng cuối cùng của bảng dữ liệu")
print("10 dòng đầu tiên của bảng dữ liệu:")
print(data.head(10))
print("10 dòng cuối cùng của bảng dữ liệu:")
print(data.tail(10))

print("b) Cho biết bảng dữ liệu có bao nhiêu dòng và bao nhiêu cột?")
num_rows, num_cols = data.shape
print(f"Bảng dữ liệu có {num_rows} dòng và {num_cols} cột.")

print("c) Cho biết thông tin về các cột dữ liệu và kiểu của từng cột trong bảng")
#print("Thông tin về các cột dữ liệu và kiểu của từng cột trong bảng:")
print(data.dtypes)

print("d) Cho biết số học sinh bị thiếu điểm môn Ngữ Văn và môn Ngoại Ngữ")
num_missing_ngu_van = data['ngu_van'].isna().sum()
num_missing_ngoai_ngu = data['ngoai_ngu'].isna().sum()
print(f"Số học sinh bị thiếu điểm môn Ngữ Văn là {num_missing_ngu_van}.")
print(f"Số học sinh bị thiếu điểm môn Ngoại Ngữ là {num_missing_ngoai_ngu}.")


# In[22]:


print("Câu 2: Tính trung bình, độ lệch chuẩn và khoảng dữ liệu của cột điểm thi môn Toán")

mean = data['toan'].mean()
std = data['toan'].std()
rng = data['toan'].max() - data['toan'].min()

print("a) Tính trung bình")
print(f"Trung bình: {mean:.2f}")

print("b) Tính độ lệch chuẩn")
print(f"Độ lệch chuẩn: {std:.2f}")

print("c) khoảng dữ liệu")
print(f"Khoảng dữ liệu: {rng:.2f}")


# In[10]:


import matplotlib.pyplot as plt
print("Câu 3")

print("a) Đếm số lượng học sinh thi khối KHTN và thi khối KHXH")
counts = data['Khoi'].value_counts()
num_khtn = counts['KHTN']
num_kxh = counts['KHXH']
print(f"Số lượng học sinh thi khối KHTN là {num_khtn}.")
print(f"Số lượng học sinh thi khối KHXH là {num_kxh}.")

print("b) Vẽ đồ thị Pie để so sánh mối tương quan giữa 'KHTN' và 'KHXH' ")
labels = ['KHTN', 'KHXH']
sizes = [num_khtn, num_kxh]
colors = ['yellowgreen', 'gold']
plt.pie(sizes, labels=labels, colors=colors, autopct='%.1f%%', startangle=90)
plt.axis('equal')
plt.show()


# In[23]:


print("Câu 4")

print("a) Liệt kê 20 học sinh có điểm Toán cao nhất")
top_20_toan = data.nlargest(20, 'toan')
print("20 học sinh có điểm Toán cao nhất:")
print(top_20_toan[['sbd', 'toan']])

print("b) Liệt kê 20 học sinh có điểm Toán thấp nhất")
bottom_20_toan = data.nsmallest(20, 'toan')
print("20 học sinh có điểm Toán thấp nhất:")
print(bottom_20_toan[['sbd', 'toan']])

print("c) Cho biết có bao nhiêu điểm 10 môn Toán") 
num_10_toan = (data['toan'] == 10).sum()
print(f"Số điểm 10 môn Toán là {num_10_toan}.")


# In[27]:


import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('diem_thi_thpt_2022.csv')

print("Câu 5")
print("số học sinh của 3 thành phố")
counts = data['tentinh'].value_counts()
num_HN = counts['thành phố hà nội']
print(f"Số lượng học sinh của Hà Nội là {num_HN}.")

counts = data['tentinh'].value_counts()
num_HCM = counts['thành phố hồ chí minh']
print(f"Số lượng học sinh của tp HCM là {num_HCM}.")

counts = data['tentinh'].value_counts()
num_DN = counts['thành phố đà nẵng']
print(f"Số lượng học sinh của Đà Nẵng là {num_DN}.")


print("Biểu đồ Bar thống kê số học sinh theo vùng")
data = {'Vùng': ['thành phố hà nội', 'thành phố hồ chí minh', 'thành phố đà nẵng'],
        'Số học sinh': [num_HN, num_HCM, num_DN]}

df = pd.DataFrame(data)

plt.bar(df['Vùng'], df['Số học sinh'])
plt.xlabel('Vùng')
plt.ylabel('Số học sinh')
plt.title('Biểu đồ Bar thống kê số học sinh theo vùng')
plt.show()


# In[ ]:




