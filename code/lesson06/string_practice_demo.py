text = "  OpenAI ChatGPT  "

# 1. 输出字符串长度
print(f"字符串长度：{len(text)}")
# 2. 输出第一个字符（注意有空格）
print(f"第一个字符：{text[2]}")
# 3. 输出去掉前两个空格后的 "OpenAI"
print(f"去掉前两个空格：{text.replace("  ","")}")
# 4. 输出最后三个字符 "PT "
print(f"最后三个字符：{text[-3:]}")
# 5. 输出全部大写
print(f"全部大写：{text.upper()}")
# 6. 把 ChatGPT 改成 GPT-5
print(f"ChatGPT 改成 GPT-5：{text.replace("ChatGPT","GPT-5")}")
