import discord
from discord.ext import commands

from random import seed,randint

import pandas as pd



client =commands.Bot(command_prefix="!")
#tellsversion
@client.command(name='version')
async def version(context):
    myEmbed=discord.Embed(title="Current Version",descrption="version 1.0",color=0x00ff00)
    myEmbed.add_field(name="Description",value="Hi i am a bot my name is chitti",inline=False)
    myEmbed.add_field(name="creator:",value="ARYAN",inline=False)
    myEmbed.add_field(name="date made on:",value="14 jan 20201",inline=False)
    myEmbed.set_footer(text="bus itna hi hai dost")
    await context.message.channel.send(embed=myEmbed)
#tellscommands
@client.command(name='commands')
async def version(context):
    myEmbed=discord.Embed(title="Commands",descrption="these are my current commands",color=0x00ff00)
    myEmbed.add_field(name="requirement",value="add a '!' before the command",inline=False)
    myEmbed.add_field(name="command 1:",value="version(gives info)",inline=False)
    myEmbed.add_field(name="command 2:",value="dm(sends dm)",inline=False)
    myEmbed.add_field(name="command 3:",value="are_u_online(tells if bot is online)",inline=False)
    myEmbed.add_field(name="command 4:",value="append(appends name to database without which u cant play games)",inline=False)
    myEmbed.add_field(name="command 5:",value="rps(rock paper scissor)",inline=False)
    myEmbed.add_field(name="command 5:",value="roll(roll a dice)",inline=False)
    myEmbed.add_field(name="command 5:",value="score(tells your total game score till date",inline=False)
    myEmbed.set_footer(text="thats it")
    await context.message.channel.send(embed=myEmbed)
#sends direct message
@client.command(name='dm')
async def version(context):
    await context.message.author.send("hey thanks for using a basic command")
#appends username to output.csv
@client.command(name='append')
async def version(context):
    df=pd.read_csv('discord bots\output.csv',index_col=0)
    var=False
    for j in df['NAMES']:
        if str(j)==str(context.message.author):
            await context.message.channel.send('Gyou already have written append')
            var=True
            break
    if var==False:
        df=df.append({"NAMES":context.message.author,"SCORE":0},ignore_index=True)
        await context.message.channel.send('you have been added to the database'+' '+str(context.message.author))
    df.to_csv('discord bots\output.csv')

#tellsscore
@client.command(name='score')
async def version(context):
    df=pd.read_csv('discord bots\output.csv',index_col=0)
    userindex=0
    for j in df['NAMES']:   
        if str(j)==str(context.message.author):
            break
        userindex+=1
    score=df["SCORE"][userindex]
    await context.message.channel.send("your score"+" "+str(context.message.author)+" ="+str(score))

#roll
@client.command(name='roll')
async def version(context,arg):
    #finding the user
    df=pd.read_csv('discord bots\output.csv',index_col=0)
    userindex=0
    length=len(df['NAMES'])
    for j in df['NAMES']:   
        if str(j)==str(context.message.author):
            break
        userindex+=1
    if userindex>=length-1:
        await context.message.channel.send("write '!append' command before playing games")
    #main function
    number=randint(1,6)
    lst=[1,2,3,4,5,6]
    if int(arg) not in lst:
        await context.message.channel.send("incorrect command")
        pass
    score=df["SCORE"][userindex]
    if int(arg)==number:
        df["SCORE"][userindex]=score+6
        await context.message.channel.send(str(number)+"\nnice "+str(context.message.author)+" u win,\ntotal score till date is= "+str(score+6))
        df.to_csv('discord bots\output.csv')
    else:
        df["SCORE"][userindex]=score-1
        await context.message.channel.send(str(number)+"\noh no "+str(context.message.author)+" u are the looser,\ntotal score till date is= "+str(score-1))
        df.to_csv('discord bots\output.csv')

#rockpapersissor
@client.command(name='rps')
async def version(context,arg):
    #finding the user
    df=pd.read_csv('discord bots\output.csv',index_col=0)
    userindex=0
    length=len(df['NAMES'])
    for j in df['NAMES']:   
        if str(j)==str(context.message.author):
            break
        userindex+=1
    if userindex>=length-1:
        await context.message.channel.send("write '!append' command before playing games")
    #main function
    number=randint(0,2)
    lst=['rock','paper','scissor']
    if str(arg) not in lst:
        await context.message.channel.send("invald command")
        pass 
    botsresponce=lst[number]
    score=df["SCORE"][userindex]
    if str(arg)=="rock":
        if number==2:
            df["SCORE"][userindex]=score+1
            await context.message.channel.send(str(botsresponce)+"\nnice "+str(context.message.author)+" u win,\ntotal score till date is= "+str(score+1))
            df.to_csv('discord bots\output.csv')
        elif number==0:
            await context.message.channel.send(str(botsresponce)+"\n "+str(context.message.author)+" its a draw,\ntotal score till date is= "+str(score))
        elif number==1:
            df["SCORE"][userindex]=score-1
            await context.message.channel.send(str(botsresponce)+"\noh no "+str(context.message.author)+" u are the looser,\ntotal score till date is= "+str(score-1))
            df.to_csv('discord bots\output.csv')
    if str(arg)=="paper":
        if number==0:
            df["SCORE"][userindex]=score+1
            await context.message.channel.send(str(botsresponce)+"\nnice "+str(context.message.author)+" u win,\ntotal score till date is= "+str(score+1))
            df.to_csv('discord bots\output.csv')
        elif number==1:
            await context.message.channel.send(str(botsresponce)+"\n "+str(context.message.author)+" its a draw,\ntotal score till date is= "+str(score))
        elif number==2:
            df["SCORE"][userindex]=score-1
            await context.message.channel.send(str(botsresponce)+"\noh no "+str(context.message.author)+" u are the looser,\ntotal score till date is= "+str(score-1))
            df.to_csv('discord bots\output.csv')
    if str(arg)=="scissor":
        if number==1:
            df["SCORE"][userindex]=score+1
            await context.message.channel.send(str(botsresponce)+"\nnice "+str(context.message.author)+" u win,\ntotal score till date is= "+str(score+1))
            df.to_csv('discord bots\output.csv')
        elif number==2:
            await context.message.channel.send(str(botsresponce)+"\n "+str(context.message.author)+" its a draw,\ntotal score till date is= "+str(score))
        elif number==0:
            df["SCORE"][userindex]=score-1
            await context.message.channel.send(str(botsresponce)+"\noh no "+str(context.message.author)+" u are the looser,\ntotal score till date is= "+str(score-1))
            df.to_csv('discord bots\output.csv') 

    
    await context.message.channel.send("*work")
#checks if online
@client.command(name='are_u_online')
async def version(context):
    await context.message.channel.send("i am online friend")

#on ready
@client.event
async def on_ready():
    #un commet next 2 lines if it is first time reunning the bot or to restart the pandas data in output.csv
    #df=pd.DataFrame({"NAMES":['hello','hey'],"SCORE":[0,0]})           
    #df.to_csv('discord bots\output.csv')

    general_channel=client.get_channel(696684963315187725)##channel where it says something when turned online
    await general_channel.send('hello i am on')
    seed(1)
    value=randint(0,4)
    if value==0:
        n="hi"
    elif value==1:
        n="hello"
    elif value=="2":
        n="namaste"
    elif value=="3":
        n="hey"
    await client.change_presence(status=discord.Status.online,activity=discord.Game(n))

#ondisconect
@client.event
async def on_disconnect():

    general_channel=client.get_channel(696684963315187725) #channel where it says bye
    await general_channel.send('bye')




client.run("Nzk5MTYyNjM3MTM1OTA0Nzc4.X__kNA.eJY6s5IJkSz7RDNLoyMwuhBxdi0")       ## the main bot token which only the creator can set