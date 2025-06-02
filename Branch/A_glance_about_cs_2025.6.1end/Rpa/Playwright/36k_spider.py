from playwright.sync_api import sync_playwright
from datetime import datetime
import yagmail
import schedule
import time
import requests

class AiNews:
    timeout_value = 60000
    def __init__(self):
        self.NewsList = []

    def Now(self):
        return datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
    
    def loveword(self):
        try:
            result = requests.get(url = "https://api.pearktrue.cn/api/jdyl/qinghua.php").text
            return result
        except Exception as e:
            return None
        
    def GetNews(self):
        with sync_playwright() as driver:

            # 开启broswer
            browser = driver.chromium.launch(headless=True, timeout = AiNews.timeout_value)

            # 创建浏览器上下文
            # 请求头
            headers = {
                "user-agent": "Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 UOS"
            }
            context = browser.new_context(
                extra_http_headers=headers,  # 请求头
            )

            print("正在打开浏览器")
            page = context.new_page()
            page.set_default_timeout(AiNews.timeout_value)
            # 导航至指定页面
            print("正在导航至36KAi新闻页面")
            page.goto(
                "https://www.36kr.com/information/AI/", 
                timeout = AiNews.timeout_value
                )
            try:
                print("正在获取新闻\n\n")
                news = page.locator(".title-wrapper.ellipsis-2").all()
                for i in news:
                    title = i.locator("a").inner_text()
                    href = i.locator("a").get_attribute("href")
                    n = f"{title}https://www.36kr.com{href}"
                    self.NewsList.append(n)
                print(self.NewsList)
                return self.NewsList
            except Exception as e:
                print(e)
    
    def SendMail(self):

        Time = self.Now()
        email = "1773384983@qq.com"
        password = ""

        yag = yagmail.SMTP(user = email, 
                           password = password,
                           host='smtp.qq.com',
                           port=465,
                           smtp_ssl=True)

        # 邮件标题
        subject = f"{self.loveword()}今日AI热点 获取时间{Time}"
        print(subject)
        # 收件人邮箱
        to = ["498734867@qq.com", 
              "1773384983@qq.com", 
              "3560806778@qq.com", 
              "3236519337@qq.com", 
              "1959847930@qq.com", 
              "2996583641@qq.com"]
        
        # to = ["2996583641@qq.com"] 坤哥
        # to = ["1773384983@qq.com"]
        # 邮件内容
        contents = self.GetNews()

        # 发送邮件
        try:
            print("正在发送邮件")
            yag.send(to=to, subject=subject, contents=contents)
            print(f"邮件已成功发送至 {to}")
        except Exception as e:
            print(f"发送邮件时出错: {e}")
        finally:
            # 关闭连接
            yag.close()
if __name__ == "__main__":
    def task():
        NewsReport = AiNews()
        NewsReport.SendMail()
        
    schedule.every().day.at("05:00").do(task)
    schedule.every().day.at("10:00").do(task)
    schedule.every().day.at("17:00").do(task)

    schedule.every(6).seconds.do(task)
    while True:
        print(f'正在监听, 当前时间{datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")}')
        schedule.run_pending()
        time.sleep(2)