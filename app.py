from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import streamlit as st
import os
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

st.title("キャリアに関する悩みを相談するアプリ")

st.write("##### 動作モード: キャリアコンサルティング")
st.write("相談ポイントを選択し、入力フォームに相談内容を入力すると適切に回答してくれます。")

selected_item = st.radio(
    "相談モードを選択してください。",
    ["キャリアの悩み", "人間関係の悩み", "その他"]
)

st.divider()

if selected_item == "キャリアの悩み":
    input_message = st.text_input(label="相談したいことを入力して下さい。")
    system_prompt = "あなたはキャリアの悩みに詳しいアドバイザーです。相談内容に対して、優先順位順に重要な3つのアドバイスを日本語で箇条書きで出してください。"

elif selected_item == "人間関係の悩み":
    input_message = st.text_input(label="相談したいことを入力して下さい。")
    system_prompt = "あなたは人間関係の悩みに詳しいアドバイザーです。相談内容に対して、優先順位順に重要な3つのアドバイスを日本語で箇条書きで出してください。"

elif selected_item == "その他": 
    input_message = st.text_input(label="相談したいことを入力して下さい。")
    system_prompt = "あなたはその他の悩みに詳しいアドバイザーです。相談内容に対して、優先順位順に重要な3つのアドバイスを日本語で箇条書きで出してください。"

# LLM呼び出しとStreamlit表示の統合
if st.button("実行"):
    st.divider()
    if input_message:
        st.write(f"相談内容: **{input_message}**")

        llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=input_message),
        ]
        result = llm(messages)

        st.write("### 回答")
        st.write(result.content)
    else:
        st.error("相談内容を入力してから「実行」ボタンを押してください。")

    
