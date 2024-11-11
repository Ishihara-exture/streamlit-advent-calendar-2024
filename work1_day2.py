import streamlit as st

st.title("Streamlitクリスマスカード 🎅")

# ボタンを押すと雪が降る
button_pushed = st.button("雪を降らせる")
if button_pushed:
    st.snow()

# テキストを入力させる
name = st.text_input(f"あなたのお名前")
# 選択肢から国を選ばせる
country = st.selectbox(f"あなたが住んでいる国", ["", "日本", "アメリカ", "中国", "オーストラリア"])

# 入力内容を表示する
st.write(name)
st.write(country)

# 名前と国が両方とも入力されたとき
if name != "" and country != "":
    st.write("必要な情報が揃いました！")
