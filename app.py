from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI

# =========================
# LLMに問い合わせる関数
# =========================
def ask_llm(user_input: str, expert_type: str) -> str:
    if expert_type == "仕事効率化の専門家":
        system_prompt = "あなたは仕事効率化の専門家です。実践的で具体的なアドバイスをしてください。"
    else:
        system_prompt = "あなたは健康管理の専門家です。初心者にも分かりやすく説明してください。"

    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.5
    )

    # ★ここが新しいやり方：辞書形式で messages を渡す
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]

    response = llm.invoke(messages)
    return response.content


# =========================
# Streamlit UI
# =========================
st.title("LLM機能付きWebアプリ")
st.write("""
このアプリでは、入力したテキストに対して  
選択した分野の専門家としてLLMが回答します。
""")

expert = st.radio(
    "専門家の種類を選択してください",
    ["仕事効率化の専門家", "健康管理の専門家"]
)

user_text = st.text_input("LLMに質問したい内容を入力してください")

if st.button("実行"):
    if user_text:
        with st.spinner("LLMが考え中です..."):
            answer = ask_llm(user_text, expert)
        st.write("### 回答")
        st.write(answer)
    else:
        st.error("質問内容を入力してください。")
