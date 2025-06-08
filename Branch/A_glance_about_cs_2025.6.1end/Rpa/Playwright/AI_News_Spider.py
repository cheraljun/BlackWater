from playwright.sync_api import sync_playwright
from datetime import datetime
import yagmail
import schedule
import time
import requests

class Aggregation_News:
    
    def __init__(self):
        self._36KList = []
        self._AggregationList = []
        self.timeout_value = 6000000

    def GetTime(self):
        return f'获取时间: {datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")}'
    
    def loveword(self):
        try:
            result = requests.get(url = "https://api.pearktrue.cn/api/jdyl/qinghua.php").text
            return result
        except Exception as e:
            return None
        
    def Get_36K_News(self):
        with sync_playwright() as driver:
            # 开启broswer
            browser = driver.chromium.launch(headless=True, timeout = self.timeout_value)
            # 创建浏览器上下文
            # 请求头
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
            }
            context = browser.new_context(extra_http_headers=headers)

            print("正在打开浏览器")
            page = context.new_page()
            page.set_default_timeout(self.timeout_value)

            # 导航至指定页面
            print("正在导航至36KAi新闻页面")
            page.goto(
                "https://www.36kr.com/information/AI/", 
                timeout = self.timeout_value
                )
            try:
                class_title_wrapper_ellipsis_2 = page.locator(".title-wrapper.ellipsis-2").all()
                for news in class_title_wrapper_ellipsis_2:
                    title = news.locator("a").inner_text()
                    href = news.locator("a").get_attribute("href")
                    result = f"{title} https://www.36kr.com{href}"
                    self._36KList.append(result)
                    print(result)

                self.SendMail(self._36KList, "来源: https://www.36kr.com/information/AI/")

            except Exception as e:
                print(e)

    def Get_Aggregation_Ai_News(self):
        with sync_playwright() as driver:
            # 开启broswer
            browser = driver.chromium.launch(headless=True, timeout = self.timeout_value)
            # 创建浏览器上下文
            # 请求头
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.51"
            }
            context = browser.new_context(extra_http_headers=headers)
            print("正在打开浏览器")
            page = context.new_page()
            page.set_default_timeout(self.timeout_value)
            # 导航至指定页面
            print("正在导航至https://www.ainav.cn/news/")
            page.goto(
                "https://www.ainav.cn/news/", 
                timeout = self.timeout_value
                )
            try:
                print("已导航至https://www.ainav.cn/news/, 等待10秒等待全部新闻加载")
                page.wait_for_timeout(10000)

                class_ml2 = page.locator(".ml-2").all()
                for news in class_ml2:
                    title = news.inner_text()
                    href = news.get_attribute("href")
                    result = f"{title} {href}"
                    self._AggregationList.append(result)
                    print(f"{title} {href}\n")

                self.SendMail(self._AggregationList, "来源: https://www.ainav.cn/news/")

            except Exception as e:
                print(e)
    
    def SendMail(self, newslist, source = "AI新闻"):

        email = "1773384983@qq.com"
        password = ""

        yag = yagmail.SMTP(user = email, 
                           password = password,
                           host='smtp.qq.com',
                           port=465,
                           smtp_ssl=True)

        # 邮件标题
        subject = f"{source} {self.GetTime()} {self.loveword()}"
        print(subject)
        # 收件人邮箱
        to = ["1773384983@qq.com", 
              "3560806778@qq.com", 
              "3236519337@qq.com", 
              "1959847930@qq.com", 
              "1281143618@qq.com", 
              "2996583641@qq.com"]
        # 邮件内容
        contents = newslist

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
    news_report = Aggregation_News()

    schedule.every().day.at("05:00").do(news_report.Get_36K_News)
    schedule.every().day.at("17:00").do(news_report.Get_Aggregation_Ai_News)

    # schedule.every(10).seconds.do(news_report.Get_36K_News)
    # schedule.every(10).seconds.do(news_report.Get_Aggregation_Ai_News)

    while True:
        print(f'正在监听, 当前时间：{datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")}')
        schedule.run_pending()
        time.sleep(1)