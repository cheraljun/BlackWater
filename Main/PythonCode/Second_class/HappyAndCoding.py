import requests

class HappyCode:
    def __init__(self):
        pass
    def AI_talk(self):
        question = input("请提问?")
        url = "https://api.siliconflow.cn/v1/chat/completions"
        payload = {
            "model": "Qwen/Qwen3-8B",
            "messages": [
                {
                    "role": "user",
                    "content": f"{question}"
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
            "Authorization": "Bearer sk-maadyokebopfltzxonapnlitaucqxbpwvzkvpwizihvnhsmc",
            "Content-Type": "application/json"
        }

        response = requests.request("POST", url, json=payload, headers=headers).text
        print(response)

    def data_type(self):
        print(type(None))

        print(type("字符串"))

        print(type(123))
        print(type(1.23))

        print(type(True))
        print(type(False))
        
        print(type(["我爱你", "我超级爱你", 520]))
        print(type(("我爱你", "我超级爱你", 520)))
        print(type({"我说": "我爱你", "I say": "I love you"}))
        print(type({1, 2, 2}))

if __name__ == "__main__":
    TodayCode = HappyCode()
    ''' 
    TodayCode.AI_talk()
    TodayCode.data_type()
    '''
    while True:
        TodayCode.AI_talk()