import telebot
from telebot import types

with open("token.tok", "r") as tok:
	toke = tok.read()
	if len(toke) == 46:
		token = toke
	else: exit()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	keysi=types.KeyboardButton("КЕЙСЫ")
	izgotov=types.KeyboardButton("ИЗГОТОВЛЕНИЕ")
	rapocl=types.KeyboardButton("РАБОТЫ ПОД КОЮЧ")
	markup.add(keysi)
	markup.add(izgotov)
	markup.add(rapocl)
	bot.send_message(message.chat.id,"Здравствуйте, выберите что вы хотите посмотреть:", reply_markup=markup)
	if message.text == "/start":
		with open("ids.bot", "r+") as ids:
			lines = ids.readlines()
			ides = True
			print(f"{message.chat.id} - Start bot")
			for i in range(len(lines)):
				if lines[i] == message.chat.id:
					pass
				else: 
					ides = False
			if ides == False:
				idsr = ids.read()
				ids.write(f"\n{message.chat.id}")
				print(message.chat.id)

@bot.message_handler(commands=['ros'])
def ros(message):
	text = message.text.split("/ros ")[1::1]
	adid = open("admin.id", "r")
	ids = open("ids.bot", "r")
	idlines = ids.readlines()
	if message.chat.id == int(adid.read()):
		if not text:
			bot.send_message(message.chat.id, "ERROR: Вы не ввели текст рассылки")
		else:
			bot.send_message(message.chat.id, f"Отрповляю россылку с текстом {text}")
			bot.send_message(message.chat.id, text)
			for i in range(len(idlines)):
				if i == 0: pass
				else:
					bot.send_message(idlines[i], text)
	else:
		bot.send_message(message.chat.id, "ERROR: У вас нет привелегий администратора что бы использовать эту команду!")

@bot.message_handler(content_types=['text'])
def func(message):
	text = message.text
	if text == "❌ВЫХОД❌":
		start_message(message)

	elif text == "КЕЙСЫ":
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		exit=types.KeyboardButton("❌ВЫХОД❌")
		markup.add(exit)    
		bot.send_message(message.chat.id,"Извините, пока-что у нас нет кейсов🙁", reply_markup=markup)

	elif text == "ИЗГОТОВЛЕНИЕ":
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		servmat=types.KeyboardButton("Глубокий, насыщенный серый в матовом исполнении")
		det=types.KeyboardButton("Внимательны к деталям")
		beton=types.KeyboardButton("Версия под бетон, в готовом варианте")
		factur=types.KeyboardButton("Фактура")
		matzak=types.KeyboardButton("Матовые заготовки")    
		onenuw=types.KeyboardButton("Ещё два наших изготовлений")
		izstup=types.KeyboardButton("Изготовление ступеней")
		glubch=types.KeyboardButton("Глубокий, насыщенный черный")
		rosglan=types.KeyboardButton("Роскошный глянец")
		exit=types.KeyboardButton("❌ВЫХОД❌")
		markup.add(servmat)
		markup.add(det)
		markup.add(beton)
		markup.add(factur)
		markup.add(matzak)
		markup.add(onenuw)
		markup.add(izstup)
		markup.add(glubch)
		markup.add(rosglan)
		markup.add(exit)    
		bot.send_message(message.chat.id,"Пожалуйса, выберите что хотите посмотреть:", reply_markup=markup)

	elif text == "РАБОТЫ ПОД КОЮЧ":
		markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
		stuppodder=types.KeyboardButton("Ступени под дерево")
		stupsvet=types.KeyboardButton("Ступени в светлом варианте")
		ocher=types.KeyboardButton("Очередные наши работы")
		exit=types.KeyboardButton("❌ВЫХОД❌")
		markup.add(stuppodder)
		markup.add(stupsvet)
		markup.add(ocher)
		markup.add(exit)    
		bot.send_message(message.chat.id,"Пожалуйса, выберите что хотите посмотреть:", reply_markup=markup)

	elif text == "Глубокий, насыщенный серый в матовом исполнении":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/servmat/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/servmat/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/servmat/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Глубокий, насыщенный серый, в матовом исполнении")

	elif text == "Внимательны к деталям":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/det/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/det/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/det/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Внимательны к деталям📐🛠️")

	elif text == "Версия под бетон, в готовом варианте":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/beton/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/beton/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/beton/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Выглядит стильно и современно!")

	elif text == "Фактура":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/factur/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/factur/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/factur/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Обратите внимание на эту фактуру🔥")

	elif text == "Матовые заготовки":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/matzak/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/matzak/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/matzak/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Наши матовые заготовки, скоро отправятся к заказчику!")

	elif text == "Ещё два наших изготовлений":
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/3.jpg', 'rb'))
		bot.send_message(message.chat.id,"~~~~~~~~~~")
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/4.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/5.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/onenuw/6.jpg', 'rb'))
		bot.send_message(message.chat.id,"Ещё два наших изготовлений")

	elif text == "Изготовление ступеней":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/izstup/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Только посмотрите на эту мерцающую текстуру🔥")
		bot.send_message(message.chat.id,"~~~~~~~~~~")
		bot.send_video(message.chat.id, video=open('data/video/izgotov/izstup/2.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/3.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/4.jpg', 'rb'))
		bot.send_message(message.chat.id,"Изготовление ступеней, идеально ровные и гладкие стыки керамогранита")
		bot.send_message(message.chat.id,"~~~~~~~~~~")
		bot.send_video(message.chat.id, video=open('data/video/izgotov/izstup/3.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/5.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/izstup/6.jpg', 'rb'))
		bot.send_message(message.chat.id,"Изготовление ступеней любой сложности.")

	elif text == "Глубокий, насыщенный черный":
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/glubch/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/glubch/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/glubch/3.jpg', 'rb'))
		bot.send_message(message.chat.id,"Глубокий, насыщенный черный, выглядит стильно, прослужит вам долгие годы")

	elif text == "Роскошный глянец":
		bot.send_video(message.chat.id, video=open('data/video/izgotov/rasglan/1.mp4', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/rasglan/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/izgotov/rasglan/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Роскошный глянец, подберем цвет/рисунок/фактуру под ваш запрос!")

	elif text == "Ступени под дерево":
		bot.send_video(message.chat.id, video=open('data/video/rapocl/stuppodder/1.MOV', 'rb'))
		bot.send_video(message.chat.id, video=open('data/video/rapocl/stuppodder/2.MOV', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stuppodder/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stuppodder/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stuppodder/3.jpg', 'rb'))
		bot.send_message(message.chat.id,"Ступени под дерево? Легко! Главное отличие дерева от керамогранита - долговечность, ступени из керамогранита прослужат вам гораздо больше времени!")

	elif text == "Ступени в светлом варианте":
		bot.send_video(message.chat.id, video=open('data/video/rapocl/stupsvet/1.MOV', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stupsvet/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stupsvet/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stupsvet/3.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/stupsvet/4.jpg', 'rb'))
		bot.send_message(message.chat.id,"Ступени в светлом варианте. Как вам? Изготовление и монтаж выполнены нашей командой мастеров!")

	elif text == "Очередные наши работы":
		bot.send_video(message.chat.id, video=open('data/video/rapocl/ocher/1/1.MOV', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/1/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/1/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/1/3.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/1/4.jpg', 'rb'))
		bot.send_message(message.chat.id,"Очередное наше изготовление и монтаж, оцените качество проделанной работы нашими мастерами🔥")
		bot.send_message(message.chat.id,"~~~~~~~~~~")
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/2/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/2/2.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/2/3.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/2/4.jpg', 'rb'))
		bot.send_message(message.chat.id,"Нашей изготовление + монтаж нашими мастерами = довольный клиент, не переживающий за результат!")
		bot.send_message(message.chat.id,"~~~~~~~~~~")
		bot.send_video(message.chat.id, video=open('data/video/rapocl/ocher/3/1.MOV', 'rb'))
		bot.send_video(message.chat.id, video=open('data/video/rapocl/ocher/3/2.MOV', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/3/1.jpg', 'rb'))
		bot.send_photo(message.chat.id, photo=open('data/photo/rapocl/ocher/3/2.jpg', 'rb'))
		bot.send_message(message.chat.id,"Очередное наше изготовление и монтаж, клиент доволен, а мы рады качественно выполнять свою работу для вас!")

bot.infinity_polling()