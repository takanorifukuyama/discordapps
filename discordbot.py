import discord # インストールした discord.py

client = discord.Client() # 接続に使用するオブジェクト

channel = client.get_channel('508709774477754368')
await client.send_message(channel,'勝手に喋るよ')

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NTA4NzA0MTYwNTQwMDAwMzAw.DsDHeQ.MQGGd-MrJlx-AI59cw1GAYAxehc')
