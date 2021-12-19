# -*- coding: utf-8 -*-
"""Untitled33.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zS47lAZ7jvYGieRw4PU33l9mQdacg65T
"""

# 2021/12/19
# BY 건우

# 아이린 사진 색 바꾸기

# 아이린 사진을 파이썬에서 시각화 하시오 !

from PIL import Image           # 사진을 파이썬으로 불러오기 위한 모듈 임폴트
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("/content/drive/MyDrive/아이린.jpg")    # 사진을 파이썬으로 불러옵니다.
img_pixel = np.array(img)         # 불러온 숫자값을 numpy array 로 변환합니다.
plt.imshow(img_pixel)          # 이미지 시각화
print( img_pixel.shape )        # (500,500,3)
#                    						↑    ↑   ↑
#	                  						가로 세로 색조( R, G, B )



# 아이린 사진에서 red 부분 행렬만 시각화 하시오 !

from PIL import Image           # 사진을 파이썬으로 불러오기 위한 모듈 임폴트
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("/content/drive/MyDrive/아이린.jpg")    # 사진을 파이썬으로 불러옵니다.
img_pixel = np.array(img)         # 불러온 숫자값을 numpy array 로 변환합니다.
img_pixel[ : , : , 1 ] = 0        # green 행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
img_pixel[ : , : , 2 ] = 0         # blue  행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
plt.imshow(img_pixel)          # 이미지 시각화
print( img_pixel.shape )        # (500,500,3)



# 아이린 사진에서 green 부분 행렬만 시각화 하시오 !

from PIL import Image           # 사진을 파이썬으로 불러오기 위한 모듈 임폴트
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("/content/drive/MyDrive/아이린.jpg")    # 사진을 파이썬으로 불러옵니다.
img_pixel = np.array(img)         # 불러온 숫자값을 numpy array 로 변환합니다.
img_pixel[ : , : , 0 ] = 0        # red 행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
img_pixel[ : , : , 2 ] = 0         # blue  행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
plt.imshow(img_pixel)          # 이미지 시각화
print( img_pixel.shape )        # (500,500,3)



# 아이린 사진에서 blue 부분 행렬만 시각화 하시오 !

from PIL import Image           # 사진을 파이썬으로 불러오기 위한 모듈 임폴트
import numpy as np
import matplotlib.pyplot as plt

img = Image.open("/content/drive/MyDrive/아이린.jpg")    # 사진을 파이썬으로 불러옵니다.
img_pixel = np.array(img)         # 불러온 숫자값을 numpy array 로 변환합니다.
img_pixel[ : , : , 0 ] = 0        # red 행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
img_pixel[ : , : , 1 ] = 0         # green  행렬을 전부 0으로 변경 ( 검정색으로 변경해라 )
plt.imshow(img_pixel)          # 이미지 시각화
print( img_pixel.shape )        # (500,500,3)



# 아이린 사진을 흑백사진으로 변경하시오 !

j= '/content/drive/MyDrive/아이린.jpg'

import numpy as np  #  신경망에 사진을 입력할때 숫자행렬로 입력해야하기 때문에 필요
import matplotlib.pyplot as plt # 사진을 파이썬에서 시각화하기 위해 필요
import matplotlib.image as mpimg #  사진을 불러와서 숫자로 변환해주기 위해 필요

def rgb2gray(rgb):  # 흑백으로 색깔을 변경하기 위한 함수 
    return np.dot(rgb[ :, :, : ], [0.299, 0.587, 0.114])
                       
img = mpimg.imread(j)  #  사진을 숫자로 변경 
gray = rgb2gray(img)  # 컬러를 흑백으로 변환 

plt.imshow(gray, cmap = plt.get_cmap('gray'))  # 시각화 합니다. 
plt.show()





