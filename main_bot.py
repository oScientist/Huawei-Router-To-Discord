import asyncio
import discord
from discord.ext import commands
from HuaweiDiscordFramework import *
import subprocess

TOKEN = ""
intents = discord.Intents.all()
Bot = commands.Bot(command_prefix='!',intents=intents)

Helpmessage = """``Available Commands:
1. on - Turns on the Mac filter.
2. off - Turns off the Mac filter.
3. dhcp - Logged devices.
4. whitelist - Whitelisted devices list.
5. add <mac_address> - Add a device.
6. remove <mac_address> - Remove a device.
7. wlan <on/off> - Turn on/off Wireless Network
8. help - Shows this.
9. restart - Reboots the router.``
"""


Bot.remove_command('help')
@Bot.event
async def on_ready():
    Channel = Bot.get_channel(1183747707563671594)
    Timern = get_current_time()
    devicename = get_device_name()
    await Channel.send(f'[{Timern}] **Logged in as {Bot.user.name} on {devicename} (192.168.100.2).**\n' )

@Bot.command()
async def on(ctx):
    Messages = on1()
    await ctx.send(Messages)
@Bot.command()
async def off(ctx):
    Message2 = off2()
    await ctx.send(Message2)
@Bot.command()
async def dhcp(ctx):
    Message3 = dhcplist1()
    await ctx.send(f'``{Message3}``')
@Bot.command()
async def whitelist(ctx):
    Message4 = get_mac_whitelist()
    await ctx.send(f"``{Message4}``")
@Bot.command()
async def add(ctx, mac_address):
    Reply = add1(mac_address)    
    await ctx.send(Reply)
@Bot.command()
async def remove(ctx, indexnumber):
    reply = remove1(indexnumber)
    await ctx.send(f"``{reply}``")    
@Bot.command()
async def wlan(ctx, option):
   replyme = wlan1(option)
   await ctx.send(replyme)   
@Bot.command()
async def help(ctx):
    await ctx.send(Helpmessage)   
@Bot.command()
async def restart(ctx):
 cec = rebat()
 await ctx.send(cec)
 

async def handle_disconnect():
    while True:
        try:
            if not Bot.is_closed():
                await Bot.wait_until_ready()
                
        except discord.ConnectionClosed:
            
            await asyncio.sleep(5)


async def main():
    await Bot.start(TOKEN)



asyncio.run(main())
