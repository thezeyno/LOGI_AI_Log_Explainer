import streamlit as st
import requests
import os
from dotenv import load_dotenv

# 1. Ayarlar
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(page_title="Logi - AI Log Explainer", page_icon="🤖")

st.title("🤖 Logi'ye Hoş Geldin!")
st.markdown("### Karmaşık logları ver, çözümü al.")

log_input = st.text_area("Hata mesajını buraya yapıştır:", height=150)

if st.button("Logi, Çöz Şunu! ✨"):
    if log_input:
        with st.spinner("Logi analiz ediyor..."):
            # BU KISIM SIHİRLİ: Doğrudan v1 kapısına gidiyoruz, beta ile işimiz yok!
            # Mevcut URL satırını bul ve bununla değiştir:
            # Koddaki URL'yi tam olarak bu yap (Kendi anahtarın .env içinde kalsın)
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent?key={API_KEY}"
            
            payload = {
                "contents": [{
                    "parts": [{"text": f"Bir sistem asistanı olarak şu logu analiz et ve adım adım çözüm sun: {log_input}"}]
                }]
            }
            
            try:
                response = requests.post(url, json=payload)
                result = response.json()
                
                # Yanıtı ekrana yazdır
                answer = result['candidates'][0]['content']['parts'][0]['text']
                st.success("Analiz Tamamlandı!")
                st.markdown("---")
                st.markdown(answer)
                
            except Exception as e:
                st.error("Logi şu an bir bağlantı sorunu yaşıyor. Lütfen API anahtarını ve internetini kontrol et.")
                # Hata detayını merak edersek: st.write(result)
    else:
        st.warning("Önce bir log gir!")