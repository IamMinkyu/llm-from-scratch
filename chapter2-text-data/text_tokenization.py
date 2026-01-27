
import urllib.request
import re

url = ("https://raw.githubusercontent.com/rickiepark/"
       "llm-from-scratch/main/ch02/01_main-chapter-code/"
       "the-verdict.txt")
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("총 문자 개수:", len(raw_text))
print(raw_text[:99])

preproccessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preproccessed = [item.strip() for item in preproccessed if item.strip()]
print(len(preproccessed))
print(preproccessed[:30])