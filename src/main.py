import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

def read_text_file(file_path):
    try:
        with open(file_path,'r',encoding="utf-8") as f:
            text = f.read()
            return text
    except FileNotFoundError:
        print(f"错误：文件{file_path}不存在")

    except Exception as e:
        print(f"读取文件失败：{e}")
        return None

def summarize_text(text):
    try:
        responses = client.chat.completions.create(
            model = "deepseek-chat",
            messages = [
                {"role": "system", "content": "你是一个文本总结助手，请你对用户提供的文本进行总结"},
                {"role": "user", "content": f"请总结下面这篇文本：{text}"},
            ],
            stream=False
        )
        summary = responses.choices[0].message.content
        return summary
    except Exception as e:
        print(f"调用模型失败：{e}")
        return None

def main():
    print("="*50)
    print("问答程序已经启动...")
    print("="*50)

    while True:

        file_path = input("文本文件地址：")
        if file_path in ['exit', 'quit', 'q']:
            print("再见！")
            break

        if not file_path:
            print("请输入问题")
            continue

        print("思考中...")
        text = read_text_file(file_path)
        summary = summarize_text(text)
        print(f"总结\n{summary}")

        print("正在保存文件...")
        with open('text.txt','w',encoding="utf-8") as file:
            file.write(summary)
        print("总结已保存到text.txt文件当中")

if __name__=="__main__":
    main()