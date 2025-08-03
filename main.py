import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot logado como {bot.user}")

# 🔨 COMANDO: limpar mensagens
@bot.command()
@commands.has_permissions(manage_messages=True)
async def limpar(ctx, quantidade: int):
    await ctx.channel.purge(limit=quantidade + 1)
    await ctx.send(f"{quantidade} mensagens apagadas!", delete_after=5)

# 🔨 COMANDO: expulsar usuário
@bot.command()
@commands.has_permissions(kick_members=True)
async def expulsar(ctx, membro: discord.Member, *, motivo=None):
    await membro.kick(reason=motivo)
    await ctx.send(f"{membro} foi expulso. Motivo: {motivo}")

# 🔨 COMANDO: banir usuário
@bot.command()
@commands.has_permissions(ban_members=True)
async def banir(ctx, membro: discord.Member, *, motivo=None):
    await membro.ban(reason=motivo)
    await ctx.send(f"{membro} foi banido. Motivo: {motivo}")

# 🔍 COMANDO: listar membros
@bot.command()
async def membros(ctx):
    membros = "\n".join([m.name for m in ctx.guild.members])
    await ctx.send(f"Lista de membros:\n{membros}")

bot.run(TOKEN)