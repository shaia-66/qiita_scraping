import csv
from datetime import datetime
import os

class OutPut(object):
    def __init__(self, data):
        self.data = data
        self.now = datetime.now()

    def output_csv(self):
        # 結果を書き込むCSVのパスを指定
        dir = os.environ['HOME'] + '/Desktop/qiita_safari/result.csv'
        # CSVファイル用のヘッダ
        csv_header = ["著者", "タイトル", "URL"]
        # 格納するデータをリスト型で宣言
        csv_data = []
        # リストにデータを格納
        csv_data.append(csv_header)
        with open(dir, "w", encoding="utf-8_sig") as f:
            # "result.csv"に書き込む(ペンを持った状態)
            writer = csv.writer(f, lineterminator="\n")
            for data in self.data:
                # 1行ずつ取得してリストに格納
                csv_data.append(data)
            # ヘッダと、1行ずつ格納されたデータを"result.csv"に書き込む'(CSV型で)
            writer.writerows(csv_data)
