import discord
from datetime import datetime, date, time
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os


default_greeting = "**{0}**\n<@{1.id}> (`{1.display_name}`)**Left the server!**``` ```"
default_settings = {"EXIT": default_greeting, "ON": False, "CHANNEL": None}

class Exit:
    """Dissmisses new members to the server in the default channel"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/dismissal/settings.json", "load")


    @commands.group(pass_context=True, no_pm=True)
    @checks.admin_or_permissions(manage_server=True)
    async def exitset(self, ctx):
        """Sets dismissal module settings"""
        server = ctx.message.server
        if server.id not in self.settings:
            self.settings[server.id] = default_settings
            self.settings[server.id]["CHANNEL"] = server.default_channel.id
            fileIO("data/dismissal/settings.json","save",self.settings)
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            msg = "```"
            msg += "EXIT: {}\n".format(self.settings[server.id]["EXIT"])
            msg += "CHANNEL: #{}\n".format(self.get_exit_channel(server)) 
            msg += "ON: {}\n".format(self.settings[server.id]["ON"]) 
            msg += "```"
            await self.bot.say(msg)

    @exitset.command(pass_context=True)
    async def message(self, ctx, *, format_msg):
        """Sets the exit message format for the server.

        {0} is the timestamp
        {1} is user
        Default is set to: 
            **{0}**\n<@{1.id}> ({1.display_name}) **Left the server!**``` ```

        Example format:
            {0}\n{1.name} left!
        """
        server = ctx.message.server
        self.settings[server.id]["EXIT"] = format_msg
        fileIO("data/dismissal/settings.json","save",self.settings)
        await self.bot.say("Dismissal message set for the server.")
        await self.send_testing_msg(ctx)

    @exitset.command(pass_context=True)
    async def toggle(self, ctx):
        """Turns on/off dismissing new users to the server"""
        server = ctx.message.server
        self.settings[server.id]["ON"] = not self.settings[server.id]["ON"]
        if self.settings[server.id]["ON"]:
            await self.bot.say("I will now dismiss old users from the server.")
            await self.send_testing_msg(ctx)
        else:
            await self.bot.say("I will no longer dismiss old users.")
        fileIO("data/dismissal/settings.json", "save", self.settings)

    @exitset.command(pass_context=True)
    async def channel(self, ctx, channel : discord.Channel=None): 
        """Sets the channel to send the exit message

        If channel isn't specified, the server's default channel will be used"""
        server = ctx.message.server
        if channel == None:
            channel = ctx.message.server.default_channel
        if not server.get_member(self.bot.user.id).permissions_in(channel).send_messages:
            await self.bot.say("I do not have permissions to send messages to {0.mention}".format(channel))
            return
        self.settings[server.id]["CHANNEL"] = channel.id
        fileIO("data/dismissal/settings.json", "save", self.settings)
        channel = self.get_exit_channel(server)
        await self.bot.send_message(channel,"I will now send dismissal messages to {0.mention}".format(channel))
        await self.send_testing_msg(ctx)


    async def member_remove(self, member):
        server = member.server
        if server.id not in self.settings:
            self.settings[server.id] = default_settings
            self.settings[server.id]["CHANNEL"] = server.default_channel.id
            fileIO("data/dismissal/settings.json","save",self.settings)
        if not self.settings[server.id]["ON"]:
            return
        if server == None:
            print("Server is None. Private Message or some new fangled Discord thing?.. Anyways there be an error, the user was {}".format(member.name))
            return
        channel = self.get_exit_channel(server)
        if self.speak_permissions(server):
            await self.bot.send_message(channel, self.settings[server.id]["EXIT"].format(datetime.now(), member))
        else:
            print("Permissions Error. User that joined: {0.name}".format(member))
            print("Bot doesn't have permissions to send messages to {0.name}'s #{1.name} channel".format(server,channel))


    def get_exit_channel(self, server):
        return server.get_channel(self.settings[server.id]["CHANNEL"])

    def speak_permissions(self, server):
        channel = self.get_exit_channel(server)
        return server.get_member(self.bot.user.id).permissions_in(channel).send_messages

    async def send_testing_msg(self, ctx):
        server = ctx.message.server
        channel = self.get_exit_channel(server)
        await self.bot.send_message(ctx.message.channel, "`Sending a testing message to `{0.mention}".format(channel))
        if self.speak_permissions(server):
            await self.bot.send_message(channel, self.settings[server.id]["EXIT"].format(datetime.now(), ctx.message.author))
        else: 
            await self.bot.send_message(ctx.message.channel,"I do not have permissions to send messages to {0.mention}".format(channel))
        

def check_folders():
    if not os.path.exists("data/dismissal"):
        print("Creating data/dismissal folder...")
        os.makedirs("data/dismissal")

def check_files():
    f = "data/dismissal/settings.json"
    if not fileIO(f, "check"):
        print("Creating dismissal settings.json...")
        fileIO(f, "save", {})


def setup(bot):
    check_folders()
    check_files()
    n = Exit(bot)
    bot.add_listener(n.member_remove,"on_member_remove")
    bot.add_cog(n)
