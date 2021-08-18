# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:26:05 2021

@author: su
"""

import photo_module as m

while True:
    photo_name = input("請輸入要下載的圖片名稱: ")
    download_num = int(input("請輸入要下載的圖片數量: "))
    photo_list = m.get_photolist(photo_name, download_num)
    
    if photo_list == None:
        print("找不到圖片, 請換關鍵字再試試看")
    else:
        if len(photo_list) < download_num:
            print("找到的相關圖片僅有", len(photo_list), "張")
        else:
            print("取得所有圖片連結")
        break
    
folder_name = m.create_folder(photo_name)

print("開始下載...")

m.get_photothread(folder_name, photo_name, photo_list)

print("\n下載完畢")