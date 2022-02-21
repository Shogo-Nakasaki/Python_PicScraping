# 自分でカスタムできる画像収集ツールが欲しい
# 上記目標を達成するために、Pythonで自力作成することにした

#色々と追加
import requests
from bs4 import BeautifulSoup
import os
import time

# 画像を収集する
def make_dlfile(URL,images,path):
    # URL内を解析
    soup = BeautifulSoup(requests.get(URL).content, 'lxml')
    # imgタグを取得し、linkに格納
    # その後、拡張子ごとにタグを取得→imagesに格納
    for link in soup.find_all("img"):
        # srcタグから
        if link.get("src")and link.get("src").endswith(".jpg"):
            images.append(link.get("src"))
        elif link.get("src")and link.get("src").endswith(".png"):
            images.append(link.get("src"))
        # data-srcタグから
        if link.get("data-src")and link.get("data-src").endswith(".jpg"):
            images.append(link.get("data-src"))
        elif link.get("data-src")and link.get("data-src").endswith(".png"):
            images.append(link.get("data-src"))
    # 保存する本体
    for target in images:
        re = requests.get(target)
        with open(path + '/' + target.split('/')[-1], 'wb') as file:
            file.write(re.content)
            print("-----save-----")
            time.sleep(1)

# 指定名のフォルダを作成する
def make_directory(name):
    if not os.path.isdir(name):
        os.makedirs(name)

# URLやフォルダ名を記入する
def main():
    while(True):
        images = []
        url = input(f"保存したいサイトのURLを記載してください。\nPlease provide the URL of the site you want to save.\n終了したいときは「0」を入力してください。\nIf you want to quit, enter 0.\n>>")
        if url =='0':
            print("終了します。\nend")
            break
        time.sleep(1)
        text = input(f"保存するフォルダ名を記載してください。\nProvide the name of the folder where you want to save the file.\n>>")
        path = 'D:00_ScrapingPic\ ' + str(text)
        time.sleep(1)
        make_directory(path)
        make_dlfile(url, images, path)
        print("画像収集完了")

# 以下本文
main()