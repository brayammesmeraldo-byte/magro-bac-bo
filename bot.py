from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import data

TOKEN = "8586340424:AAF5Xno3ZiGMJatNX30r8_c_2dn5h"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏆 MAGRO BAC BO — GOLD EDITION 🎰\n\n"
        "Comandos:\n"
        "/add P - Registrar Player\n"
        "/add B - Registrar Banker\n"
        "/add T - Registrar Tie\n"
        "/stats - Estatísticas\n"
        "/suggest - Tendência atual"
    )

async def add(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Use: /add P, /add B ou /add T")
        return
    result = context.args[0].upper()
    if result not in ["P", "B", "T"]:
        await update.message.reply_text("❌ Valor inválido. Use P, B ou T.")
        return
    data.add_result(result)
    await update.message.reply_text(f"🎯 Resultado {result} registrado com sucesso.")

async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    stats = data.get_stats()
    msg = (
        f"📊 MAGRO BAC BO — Estatísticas:\n"
        f"Rodadas: {stats['total']}\n"
        f"Player: {stats['P_pct']}%\n"
        f"Banker: {stats['B_pct']}%\n"
        f"Tie: {stats['T_pct']}%"
    )
    await update.message.reply_text(msg)

async def suggest(update: Update, context: ContextTypes.DEFAULT_TYPE):
    s = data.suggest()
    await update.message.reply_text(f"💡 Tendência estatística atual: {s}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("stats", stats))
app.add_handler(CommandHandler("suggest", suggest))

app.run_polling()