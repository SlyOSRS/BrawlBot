import io
import json
import re
import pandas as pd
import random
import discord
from token_ import token_
from sheets import *
from discord.ext import commands, tasks
from matplotlib import pyplot as plt

blacklistUsers = [992528378315931738]
whitelistUsers = []

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', description="This is a Helper Bot", intents=intents, case_insensitive=True)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def ep(ctx):
    Zenyte = 100
    Onyx = 75
    Dragonstone = 50
    Diamond = 25
    Ruby = 15
    Emerald = 10
    Sapphire = 5
    Labourer = 0
    if ctx.author == bot.user:
        return
    print("{} | {} executed \"{}\" at {}.".format(ctx.author.display_name, ctx.author.id, ctx.message.content, datetime.datetime.utcnow()))
    player = ctx.message.content.lower() #This gets the user message. Ex: !point A Kimura
    removing_command = player[4:] 
    names = sheet.values().get(spreadsheetId=Noobs_EP,range=Noobs_EP_Range).execute()
    values = names.get('values', [])
    undercaseValues = [ [ i.lower() for i in innerlist ] for innerlist in values] # Makes values into lowercase
    df = pd.DataFrame(undercaseValues) #Puts the values from the Sheets API values into Pandas.
    searched = df[0].str.contains(removing_command).tolist() # Searches through the entire value list. If matches from user input, makes the list show True.
    found = {k:v for k, v in enumerate(searched) if v == True} # https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list
    found1 = json.dumps(found) #converts dict into string# https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list
    regexDict = re.search("\"(.*?)\"", found1) #Regex to modify the string dump. Could possibly look into removing this
    row = int(regexDict.group(1)) #This grabs the group value (the row which the name is on) from the dict to string dump I just did.
    #print(f"Name: {values[row][0]}\nTeam: {values[row][1]}\nPoints: {values[row][2]}\nSubmissions: {values[row][3]}")
    points = int(values[row][2])
    if points >= Zenyte:
        rank = ""
    elif points >= Onyx <= Zenyte:
        rank = "{} event points to achieve Zenyte ".format(Zenyte - points)
    elif points >= Dragonstone <= Onyx:
        rank = "{} event points to achieve Onyx".format(Onyx - points)
    elif points >= Diamond <= Dragonstone:
        rank = "{} event points to achieve Dragonstone".format(Dragonstone - points)
    elif points >= Ruby <= Diamond:
        rank = "{} event points to achieve Diamond".format(Diamond - points)
    elif points >= Emerald <= Ruby:
        rank = "{} event points to achieve Ruby".format(Ruby - points)
    elif points >= Sapphire <= Emerald:
        rank = "{} event points to achieve Emerald".format(Emerald - points)
    elif points >= Labourer <= Sapphire:
        rank = "{} event points to achieve Sapphire".format(Sapphire - points)
    #print(values)
    else:
        rank = 'error'
    
    if points >= Zenyte:
        await ctx.send((f"RSN: {values[row][0]}\nRank: {values[row][3]}\nEvent Points: {values[row][2]}"))
    else:
        await ctx.send((f"RSN: {values[row][0]}\nRank: {values[row][3]}\nEvent Points: {values[row][2]}\nNext Rank in {rank}"))

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

@bot.command()
async def traps(ctx):
    print("{} | {} executed \"{}\" at {}.".format(ctx.author.display_name, ctx.author.id, ctx.message.content, datetime.datetime.utcnow()))
    embed = discord.Embed(title=f"Old Greg", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.set_image(url="https://i.pinimg.com/736x/58/85/40/588540eebfcf64880422f1983d7d2940--old-gregg-too-funny.jpg")
    embed.set_footer(text="Requested by: {}".format(ctx.author.display_name))
    await ctx.send(embed=embed)

    

@bot.command()
async def chart(ctx):
    teamPoints = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=totalPoints).execute()
    allPoints = teamPoints.get('values', [])
    redPoints = int(allPoints[0][0])
    bluePoints = int(allPoints[1][0])
    greenPoints = int(allPoints[2][0])

    teams = ['Red', 'Blue', 'Green']
    values = [redPoints, bluePoints, greenPoints]
    print(type(greenPoints))
    fig, ax = plt.subplots()

    ax.bar(teams, values, color=teams)

    for i, f in enumerate(values):
        plt.text(x=i-0.32, y = f-250, s=f"{f}", fontdict=dict(fontsize=35))

    plt.tight_layout()
    plt.savefig('images/graph.png')
    plt.close(fig)

    with open('images/graph.png', 'rb') as f:
        file = io.BytesIO(f.read())
    
    colour = 0x00b2ff
    embed = discord.Embed(title='Brawl Scoreboard', colour=colour)
    image = discord.File(file, filename='graph.png')
    embed.set_image(url=f'attachment://graph.png')

    await ctx.send(file=image, embed=embed)
    #plt.show()
    print("Red Points: {}\nBlue Points: {}\nGreen Points: {}".format(redPoints, bluePoints, greenPoints))
    

@bot.command(pass_context=True)
async def point(ctx):
    if ctx.author == bot.user:
        return
    print("{} | {} executed \"{}\" at {}.".format(ctx.author.display_name, ctx.author.id, ctx.message.content, datetime.datetime.utcnow()))
    player = ctx.message.content.lower() #This gets the user message. Ex: !point A Kimura
    removing_command = player[7:] #This removes the !point from the message, only leaving the username. Ex: !point A Kimura turns into A Kimura
    names = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=members).execute()
    values = names.get('values', [])
    undercaseValues = [ [ i.lower() for i in innerlist ] for innerlist in values] # Makes values into lowercase
    df = pd.DataFrame(undercaseValues) #Puts the values from the Sheets API values into Pandas.
    searched = df[0].str.contains(removing_command).tolist() # Searches through the entire value list. If matches from user input, makes the list show True.
    found = {k:v for k, v in enumerate(searched) if v == True} # https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list
    found1 = json.dumps(found) #converts dict into string
    regexDict = re.search("\"(.*?)\"", found1) #Regex to modify the string dump. Could possibly look into removing this
    row = int(regexDict.group(1)) #This grabs the group value (the row which the name is on) from the dict to string dump I just did.
    #print(f"Name: {values[row][0]}\nTeam: {values[row][1]}\nPoints: {values[row][2]}\nSubmissions: {values[row][3]}")
    await ctx.send((f"Name: {values[row][0]}\nTeam: {values[row][1]}\nPoints: {values[row][2]}\nSubmissions: {values[row][3]}"))

@bot.command(pass_context=True)
async def points(ctx):
    if ctx.author == bot.user:
        return
    print("{} | {} executed \"{}\" at {}.".format(ctx.author.display_name, ctx.author.id, ctx.message.content, datetime.datetime.utcnow()))
    player = ctx.message.content.lower() #This gets the user message. Ex: !point A Kimura
    removing_command = player[8:] #This removes the !point from the message, only leaving the username. Ex: !point A Kimura turns into A Kimura
    names = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=members).execute()
    values = names.get('values', [])
    undercaseValues = [ [ i.lower() for i in innerlist ] for innerlist in values] # Makes values into lowercase
    df = pd.DataFrame(undercaseValues) #Puts the values from the Sheets API values into Pandas.
    searched = df[0].str.contains(removing_command).tolist() # Searches through the entire value list. If matches from user input, makes the list show True.
    found = {k:v for k, v in enumerate(searched) if v == True} # https://stackoverflow.com/questions/21448225/getting-indices-of-true-values-in-a-boolean-list
    found1 = json.dumps(found) #converts dict into string
    regexDict = re.search("\"(.*?)\"", found1) #Regex to modify the string dump. Could possibly look into removing this
    row = int(regexDict.group(1)) #This grabs the group value (the row which the name is on) from the dict to string dump I just did.
    await ctx.send((f"Name: {values[row][0]}\nTeam: {values[row][1]}\nPoints: {values[row][2]}\nSubmissions: {values[row][3]}"))

@bot.command()
async def testing(ctx):
    print("Author: {} \nAuthor ID: {} \nDiscord username: {}".format(ctx.author.display_name, ctx.author.id, ctx.author))
    await ctx.send("Author: {} \nAuthor ID: {} \nDiscord username: {}".format(ctx.author.display_name, ctx.author.id, ctx.author))

@bot.command()
async def flip(ctx):
    User = ctx.author.id
    if User in blacklistUsers:
        await ctx.send("No flip for you")
        return
    coin = random.randint(0,1)    
    if coin == 0:
        embed = discord.Embed(title=f"Heads", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url="https://i5.walmartimages.com/asr/3850a9da-7ed7-4bbd-915a-3a8e38e0195a_1.83cc29729d27461002ccd2748d4a3a5f.jpeg")
        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
    if coin == 1:
        embed = discord.Embed(title=f"Tails", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.set_image(url="https://bjc.edc.org/June2017/bjc-r/img/5-algorithms/img_flipping-a-coin/Tails.png")
        embed.set_footer(text="Requested by: {}".format(ctx.author.display_name))
        await ctx.send(embed=embed)
    
@bot.command()
async def whoami(ctx):
    User = ctx.author.id
    #await ctx.send(ctx.author)
    embed = discord.Embed(title=f"Account Information", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Discord name", value=f"{ctx.author}", inline=False)
    embed.add_field(name="Server Name", value=f"{ctx.author.display_name}", inline=False)
    embed.add_field(name="Discord ID", value=f"{ctx.author.id}", inline=False)
    
    await ctx.send(embed=embed)

@bot.command()
#Future update after getting it working. Can reduce lines by having array with team
async def mvp(ctx):
    
    names = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=playerName).execute()
    values = names.get('values', [])

    teamPoints = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=totalPoints).execute()
    allPoints = teamPoints.get('values', [])

    embed = discord.Embed(title=f"Red Team", color=discord.Color.red())
    embed.add_field(name="Total points", value=f"{allPoints[0][0]}", inline=False)
    embed.add_field(name="Red's MVP", value=f"{values[0][1]}")
    embed.add_field(name="Points", value=f"{values[0][2]}")
    await ctx.send(embed=embed)
    #print(redMVP.id)

    embed = discord.Embed(title=f"Blue Team", color=discord.Color.blue())
    embed.add_field(name="Total points", value=f"{allPoints[1][0]}", inline=False)
    embed.add_field(name="Blue's MVP", value=f"{values[1][1]}")
    embed.add_field(name="Points", value=f"{values[1][2]}")
    await ctx.send(embed=embed)
    #print(blueMVP.id)

    embed = discord.Embed(title=f"Green Team", color=discord.Color.green())
    embed.add_field(name="Total points", value=f"{allPoints[2][0]}", inline=False)
    embed.add_field(name="Green's MVP", value=f"{values[2][1]}")
    embed.add_field(name="Points", value=f"{values[2][2]}")
    await ctx.send(embed=embed)
    #print(greenMVP.id)
    print("{} | {} executed !mvp at {}".format(ctx.author.display_name, ctx.author.id, datetime.datetime.utcnow()))
    #update()
    #print(data[0][1])

@bot.command()
async def teams(ctx):
    teamNames = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range=namesOnly).execute()
    allPoints = teamNames.get('values', [])
    print(allPoints[1])
    embed = discord.Embed(title=f"Red Team", color=discord.Color.red())   
    embed.add_field(name="Members", value=f"Abysse\nDoombo\n227 7\nA Kimura\nAkayasimowin\nBunny Luck\nChet Ripley\nCoolit\nDay6\nEmaxganis\nGemotiveerd\nItsNotGood\nJacob\nLil Pihmpin\nShuttleworth\nSkordeath", inline=False)
    await ctx.send(embed=embed)

    embed = discord.Embed(title=f"Green Team", color=discord.Color.green())   
    embed.add_field(name="Members", value=f"A Papa Smurf\nCadias Stand\nD0 C\nDante\nDemi-Dragoon\nDusty_y\nEden95\n3TickUrMom\nJorge Strait\nWAJ\nRoflOS\nkarlmarxreal\nTaters X\nre2pect\nSwimm\nWhale Green\nneedanegirl", inline=False)
    await ctx.send(embed=embed)

    embed = discord.Embed(title=f"Blue Team", color=discord.Color.blue())   
    embed.add_field(name="Members", value=f"SquinkaBinka\nStelthshield\nSyxSynz\nTheifah\nVersace\nEnvetoids\nYouSuck\nLitty Goose\nmr. pbh444\nPwnrPizzaman\nR td\nSpacey\nA curry\nfly2\nGUCC1MESSIAH\nIron APK\nKekblob", inline=False)
    await ctx.send(embed=embed)
    print('')

@bot.command()
async def restartBot(ctx,):
    os.execv(sys.executable, ['python'] + sys.argv)

@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Discord Server Information", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}", inline=False)
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}", inline=False)
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")

    await ctx.send(embed=embed)
# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="OldSchool Runescape"))
    print('The bot is ready to run!')
    #time.sleep(5)
    #if not updateMessage.is_running():
        #updateMessage.start()


@bot.listen()
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!'):
        return
    if "ratting" in message.content.lower():
        print("Ratting was used!")
        await message.channel.send(r"You've summoned the Rat")
        await message.channel.send("https://pbs.twimg.com/media/EvrMuMRVIAY3AbO.jpg")
        await bot.process_commands(message)
    if "doombo" in message.content.lower():
        await message.channel.send(r'Just get a better drop')
        await bot.process_commands()
    if "pvp" in message.content.lower():
        await message.channel.send(r'Vote no to all Player vs Player polls')
        await bot.process_commands(message)
    if "demi" in message.content.lower():
        await message.channel.send(r'<:Elysniff:995852090616328272>')
        await bot.process_commands(message)
    if "winston" in message.content.lower():
        await message.channel.send(r'<:winningston:951894950298136646>')
        await bot.process_commands(message)

bot.run(token_)
