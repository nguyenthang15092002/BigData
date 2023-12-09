import pandas as pd
import numpy as np

df = pd.read_csv('./ex1data1.txt', header=None)

df.head()

# Mô tả thông tin cơ bản của dữ liệu
df.describe()