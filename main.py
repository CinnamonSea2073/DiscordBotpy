import os
import nextcord
from nextcord.ext import commands
import nextcord as discord
import aiohttp
import requests
import time
import re
import queue
import asyncio
from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis
import yaml

TOKEN = "TOKEN"
bot = commands.Bot(command_prefix="!")
api = "https://api.mcsrvstat.us/2/go.mcsvr.online:28231"
url = 'https://www.google.com/?hl=ja'
client = nextcord.Client()
member_mention = "<@698127042977333248>"
cnmn = ["しなも", "シナモ", "cinnamon", "しなしな", "しなっと","香辛料","品物","698127042977333248","シナシナ"]#'しなもん, シナモン, cinnamon, しなしな, しなっとモンスター'
#'しなもん", "シナモン", "cinnamon", "しなしな", "しなっとモンスター'   
ae = ["@e"]
gijyutu = ["技術的"]
member = None
with open('mcid.yaml') as file:
    member = yaml.safe_load(file)

class MyQueue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        result = self.queue[0]
        del self.queue[0]
        return result

q = queue.Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print(q.get())

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("CinnamonGame")) #Pythonをプレイ中
    print(f"Bot '{bot.user.name}' が起動しました")

@bot.command()
async def mcid(ctx, mcid):
    ctx.send(member.get(str(mcid)))

@bot.listen()
async def on_message(message):
        channel = message.channel
        if not message.author.bot or message.author.id == 893450751899222046:
           for i in ae:
            if i in message.content:
                msg = f'うわあああああああやめろおおおおおおお'
                print(f'Message from {message.author}: {message.content}')
                await channel.send(msg,delete_after=10)
                break


@bot.listen()
async def on_message(message):
        channel = message.channel
        if not message.author.bot or message.author.id == 893450751899222046:
          for i in cnmn:
            if i in message.content:
           #if re.search(message.content, cnmn):
           #message.content.lower() in cnmn
              print("一致したよ")
              if askafk == True:
                 msg = f'しなもんはいま放置中だよ'
                 print(f'Message from {message.author}: {message.content}')
                 await channel.send(msg,delete_after=10)
                 break

@bot.listen()
async def on_message(message):
        channel = message.channel
        if not message.author.bot or message.author.id == 893450751899222046:
          for i in gijyutu:
            if i in message.content:
           #if re.search(message.content, cnmn):
           #message.content.lower() in cnmn
              print("一致したよ")
              embed = discord.Embed( # Embedを定義する
                          color=0x1e90ff, # フレーム色指定(今回は緑)
                          )

              embed.set_image(url="https://cdn.discordapp.com/attachments/881524267601244225/956594271740371015/5000choyen.png") # 大きな画像タイルを設定できる

              await channel.send(embed=embed) # embedの送信には、embed={定義したembed名}
              break

@bot.command()
async def charttest(ctx):
    Width = 400
    Height = 250
    chart = SimpleLineChart(Width, Height)
    chart.set_colours(['333333'])
    chart.set_line_style(index=0, thickness=5)
    #chart.add_data(f"{add}")
    chart.add_data([9, 2, 4, 8, 13])
    chart.set_axis_labels(Axis.BOTTOM, [0, 1, 2, 3])
    chart.set_axis_labels(Axis.LEFT, ["low", "middle", "high"])
    chart.set_title("鯖参加人数グラフテスト")
    embed = discord.Embed()
    embed.set_image(url=f"{chart.get_url()}")
    embed.set_footer(text="made by CinnamonSea2073",
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")
    await ctx.send(embed=embed)
    
    myq = MyQueue()
    myq.enqueue(0)
    myq.enqueue(1)
    print(myq.dequeue())
    print(myq.dequeue())
    print(myq.dequeue())


@bot.command()
async def afk(ctx,afkq):
    #afkq = str(afkq)
    if ctx.author.id == 698127042977333248:
       if afkq == "y":
          global askafk
          askafk = True
          print("afknow")
          embed = discord.Embed( 
                          title="Afk中",
                          color= 0x1e90ff , 
                          )
          await ctx.send(embed=embed)
       elif afkq == "n":
          askafk = False  
          print("afkend")
          embed = discord.Embed( 
                          title="Afkを解除",
                          color= 0x1e90ff , 
                          )
          await ctx.send(embed=embed)
    else:
        embed = discord.Embed( 
                          title="しなもん専用コマンドです",
                          color= 0xdc143c , 
                          )
        await ctx.send(embed=embed)

@bot.command(name="time")
async def timecmd(ctx,timer):
    channel = ctx.channel
    timer = int(timer)
    mtime = timer
    timer = timer * 60
    if timer == timer:
      if timer < 259200:
            embed = discord.Embed(
                          title="タイマーStert",
                          color=0x1e90ff,
                          description=f"<@{ctx.author.id}>\n{mtime}分後に通知します。",
                          )

            embed.set_footer(text="made by CinnamonSea2073",
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

            await ctx.send(embed=embed)
            msg = f'【Minecraftチャット向け】タイマーを開始します。{mtime}分後に通知します。'
            await channel.send(msg,delete_after=10)

            if timer > 60 :
              iftimer = timer-60
              await asyncio.sleep(iftimer)
              msg = f'<@{ctx.author.id}>'
              await channel.send(msg)
              embed = discord.Embed(
                          title="タイマー残り1分",
                          color=0x1e90ff,
                          description=f"{mtime}分間のタイマーが残り1分で終了します。",
                          )

              embed.set_footer(text="made by CinnamonSea2073",
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

              await ctx.send(embed=embed)
              msg = f'【Minecraftチャット向け】{mtime}分間のタイマーが残り1分で終了します。'
              await channel.send(msg,delete_after=10)
              await asyncio.sleep(60)
            else:
              await asyncio.sleep(timer)

            msg = f'<@{ctx.author.id}>'
            await channel.send(msg)
            embed = discord.Embed(
                          title="タイマー終了",
                          color=0x1e90ff,
                          description=f"{mtime}分間のタイマーが終了しました。",
                          )

            embed.set_footer(text="made by CinnamonSea2073",
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

            await ctx.send(embed=embed)
            msg = f'【Minecraftチャット向け】{mtime}分間のタイマー終了です。'
            await channel.send(msg,delete_after=10)
 
      else:
        msg = f'<@{ctx.author.id}>'
        await channel.send(msg)
        embed = discord.Embed(
                      title="ざけんな",
                      color=0x1e90ff,
                      description=f"{mtime}分間とか三日以上やんけ、やってられっかよ",
                      )
        await ctx.send(embed=embed)

        embed.set_footer(text="made by CinnamonSea2073",
                 icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")
          


@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def css(ctx):
    embed = discord.Embed()

    embed.set_image(url="https://cdn.discordapp.com/attachments/927764512327733308/937724046534123570/637038_i.png") # 大きな画像タイルを設定できる

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
async def hosii(ctx,up,down):
    embed = discord.Embed(color=0x1e90ff)
    url = f"https://gsapi.cyberrex.jp/image?top={up}&bottom={down}"
    await ctx.send(url)
    embed.set_image(url=f"https://gsapi.cyberrex.jp/image?top={up}&bottom={down}") 

    embed.set_footer(text="made by CinnamonSea2073", 
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) 
    await ctx.send(f"https://gsapi.cyberrex.jp/image?top={up}&bottom={down}")

@bot.command()
async def pi(ctx):
    await ctx.send("<@698127042977333248>")
    embed = discord.Embed( # Embedを定義する
                          title="しなもんサーバー開けやがれ",# タイトル
                          color=0x1e90ff, # フレーム色指定(今回は緑)
                          description="<@698127042977333248>", # Embedの説明文 必要に応じて
                          
                          )

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
async def face(ctx, username):
    mojang = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()
    isvalid = mojang.get("id",None)
    if isvalid is None:
        await ctx.send("プレイヤー'{}'は存在しません。".format(username))
    else:
        crafatar = requests.get(f"https://crafatar.com/avatars/{mojang['id']}", stream=True)
        with open(f"{username}.png", "wb") as f:
            f.write(crafatar.content)
        file = discord.File(f"{username}.png", filename=f"{username}.png")
        embed = discord.Embed(title=f"{username} のお顔")
        embed.set_image(url=f"attachment://{username}.png")
        await ctx.send(file=file,embed=embed)
        os.remove(f"{username}.png")

@bot.command()
async def super(ctx,money,bun):
  money = int(money)
  if money <= 199 :
    Dcoler = 0x1e90ff
  elif 200 <= money <= 499 :
    Dcoler = 0x87ceeb
  elif 500 <= money <= 999 :
    Dcoler = 0x66cdaa
  elif 1000 <= money <= 1999 :
    Dcoler = 0xffd700
  elif 2000 <= money <= 4999 :
    Dcoler = 0xff8c00
  else:
    Dcoler = 0xdc143c

      
  embed = discord.Embed( 
                          title=f"¥{int(money)}",
                          color= Dcoler , 
                          description=str(bun), 
                          )
  await ctx.send(embed=embed)

@bot.command()
async def list(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as response:
            resp = await response.json()

    online = resp['players']['online']
    online = int(online)
    print(online)
    if online > 0:
      embed = discord.Embed( 
                          title="ふぃぼなっちサーバー",
                          color=0x1e90ff, 
                          description="ここはふぃぼなっちサーバです。\nとても皆様元気でうれしい。", 
                          url="https://api.mcsrvstat.us/2/go.mcsvr.online:28231" 
                          )
      embed.set_thumbnail(url="https://cdn.discordapp.com/icons/879288794560471050/0f7aff706944613474e1cfc38128ac4f.webp?size=100%22")
      embed.add_field(inline=True,name=resp['hostname'],value=resp['ip'])
      embed.add_field(inline=True,name=resp['version'],value=resp['software'])
      players = "\n".join(resp['players']['list'])
      embed.add_field(inline=False,name="参加者",value=players)
      OnlineMember = resp['players']['online']
      MaxMember = resp['players']['max']
      s = f"接続人数 {OnlineMember}\n{MaxMember}"
      embed.set_footer(text=('/'.join(s.splitlines())))
      await ctx.send(embed=embed) 
    
    else:
      embed = discord.Embed( 
                          title="ふぃぼなっちサーバー",
                          color=0x1e90ff, 
                          description="ここはふぃぼなっちサーバです。\nとても皆様元気でうれしい。", 
                          url="https://api.mcsrvstat.us/2/go.mcsvr.online:28231" 
                          )
      embed.set_thumbnail(url="https://cdn.discordapp.com/icons/879288794560471050/0f7aff706944613474e1cfc38128ac4f.webp?size=100%22")
      embed.add_field(inline=True,name=resp['hostname'],value=resp['ip'])
      embed.add_field(inline=True,name=resp['version'],value=resp['software']) 
      OnlineMember = resp['players']['online']
      MaxMember = resp['players']['max']
      s = f"接続人数 {OnlineMember}\n{MaxMember}"
      embed.set_footer(text=('/'.join(s.splitlines())))
      await ctx.send(embed=embed) 

@bot.command()
async def stat(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get(api) as response:
            resp = await response.json()

    online = resp["online"]
    online = str(online)
    print(online)
    if "True" in online:
      embed = discord.Embed( 
                          title="Server Stat",
                          color=0x1e90ff, 
                          description="サーバーはオンラインです。\n(５分程度の遅延がある場合があります)", 
                          url="https://api.mcsrvstat.us/2/go.mcsvr.online:28231" 
                          )
      embed.add_field(inline=False,name="HostName",value=resp['hostname'])
      embed.add_field(inline=False,name="IP",value=resp["ip"]) 
      embed.add_field(inline=False,name="ポート",value=resp['port'])
      embed.add_field(inline=False,name="バージョン",value=resp['version'])
      embed.add_field(inline=False,name="ソフトウェア",value=resp['software'])
      embed.add_field(inline=False,name="最大人数",value=resp['players']['max'])
      embed.add_field(inline=False,name="接続人数",value=resp['players']['online'])
      embed.set_footer(text="made by CinnamonSea2073", 
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")
      await ctx.send(embed=embed) 

    else:
      embed = discord.Embed( 
                          title="Server Stat",
                          color=0x1e90ff, 
                          description="サーバーはオフラインです。\n(５分程度の遅延がある場合があります)", 
                          url="https://api.mcsrvstat.us/2/go.mcsvr.online:28231" 
                          ) 
      embed.add_field(inline=False,name="hostname",value=resp['hostname'])
      embed.add_field(inline=False,name="version",value=resp['version'])
      embed.set_footer(text="made by CinnamonSea2073", 
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")
      await ctx.send(embed=embed) 
            
    players = "\n".join(resp['players']['list'])
    embed = discord.Embed( 
                          title="参加者",
                          color=0x1e90ff, 
                          description=players, 
                          url="https://api.mcsrvstat.us/2/go.mcsvr.online:28231" 
                          )
    embed.set_footer(text="made by CinnamonSea2073", 
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")
    await ctx.send(embed=embed) 

@bot.command()
async def nether(ctx,x,y):
    await ctx.send(f"x:{int(x)/8}\ny:{int(y)/8}")

@bot.command()
async def world(ctx,x,y):
    await ctx.send(f"x:{int(x)*8}\nz:{int(y)*8}")

@bot.command()
async def gotobed(ctx):
    await ctx.send(":thinking::right_facing_fist::boom::bed:")

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def test(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="Example Embed",# タイトル
                          color=0x1e90ff, # フレーム色指定(今回は緑)
                          description="Example Embed for Advent Calendar", # Embedの説明文 必要に応じて
                          url="https://example.com" # これを設定すると、タイトルが指定URLへのリンクになる
                          )

    embed.set_thumbnail(url="https://image.example.com/thumbnail.png") # サムネイルとして小さい画像を設定できる

    embed.set_image(url="https://image.example.com/main.png") # 大きな画像タイルを設定できる

    embed.add_field(name="フィールド１",value="値１") # フィールドを追加。
    embed.add_field(name="フィールド２",value="値２")

    embed.set_footer(text="made by nashiroaoi", # フッターには開発者の情報でも入れてみる
                     icon_url="https://dev.exapmple.com/profile.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def dynmap(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="Dynmapサイトはここをクリック",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          description="11月16日17時更新(手動)", # Embedの説明文 必要に応じて
                          url="http://34.146.152.110:8123/" # これを設定すると、タイトルが指定URLへのリンクになる
                          )

    embed.set_image(url="https://cdn.discordapp.com/attachments/900684389040672788/910074445954174976/unknown.png") # 大きな画像タイルを設定できる

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def bigdynmap(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="Dynmapサイトはここをクリック",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          description="11月16日17時更新(手動)", # Embedの説明文 必要に応じて
                          url="http://34.146.152.110:8123/" # これを設定すると、タイトルが指定URLへのリンクになる
                          )

    embed.set_image(url="https://cdn.discordapp.com/attachments/900684389040672788/910074534013599744/unknown.png") # 大きな画像タイルを設定できる

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
async def cin(ctx):
    await ctx.send("https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def jam(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="Jamサイトはここをクリック",# タイトル
                          color=0xFFFF00, # フレーム色指定(今回は緑)
                          url="https://jamboard.google.com/d/18ZEnJ441G4R-5ziwrW-MJ9pGooFggW93q5wfWh18BlY/edit?usp=sharing" # これを設定すると、タイトルが指定URLへのリンクになる
                          )

    embed.set_image(url="https://cdn.discordapp.com/attachments/900684389040672788/901815589914411029/unknown.png") # 大きな画像タイルを設定できる

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def vbigdynmap(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="Dynmapサイトはここをクリック",# タイトル
                          color=0x00ff00, # フレーム色指定(今回は緑)
                          description="11月16日17時更新(手動)", # Embedの説明文 必要に応じて
                          url="http://34.146.152.110:8123/" # これを設定すると、タイトルが指定URLへのリンクになる
                          )

    embed.set_image(url="https://cdn.discordapp.com/attachments/900684389040672788/910074766902321182/unknown.png") # 大きな画像タイルを設定できる

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}

@bot.command()
# 今回はon_readyでログイン時に指定チャンネルにEmbedを送信させていますが、on_messageでユーザー入力に反応するときも要領は同じです。
async def shop(ctx):
    embed = discord.Embed( # Embedを定義する
                          title="チェストショップの作り方！",# タイトル
                          color=0x1e90ff, # フレーム色指定(今回は緑
                          description="チェストに在庫を入れて、チェストに接する形で看板を設置してください。",
                          )
    
    embed.add_field(name="看板の書き方",value="一行目:　 (何も書かない)\n二行目: 　売り買いしたい個数\n三行目:　 B<売る値段>:S<買う値段>\n四行目: 　アイテムID\n（アイテムIDはゲーム内で売り買いしたいアイテムを持った状態で\n/iteminfoと打つと出てきます")

    embed.set_footer(text="made by CinnamonSea2073", # フッターには開発者の情報でも入れてみる
                     icon_url="https://images-ext-2.discordapp.net/external/2FdKTBe_yKt6m5hYRdiTAkO0i0HVPkGDOF7lkxN6nO8/%3Fsize%3D128%26overlay/https/crafatar.com/avatars/5d3e654c29bb4ae59e3a5df78372597b.png")

    await ctx.send(embed=embed) # embedの送信には、embed={定義したembed名}


bot.run(TOKEN)
