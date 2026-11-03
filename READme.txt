TraceGuard: Social Media Text Analyzer (research project)

Reads recent public posts from a Telegram channel (Instagram and X
scrapers are included but need their own credentials), compares the text
to a reference set using TF-IDF and cosine similarity, and generates a PDF
report with a summary (facebook/bart-large-cnn) and a word cloud.

Intended use: education and research on public content only. The score
measures word overlap with a reference set you provide. It is not
evidence about any person or channel. Do not use it to target individuals.

SETUP (Windows PowerShell)
1. git clone https://github.com/hemanth10718/Real-Time_Social_Media_Monitoring_NLP_Pipeline
2. cd into the "Trace Guard" folder
3. Use Python 3.11 or 3.12 (3.13 fails on the pinned pandas):
   py -3.11 -m venv venv
   venv\Scripts\Activate.ps1
   pip install -r requirements.txt
4. Create a .env file in "Trace Guard" (never commit it):
   FLASK_SECRET_KEY=<random string>
   TELEGRAM_API_ID=<from my.telegram.org>
   TELEGRAM_API_HASH=<from my.telegram.org>
   TELEGRAM_SESSION=<created in step 5>
   Optional: INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD, TWITTER_BEARER_TOKEN
5. One-time Telegram login. It stores a session string in .env, which gives
   access to that Telegram account, so keep it private:
   python -c "import os; from dotenv import load_dotenv; from telethon.sync import TelegramClient; from telethon.sessions import StringSession; load_dotenv(); c=TelegramClient(StringSession(), int(os.getenv('TELEGRAM_API_ID')), os.getenv('TELEGRAM_API_HASH')); c.start(); open('.env','a').write('\nTELEGRAM_SESSION='+c.session.save()+'\n'); c.disconnect(); print('saved')"
6. python app.py, then open http://127.0.0.1:5000/telegram and enter a
   public channel such as @telegram.

NOTES
- The first report downloads a ~1.6 GB model (facebook/bart-large-cnn).
- reference_data.csv holds made-up sample text. Replace it with your own
  set. Both CSVs need a "text" column.
- X (Twitter) API access for reading is paid, so it was not used for testing.
- Stack: Flask, pandas, scikit-learn, transformers + torch, wordcloud,
  fpdf2, telethon, tweepy, instaloader.
