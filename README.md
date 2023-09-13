# README for a Work-in-Progress - Looking for Party Bot

A Discord Bot in development that helps players find groups to play "Baldur's Gate 3." Here are some key points:

## Description
This bot is intended to be used on Discord servers for "Baldur's Gate 3" players who want to find other players to form a party.

## Features

1. **Party Search Questionnaire**: Players can open a questionnaire to indicate their available schedule, the number of people they are looking for, the desired gameplay type, their class, and if they already have someone in the group. This questionnaire is used to create a post in the "Looking for Party" channel.

2. **Accepting and Rejecting Party Invitations**: When someone shows interest in the party post, other players can accept or reject the invitation. This is done through "Accept" and "Reject" buttons in the party search messages.

3. **Joining and Leaving the Party**: Players can join or leave the party using dedicated buttons. The bot checks if someone has already joined the party and prevents them from joining again.

## Under Construction
This bot is a work in progress, which means there may be bugs or incomplete features. Make sure to regularly check the repository or wherever the code is hosted for updates and fixes.

## Setup
To use this bot, follow these steps:

1. **Bot Token**: Replace `'TOKEN'` in the last line of the code with your own Discord bot's authentication token.

2. **Permissions**: Ensure that the bot has the necessary permissions to read messages, send messages, manage messages, add reactions, and create channels.

3. **Category and Channel**: Make sure a category called "Looking for Party" exists on your server, and the bot will create a channel called "looking-for-party" within that category.

4. **Additional Configurations**: Customize any other settings or messages as needed for your server.

## How to Use

1. Type `!start_party` on your server to initiate the questionnaire and look for a party.

2. Complete the questionnaire when prompted.

3. Interested parties can click "Accept" or "Reject" buttons in the party search messages.

4. Players can use the "Join Party" or "Leave Party" buttons to join or leave a party.

Please ensure that you have the necessary permissions to execute the commands and use the features of this bot on your server.

## Note
Make sure your development environment is properly set up with the `discord.py` library and any required dependencies.

**Legal Disclaimer**: Remember to follow Discord guidelines and respect the Terms of Service when using this bot on public servers.

Keep in mind that, as it's a work in progress, you may encounter bugs or issues.
