from scrapy import Scrapy
from outputcsv import OutPut
import login

import time

def main():
    # scrapyのインスタンス生成
    sc = Scrapy()
    # qiitaにログイン
    login.main(sc.driver)
    # 3s待機
    time.sleep(3)
    # インスタンス内の関数呼び出し
    results = sc.get_trend_data()
    # OutPutに引数を与えて、インスタンスの生成
    output = OutPut(results)
    # インスタンスの関数を呼び出す
    output.output_csv()

# メイン処理
if __name__ == "__main__":
    print("--------- 処理開始 --------- ")
    main()
    print("--------- 処理終了 --------- ")
