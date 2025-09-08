import os
import requests
import configparser
import discord
from discord import app_commands
from discord.ext import commands

# 讀取設定檔
BASE_DIR = os.path.dirname(__file__)
config_path = os.path.join(BASE_DIR, "config.ini")
config = configparser.ConfigParser()
config.read(config_path)

API_KEY = config["maple"]["API_KEY"]
API_URL = config["maple"]["API_URL"]
OCID_URL = config["maple"]["OCID_URL"]

headers = {"x-nxopen-api-key": API_KEY}

# Discord Bot Client
intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)
#client = discord.Client(intents=intents)

DISCORD_TOKEN = config["discord"]["TOKEN"]
CHANNEL_ID = int(config["discord"]["CHANNEL_ID"])

#抓取角色ID
def get_ID(name):
    response = requests.get(OCID_URL, headers=headers, params={"character_name": name})
    if response.status_code == 200:
        data = response.json()
        OCID = data["ocid"]
        return OCID
    else:
        return None

#抓取角色資訊
def get_character_data(name):
    response = requests.get(API_URL, headers=headers, params={"ocid": get_ID(name)})
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(response.status_code, response.text)
        return None

# Slash Command: /角色
@client.tree.command(name="角色", description="查詢角色資訊")
@app_commands.describe(name="角色名稱")
async def character(interaction: discord.Interaction, name: str):
    get_data = get_character_data(name)
    channel = client.get_channel(CHANNEL_ID)
    if channel and get_data:
        #排版
        embed = discord.Embed(
            title=f"角色查詢結果 - {get_data['character_name']}",
            color=0x00ffcc
        )
        embed.add_field(name="等級", value=get_data["character_level"], inline=True)
        embed.add_field(name="職業", value=get_data["character_class"], inline=True)
        embed.add_field(name="性別", value=get_data["character_gender"], inline=True)
        # 加上角色頭像
        if "character_image" in get_data:
            embed.set_thumbnail(url=get_data["character_image"])
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(
            title="錯誤",
            description="無法找到指定的頻道或角色資料",
            color=0xff0000
        )
        print("無法找到指定的頻道或角色資料")
        await interaction.response.send_message(embed=embed)
@client.event
async def on_ready():
    print(f"✅ 已登入 Discord Bot：{client.user}")
    try:
        synced = await client.tree.sync()
        print(f"Slash Commands 已同步：{len(synced)} 個")
    except Exception as e:
        print(e)

client.run(DISCORD_TOKEN)