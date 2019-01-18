#     _   _ ____  _______        __
#    | \ | / ___||  ___\ \      / /
#    |  \| \___ \| |_   \ \ /\ / / 
#    | |\  |___) |  _|   \ V  V /  
#    |_| \_|____/|_|      \_/\_/................................

@bot.command(pass_context=True, no_pm=True, aliases=["r", "r34", "rule"])
@commands.cooldown(3, 5)
async def rule34(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["anime", "ass", "boobs", "anal", "pussy", "thighs", "yaoi", "yuri", "bdsm"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "http://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, message)
	try:
		response = requests.get(url)
		data = json.loads(response.text)
		limit = len(data)
	except json.JSONDecodeError:
		embed=discord.Embed(description = "Couldn't find a picture with that tag or there was a server problem", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = "http://img.rule34.xxx/images/{}/{}".format(x["directory"], x["image"])
	embed=discord.Embed(title = "Enjoy {}, lewd!!!".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From Rule34, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True, aliases=["yan"])
@commands.cooldown(3, 5)
async def yandere(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["pantsu", "swimsuits", "dress", "breasts", "animal ears", "open shirt", "bra", "no bra", "cameltoe", "loli"\
				" thighhighs", "cleavage", "nipples", "ass", "bikini", "naked", "pussy", "panty pull", "see through", "underboob"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://yande.re/post/index.json?limit={}&tags={}".format(limit, message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = x["file_url"]
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From yande.re, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True, aliases=["dan"])
@commands.cooldown(3, 5)
async def danbooru(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["breasts", "blush", "skirt", "thighhighs", "large breasts", "underwear", "panties"\
				"nipples", "ass", "pantyhose", "nude", "pussy"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://danbooru.donmai.us/post/index.json?limit={}&tags={}".format(limit, message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	if x["file_url"].startswith("http"):
		final_url = x["file_url"]
	else:
		final_url = "http://danbooru.donmai.us{}".format(x["file_url"])
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From danbooru, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True, aliases=["gel"])
@commands.cooldown(3, 5)
async def gelbooru(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["ass", "breasts", "cameltoe", "long hair", "female", "pussy", "nude", "on bed"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit,message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = x["file_url"]
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From gelbooru, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True, aliases=["xb"])
@commands.cooldown(3, 5)
async def xbooru(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["ass", " breasts", "pussy", "female", "nude", "bdsm", "spanking"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://xbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = "http://img3.xbooru.com/images/{}/{}".format(x["directory"], x["image"])
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From xbooru, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)

@bot.command(pass_context=True, no_pm=True, aliases=["rb"])
@commands.cooldown(10, 10)
async def realbooru(ctx, *, message:str=None):
	if ctx.message.channel.is_nsfw == False:
		embed=discord.Embed(description = "This is not a **nsfw** channel", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	limit = 100
	if message==None:
		listu = ["ass", " breasts", "pussy", "female", "nude", "bdsm", "spanking"]
		message = listu[random.randint(0, len(listu)-1)]
	message = message.replace(" ", "_")
	url = "https://realbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, message)
	response = requests.get(url)
	data = json.loads(response.text)
	limit = len(data)
	if not data:
		embed=discord.Embed(description = "Couldn't find a picture with that tag", color = 0x3333cc)
		x = await bot.say(embed=embed)
		await asyncio.sleep(5)
		return await bot.delete_message(x)
	x = data[random.randint(0, limit-1)]
	final_url = "https://realbooru.com/images/{}/{}".format(x["directory"], x["image"])
	embed=discord.Embed(title = "Enjoy {}, ".format(ctx.message.author.name), color = 0x3333cc)
	embed.set_image(url = final_url)
	embed.set_footer(text = "From realbooru, Tag: {}, Results found: {}".format(message, limit))
	await bot.say(embed=embed)
