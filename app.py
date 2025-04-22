import streamlit as st
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# 認証ファイルでログイン（credentials.jsonは同じフォルダに保存済）
import json
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds_dict = json.loads(st.secrets["GOOGLE_SHEET_CREDENTIALS"])
creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
client = gspread.authorize(creds)

# ✅ スプレッドシートのURL（あなたの共有シート）
SHEET_URL = "https://docs.google.com/spreadsheets/d/1vlpgyrgxNEqQylHdno5H47EFyFtYkt9iHOrNhDmkP6E/edit#gid=0"
sheet = client.open_by_url(SHEET_URL).sheet1

# Streamlit フォームUI
st.set_page_config(layout="centered")
st.title("✅ Google Sheets 連携フォーム")

name = st.text_input("名前")
age = st.number_input("年齢", min_value=0, max_value=120, step=1)
address = st.text_input("住所")

if st.button("登録"):
    if name and address:
        sheet.append_row([name, age, address])
        st.success("✅ 登録完了！Google Sheets に書き込まれました")
    else:
        st.warning("⚠ 名前と住所は必須です")
