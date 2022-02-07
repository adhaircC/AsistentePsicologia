from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from random import randint

bot = Bot(token='5201672492:AAHSfjSyNqQyiCX-zyYv1EITNvXkcaGDIB4')
dp = Dispatcher(bot)

buttonSalir = InlineKeyboardButton(text="👋 Adios", callback_data="salir")
buttonA = InlineKeyboardButton(text="PROBLEMAS EN ESTUDIANTES UNIVERSITARIOS", callback_data="nodoA")
#Jose
buttonB = InlineKeyboardButton(text="BAJA AUTOESTIMA", callback_data="nodoB")
buttonC = InlineKeyboardButton(text="PROBLEMAS PERSONALES", callback_data="nodoC")
buttonD = InlineKeyboardButton(text="BAJO RENDIMIENTO", callback_data="nodoD")
buttonE = InlineKeyboardButton(text="BULLYNG", callback_data="nodoE")
buttonF = InlineKeyboardButton(text="INSEGURIDAD", callback_data="nodoF")
#Joel
buttonG = InlineKeyboardButton(text="FALTA DE MOTIVACION", callback_data="nodoG")
buttonH = InlineKeyboardButton(text="ADDICIONES", callback_data="nodoH")
buttonI = InlineKeyboardButton(text="BAJO NIVEL SOCIOECONOMICO", callback_data="nodoI")
buttonJ = InlineKeyboardButton(text="VIOLENCIA FAMILIAR", callback_data="nodoJ")
#Amilcar
buttonK = InlineKeyboardButton(text="ESTUDIA PERO NO LO REFLEJA EN SUS NOTAS", callback_data="nodoK")
buttonL = InlineKeyboardButton(text="TRABAJA Y NO TIENE TIEMPO PARA DEDICARSE A SUS ESTUDIOS", callback_data="nodoL")
buttonO = InlineKeyboardButton(text="FALTA DE HERRAMIENTAS", callback_data="nodoO")
buttonP = InlineKeyboardButton(text="MALA ALIMENTACION", callback_data="nodoP")
#Adhair
buttonQ = InlineKeyboardButton(text="DROGADICCION", callback_data="nodoQ")
buttonR = InlineKeyboardButton(text="DEFICIT DE ATENCIO Y CONCENTRACION", callback_data="nodoR")
buttonX = InlineKeyboardButton(text="LUDOPATIA", callback_data="nodoX")
buttonW = InlineKeyboardButton(text="ALCOHOLISMO", callback_data="nodoW")


MenuPrincipal = InlineKeyboardMarkup().add(buttonA).add(buttonSalir)
MenuEstudianteConProblemas = InlineKeyboardMarkup().add(buttonB).add(buttonD)
MenuBajaAutoestima = InlineKeyboardMarkup().add(buttonE, buttonF, buttonG, buttonC)
MenuBajoRendimiento = InlineKeyboardMarkup().add(buttonG, buttonK).add(buttonL)
MenuProblemasPersonales = InlineKeyboardMarkup().add(buttonH, buttonI, buttonJ)
MenuAdicciones = InlineKeyboardMarkup().add(buttonW, buttonX, buttonQ)
MenuBajoNivelSocioeconomico = InlineKeyboardMarkup().add(buttonP, buttonO)
MenuEstudiaPeroNoRefleja = InlineKeyboardMarkup().add(buttonO, buttonR)

@dp.message_handler(commands=['Empezar'])
async def asistente_psicologia(message: types.Message):
    await message.reply("Hola soy Roxy tu asistente de psicologia:", reply_markup=MenuPrincipal)


@dp.callback_query_handler(text=["nodoA", "nodoB", "nodoC", "nodoD", "nodoE", "nodoF", "nodoG", "nodoH","nodoI" , "nodoJ", "nodoK","nodoL" ,"nodoO" ,"nodoP" ,"nodoQ" , "nodoR", "nodoX", "nodoW"])
async def respuestas_asistente(call: types.CallbackQuery):
    if call.data == "nodoA":
        await call.message.reply("bla bla bla:", reply_markup=MenuEstudianteConProblemas)
    if call.data == "nodoB":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuBajaAutoestima)
    if call.data == "nodoC":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuProblemasPersonales)
    if call.data == "nodoD":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuBajoRendimiento)
    if call.data == "nodoE":
        await call.message.answer("resp")
    if call.data == "nodoF":
        await call.message.answer("resp")
    if call.data == "nodoG":
        await call.message.answer("resp")
    if call.data == "nodoH":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuAdicciones)
    if call.data == "nodoI":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuBajoNivelSocioeconomico)
    if call.data == "nodoJ":
        await call.message.answer("resp")
    if call.data == "nodoK":
        await call.message.reply("bla bla bla bla:", reply_markup=MenuEstudiaPeroNoRefleja)
    if call.data == "nodoL":
        await call.message.answer("resp")
    if call.data == "nodoO":
        await call.message.answer("resp")
    if call.data == "nodoP":
        await call.message.answer("resp")
    if call.data == "nodoQ":
        await call.message.answer("resp")
    if call.data == "nodoR":
        await call.message.answer("resp")
    if call.data == "nodoX":
        await call.message.answer("resp")
    if call.data == "nodoW":
        await call.message.answer("resp")

    await call.answer()

executor.start_polling(dp)