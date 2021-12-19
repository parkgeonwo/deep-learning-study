# -*- coding: utf-8 -*-
"""Untitled32.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TjA89xdp_Sj7jRZs-Q6-RUrGNcFEByJ3
"""

# 2021/12/19
# BY 건우



# 100개의 필기체 데이터를 3층 신경망에 넣고 정확도를 확인하시오 !


# 0. 필요한 함수 불러옵니다.

def sigmoid(x):
    return 1 / (1+np.exp(-x) )

def softmax(a):
    C = np.max(a)
    minus = a - C
    exp_a = np.exp(minus)                # 분자
    sum_exp_a = np.sum(exp_a)         # 분모
    y = exp_a / sum_exp_a
    return y

# 1. 신경망이 필요한 가중치와 바이어스를 가져옵니다.

import pickle

def init_network():
    with open("sample_weight.pkl", "rb") as f:
        network = pickle.load(f)
    return network

network = init_network()
w1, w2, w3 = network['W1'], network['W2'], network['W3']
b1, b2, b3 = network['b1'], network['b2'] , network['b3']

# 2. mnist 데이터를 불러옵니다.

from dataset.mnist import load_mnist
( x_train, t_train ) , ( x_test, t_test ) = load_mnist( flatten = True, normalize = True )

# 3. 신경망을 구성합니다.

# 0층 (입력층)
x = x_train[0:100]          # 일단 100개의 필기체 데이터를 가져옵니다.

# 1층 (은닉층)

y = np.dot(x,w1) + b1
y_hat = sigmoid(y)
# print(y_hat)

# 2층 (은닉층)

z = np.dot(y_hat,w2) + b2
z_hat = sigmoid(z)
# print(z_hat)
# print(z_hat.shape)

# 3층 (출력층)

k = np.dot(z_hat,w3) + b3
k_hat = softmax(k)
# print(k_hat)
# print(k_hat.shape)


# 예측값 /정답 출력
a = np.argmax(k_hat, axis=1)         # 예측값

b = t_train[0:100]             # 정답 100개

print( sum(a==b) )        # 96

