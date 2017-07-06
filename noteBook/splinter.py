import splinter
browser = splinter.Browser(driver_name='chrome')
# 逐一去按按鈕
# browser.visit('https://ianchenhq.com')
# elem = browser.find_by_xpath('/html/body/div/div/div[1]/aside/ul/li[1]/a')
# elem.click()
# elem = browser.find_by_xpath('/html/body/div/div/div[1]/aside/ul/li[2]/a')
# elem.click()
# elem = browser.find_by_xpath('/html/body/div/div/div[1]/aside/ul/li[3]/a')
# elem.click()
# browser.back()

# 取得cookies
# cookies = browser.cookies.all()
# print(cookies)

# 登入
# browser.visit('https://thingiverse.com')
# browser.click_link_by_partial_text("Sign in / Join")
# # 指向彈出的另一頁(第一頁為0)
# browser.windows[1].is_current = True
# browser.fill('username', 'ytn63241@tqosi.com')
# browser.fill('password', 'pythonetl')
# browser.click_link_by_id("sso_sign_in")
# browser.cookies.all()

# 選單選取並將畫面移到最後面
browser.visit('https://thingiverse.com')
elem = browser.find_by_css('a.dropdown-toggle')
elem.click()
elem = browser.find_by_xpath('//*[@id="push-main"]/div[2]/div/ul/li[2]/ul/li[1]/a')
elem.click()
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
browser.screenshot('d:/myscreenshot.png')