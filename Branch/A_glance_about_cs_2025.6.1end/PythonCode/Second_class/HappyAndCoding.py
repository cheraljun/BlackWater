import requests

class AiLove:
    def __init__(self):
        pass

    def loveword(self):
        self.result = requests.get(url="https://api.pearktrue.cn/api/jdyl/qinghua.php").text
        print(f"请求情话成功:{self.result}\n")
    
    def AI_talk(self):
        self.loveword()
        url = "https://api.siliconflow.cn/v1/chat/completions"
        payload = {
            "model": "Qwen/Qwen3-8B",
            "messages": [
                {
                    "role": "user",
                    "content": f"{self.result}"
                }
            ],
            "stream": False,
            "max_tokens": 512,
            "enable_thinking": False,
            "thinking_budget": 4096,
            "min_p": 0.05,
            "stop": None,
            "temperature": 0.7,
            "top_p": 0.7,
            "top_k": 50,
            "frequency_penalty": 0.5,
            "n": 1,
            "response_format": {"type": "text"},
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "description": "<string>",
                        "name": "<string>",
                        "parameters": {},
                        "strict": False
                    }
                }
            ]
        }
        headers = {
            "Authorization": "Bearer <apikey>",
            "Content-Type": "application/json"
        }
        print(f"AI收到情话: {self.result}\n正在分析...\n")
        AIresult = requests.request("POST", url, json=payload, headers=headers).text
        return f"AI返回结果是: \n{AIresult}\n\n\n"

if __name__ == "__main__":
    love = AiLove()
    while True:
        result = love.AI_talk()
        print(result)