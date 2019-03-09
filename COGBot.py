import discord
from discord.ext import commands
import asyncio
import COGBotToken

moderator_delete = 0

messageChannel = discord.Object(id="447299800761892865")
serverLogsChannel = discord.Object(id="343796978280300555")
welcomeChannel = discord.Object(id="151656795016790017")
roleMessageID = "545157694944706573"

liveserverid = "151656795016790017"
livechannelid = "447299800761892865"
editlogid = discord.Object(id="548484235976245258")
deletelogid = discord.Object(id="548484352212992010")

# Emojis and Reactions

eiagree = "<:iagree:445865909136130058>"
edestinytwo = "<:DestinyTwo:430665230293532682>"
egmod = "<:GMod:352762291382517760>"
eothergames = "<:OTHERGAMES:387858666973298688>"
eoverwatch = "<:Overwatch:329180882277498880>"
ebattleroyale = "<:BattleRoyale:430659965708140575>"
erainbowsixsiege = "<:RainbowSixSiege:430658203328577536>"
eseaofthieves = "<:SeaOfThieves:430666886347489300>"
etitanfalltwo = "<:Titanfall2:278835758998224896>"
ewarframe = "<:Warframe:363829883908128780>"
ecoglogo = "<:COGlogo:406981453923221515>"
eark = "<:ark:455602617821691914>"
eseeall = "<:seeall:455608619409473536>"
emonster = "<:MonsterHunter:482885427964018706>"
eapex = "<:Apex_legends:542237535036899328>"

ruleschannel = "<#343977843035996161>"

inviteMessage = f"""So, you want to invite your friends to COG?
We are always happy to have new and friendly faces in {ecoglogo}.
Before sending them an invite, please ensure they are 16+ (See {ruleschannel}).

Invite link: `https://discord.gg/6Vnd9MK`

Thanks for helping grow COG and keeping this community united 👍🏻."""

musicPMMessage = """Here are some useful commands for COG's **DJ Bots**

Rythm has every command you need to have a great music experience, these include:
                            -----------------------------
**play**     Plays a song with the given name or url.
**disconnect**     Disconnect the bot from the voice channel it is in.
**np**     Shows what song the bot is currently playing.
**aliases**     List command aliases.
**skip**     Skips the currently playing song.
**seek**     Seeks to a certain point in the current track.
**soundcloud**     Searches soundcloud for a song.
**search**     Searches YouTube for results of a URL.
**loop**     Loop the currently playing song.
**join**     Summons the bot to your voice channel.
**lyrics**     Gets the lyrics of the current playing song.
**resume**     Resume paused music.
**skipto**     Skips to a certain position in the queue.
**clear**     Clears the queue.
**replay**     Reset the progress of the current song
**pause**     Pauses the currently playing track.
**removedupes**     Removes duplicate songs from the queue.
**playtop**     Like the play command, but queues from the top.
**shuffle**     Shuffles the queue.
**queue**     View the queue. To view different pages, type the command with the specified page number after it (queue 2).

                            -----------------------------
For *OTHER* DJ Commands you can find them by typing: `!aliases`

**__NOTE__** *some commands require **DJ** role. These will be given to certain members and regular __trusted__ users* 😉."""


class EmojiCommands:
    def __init__(self, bot):
        self.bot = bot



    @commands.command(pass_context=True, no_pm=True)
    async def invite(self, ctx):
        await bot.say(inviteMessage)

    @commands.command(pass_context=True, no_pm=True)
    async def djcommands(self, ctx):
        msg = await bot.send_message(ctx.message.channel,
                                     f"{ctx.message.author.mention}, a list of DJ Commands has been sent to your Private Messages")
        await bot.send_message(ctx.message.author, musicPMMessage)
        await asyncio.sleep(5)
        await bot.delete_message(msg)

    @commands.command(pass_context=True, no_pm=True)
    async def gethelp(self, ctx):
        user = ctx.message.author.mention
        await bot.send_message(ctx.message.channel, f"""❓ ❓ ❓ ❓ ❓ ❓ ❓ ❓ ❓
I'll call for help for you 😉

*In the meantime if you haven't posted your* **Question/Problem** *please do so now!*

{user} would like some help <@&181980396542492683> ⚠""")

    @commands.command(pass_context=True, no_pm=True)
    async def suggest(self, ctx, *, msg: str):
        author = ctx.message.author.mention
        message = await bot.say(f"""{author} has suggested:
```{msg}```
To make your own suggestion, type `.suggest [Your suggestion here.]`.

Please click the reaction below to vote.""")
        emojis = message.server.emojis
        for e in ["voteyes", "voteno"]:
            emoji = discord.utils.get(emojis, name=e)
            await bot.add_reaction(message, emoji)
        await asyncio.sleep(5)
        await bot.delete_message(ctx.message)

    @commands.command(pass_context=True, no_pm=True)
    async def howtoplaymusic(self, ctx):
        author = ctx.message.author.mention
        msg = await bot.say(f"""{author},
**__!🎶| DJ (.howtoplaymusic)__**:
1. Type: **!join** - the bot will join to your current channel (Please use <#257033350487736321>).
2. Type: **!play [URL/song]** - this will add the video to the *!queue*.

                **!djcommands** for more commands.

                           --------
*If bot is too loud just right click it and lower the 'user volume'.*

Still stuck type: *!aliases*.""")
        await asyncio.sleep(120)
        await bot.delete_message(msg)



bot = commands.Bot(command_prefix='.')
bot.add_cog(EmojiCommands(bot))




async def postMessage(roleName, status, user):
    msg = await bot.send_message(messageChannel, user.mention + f": {roleName} role has been {status}.")
    await deleteMessage(msg)


async def postWelcome(user):

    userRoles = ""
    for y in user.roles:
        userRoles += y.name + ", "
    #print(userRoles[:-2])

    await asyncio.sleep(60)

    embed = discord.Embed(title="Welcome to COG!", color=0x6093c4)
    embed.set_author(name=user.display_name, icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text=f"Roles: {userRoles[:-2]}")
    msg = await bot.send_message(welcomeChannel, embed=embed)
    await bot.add_reaction(msg, "👋")


async def deleteMessage(msg):
    await asyncio.sleep(5)
    await bot.delete_message(msg)


async def giveRole(ref, role, user):
    newRole = discord.utils.get(ref, name=role)
    await bot.add_roles(user, newRole)


async def takeRole(ref, role, user):
    oldRole = discord.utils.get(ref, name=role)
    await bot.remove_roles(user, oldRole)


@bot.event
async def on_command_error(error, ctx):
    print(error)
    author = ctx.message.author.mention
    if not str(error).startswith('Command'):
        msg = await bot.send_message(ctx.message.channel, f"""{author}, you have not entered a suggestion. 
Try again with `.suggest [Your suggestion here.]`""")
        await asyncio.sleep(5)
        await bot.delete_message(msg)
        await bot.delete_message(ctx.message)

@bot.event
async def on_reaction_add(reaction, user):
    roles = reaction.message.server.roles
    role = ""
    print(reaction.message.id)
    if not user.bot:
        if reaction.message.id == roleMessageID:
            if reaction.emoji.name == "iagree":
                role = "Friends"
            if "friends" in [y.name.lower() for y in user.roles]:
                if reaction.emoji.name == "DestinyTwo":
                    role = "Destiny"
                elif reaction.emoji.name == "Apex_legends":
                    role = "Apex Legends"
                elif reaction.emoji.name == "Anthem":
                    role = "Anthem"
                elif reaction.emoji.name == "MonsterHunter":
                    role = "Monster Hunter"
                elif reaction.emoji.name == "OTHERGAMES":
                    role = "OTHER GAMES"
                elif reaction.emoji.name == "Overwatch":
                    role = "Overwatch"
                elif reaction.emoji.name == "BattleRoyale":
                    role = "Battle Royale"
                elif reaction.emoji.name == "RainbowSixSiege":
                    role = "Rainbow Six Siege"
                elif reaction.emoji.name == "Titanfall2":
                    role = "Titanfall"
                elif reaction.emoji.name == "Warframe":
                    role = "Warframe"
                elif reaction.emoji.name == "seeall":
                    role = "See EVERYTHING"
            else:
                if role is not "Friends":
                    msg = await bot.send_message(messageChannel, user.mention + ": You must agree to the server rules before adding game roles.")
                    await bot.remove_reaction(reaction.message, reaction.emoji, user)
                    await deleteMessage(msg)

    if role is not "Friends" and role is not "":
        await giveRole(roles, role, user)
        await postMessage(role, "given", user)

    if role == "Friends":
        if not "friends" in [y.name.lower() for y in user.roles]:
            await giveRole(roles, role, user)
            msg = await bot.send_message(messageChannel, user.mention + ": Thank you for agreeing to the server rules.")
            await bot.send_message(serverLogsChannel, user.mention + " has agreed to the server rules.")
            await asyncio.sleep(5)
            await deleteMessage(msg)
            await postWelcome(user)
            


@bot.event
async def on_reaction_remove(reaction, user):
    roles = reaction.message.server.roles
    role = ""
    if not user.bot:
        if reaction.message.id == roleMessageID:
            if "friends" in [y.name.lower() for y in user.roles]:
                if reaction.emoji.name == "iagree":
                    role = "Friends"
                elif reaction.emoji.name == "DestinyTwo":
                    role = "Destiny"
                elif reaction.emoji.name == "MonsterHunter":
                    role = "Monster Hunter"
                elif reaction.emoji.name == "OTHERGAMES":
                    role = "OTHER GAMES"
                elif reaction.emoji.name == "Overwatch":
                    role = "Overwatch"
                elif reaction.emoji.name == "BattleRoyale":
                    role = "Battle Royale"
                elif reaction.emoji.name == "RainbowSixSiege":
                    role = "Rainbow Six Siege"
                elif reaction.emoji.name == "Titanfall2":
                    role = "Titanfall"
                elif reaction.emoji.name == "Warframe":
                    role = "Warframe"
                elif reaction.emoji.name == "Apex_legends":
                    role = "Apex Legends"
                elif reaction.emoji.name == "Anthem":
                    role = "Anthem"
                elif reaction.emoji.name == "seeall":
                    role = "See EVERYTHING"

    if role is not "Friends" and role is not "":
        await takeRole(roles, role, user)
        await postMessage(role, "taken", user)

    if role == "Friends":
        msg = await bot.send_message(messageChannel, user.mention + ": You can't unagree to the rules.")
        await bot.send_message(serverLogsChannel, user.mention + " has attempted to unagree to the server rules.")
        await asyncio.sleep(5)
        await deleteMessage(msg)

@bot.event
async def on_message_edit(before, after):
    if after.content != before.content:
        if after.content is not None:
            author = before.author.mention

            await bot.send_message(editlogid, f"""==========
A message in {before.channel.mention} has been edited by {author}.
        
Original: ```{before.content}```
Edited: ```{after.content}```""")

@bot.event
async def on_message_delete(message):
    global moderator_delete

    if moderator_delete == 0:
        print(f"Deletion triggered by {message.author}")
        if message.content is not None:
            if not message.author.id == "445867817707896834":
                if not message.channel.id == "447299800761892865":
                    await bot.send_message(deletelogid, f"""==========
A message has been deleted from {message.channel.mention}.
        
Author: {message.author.mention}
Content: ```{message.content}```""")


async def moderatorDelete(reaction, user):
    global moderator_delete

    moderator_delete = 1
    await bot.send_message(deletelogid, f"""==========
A message has been deleted from {reaction.message.channel.mention} by {user.mention}.

Author: {reaction.message.author.mention}
Content: ```{reaction.message.content}```""")
    await bot.delete_message(reaction.message)
    await asyncio.sleep(0.5)
    moderator_delete = 0

@bot.event
async def on_member_join(member):
    await bot.send_message(serverLogsChannel, member.mention + " has joined the server.")


@bot.event
async def on_member_remove(member):
    await bot.send_message(serverLogsChannel, member.mention + " has left the server.")


@bot.event
async def on_member_ban(member):
    await bot.send_message(serverLogsChannel, member.mention + "  has been banned from the server.")


@bot.event
async def on_member_unban(server, user):
    await bot.send_message(serverLogsChannel, user.mention + " has been unbanned from the server.")


@bot.event
async def on_ready():
    #i = 0
    #msg = None

    server = bot.get_server(liveserverid)
    channel = discord.utils.get(server.channels, id=livechannelid)
    msgs = bot.logs_from(channel)

    async for m in msgs:
        if m.id == "545157694944706573":
            bot.messages.append(m)
    #        if i == 0:
    #            msg = m
    #            i += 1

    #await bot.edit_message(msg, rolesMessage)

    print("COGBot ready to work!")


if __name__ == "__main__":
    bot.run(COGBotToken.token)
