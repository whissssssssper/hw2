# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hjw2DdWZDVKxSHQszsNl2j96K6RvVR4B
"""

def check_even():
    while True:
        try:
            # 讓使用者輸入一個整數
            num = input("請輸入一個整數：")

            # 如果輸入是空字符串，提示用戶重新輸入
            if num.strip() == '':
                print("請不要輸入空字符串，請重新輸入。\n")
                continue

            # 將輸入轉換為整數
            num = int(num)

            # 判斷是否為偶數
            if num % 2 == 0:
                print("{} 是一個偶數。\n".format(num))
            else:
                print("{} 不是一個偶數。\n".format(num))

            # 處理完畢後退出迴圈
            break

        except ValueError:
            # 處理異常輸入（非數字）
            print("請輸入一個有效的整數，請重新輸入。\n")

if __name__ == "__main__":
    check_even()