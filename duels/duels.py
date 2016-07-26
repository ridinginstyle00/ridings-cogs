import discord
from discord.ext import commands
from .utils import checks
from .utils.dataIO import dataIO
from __main__ import send_cmd_help
from __main__ import settings
from random import choice
from random import sample
import os
import logging
import aiohttp
import asyncio
import time
import copy


client = discord.Client()

class Duels:

	def __init__(self, bot):
		self.bot = bot
		self.duelist = dataIO.load_json("data/duels/duelist.json")
		self.nuels = "duels"
		self.wlt = dataIO.load_json("data/duels/account.json")
		
	@commands.group(name="duels5", pass_context=True)
	async def _duels(self, ctx):
		"""Duel with another player!!"""
		if ctx.invoked_subcommand is None:
			await send_cmd_help(ctx)
	
	@commands.command(name="duel5", pass_context=True, no_pm=True)
	async def _duel(self, ctx, user: discord.Member=None, otheruser : discord.Member=None):
		"""Duel another player"""
		if not user or not otheruser:
			await self.bot.reply("Please mention two users that you want to see a duel of!")
		elif user.id == otheruser.id:
			await self.bot.reply("Silly, you can't see a duel of someone against themselves!")
		else:
						try:
							nick_player1 = user.name
							nick_player2 = otheruser.name
							action = self.duelist[self.nuels]
							action_damage1, action_damage2, action_damage3, action_damage4 = self.action_damage()
							action_chosen1, action_chosen2, action_chosen3, action_chosen4 = sample(action,4)
							hp_player1 = 30
							hp_player2 = 30
							player1_id = user.id
							player2_id = otheruser.id
				
							await self.bot.say("**{}** dueled **{}**!!\n\nPlease wait for the duel to start! Both players will begin with **{}** health!".format(user.mention, otheruser.mention, hp_player1))
							await asyncio.sleep(1)
							await self.bot.say("**{}** `{}` **{}** and took off **{}** health!".format(nick_player1, action_chosen1, nick_player2, action_damage1))
							hp_player2 = hp_player2 - action_damage1
							await asyncio.sleep(1)
							await self.bot.say("**{}** `{}` **{}** and took off **{}** health!".format(nick_player2, action_chosen2, nick_player1, action_damage2))
							hp_player1 = hp_player1 - action_damage2
							await asyncio.sleep(1)	
							await self.bot.say("**{}** `{}` **{}** and took off **{}** health!".format(nick_player1, action_chosen3, nick_player2, action_damage3))
							hp_player2 = hp_player2 - action_damage3
							await asyncio.sleep(1)
							await self.bot.say("**{}** `{}` **{}** and took off **{}** health!".format(nick_player2, action_chosen2, nick_player1, action_damage4))
							hp_player1 = hp_player1 - action_damage4
	
							if hp_player1 > hp_player2:
								winning_player = nick_player1
								losing_player = nick_player2
								remaining_hp = hp_player1
								await asyncio.sleep(1)	
								await self.bot.say("After 4 rounds of bloody combat, the winner is **{}** with **{}** health!".format(winning_player, remaining_hp))
								if player1_id not in self.wlt:
									self.wlt[player1_id] = {"name": winning_player, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(winning_player))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(winning_player))
									await self.bot.say("{} gained +1 WIN!!".format(winning_player))
									self.wlt[player1_id]["Wins"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 WIN!!".format(winning_player))
									self.wlt[player1_id]["Wins"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
		
								if player2_id not in self.wlt:
									self.wlt[player2_id] = {"name": losing_player, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(losing_player))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(losing_player))
									self.wlt[player2_id]["Losses"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 LOSE!!".format(losing_player))
									self.wlt[player2_id]["Losses"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
						
							elif hp_player1 == hp_player2:
								remaining_hp = hp_player1
								await asyncio.sleep(1)	
								await self.bot.say("After 4 rounds of bloody combat, the winner is **no one because it's a draw** with both players still having **{}** health!".format(remaining_hp))
								if player1_id not in self.wlt:
									self.wlt[player1_id] = {"name": nick_player1, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(nick_player1))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(nick_player1))
									await self.bot.say("{} gained +1 TIE!!".format(nick_player1))
									self.wlt[player1_id]["Ties"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 TIE!!".format(nick_player1))
									self.wlt[player1_id]["Ties"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								
								if player2_id not in self.wlt:
									self.wlt[player2_id] = {"name": nick_player2, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(nick_player2))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(nick_player2))
									await self.bot.say("{} gained +1 TIE!!".format(nick_player2))
									self.wlt[player2_id]["Ties"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 TIE!!".format(nick_player2))
									self.wlt[player2_id]["Ties"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								
							else:
								winning_player = nick_player2
								losing_player = nick_player1
								remaining_hp = hp_player2
								await asyncio.sleep(1)	
								await self.bot.say("After 4 rounds of bloody combat, the winner is **{}** with **{}** health!".format(winning_player, remaining_hp))
								if player2_id not in self.wlt:
									self.wlt[player2_id] = {"name": winning_player, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(winning_player))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(winning_player))
									await self.bot.say("{} gained +1 WIN!!".format(winning_player))
									self.wlt[player2_id]["Wins"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 WIN!!".format(winning_player))
									self.wlt[player2_id]["Wins"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								if player1_id not in self.wlt:
									self.wlt[player1_id] = {"name": losing_player, "Wins": 0, "Losses": 0, "Ties": 0}
									dataIO.save_json("data/duels/account.json", self.wlt)
									await self.bot.say("{} has not yet entered the duel tournament!".format(losing_player))
									await asyncio.sleep(.5)
									await self.bot.say("{} has joined the duel tournament, currently changing settings!".format(losing_player))
									await self.bot.say("{} gained +1 LOSE!!".format(losing_player))
									self.wlt[player1_id]["Losses"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
								else:
									await self.bot.say("{} gained +1 LOSE!!".format(losing_player))
									self.wlt[player1_id]["Losses"] += 1
									dataIO.save_json("data/duels/account.json", self.wlt)
							
						except IndexError:
							await self.bot.say("Uh oh! it seems your list is empty! Add options with %cduels add" % settings.prefixes[0])
						except KeyError:
							await self.bot.say("Uh oh! it seems your list is empty! Add options with %cduels add" % settings.prefixes[0])
	@_duels.command(pass_context=True, no_pm=True)
	@checks.admin_or_permissions(manage_server=True)
	async def add (self, ctx, Duel : str):
		"""Adds a duel to the list"""
		if self.nuels not in self.duelist:
			self.duelist[self.nuels] = []
			dataIO.save_json("data/duels/duelist.json", self.duelist)
		if Duel in self.duelist[self.nuels]:
			await self.bot.say("Uh oh. It seems {} has already been added to the list.".format(Duel))
		else:
			self.duelist[self.nuels].append(Duel)
			dataIO.save_json("data/duels/duelist.json", self.duelist)
			await self.bot.say("{} has been added to the duel list!".format(Duel))
			
	@_duels.command(pass_context=True, no_pm=True)
	async def join(self, ctx, user: discord.Member=None):
		"""Join tournament"""
		user = ctx.message.author	
		if user.id not in self.wlt:
			self.wlt[user.id] = {"name": user.name, "Wins": 0, "Losses": 0, "Ties": 0}
			dataIO.save_json("data/duels/account.json", self.wlt)
			await self.bot.say("{} has joined the tournament!".format(user.mention))
		else:
			await self.bot.say("{} has already joined the tournament".format(user.mention))
			
	@_duels.command(name="stats", pass_context=True)
	async def _stats(self, ctx, user : discord.Member=None):
		"""Show rank and XP of users.

		Defaults to yours."""
		if not user:
			user = ctx.message.author 
			if self.check_joined(user.id):
				await self.bot.say("{}'s stats: **Wins: {} | Losses: {} | Ties: {} **".format(user.name, self.get_wins(user.id),
                                                                         self.get_losses(user.id),
                                                                         self.get_ties(user.id)))
			else:
				await self.bot.say("{}, you are not yet in the tournament!".format(user.mention))
		else:
			if self.check_joined(user.id):
				await self.bot.say("{}'s stats: **Wins: {} | Losses: {} | Ties: {} **".format(user.name, self.get_wins(user.id),
                                                                         self.get_losses(user.id),
                                                                         self.get_ties(user.id)))
			else:
				await self.bot.say("This user has not joined the tournament")
				
	@_duels.command(pass_context=True, no_pm=True)
	async def show (self, ctx):
		"""Shows list of available duels"""
		s = "\n"
		y = s.join(self.duelist[self.nuels])
		await self.bot.say("List of available duel things:\n{}".format(y))
		
	@_duels.command(pass_context=True, no_pm=True)
	async def remove (self, ctx, Duel : str):
		"""removes a duel from the list"""
		try:
			x = self.duelist[self.nuels].remove(Duel)
			if x is not ValueError:
				dataIO.save_json("data/duels/duelist.json", self.duelist)
				await self.bot.say("{} has been successfully removed from the duel list!".format(Duel))
		except ValueError:
			await self.bot.say("I can't remove what hasn't been added to the list to begin with.")
			
	@_duels.command(pass_context=True, no_pm=True)
	async def reset (self, ctx):
		"""For when you have waaay too many duels"""
		if len(self.duelist[self.nuels]) > 0:
			self.duelist[self.nuels] = []
			dataIO.save_json("data/duels/duelist.json", self.duelist)
			await self.bot.say("Duel list has been reset")
		else:
			await self.bot.say("I can't delete a list that's already empty")
			
	def action_choose (self):
		action = choice(sample(self.duelist[self.nuels],1))
		return action

	def multiple_action_choose (self):
		action1 = self.action_choose()
		action2 = self.action_choose()
		action3 = self.action_choose()
		action4 = self.action_choose()
		return action1, action2, action3, action4
		
	def action_damage (self):
		action_chosen1, action_chosen2, action_chosen3, action_chosen4 = self.multiple_action_choose()
		action_damage1 = self.duelist[self.nuels].index(action_chosen1)
		action_damage2 = self.duelist[self.nuels].index(action_chosen2)
		action_damage3 = self.duelist[self.nuels].index(action_chosen3)
		action_damage4 = self.duelist[self.nuels].index(action_chosen4)
		return action_damage1, action_damage2, action_damage3, action_damage4
		
	def check_joined(self, id):
		if id in self.wlt:
			return True
		else:
			return False
			
	def get_wins(self, id):
		if self.check_joined(id):
			return self.wlt[id]["Wins"]

	def get_losses(self, id):
		if self.check_joined(id):
			return self.wlt[id]["Losses"]
			
	def get_ties(self, id):
		if self.check_joined(id):
			return self.wlt[id]["Ties"]
		
def check_folders():
    if not os.path.exists("data/duels"):
        print("Creating data/duels folder...")
        os.mkdir("data/duels")
		
def check_files():
    fp = "data/duels/duelist.json"
    if not dataIO.is_valid_json(fp):
        print("Creating duelist.json...")
        dataIO.save_json(fp, {})
    wlt = "data/duels/account.json"
    if not dataIO.is_valid_json(wlt):
        print("creating account.json...")
        dataIO.save_json(wlt, {})

def setup(bot):
    global logger
    check_folders()
    check_files()
    n = Duels(bot)
    logger = logging.getLogger("red.duels")
    if logger.level == 0: # Prevents the logger from being loaded again in case of module reload
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(filename='data/duels/duels.log', encoding='utf-8', mode='a')
        handler.setFormatter(logging.Formatter('%(asctime)s %(message)s', datefmt="[%d/%m/%Y %H:%M]"))
        logger.addHandler(handler)
    bot.add_cog(n)