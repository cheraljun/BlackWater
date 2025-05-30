import requests
import random
from datetime import datetime
from playwright.sync_api import sync_playwright
# 爬虫检测，商业版用
# from kkrobots import Parse

class Bottle:
    # 版权
    copyright = "_YESyes!"

    # 全局超时时间
    timeout_value = 60000

    # 初始化实例对象
    def __init__(self):
        # 欢迎
        self.welcome = f"\n欢迎使用由{Bottle.copyright}开发的小红书Post!\n"
        # 初始化滚动计数, 去重的笔记id集合
        self.scroll_count = 0
        self.note_id = set()
        
    # 模拟人类等待
    def human_wait(self):
        wait = random.randint(3000, 5000)
        print(f"模拟人类等待, 等待{wait/1000}秒")
        return wait
    
    # 情话api
    def loveword(self):
        try:
            result = requests.get(url = "https://api.pearktrue.cn/api/jdyl/qinghua.php").text
            return result
        except Exception as e:
            return None

    # 主函数Post
    def Post(self):
        # 欢迎
        print(self.welcome)
        # 启动playwright driver
        with sync_playwright() as driver:

            # 开启broswer
            browser = driver.chromium.launch(headless=True, timeout = Bottle.timeout_value)

            # 创建浏览器上下文
            # 请求头
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
            }
            cookies = [
                {"name": "web_session", "value": "040069b9461fe573021dba710d3a4ba206995a", "domain": ".xiaohongshu.com", "path": "/"}
            ]
            context = browser.new_context(
                extra_http_headers=headers,  # 请求头
            )
            context.add_cookies(cookies)

            print("正在打开浏览器")
            page = context.new_page()
            page.set_default_timeout(Bottle.timeout_value)

            # 导航至指定页面
            print("正在导航至小红书主页")
            page.goto(
                "https://www.xiaohongshu.com/explore", 
                timeout = Bottle.timeout_value
                )




            X = input("循环x轮?")
            for x in range(1, int(X), 1):

                # 滚动操作
                page.keyboard.press("PageDown")
                self.scroll_count = self.scroll_count + 1
                print(f"🚀🚀🚀 第{self.scroll_count}轮滚动中 🚀🚀🚀")

                try:
                    # 获取探索页容器
                    explore_page = page.locator("#exploreFeeds")
                    # 获取探索页所有笔记
                    note_items = explore_page.locator(".note-item")
                    for i in range(note_items.count()):
                        item = note_items.nth(i)
                        # 标题
                        note_title = item.locator(".title").inner_text()
                        # 作者
                        note_author = item.locator(".name").nth(0).inner_text() # 登陆
                        '''
                        note_author = item.locator(".name").inner_text() #免登录
                        '''
                        # 喜欢数
                        note_like = item.locator(".count").inner_text()
                        # 缩略图
                        note_img = item.locator("img").nth(0).get_attribute("src")
                        # 笔记链接
                        note_href = item.locator(".cover.mask.ld").get_attribute("href")
                        # 获取当前笔记的时间
                        note_time = datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")

                        print(f"当前为第{x}轮滚动时的第{i}个笔记, 获取时间{note_time}\n标题{note_title}\n作者{note_author}\n喜欢{note_like}\n预览图{note_img}\n笔记链接https://www.xiaohongshu.com{note_href}\n")

                        # 获取笔记唯一id并加入集合，去重用
                        id = f"{note_title}{note_author}{note_href}"
                        if id not in self.note_id:
                            self.note_id.add(id)
                            
                            # 评论的主逻辑
                            print("鼠标悬停于笔记上方")
                            item.locator('.cover.mask.ld').hover()
                            page.wait_for_timeout(self.human_wait())

                            print("正在点击进入笔记")
                            item.locator('.cover.mask.ld').click()
                            page.wait_for_timeout(self.human_wait())
                            
                            love = self.loveword()
                            print(f"正在填充评论...\n评论内容: {love}")
                            page.locator('#content-textarea').fill(f"正在到处漂流~漂流到好看的帖主这儿[doge]~{love}[红色心形R]")
                            page.wait_for_timeout(self.human_wait())

                            print("正在发送评论...")
                            page.locator('#content-textarea').press("Enter")
                            page.wait_for_timeout(self.human_wait())

                            print("正在退出笔记")
                            page.locator('.close.close-mask-dark').click()
                            page.wait_for_timeout(self.human_wait())

                            print(f"已评论{len(self.note_id)}条笔记!\n\n")
                    
                except Exception as e:
                    print(f"获取探索页容器失败{e}, 刷新页面")
                    page.reload()
                    continue
            input(f"已完成{X}轮滚动, 回车结束程序。")
                    
if __name__ == "__main__":
    
    # 爬虫检测，商业版用
    # parse = Parse(
    #     user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36", 
    #     test_url="https://www.xiaohongshu.com/explore"
    # )
    # can_crawl = parse.can_crawl("https://www.xiaohongshu.com/explore")

    # if can_crawl:
    
    #     XHS_Post = Bottle()
    #     XHS_Post.Post()
    # else:
    #     print("此网站不可爬虫")

    # 自娱自乐
    XHS_Post = Bottle()
    XHS_Post.Post()