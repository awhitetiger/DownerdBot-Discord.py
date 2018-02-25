import discord
import asyncio
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
	print('DownerdBot Ready :)')

@client.event
async def on_message(message):
	if message.content[:1] == '[' and message.content[-1:] == ']':#cardname
		card = message.content.replace('[', '')
		card = card.replace(']', '')
		await getCardDataName(card, message.channel)
	if message.content[:1] == '(' and message.content[-1:] == ')':#printnumber
		card = message.content.replace('(', '')
		card = card.replace(')', '')
		await getCardDataNumber(card, message.channel)

async def getCardDataName(card, channel):
	cardPrices = []
	cardUrl = 'http://yugiohprices.com/api/get_card_prices/' + card
	cardData = requests.get(url = cardUrl)
	cardData = json.loads(cardData.content)
	for x in range(len(cardData['data'])):
		cardPrices.append(cardData['data'][x]['print_tag'] + ' - ' + cardData['data'][x]['rarity'] + ' - ' + str(cardData['data'][x]['price_data']['data']['prices']['average']) + '$')
	cardPrices = '\n'.join(cardPrices)
	await client.send_message(channel, '```' + cardPrices + '```')

async def getCardDataNumber(card, channel):
	cardPrices = []
	cardUrl = 'http://yugiohprices.com/api/price_for_print_tag/' + card
	cardData = requests.get(url = cardUrl)
	cardData = json.loads(cardData.content)
	await client.send_message(channel, '```' + cardData['data']['name'] + ' - ' + cardData['data']['price_data']['rarity'] + ' - ' + str(cardData['data']['price_data']['price_data']['data']['prices']['average']) + '$```')

client.run('discord api key here boyo')
