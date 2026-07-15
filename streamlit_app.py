import random

import streamlit as st

WORDS = [
    {"word": "happy", "meaning": "행복한", "example": "I feel happy today."},
    {"word": "brave", "meaning": "용감한", "example": "She is brave in the school play."},
    {"word": "careful", "meaning": "조심하는", "example": "Be careful when you cross the street."},
    {"word": "curious", "meaning": "호기심이 많은", "example": "The child is curious about space."},
    {"word": "simple", "meaning": "간단한", "example": "This recipe is very simple."},
    {"word": "friendly", "meaning": "친절한", "example": "My teacher is friendly."},
    {"word": "quick", "meaning": "빠른", "example": "He is a quick runner."},
    {"word": "beautiful", "meaning": "아름다운", "example": "The sky looks beautiful tonight."},
    {"word": "difficult", "meaning": "어려운", "example": "Math is difficult for me."},
    {"word": "important", "meaning": "중요한", "example": "It is important to sleep well."},
]


def start_game():
    st.session_state.questions = random.sample(WORDS, k=8)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.submitted = False
    st.session_state.selected_answer = None
    st.session_state.feedback = ""
    st.session_state.last_correct = False


def build_options(correct_question):
    distractors = random.sample(
        [item for item in WORDS if item["word"] != correct_question["word"]],
        k=3,
    )
    options = [correct_question["meaning"]] + [item["meaning"] for item in distractors]
    random.shuffle(options)
    return options


def submit_answer():
    answer_key = f"answer_{st.session_state.current_index}"
    selected_answer = st.session_state.get(answer_key)

    if selected_answer is None:
        st.session_state.feedback = "답을 선택해 주세요!"
        st.session_state.submitted = False
        return

    question = st.session_state.questions[st.session_state.current_index]
    if selected_answer == question["meaning"]:
        st.session_state.score += 1
        st.session_state.feedback = "정답입니다! 😀"
        st.session_state.last_correct = True
    else:
        st.session_state.feedback = f"아쉽습니다. 정답은 {question['meaning']}입니다."
        st.session_state.last_correct = False

    st.session_state.submitted = True


if "questions" not in st.session_state:
    start_game()

st.set_page_config(page_title="영단어 게임", page_icon="📚")
st.title("📚 중학생용 영단어 게임")
st.write("영단어의 뜻을 고르고, 점수를 올려보세요!")
st.caption("한 번에 8문제를 풀고 결과를 확인할 수 있어요.")

col1, col2 = st.columns([1, 1])
with col1:
    st.metric("현재 점수", f"{st.session_state.score}/{len(st.session_state.questions)}")
with col2:
    st.metric("문제 번호", f"{st.session_state.current_index + 1}/{len(st.session_state.questions)}")

if st.button("새 게임 시작", use_container_width=True):
    start_game()

if st.session_state.current_index < len(st.session_state.questions):
    question = st.session_state.questions[st.session_state.current_index]

    st.subheader(question["word"])
    st.write(f"예문: {question['example']}")

    options = build_options(question)
    answer_key = f"answer_{st.session_state.current_index}"
    st.radio("뜻을 고르세요", options=options, key=answer_key, index=None)

    if not st.session_state.submitted:
        if st.button("정답 확인", use_container_width=True):
            submit_answer()
    else:
        if st.session_state.last_correct:
            st.success(st.session_state.feedback)
        else:
            st.error(st.session_state.feedback)

        if st.button("다음 문제", use_container_width=True):
            st.session_state.current_index += 1
            st.session_state.submitted = False
            st.session_state.selected_answer = None
else:
    st.balloons()
    st.success(f"게임 끝! 총 {st.session_state.score}문제를 맞혔어요.")
    st.write("다시 도전해 보세요!")
    if st.button("다시 시작하기", use_container_width=True):
        start_game()
