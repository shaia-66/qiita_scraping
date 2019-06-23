import exception

def main(driver):
    # ログイン画面のURL
    url = "https://qiita.com/login?redirect_to=%2F"
    # user名
    user = "shaia-66"
    # パスワード
    password = "Koamsoxng92jkf8366"

    # ログイン画面を表示
    try:
        driver.get(url)
    except:
        exception.close(driver)

    # "id=identity"の値を取得
    attribute = driver.find_element_by_name("identity")
    # 記述内容の初期化
    attribute.clear()
    # id="user"として設定
    attribute.send_keys(user)

    # "id=password"の値を取得
    attribute = driver.find_element_by_name("password")
    # 記述内容の初期化
    attribute.clear()
    # id="passworf"として設定
    attribute.send_keys(password)

    # name="commit"の値を取得
    attribute = driver.find_element_by_name("commit")
    # ボタンのクリック
    attribute.submit()

    # --- ログイン完了 ---
    return True
