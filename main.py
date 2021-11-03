import discord
from calculator import solve
import csv
import bank
import random
import economy
import useful
import compcluster
import plot

#set token
file = open("token", "r+")
token = file.read()
file.close()

client = discord.Client()

def cleantag(mes):
    mes = mes.replace('<', '')
    mes = mes.replace('>', '')
    mes = mes.replace('!', '')
    mes = mes.replace('@', '')
    return mes
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('%calc'):
        prb = list(message.content)
        while ' ' in prb:
            prb.remove(' ')

        prb = prb[5:]

        try:
            await message.channel.send(solve(prb))
        except Exception as ex:
            with open('Error_Log.csv', 'a', newline='') as log:
                writer = csv.writer(log)
                writer.writerow([prb,ex])
            log.close()
            await message.channel.send('Format your argument better...')
            await message.channel.send(ex)

    if message.content.startswith('%bal') and len(message.content) == 4:
        bal = bank.balance(message.author.id)
        embdedvar = discord.Embed(title=f"{message.author}'s balance",description=f"${bal}", color=random.randint(0, 0xffffff))
        await message.channel.send(embed=embdedvar)

    if message.content.startswith('%cbal'):
        msg = message.content.split()
        msg[1] = cleantag(msg[1])

        user = await client.fetch_user(msg[1])
        user = user.name
        bal = bank.checkbalance(msg[1])
        embdedvar = discord.Embed(title=f"{user}'s balance", description=f"${bal}",
                                  color=random.randint(0, 0xffffff))
        await message.channel.send(embed=embdedvar)

    if message.content.startswith('%cpor'):
        arg = message.content.split()
        while ' ' in arg:
            arg.remove(' ')
        portf = economy.inv(message.author.id)
        pagen = int(arg[1])
        embedvar1 = discord.Embed(title=f"page {pagen} of {message.author}'s portfolio", color=random.randint(0, 0xffffff))
        try:
            page = portf[((pagen - 1)*5) + 1:(pagen * 5) + 1]
            embedvar1.add_field(name=f"{portf[0][0]} **•** {portf[0][1]} **•** {portf[0][2]}",
                                value="None" if len(portf) < 2
                                else ''.join(f"{row[3]}. {row[0]}  **•**  {round(float(row[1][:-1]),2)}%  **•**  ${round(float(row[2]),2)}\n" for row in page),
                                inline=True
                                )
            await message.channel.send(embed=embedvar1)
        except Exception as ex:
            await message.channel.send("check formatting")
            await message.channel.send("the page probably doesnt exist")

    if message.content.startswith('%bis'):
        arg0 = message.content.split()
        while ' ' in arg0:
            arg0.remove(' ')
        market = useful.load(r'market/market.csv')
        for i in range(len(market)):
            market[i].append(i)
        npage = int(arg0[1])
        embedvar2 = discord.Embed(title=f"page {npage} of available businesses",
                                  color=random.randint(0, 0xffffff))
        try:
            page = market[((npage - 1)*5) + 1:(npage * 5) + 1]
            embedvar2.add_field(name=f"{market[0][0]} **-** {market[0][1]}",
                                value=''.join(f"{row[2] - 1}. {row[0]} **-** ${row[1]}\n" for row in page),
                                inline=True
                                )
            await message.channel.send(embed=embedvar2)
        except Exception as ex:
            await message.channel.send("check formatting")
            await message.channel.send("the page probably doesnt exist")

    if message.content.startswith('%buy'):
        arg1 = message.content.split()
        await message.channel.send(economy.buy(arg1[1], message.author.id))

    if message.content.startswith('%sell'):
        arg2 = message.content.split()
        await message.channel.send(economy.sell(arg2[1], message.author.id))

    if message.content.startswith('%bsearch'):
        arg3 = message.content.split()[1]

        try:
            data = compcluster.cat(arg3)

            embedvar3 = discord.Embed(title=f"available {arg3} businesses",
                                      color=random.randint(0, 0xffffff))

            embedvar3.add_field(name="Company Name **-** Company Price",
                                value=''.join(f"{comp[0]} **-** ${comp[1]}\n" for comp in data),
                                inline=True
                                )
            await message.channel.send(embed=embedvar3)
        except Exception as ex:
            await message.channel.send("check formatting")
            await message.channel.send("the type of company probably doesnt exist")

    if message.content.startswith("%help"):
        directory = useful.load("commands.csv")
        embedvar4 = discord.Embed(title="bot commands",
                                  color=random.randint(0, 0xffffff))
        embedvar4.add_field(name=f"{directory[0][0]} **-** {directory[0][1]} **-** {directory[0][2]}",
                            value=''.join(f"***{command[0]}*** - {command[1]} **-** {command[2]}\n" for command in directory[1:]),
                            inline=True
                            )
        await message.channel.send(embed=embedvar4)

    if message.content.startswith('%plot'):
        arg5 = message.content.split()
        plot.histp(arg5[1])
        await message.channel.send(file=discord.File('image.png'))

client.run(token)

