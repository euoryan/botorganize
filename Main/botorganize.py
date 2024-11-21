import os
import json
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram.error import BadRequest

class HashtagBot:
    def __init__(self, token):
        self.token = token
        self.LIST_FILE = 'hashtag_database.json'
        self.LOG_FILE = 'bot_log.json'
        self.ALLOWED_USER_ID = ALLOWED_USER_ID
    
    def load_data(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save_data(self, data, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    
    async def start(self, update: Update, context):
        await update.message.reply_text(
            "Bot de organização de links iniciado. Envie mensagens com hashtags."
        )
    
    async def handle_message(self, update: Update, context):
        if update.message.from_user.id != self.ALLOWED_USER_ID:
            return
        
        message = update.message
        text = message.text or message.caption
        
        if not text:
            return
        
        links_data = self.load_data(self.LIST_FILE)
        log_data = self.load_data(self.LOG_FILE)
        
        message_link = f"https://t.me/c/{message.chat.id}/{message.message_id}"
        
        parts = text.split('#')
        
        title = parts[0].strip()
        
        hashtags = [tag.strip().split(' ', 1) for tag in parts[1:]]
        
        for hashtag_info in hashtags:
            tag = hashtag_info[0]
            description = hashtag_info[1] if len(hashtag_info) > 1 else title
            
            if tag not in links_data:
                links_data[tag] = []
            
            entry = {
                'text': description,
                'link': message_link
            }
            
            if entry not in links_data[tag]:
                links_data[tag].append(entry)
        
        self.save_data(links_data, self.LIST_FILE)
        
        index_message = "Links por Tag 🏷️\n\n"
        for tag in sorted(links_data.keys()):
            for entry in links_data[tag]:
                index_message += f"#{tag} {entry['text']}\n"
        
        try:
            if 'pinned_message_id' in log_data:
                await context.bot.edit_message_text(
                    chat_id=message.chat_id,
                    message_id=log_data['pinned_message_id'],
                    text=index_message
                )
            else:
                raise BadRequest("Mensagem não encontrada")
        
        except (BadRequest, Exception):
            try:
                pinned_msg = await message.chat.send_message(index_message)
                await pinned_msg.pin()
                
                log_data['pinned_message_id'] = pinned_msg.message_id
                self.save_data(log_data, self.LOG_FILE)
            
            except Exception as e:
                print(f"Erro crítico ao criar mensagem: {e}")
    
    def run(self):
        app = Application.builder().token(self.token).build()
        
        app.add_handler(CommandHandler('start', self.start))
        app.add_handler(MessageHandler(filters.ALL, self.handle_message))
        
        print("Bot iniciado...")
        app.run_polling(drop_pending_updates=True)

# Token do bot
TOKEN = 'TOKEN'

# Inicializa e roda o bot
bot = HashtagBot(TOKEN)
bot.run()