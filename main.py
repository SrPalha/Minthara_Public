import discord
from discord import app_commands

class MyClient(discord.Client):
    def __init__(self) -> None:
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.entered_party = set()  # Adicione esta linha
        self.party_members = {}  # Adicione esta linha

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        game = discord.Game("Baldur's Gate 3")
        await client.change_presence(status=discord.Status.idle, activity=game)
        print('------')
        await self.setup_hook()
 
    async def setup_hook(self) -> None:
        await self.tree.sync()

class AcceptJoinButton(discord.ui.Button): 
    def __init__(self, requester: discord.User, message: discord.Message, original_view: discord.ui.View, reject_button):
        super().__init__(style=discord.ButtonStyle.success, label="Aceitar")
        self.requester = requester
        self.message = message
        self.original_view = original_view
        self.reject_button = reject_button
        self.clicked = False

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Você aceitou {self.requester.mention} na Party.", ephemeral=True)
        if self.clicked:
            return
        self.clicked = True

        #Atualize o registro de membros da Party
        if self.message.id not in interaction.client.party_members:
            interaction.client.party_members[self.message.id] = []
        interaction.client.party_members[self.message.id].append(self.requester.id)

        #Verifique se já existem 8 pessoas na Party
        if len(interaction.client.party_members.get(self.message.id, [])) >= 8:
            await interaction.response.send_message("A Party já está cheia.", ephemeral=True)
            return

        # Lógica para adicionar o usuário à party
        embed = self.message.embeds[0]
        field_index = next((index for (index, f) in enumerate(embed.fields) if f.name == "Pessoas querendo entrar:"), None)
        
        if field_index is not None:
            old_value = embed.fields[field_index].value.strip().split()
            old_value.append(self.requester.mention)
            embed.set_field_at(field_index, name="Pessoas querendo entrar:", value=' '.join(old_value), inline=False)
            await self.message.edit(embed=embed)

        try:
            await self.requester.send(f"Você foi aceito na party de {interaction.user.mention}.")
        except discord.HTTPException:
            pass  # O usuário pode ter DMs desativadas

        # Desativar os botões
        self.style = discord.ButtonStyle.secondary
        self.label = "Aceito"
        self.disabled = True
        self.reject_button.disabled = True
        self.reject_button.style = discord.ButtonStyle.secondary
        self.reject_button.label = "Indisponível"
        await interaction.message.edit(view=self.original_view)

class RejectJoinButton(discord.ui.Button):
    def __init__(self, requester: discord.User, original_view: discord.ui.View, accept_button):
        super().__init__(style=discord.ButtonStyle.danger, label="Rejeitar")
        self.requester = requester
        self.original_view = original_view
        self.accept_button = accept_button
        self.clicked = False

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Você rejeitou {self.requester.mention} na Party.", ephemeral=True)
        if self.clicked:
            return
        self.clicked = True
        self.style = discord.ButtonStyle.secondary
        self.label = "Rejeitado"
        self.disabled = True
        self.accept_button.disabled = True
        self.accept_button.style = discord.ButtonStyle.secondary
        self.accept_button.label = "Indisponível"
        await interaction.message.edit(view=self.original_view)

                # Adicione esta parte para enviar uma DM ao usuário rejeitado
        try:
            await self.requester.send(f"Você foi rejeitado para entrar na party do {interaction.user.mention}")
        except discord.HTTPException:
            pass  # O usuário pode ter DMs desativadas

class PartyJoinLeaveButton(discord.ui.Button):
    def __init__(self, user: discord.User, join: bool, message: discord.Message):
        super().__init__(style=discord.ButtonStyle.success if join else discord.ButtonStyle.danger, label="Entrar na Party" if join else "Sair da Party")
        self.user = user
        self.join = join
        self.message = message

    async def callback(self, interaction: discord.Interaction):
        # Verifique se o usuário já entrou na party
        if self.join and interaction.user.id in interaction.client.entered_party:
            await interaction.response.send_message("Você já entrou na party e não pode entrar novamente.", ephemeral=True)
            return
        await interaction.response.send_message("Processando...", ephemeral=True)
        #após clicar no botão entrar na party essa mensagem vem
        if self.join:
            await interaction.followup.send(f"Uma mensagem foi enviada para {self.user.mention} solicitando que você entre na Party.", ephemeral=True)
        else:
            await interaction.followup.send(f"Você saiu da party do {self.user.mention}.", ephemeral=True)
        embed = self.message.embeds[0]
        field_index = next((index for (index, f) in enumerate(embed.fields) if f.name == "Pessoas querendo entrar:"), None)

        if field_index is not None:
            old_value = embed.fields[field_index].value.strip().split()

        if self.join:
            # Adicione o ID do usuário à lista de IDs que já entraram na party
            interaction.client.entered_party.add(interaction.user.id)
            accept_reject_view = discord.ui.View()
            accept_button = AcceptJoinButton(interaction.user, self.message, accept_reject_view, None)
            reject_button = RejectJoinButton(interaction.user, accept_reject_view, accept_button)
            accept_button.reject_button = reject_button  # Update the reference for reject_button

            accept_reject_view.add_item(accept_button)
            accept_reject_view.add_item(reject_button)

            try:
                await self.user.send(f"{interaction.user.mention} deseja entrar na sua Party! Você aceita?", view=accept_reject_view)
            except discord.HTTPException:
                pass  # User might have DMs disabled
        else:
            if interaction.user.mention in old_value:
                old_value.remove(interaction.user.mention)
                embed.set_field_at(field_index, name="Pessoas querendo entrar:", value=' '.join(old_value), inline=False)
                await self.message.edit(embed=embed)
                try:
                    await self.user.send(f"{interaction.user.mention} saiu da sua Party.")
                    interaction.client.entered_party.discard(interaction.user.id)
                except discord.HTTPException:
                    pass  # O usuário pode ter DMs desativadas

class PartyQuestionnaireModal(discord.ui.Modal, title='Procurando Party'):
    horario_disponivel = discord.ui.TextInput(label='Horário disponível?')
    num_pessoas = discord.ui.TextInput(label='Quantas pessoas busca e classes?')
    tipo_gameplay = discord.ui.TextInput(label='Tipo de gameplay (RP, Real, História)?')
    sua_classe = discord.ui.TextInput(label='Qual sua classe?')
    alguem_no_grupo = discord.ui.TextInput(label='Já tem alguém no grupo? Se sim, marque os @')

    async def on_submit(self, interaction: discord.Interaction):
        guild = interaction.guild

        # Verifique se a categoria "Procurando Party" já existe
        category = discord.utils.get(guild.categories, name="Procurando Party")
        
        # Se a categoria não existir, crie-a
        if not category:
            category = await guild.create_category("Procurando Party")
        
        # Verifique se o canal "Procurando Party" já existe dentro da categoria
        channel = discord.utils.get(category.text_channels, name="procurando-party")
        
        # Se o canal não existir, crie-o dentro da categoria
        if not channel:
            channel = await guild.create_text_channel("procurando-party", category=category)

        responses = [
            self.horario_disponivel.value,
            self.num_pessoas.value,
            self.tipo_gameplay.value,
            self.sua_classe.value,
            self.alguem_no_grupo.value
        ]
        
        questions = [
            "Horário disponível?",
            "Quantas pessoas busca?",
            "Tipo de gameplay (RP, Real, História)?",
            "Qual sua classe?",
            "Já tem alguém no grupo? Se sim, marque os @"
        ]

        embed = discord.Embed(title="Procurando Party", description="")
        embed.set_thumbnail(url=interaction.user.display_avatar.url)
        
        for question, answer in zip(questions, responses):
            embed.add_field(name=question, value=answer, inline=False)

        embed.add_field(name="Pessoas querendo entrar:", value="", inline=False)
        embed.add_field(name="Criador da Party:", value=interaction.user.mention, inline=False)
        embed.add_field(name="Você está procurando uma party? ", value="<@&1139606776220758157>", inline=False)  

        message = await channel.send(embed=embed)

        party_button_view = discord.ui.View()
        party_button_view.add_item(PartyJoinLeaveButton(interaction.user, True, message))
        party_button_view.add_item(PartyJoinLeaveButton(interaction.user, False, message))

        await message.edit(view=party_button_view)
        await interaction.response.send_message("Formulário enviado com sucesso!", ephemeral=True)

client = MyClient()

@client.tree.command(description="Procurar Party")
async def start_party(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Tá procurando um grupo para jogar Baldurs?",
        description="Responda o questionário e vamos achar o seu grupo :)"
    )
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Abrir Questionário", custom_id="open_party_questionnaire"))
    await interaction.response.send_message(embed=embed, view=view)

@client.event
async def on_interaction(interaction: discord.Interaction):
    if interaction.type == discord.InteractionType.component:
        if hasattr(interaction, 'data') and 'custom_id' in interaction.data:
            if interaction.data['custom_id'] == "open_party_questionnaire":
                await interaction.response.defer()  # Defer the interaction to get more time to respond
                await interaction.followup.send_modal(PartyQuestionnaireModal())  # Use followup.send_modal instead of response.send_modal

client.run('TOKEN') 
