import discord
from discord.ext import commands
from .utils import checks
from .utils.dataIO import fileIO
from __main__ import send_cmd_help
from random import randint
import os
import time

client = discord.Client()

class Levels:

    def __init__(self, bot):
        self.bot = bot
        self.cooldown = 60
        self.leader_board = fileIO("data/levels/leader_board.json", "load")
        self.gettingxp = {}
        self.xp_gaining_channels = []

    @commands.group(name="rank", pass_context=True)
    async def _rank(self, ctx):
        """Rank operations"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_rank.command(pass_context=True, no_pm=True)
    async def join(self, ctx, user: discord.Member=None):
        """Join ranking system"""
        if not user:
            user = ctx.message.author
            if user.id not in self.leader_board:
                self.leader_board[user.id] = {"name": user.name, "rank": 0, "XP": 0}
                fileIO("data/levels/leader_board.json", "save", self.leader_board)
                await self.bot.say("{} has joined the Levelboard!".format(user.mention))
            else:
                await self.bot.say("{} has already joined and is rank {}".format(user.mention, str(self.get_rank(user.id))))
        else:
            if user.id not in self.leader_board:
                self.leader_board[user.id] = {"name": user.name, "rank": 0, "XP": 0}
                fileIO("data/levels/leader_board.json", "save", self.leader_board)
                await self.bot.say("{} has joined the Levelboard!".format(user.mention))
            else:
                await self.bot.say("{} has already joined and is rank {}".format(user.mention, str(self.get_rank(user.id))))

    @_rank.command(name="set", pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_server=True)
    async def _set(self, ctx, user : discord.Member, rank : int, xp : int):
        """Set Rank and EXP"""
        if user.id in self.leader_board:
            self.leader_board[user.id] = {"name": user.name, "rank": rank, "XP": xp}
            fileIO("data/levels/leader_board.json", "save", self.leader_board)
            await self.bot.say("{}'s current stats are now: **Rank: {} XP {}/{}**".format(user.mention, self.get_rank(user.id),
                                                                         self.get_xp(user.id),
                                                                         self.get_level_xp(int(self.leader_board[user.id]["rank"]))))
        else:
            await self.bot.say("{} is not in the levelboard. Please make {} do `{}rank join` so their XP and Rank can be set!".format(user.mention, user.mention, ctx.prefix))
			
    @_rank.command(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_server=True)
    async def reset(self, ctx, user : discord.Member=None):
        """Resets your rank and EXP! UNDOABLE!!!"""
        if not user:
            user = ctx.message.author
            if user.id in self.leader_board:
                self.leader_board[user.id] = {"name": user.name, "rank": 0, "XP": 0}
                fileIO("data/levels/leader_board.json", "save", self.leader_board)
                await self.bot.say("{} has been reset in the Levelboard!".format(user.mention))
            else:
                await self.bot.say("{} has not yet joined in the Levelboard! Do `{}rank join`!".format(user.mention, ctx.prefix))
        else:
            if user.id in self.leader_board:
                self.leader_board[user.id] = {"name": user.name, "rank": 0, "XP": 0}
                fileIO("data/levels/leader_board.json", "save", self.leader_board)
                await self.bot.say("{} has been reset in the Levelboard!".format(user.mention))
            else:
                await self.bot.say("{} has not yet joined in the Levelboard! Do `{}rank join`!".format(user.mention, ctx.prefix))
    @_rank.command(name="show", pass_context=True)
    async def _show(self, ctx, user : discord.Member=None):
        """Show rank and XP of users.

        Defaults to yours."""
        if not user:
            user = ctx.message.author  # LEVEL 13 | XP 1438/1595 | TOTAL XP 9888 | Rank 5/829
            if self.check_joined(user.id):
                await self.bot.say("{} **LEVEL {} | XP {}/{} **".format(user.name, self.get_rank(user.id),
                                                                         self.get_xp(user.id),
                                                                         self.get_level_xp(int(self.leader_board[user.id]["rank"]))))
            else:
                await self.bot.say("{} you are not in the ranking system. Type `{}rank join` to join".format(user.mention, ctx.prefix))
        else:
            if self.check_joined(user.id):
                rank = self.get_rank(user.id)
                xp = self.get_xp(user.id)
                await self.bot.say("{}'s stats: **LEVEL {} | XP {}/{} **".format(user.mention, self.get_rank(user.id),
                                                                         self.get_xp(user.id),
                                                                         self.get_level_xp(int(self.leader_board[user.id]["rank"]))))
            else:
                await self.bot.say("this user has not joined the rank system")

    @_rank.command(pass_context=True)
    async def levelup(self, ctx):
        """level up. Mainly used in case Auto-Leveling doesn't work!"""
        user = ctx.message.author
        if self.leader_board[user.id]["XP"] >= self.get_level_xp(self.leader_board[user.id]["rank"]):
            self.leader_board[user.id]["rank"] += 1
            self.leader_board[user.id]["XP"] -= self.get_level_xp(self.leader_board[user.id]["rank"])
            await self.bot.say("{}: Level Up! You are now level {}".format(user.mention,
                                                                           self.leader_board[user.id]["rank"]))
        else:
            await self.bot.say("You are not ready to level up yet {}".format(user.mention))
			
    @_rank.command(pass_context=True, no_pm=True)
    async def creators(self, ctx):
        """Shows the creators of the Rank cog!"""
        user = ctx.message.author
        await self.bot.say("```There were hard efforts in the making of this cog.\n \n It took LOTS of time to make a ranking system for RED, that could replace MEE6's ranking system \n \n Here is the list of creators for this cog: \n \n funnyman \n \n Ridinginstyle00 \n \n We appreciate the help from others that helped us!!```")

    @commands.group(name="cooldown", pass_context=True)
    async def _cooldown(self, ctx):
        """cooldown options"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @_cooldown.command(pass_contex=True)
    @checks.is_owner()
    async def set(self, cooldown: int=60):
        """sets XP cool down interval"""
        self.cooldown = cooldown

    @commands.command()
    async def levelboard(self, top: int=10):
        """Prints out the rank leaderboard
        Defaults to top 10"""  # Originally coded by Airenkun - edited by irdumb - edited for ranking by Funnyman2213
        if top < 1:
            top = 10
        if top > 20:
            top = 20
        leader_board_sorted = sorted(self.leader_board.items(), key=lambda x: x[1]["rank"], reverse=True)
        if len(leader_board_sorted) < top:
            top = len(leader_board_sorted)
        topten = leader_board_sorted[:top]
        highscore = ""
        place = 1
        for id in topten:
            highscore += str(place).ljust(len(str(top)) + 1)
            highscore += (id[1]["name"] + " ").ljust(23 - len(str(id[1]["rank"])))
            highscore += str(id[1]["rank"]) + "\n"
            place += 1
        if highscore:
            if len(highscore) < 1985:
                await self.bot.say("```py\n" + highscore + "```")
            else:
                await self.bot.say("The leaderboard is too big to be displayed. Try with a lower <top> parameter.")
        else:
            await self.bot.say("No one has joined the rank system.")
			
    async def gain_xp(self, message):
        user = message.author
        id = user.id
        if self.check_joined(id):
            if id in self.gettingxp:
                seconds = abs(self.gettingxp[id] - int(time.perf_counter()))
                if seconds >= self.cooldown:
                    self.add_xp(id)
                    self.gettingxp[id] = int(time.perf_counter())
                    fileIO("data/levels/leader_board.json", "save", self.leader_board)
                if self.leader_board[user.id]["XP"] >= self.get_level_xp(self.leader_board[user.id]["rank"]):
                    self.leader_board[user.id]["rank"] += 1
                    self.leader_board[user.id]["XP"] = 0
                    msg = '{} **has leveled up and is now level {}!!!\n HURRAY!!**'
                    msg = msg.format(message.author.mention, self.leader_board[user.id]["rank"])
                    await self.bot.send_message(message.channel, msg)
                    fileIO("data/levels/leader_board.json", "save", self.leader_board)
            else:
                self.add_xp(id)
                self.gettingxp[id] = int(time.perf_counter())
                fileIO("data/levels/leader_board.json", "save", self.leader_board)

    def add_xp(self, id):
        if self.check_joined(id):
            self.leader_board[id]["XP"] += int(randint(15, 20))

    def mention_from_id(self, id):
        return "@" + str(self.leader_board[id]["name"]) + "#" + str(id)

    def get_level_xp(self, level):
        xp = 5*(int(level)**2)+50*int(level)+100
        return xp

    def check_joined(self, id):
        if id in self.leader_board:
            return True
        else:
            return False

    def get_rank(self, id):
        if self.check_joined(id):
            return self.leader_board[id]["rank"]

    def get_xp(self, id):
        if self.check_joined(id):
            return self.leader_board[id]["XP"]

    def display_time(self, seconds, granularity=2):  # What would I ever do without stackoverflow?
        intervals = (  # Source: http://stackoverflow.com/a/24542445
            ('weeks', 604800),  # 60 * 60 * 24 * 7
            ('days', 86400),  # 60 * 60 * 24
            ('hours', 3600),  # 60 * 60
            ('minutes', 60),
            ('seconds', 1),
        )

        result = []

        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append("{} {}".format(value, name))
        return ', '.join(result[:granularity])


def check_folders():
    if not os.path.exists("data/levels"):
        print("Creating data/levels folder...")
        os.mkdir("data/levels")


def check_files():
    fp = "data/levels/leader_board.json"
    if not fileIO(fp, "check"):
        print("Creating empty Leader board...")
        fileIO(fp, "save", {})


def setup(bot):
    check_folders()
    check_files()
    n = Levels(bot)
    bot.add_listener(n.gain_xp, "on_message")
    bot.add_cog(n)
