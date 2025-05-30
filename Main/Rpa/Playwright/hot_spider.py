import os
import requests
from datetime import datetime
from playwright.sync_api import sync_playwright

class Hot_spider:
    # 版权信息
    copyright = "_YESyes!"
    # 设置全局超时时间
    timeout_value = 60000
    # 初始化实例对象
    def __init__(self):
        # 欢迎
        self.welcome = f"\n欢迎使用由 💛💛💛 {Hot_spider.copyright} 💛💛💛 开发的小红书爬虫!😊\n\n超时时间有{Hot_spider.timeout_value/6000}分钟, 请耐心等待一会儿🐱~\n"
        # 初始化笔记和图片储存目录
        os.makedirs (os.path.join(os.path.dirname(os.path.abspath(__file__)), "小红书热点", "notes"), exist_ok=True)
        os.makedirs (os.path.join(os.path.dirname(os.path.abspath(__file__)), "小红书热点", "images"), exist_ok=True)
        # 初始化笔记和图片储存路径
        self.xhs_notes_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "小红书热点", "notes", "notes.md")
        # 初始化滚动计数和笔记id去重集合
        self.scroll_count = 0
        self.xhs_unique_notes_id = set()

    # 下载图片函数
    def download_images(self, xhs_note_img, xhs_note_title, xhs_note_get_time):
        try:
            # 请求图片
            picture = requests.get(url = f"{xhs_note_img}")
            timestamp = datetime.now().strftime(f"%Y%m%d%H%M%S%f")
            # 图片文件
            xhs_image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "小红书热点", "images", f"{xhs_note_title}{timestamp}.png")
            with open (xhs_image_path, "wb") as f:
                f.write(picture.content)
            print(f"{xhs_note_title}的图片已于{xhs_note_get_time}请求成功!😊")
        except Exception as e:
            print(f"⚠️出错了...{e}")
            return None
        
    # playwright和文件读写主函数
    def spider(self):
        # 欢迎界面
        print(self.welcome)
    
        # 启动playwright主程序
        with sync_playwright() as driver:

            # 开启driver和broswer
            browser = driver.chromium.launch(headless=True, timeout = Hot_spider.timeout_value)
            # 创建浏览器上下文
            # 请求头
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
                }
            # cookies
            cookies = [
                {"name": "web_session", "value": "040069b9461fe573021dba710d3a4ba206995a", "domain": ".xiaohongshu.com", "path": "/"}
                ]

            context = browser.new_context(
                extra_http_headers = headers, 
            )
            context.add_cookies(cookies)

            print("正在打开浏览器")
            page = context.new_page()
            page.set_default_timeout(Hot_spider.timeout_value)
            
            # 导航至指定页面
            print("正在导航至小红书主页")
            page.goto(
                "https://www.xiaohongshu.com/explore", 
                timeout = Hot_spider.timeout_value
            )
            page.get_by_text("穿搭").nth(0).click()
            print("已导航至穿搭界面, 即将开始获取笔记...🐱")

            try:
                # 实时写入文件, 节约内存
                with open (self.xhs_notes_path, "w", encoding="utf-8") as f:
                    while True:
                        try:
                            # input("如果此时出现验证界面, 请手动验证, 关闭登陆弹窗并导航至穿搭界面, 回车进行下一步\nnext?🐱")
                            scroll_times = input("\n滚动窗口以动态获取笔记。需要滚动多少轮?🐱\n写\"-1\"意味着无限循环...🐱\n请选择 :")
                            if scroll_times == "-1":
                                scroll_times = float("inf")
                                print(f"你选择滚动无限轮!😊\n")
                            else:
                                scroll_times = int(scroll_times)
                                print(f"你选择滚动{scroll_times}轮!😊\n")
                            break
                        except Exception as e:
                            print(f"⚠️出错了...\n{e}")
                            continue
                    while True:
                        # 退出判断
                        if scroll_times != float("inf") and self.scroll_count >= scroll_times:
                                break
                        # 滚动方法
                        page.keyboard.press("PageDown")
                        """
                        page.evaluate("window.scrollBy(0, 500)")
                        """
                        self.scroll_count = self.scroll_count + 1
                        print(f"🚀🚀🚀 第{self.scroll_count}轮滚动中 🚀🚀🚀")

                        # 获取整个界面的所有笔记
                        xhs_explore_all_notes = page.locator("#exploreFeeds") # 免登录的全部笔记
                        '''
                        xhs_explore_all_notes = page.locator(".feeds-container") # 关键词搜索页的全部笔记
                        '''
                        
                        # 遍历每一个笔记
                        xhs_note_item = xhs_explore_all_notes.locator(".note-item")
                        for i in range(xhs_note_item.count()):
                            current_xhs_note_item = xhs_note_item.nth(i)
                            # 标题
                            xhs_note_title = current_xhs_note_item.locator(".title").inner_text()
                            # 作者
                            xhs_note_author = current_xhs_note_item.locator(".name").nth(0).inner_text() # 登陆
                            '''
                            xhs_note_author = current_xhs_note_item.locator(".name").inner_text() #免登录
                            '''
                            # 喜欢数
                            xhs_note_like = current_xhs_note_item.locator(".count").inner_text()
                            # 缩略图
                            xhs_note_img = current_xhs_note_item.locator("img").nth(0).get_attribute("src")
                            # 笔记链接
                            xhs_note_href = current_xhs_note_item.locator(".cover.mask.ld").get_attribute("href")
                            # 获取当前笔记的时间
                            xhs_note_get_time = datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

                            # 判断是否重复
                            xhs_note_id = xhs_note_href
                            if xhs_note_id not in self.xhs_unique_notes_id:
                                self.xhs_unique_notes_id.add(xhs_note_id)

                                # 下载笔记图片
                                self.download_images(xhs_note_img, xhs_note_title, xhs_note_get_time)
                                # download_images(xhs_note_img)

                                # 写入内容是?
                                xhs_notes_detail = f"""当前笔记于{xhs_note_get_time}获取成功!更多内容请关注 {Hot_spider.copyright} ƪ(˘⌣˘)ʃ优雅
笔记详情: 
标题: {xhs_note_title}
作者: {xhs_note_author}
喜欢: {xhs_note_like}
预览图: \n![{xhs_note_title}的预览图未加载]({xhs_note_img} "{xhs_note_title}")
链接: https://www.xiaohongshu.com{xhs_note_href}\n"""
                                f.write(f"第{len(self.xhs_unique_notes_id)}条笔记\n{xhs_notes_detail}\n\n")

                                # 笔记获取总情况
                                print(f"{xhs_notes_detail}!")
                                print(f"已获取共计{len(self.xhs_unique_notes_id)}条笔记😊\n\n")
                
            except KeyboardInterrupt:
                print("已通过键盘终止😊")

            except Exception as e:
                print(f"⚠️出错了...{e}")

            finally:
                input(f"本次滚动{self.scroll_count}轮!😊\n获取{len(self.xhs_unique_notes_id)}条笔记😊!\n文件已写入{self.xhs_notes_path}!OK?等几秒钟释放资源回车以结束😊~")
            
if __name__ == "__main__":
    The_spider = Hot_spider()
    The_spider.spider()