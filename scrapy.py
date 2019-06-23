from selenium import webdriver
import time

class Scrapy(object):
    def __init__(self):
        # safariを用いる
        self.driver = webdriver.Safari()
        # 開くURLを指定
        self.url_day  = "https://qiita.com/"
        self.url_week = "https://qiita.com/?scope=weekly"
        self.url_mon  = "https://qiita.com/?scope=monthly"
        # 結果を入れる
        self.result = []

    def get_trend_data(self):
        # Safariを用いてURLを開く
        self.driver.get(self.url_day)
        """
         tr-Item_bodyというクラスの全情報を取得している(リスト型)
         ソースの表示ではなく、要素の確認をすることによって、より詳細な情報が取得できる
         以下の[tr-Item_body]は、各記事に格納されているclassであり、それをループで回すことにより、
         1件1件のタイトル、URL、ユーザ名を取得し、リストに格納。その後返り値でメイン処理に返す。
        """
        trends = self.driver.find_elements_by_class_name("tr-Item_body")
        for trend in trends:
            # dataをリスト型で保管(後にappendするため)
            data: list = []
            # aタグの取得
            items = trend.find_elements_by_tag_name("a")
            # itemsからhrefの取得
            href = items[0].get_attribute("href")
            # 0番目に格納されている文字列を取得(タイトル)
            title = items[0].text
            # 1番目に格納されている文字列の取得(ユーザ名)
            author = items[1].text
            # 取得した各種情報をリストに格納
            data.append(author)
            data.append(title)
            data.append(href)

            self.result.append(data)

        return self.result
