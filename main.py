import discord
from discord import app_commands, utils

class case_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout = None)

    @discord.ui.button(label = "Abrir um novo caso", style = discord.ButtonStyle.blurple, custom_id="case_buttom")
    async def case(self, interaction: discord.Interaction, button: discord.ui.Button):
        overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
            interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, attach_files = True, embed_links = True),
            interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
        }
        channel = await interaction.guild.create_text_channel(name = f"📝┃case-", overwrites=overwrites, reason=f"Caso criado por {interaction.user}",category=interaction.guild.get_channel(1043350708705050705))
        await channel.send(f"{interaction.user.mention} seu caso foi aberto!")
        await interaction.response.send_message(f"Seu caso foi aberto em {channel.mention}", ephemeral=True)

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False
        self.added = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = discord.Object(id=1043329996703412264))
            self.synced = True
        if not self.added:
            self.add_view(case_launcher())
            self.added = True
        print(f"Estou logado como {self.user}.")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild = discord.Object(id=1043329996703412264), name='case', description='Lança o sistema de casos.')
async def casing(interaction: discord.Interaction):
    embed = discord.Embed(title="Sistema de casos", description="Clique no botão abaixo para abrir um novo caso.", color=0x00ff00)
    await interaction.channel.send(embed=embed, view=case_launcher())
    await interaction.response.send_message('Sistema de casos lançado com sucesso!', ephemeral=True)

client.run('')