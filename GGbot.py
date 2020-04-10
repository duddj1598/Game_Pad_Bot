import discord
import asyncio
import random
import os

client = discord.Client()

#준비 확인
@client.event
async def on_ready():
    print(client.user.id)
    print(client.user.name)
    print("ready")
    game = discord.Game("!명령어")
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    #대화
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")
    if message.content.startswith("!명령어"):
        await message.channel.send("https://gpcommands.netlify.com")


    #주사위
    if message.content.startswith("!주사위"):
        await message.channel.send(random.randint(1, 6))


    #팀나누기
    if message.content.startswith("!팀"):
        team = message.content[3:]
        peopleteam = team.split(" / ")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split (",")
        teamname = team.split (",")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "  ▶  " + teamname[i])

    #뮤트 시키기
    if message.content.startswith("!뮤트"):
        author = message.guild.get_member(int(message.content [4:22]))
        role = discord.utils.get(message.guild.roles, name="mute")
        irole = discord.utils.get(message.guild.roles, name="Game Lover")
        await author.remove_roles(irole)
        await author.add_roles(role)
        await message.channel.send("뮤트되었습니다.")

    #뮤트 풀기
    if message.content.startswith("!언뮤트"):
        author = message.guild.get_member(int(message.content [4:23]))
        role = discord.utils.get(message.guild.roles, name="mute")
        irole = discord.utils.get(message.guild.roles, name="Game Lover")
        await author.remove_roles(role)
        await author.add_roles(irole)
        await message.channel.send("언뮤트되었습니다.")

    #투표
    if message.content.startswith("!투표"):
        vote = message.content[4:].split(" / ")
        await message.channel.send("★투표 - " + vote[0])
        for i in range(1, len(vote)):
            choose = await message.channel.send("```" + vote[i] + "```")
            if message.content.startswith(choose):
                await message.add_reaction('👍')



access_token = os.environ["BOT_TOKEN]
client.run("access_token")

#출처: https://webolutions.tistory.com/132 [Do IT Yourself]
#[출처] 컴맹도 할수있는 디스코드 봇 만들기(영상첨부)|작성자 섹시베이비
