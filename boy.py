import requests
import pandas as pd

url = "https://raw.githubusercontent.com/pbr20/tgbot/refs/heads/main/10kq/botreply.tsv"

df = pd.read_csv(url , sep="\t")

base_url = "https://api.telegram.org/bot7894013247:AAEeSeXf_MlN1M-PTtiJsvK0sh1NhPET-2g"

def read_msg(offset):
  parameters = {
      "offset" : offset
  }
  resp = requests.get(base_url + "/getUpdates" , data = parameters)
  data = resp.json()

  print(data)
  for result in data["result"]:
      send_msg(result)
  if data["result"]:
    return data["result"][-1]["update_id"] + 1

def auto_answer(message):
    answer = df.loc[df['Question'].str.lower() == message.lower()]

    if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer
    else:
      return "Sorry i don't have the answer fot that rn! I'm still trying to develop myself"

def send_msg(message):
  text = message["message"]["text"]
  chat_id = message["message"]["chat"]["id"]
  message_id = message["message"]["message_id"]
  answer = auto_answer(text)
  parameters = {
      "chat_id" : chat_id,
      "text" : answer,
      "reply_to_message_id" : message_id
  }
  resp = requests.get(base_url + "/sendMessage" , data = parameters)
  print(resp.text)

offset = 0

while True:
  offset = read_msg(offset)

