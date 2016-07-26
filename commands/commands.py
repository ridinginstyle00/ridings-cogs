import discord
from discord.ext import commands
from .utils import checks
from .utils.dataIO import fileIO
from __main__ import send_cmd_help
import random
from random import choice
from random import sample
import os
import time
import logging
import aiohttp

class Commands:

	def __init__(self, bot):
		self.bot = bot
		self.commands = fileIO("data/commands/commands.json", "load")
		self.fgt = "urafgt"
	
	@commands.command(pass_context=True, no_pm=True)
	async def sc(self, ctx, user : discord.Member=None):
		"""How to screenshot"""
		author = ctx.message.author
		if not user:
			await self.bot.say("{} says to screenshot, you must do this: \n**1)**   Press Prnt Scrn (Windows Key + Prnt Scrn for Windows 8/8.1) on your keyboard.\n**2)**  Click the chatbox.\n**3)**  Then paste. Like you're copying and pasting text (CTRL + V).".format(author.mention))	
		else:
			await self.bot.say("{} tells {} to screenshot, you must do this: \n**1)**   Press Prnt Scrn (Windows Key + Prnt Scrn for Windows 8/8.1) on your keyboard.\n**2)**  Click the chatbox.\n**3)**  Then paste. Like you're copying and pasting text (CTRL + V).".format(author.mention, user.mention))	

	@commands.command(pass_context=True, no_pm=True)
	async def black(self, ctx, user :discord.Member=None):
		"""IGG Black screen/Not Responding"""
		author = ctx.message.author
		if not user:
			await self.bot.say("**{} asks that you please follow these instructions:**\n \n http://igg-games.com/black-screen-cant-start-games.html \n \nCheck the list, if you dont have the program, install it. When you finish checking the list, if you installed even **ONE** of the programs, restart your computer".format(author.mention))
		else:
			await self.bot.say("**{} asks {} that you please follow these instructions:**\n \n http://igg-games.com/black-screen-cant-start-games.html \n \nCheck the list, if you dont have the program, install it. When you finish checking the list, if you installed even **ONE** of the programs, restart your computer".format(author.mention, user.mention))

	@commands.command(pass_context=True, no_pm=True)
	async def sfp(self, ctx, user: discord.Member=None):
		"""Super Falcon Punch"""
		author = ctx.message.author
		if not user:
			await self.bot.say("{} has Super Falcon Punched!".format(author.mention))
			with aiohttp.ClientSession() as session:
				async with session.get("https://cdn.discordapp.com/attachments/172354611477348352/193299243539234817/imgres.jpg") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.png", "wb") as f:
						f.write(test)
			await self.bot.upload("data/commands/Images/imgres.png")
		else:
			await self.bot.say("{} has Super Falcon Punched {} and blew him away!".format(author.mention, user.mention))
			with aiohttp.ClientSession() as session:
				async with session.get("https://cdn.discordapp.com/attachments/172354611477348352/193299243539234817/imgres.jpg") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.png", "wb") as f:
						f.write(test)
			await self.bot.upload("data/commands/Images/imgres.png")
			
	@commands.command(pass_context=True, no_pm=True)
	async def porn(self, ctx, user: discord.Member=None):
		"""Don't even..."""
		author = ctx.message.author
		await self.bot.say("{} Why would you try that!?".format(author.mention))
		with aiohttp.ClientSession() as session:
			async with session.get("https://media.giphy.com/media/x50F9L4tXJcDS/giphy.gif") as resp:
				test = await resp.read()
				with open("data/commands/Images/porn.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/porn.gif")
		
	@commands.command(pass_context=True, no_pm=True)
	async def cavemansponge(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://pbs.twimg.com/profile_images/735571268641001472/kM_lPhzP.jpg") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def bully(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("http://i.imgur.com/Aan5eki.jpg") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def nobully(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("http://i.imgur.com/mTfw7bk.jpg") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def kys(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://images-ext-2.discordapp.net/eyJ1cmwiOiJodHRwczovL2Nkbi5tZW1lLmFtL2luc3RhbmNlcy81MDB4LzY3NTY4NTg0LmpwZyJ9.oNix5m3kkZkmQK5V8uDlLD_fVe0.jpg") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def praiselenny(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://images-2.discordapp.net/.eJwFwVEOgyAMANC7cACwmxTxMoQhAxK1hJYvs7vvvUfNcapdVZHOuzFH40Tj0Cw0Ysm6EJUzx95YJ7pMFImpXvkWNuDsa8Vt2Tw6sICABjygtR5gsevboUdrqIbPlEDfkGgOzoHb0P0u6vcH9hAoLA.eXBAkxrHMhUgUqy17NfChORgTOg.png?width=400&height=225") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def donttouchme(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://images-2.discordapp.net/.eJwNzE1ygjAYANC7sC_wBUiIOxSo0hZ0lFLcMIhMoAX5SYKI07u37wDvqcixUVZKJUTPV5p2rXnRjVeVi27MWamyrmNNmfc1V4uu1XIh8qJqy5vgGhALmdjWbYoJWIABa0CBEtu0ECIEDMMAQyuDe3hvvIg9nA8n3JDCWb-B-e6j2fkZfK_St7qQmUzoQtr9ES9tg2CZP1mEzjIl4QnpNaCwz6d4HGZytIzzOo4pmWzJPNf18bU78cDdEPn_1t5xE6fMjZLD_rF7pQlYWbC_cPias2nS65Kpw9IH2eL7_KXcDenQFvlhiy_nW0NT9btnyu8ftc9YBA.6Vs2kyeZ-HsZADyrwAqldkWs8hg.jpg?width=289&height=299") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.png")
		
	@commands.command(pass_context=True, no_pm=True)
	async def facepalm(self, ctx, user : discord.Member = None):
		"""Facepalm yourself"""
		author = ctx.message.author
		if not user:
			await self.bot.say("{} facepalmed his/her self!".format(author.mention))
		else:
			await self.bot.say("{} facepalmed his/her self due to {}'s actions!".format(author.mention, user.mention))
			
	@commands.command(pass_context=True, no_pm=True)
	async def realcopypasta(self, ctx):
		"""Real Copy Pasta"""
		await self.bot.say("WHATA FUCK MAN xD i just fall of my chair kuz i couldnt and i CANT stop laugh xDXDXDXDXDDDDDDDDDDDDXXXXXXXXXXXXXXXXXXXDDDDDDDDDDDDDDDDDDD OMGOSH DDDDDXXXXXXXXXXXXXXXXXXXXXXXDDDDDDDDDDDDDDDDDDDDDDDDDDDD DDDDDD LOOOOOOOOOLLLLL THIS IS A SHIT XDDDDDDDDDDDDDDDDDDDDXDDDDDDDDDDDDDDDDDDDDD A BIG ONE XDDDDDDDD A GRAT ONE XXXXXXDDDD CONGRATS MAN XD")
			
	@commands.command(pass_context=True, no_pm=True)
	async def suckmydonut(self, ctx, user : discord.Member = None):
		"""Caveman Sponge"""
		author = ctx.message.author
		if not user:
			with aiohttp.ClientSession() as session:
				async with session.get("http://owned.com/media/_cache/adjusted/postblock/image/4/6/7/2/4672.jpg.png") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.png", "wb") as f:
						f.write(test)
						await self.bot.say("{} says to:".format(author.mention))
			await self.bot.upload("data/commands/Images/imgres.png")
		else:
			with aiohttp.ClientSession() as session:
				async with session.get("http://owned.com/media/_cache/adjusted/postblock/image/4/6/7/2/4672.jpg.png") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.png", "wb") as f:
						f.write(test)
						await self.bot.say("{} tells {} to:".format(author.mention, user.mention))
			await self.bot.upload("data/commands/Images/imgres.png")
			
	@commands.command(pass_context=True, no_pm=True)
	@checks.admin_or_permissions(manage_server=True)
	async def spank(self, ctx, user : discord.Member = None):
		"""Spank"""
		author = ctx.message.author
		if not user:
			with aiohttp.ClientSession() as session:
				async with session.get("https://images-ext-1.discordapp.net/eyJ1cmwiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMDc5NDI2NTIyNzU2MDE0MDgvMTA3OTQ1MDg3MzUwMDc5NDg4L1R1SEdKLmdpZiJ9.-XeFHSFOR0nv53M34HeUBqQc7Wc.gif") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.gif", "wb") as f:
						f.write(test)
						await self.bot.say("{} spanked someone! :scream:".format(author.mention))
			await self.bot.upload("data/commands/Images/imgres.gif")
		else:
			with aiohttp.ClientSession() as session:
				async with session.get("https://images-ext-1.discordapp.net/eyJ1cmwiOiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdHRhY2htZW50cy8xMDc5NDI2NTIyNzU2MDE0MDgvMTA3OTQ1MDg3MzUwMDc5NDg4L1R1SEdKLmdpZiJ9.-XeFHSFOR0nv53M34HeUBqQc7Wc.gif") as resp:
					test = await resp.read()
					with open("data/commands/Images/imgres.gif", "wb") as f:
						f.write(test)
						await self.bot.say("{} spanked {}! :scream:".format(author.mention, user.mention))
			await self.bot.upload("data/commands/Images/imgres.gif")
			
	@commands.command(pass_context=True, no_pm=True)
	async def knowyourplace(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://media.giphy.com/media/PcNqCl1OsVYre/giphy.gif") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.gif")
		
	@commands.command(pass_context=True, no_pm=True)
	async def honk(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://images-2.discordapp.net/.eJwFwcENwyAMAMBdGAAHDAVnGwSUICV1hN1X1N1795jvOs1uDtVbdoA2pfJqVpRXGd0O5nH2ck-xlS8oqqUeV_-ogNtoi-gxhERImZwHRy8MKSaPDqP3LmVomeyYb_P7A3heIJU.GyQkra1LBGCzKzEMLjx_uAtFNoc.gif") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.gif")
		
	@commands.command(pass_context=True, no_pm=True)
	async def lenny(self, ctx):
		"""Caveman Sponge"""
		author = ctx.message.author
		with aiohttp.ClientSession() as session:
			async with session.get("https://cdn.discordapp.com/attachments/105010597954871296/195260231301726210/eJwFwcENwyAMAMBdGABjORjICp0CEUKQIETgPqqqu_fuq96zqV1dIs_aAY660piHXjJmLFmXMUrL8alLp9EhisR09XzLAnTkvQvMhhDREzFgMNZvBi2hZd6CcVB7e7lP0aWe6vcHA6MiZA.JU3c8-28Pi5_ejkRZusCEFRk7kk.gif") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.gif")
		
	@commands.command(pass_context=True, no_pm=True)
	async def urafgt(self, ctx):
		"""Super Falcon Punch"""
		author = ctx.message.author
		foo = ["https://media.giphy.com/media/13r5cLwRjhteQE/giphy.gif", "https://cdn.discordapp.com/attachments/112306806658772992/148872883932758017/yyI9LEZ.gif"]
		with aiohttp.ClientSession() as session:
			async with session.get("{}".format(random.choice(foo))) as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.gif")
		
	@commands.command(pass_context=True, no_pm=True)
	async def datboi(self, ctx):
		"""Dait Boi"""
		author = ctx.message.author
		foo = ["http://i1.kym-cdn.com/photos/images/newsfeed/001/112/704/8a8.jpg", "http://2static.fjcdn.com/pictures/Origins_3c4898_5920950.jpg", "http://i3.kym-cdn.com/photos/images/original/001/116/633/8e9.jpg", "http://www.kappit.com/img/pics/201605_1023_iagcb_sm.jpg", "https://img0.etsystatic.com/125/1/12078849/il_340x270.969775168_rzq8.jpg", "https://i.ytimg.com/vi/fs5Sudmauks/maxresdefault.jpg", "http://i1.kym-cdn.com/photos/images/original/001/118/006/5b1.jpg", "http://i3.kym-cdn.com/photos/images/newsfeed/001/118/078/22b.jpeg", "http://i3.kym-cdn.com/photos/images/newsfeed/001/118/014/e78.png", "https://images-ext-1.discordapp.net/eyJ1cmwiOiJodHRwOi8vY2RuLnNtb3NoLmNvbS9zaXRlcy9kZWZhdWx0L2ZpbGVzLzIwMTYvMDUvZGF0LWJvaS1tZW1lcy1ib3ktd2hvLWxpdmVkLmpwZyJ9.WBSEhlT69xiEWq0KRgR90j9YwDA.jpg?width=243&height=249", "http://i2.kym-cdn.com/photos/images/newsfeed/001/112/712/650.jpg"]
		with aiohttp.ClientSession() as session:
			async with session.get("{}".format(random.choice(foo))) as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.png", "wb") as f:
					f.write(test)
					await self.bot.say("Here comes dat boi! o shit waddup!:\n")
		await self.bot.upload("data/commands/Images/imgres.png")

	@commands.command(pass_context=True, no_pm=True)
	async def kirito(self, ctx, user: discord.Member=None):
		"""Don't even..."""
		author = ctx.message.author
		await self.bot.say("{} Oh but of course:".format(author.mention))
		with aiohttp.ClientSession() as session:
			async with session.get("https://images-2.discordapp.net/eyJ1cmwiOiJodHRwczovL2Rpc2NvcmQuc3RvcmFnZS5nb29nbGVhcGlzLmNvbS9hdHRhY2htZW50cy8xNzUyNDY4MDg5NjcxNTE2MTYvMTkxMzA0MzA5Njg0Njk5MTM3L0NpaENKRHRVb0FBS0QyUS5qcGcifQ.BpVypO0y2BQ9akgeyTBXG1kI1a0.jpg?width=281&height=299") as resp:
				test = await resp.read()
				with open("data/commands/Images/imgres.jpg", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/imgres.jpg")
		
	@commands.command(pass_context=True, no_pm=True)
	async def pussy(self, ctx, user: discord.Member=None):
		"""Don't even..."""
		author = ctx.message.author
		await self.bot.say("{} What were you hoping to see!?".format(author.mention))
		with aiohttp.ClientSession() as session:
			async with session.get("https://media.giphy.com/media/cu8kC3h8SmuBy/giphy-tumblr.gif") as resp:
				test = await resp.read()
				with open("data/commands/Images/pussy.gif", "wb") as f:
					f.write(test)
		await self.bot.upload("data/commands/Images/pussy.gif")
		
	@commands.command(name="alertmods", pass_context=True, no_pm=True)
	async def _alertmods(self, ctx, *, message = "", user : discord.Member = None):
		"""Get help"""
		author = ctx.message.author
		roles = "<@&190315908562944001> <@&187073925442830336> <@&189313142612951041>"
		if message:
			await self.bot.say("{} : {} needs your help!\nReasoning : **{}**".format(roles, author.mention, message))
		else:
			await self.bot.say("{} : {} needs your help!\nNext time, add your message to the end of the command, so that the issue is stated there as well\n\nExmple: `alertmods Message goes here`\n\n```THAT DOES NOT MEAN, TO CALL THE COMMAND AGAIN WITH THE MESSAGE! ONLY A REMINDER!\n\nIF YOU CALL THIS COMMAND WITH THE MESSAGE RIGHT AFTER THIS MESSAGE, THEN YOU WILL BE PUNISHED!!```".format(roles, author.mention))

def check_folders():
    if not os.path.exists("data/commands"):
        print("Creating data/commands folder...")
        os.mkdir("data/commands")
    if not os.path.exists("data/commands/Images"):
        print("Creating data/commands/Images folder...")
        os.mkdir("data/commands/Images")


def check_files():
    fp = "data/commands/commands.json"
    if not fileIO(fp, "check"):
        print("Creating commands.json...")
        fileIO(fp, "save", {})

def setup(bot):
    global logger
    check_folders()
    check_files()
    n = Commands(bot)
    logger = logging.getLogger("red.commands")
    if logger.level == 0: # Prevents the logger from being loaded again in case of module reload
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='data/commands/commands.log', encoding='utf-8', mode='a')
        handler.setFormatter(logging.Formatter('%(asctime)s %(message)s', datefmt="[%d/%m/%Y %H:%M]"))
        logger.addHandler(handler)
    bot.add_cog(n)