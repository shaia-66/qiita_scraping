def close(driver):
    # ブラウザを閉じる
    driver.quit()
    print('異常を検知したため、ブラウザを終了します。')
    return True
