# Read-Me do Código em Construção - Procurando Party Bot

Este é um bot de Discord em construção que ajuda os jogadores a encontrar grupos para jogar "Baldur's Gate 3". Aqui estão alguns pontos-chave:

## Descrição
Este bot é destinado a ser usado em servidores do Discord para jogadores de "Baldur's Gate 3" que desejam encontrar outros jogadores para montar uma party.

## Funcionalidades

1. **Questionário de Procura de Party**: Os jogadores podem abrir um questionário para indicar seu horário disponível, o número de pessoas que estão procurando, o tipo de gameplay desejado, sua classe e se já têm alguém no grupo. Esse questionário é usado para criar uma postagem no canal "Procurando Party".

2. **Aceitar e Rejeitar Convites para a Party**: Quando alguém se interessa pela postagem da party, outros jogadores podem aceitar ou rejeitar o convite. Isso é feito por meio de botões "Aceitar" e "Rejeitar" nas mensagens de procura da party.

3. **Entrar e Sair da Party**: Os jogadores podem entrar ou sair da party com a ajuda de botões dedicados. O bot verifica se alguém já entrou na party e impede que entrem novamente.

## Em Construção
Este bot está em construção, o que significa que pode haver bugs ou recursos incompletos. Certifique-se de verificar regularmente o repositório ou o local onde o código está hospedado para atualizações e correções.

## Configuração
Para usar este bot, siga estas etapas:

1. **Token do Bot**: Substitua `'TOKEN'` na linha final do código pelo token de autenticação do seu próprio bot do Discord.

2. **Permissões**: Certifique-se de que o bot tenha as permissões adequadas para ler mensagens, enviar mensagens, gerenciar mensagens, adicionar reações e criar canais.

3. **Categoria e Canal**: Certifique-se de que exista uma categoria chamada "Procurando Party" em seu servidor, e o bot criará um canal chamado "procurando-party" dentro dessa categoria.

4. **Configurações Adicionais**: Certifique-se de personalizar qualquer outra configuração ou mensagem necessária para o seu servidor.

## Como Usar

1. Digite `!start_party` no seu servidor para iniciar o questionário e procurar por uma party.

2. Complete o questionário quando solicitado.

3. Os interessados podem clicar nos botões "Aceitar" ou "Rejeitar" nas mensagens de procura da party.

4. Os jogadores podem usar os botões "Entrar na Party" ou "Sair da Party" para participar ou sair de uma party.

Lembre-se de que você deve ter as permissões adequadas para executar os comandos e usar as funcionalidades deste bot em seu servidor.

## Observação
Certifique-se de que o seu ambiente de desenvolvimento está configurado corretamente com a biblioteca `discord.py` e as dependências necessárias.

**Aviso Legal**: Lembre-se de seguir as diretrizes do Discord e respeitar os Termos de Serviço ao usar este bot em servidores públicos.

Tenha em mente que, como está em construção, você pode encontrar bugs ou problemas.
