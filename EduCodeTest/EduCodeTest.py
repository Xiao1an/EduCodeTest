import time

from DrissionPage import Chromium


def TestGo(code):
    tab = Chromium().new_tab()
    tab.get('https://src.sjtu.edu.cn/register/')
    time.sleep(5)
    tab.actions.move_to('xpath:/html/body/div/div/div[2]')
    tab.ele('xpath://*[@id="id_invitecode"]').input(code)
    tab.ele('xpath://*[@id="id_nickname"]').input(12345)
    tab.ele('xpath://*[@id="id_email"]').input("12345@qq.com")
    tab.ele('xpath://*[@id="id_password1"]').input(12345)
    tab.ele('xpath://*[@id="id_password2"]').input(12345)
    time.sleep(5)
    try:
        tab.ele('xpath://*[@id="rectMask"]').click()
    except:
        tab.ele('xpath://*[@id="rectTop"]').click()

    time.sleep(5)
    tab.ele('xpath:/html/body/div/div/div[1]/div/form/div[7]/input').click()
    result = tab.ele('xpath:/html/body/div/div/div[1]/div/div/p').text
    tab.close()
    return result


if __name__ == '__main__':
    f = open("codelist.txt", "r", encoding="utf-8")
    w = open("OkCodeList.txt", "a+", encoding="utf-8")
    list = f.read().split("\n")
    for i in list:
        result = TestGo(i)
        if result == "* 该昵称已被注册":
            w.write(i + "\n")
        else:
            print(i + " 目前已经不可用！")
        time.sleep(4)
