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


def render_word_game():
    st.title("📚 영단어 게임")
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
    else:
        st.balloons()
        st.success(f"게임 끝! 총 {st.session_state.score}문제를 맞혐어요.")
        st.write("다시 도전해 보세요!")
        if st.button("다시 시작하기", use_container_width=True):
            start_game()


def render_bts_page():
    st.title("🎤 BTS 소개")
    st.write("BTS는 한국의 아주 유명한 음악 그룹입니다.")
    st.write("멋진 음악, 화려한 춤, 그리고 따뜻한 메시지로 많은 사람들에게 사랑받고 있어요.")

    st.image(
        "https://images.unsplash.com/photo-1516280440614-37939bbacd81?auto=format&fit=crop&w=1200&q=80",
        caption="BTS의 특별한 무대",
        use_container_width=True,
    )

    st.subheader("✨ BTS의 매력")
    st.markdown(
        "- 멋진 노래와 춤을 보여줘요.\n"
        "- 친구들과 함께 성장하는 이야기를 담아요.\n"
        "- 세계 많은 사람들에게 사랑받고 있어요."
    )

    st.subheader("🌟 멤버")
    members = [
        ("RM", "리더이자 랩을 맡아요.", "https://images.unsplash.com/photo-1501386761578-eac5c94b800a?auto=format&fit=crop&w=600&q=80"),
        ("진", "부드러운 목소리로 노래해요.", "https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?auto=format&fit=crop&w=600&q=80"),
        ("슈가", "재치 있는 랩과 멋진 표현을 해요.", "https://images.unsplash.com/photo-1470225620780-dba8ba36b745?auto=format&fit=crop&w=600&q=80"),
        ("제이홉", "에너지 넘치는 춤과 노래를 보여줘요.", "https://images.unsplash.com/photo-1511671782779-c97d3d27a1d4?auto=format&fit=crop&w=600&q=80"),
        ("지민", "유연한 춤과 강한 분위기를 보여줘요.", "https://images.unsplash.com/photo-1498036882173-b41c28a8ba34?auto=format&fit=crop&w=600&q=80"),
        ("뷔", "차분하면서도 특별한 매력을 보여줘요.", "https://images.unsplash.com/photo-1524504388940-b1c1722653e1?auto=format&fit=crop&w=600&q=80"),
        ("정국", "높은 음역대와 열정적인 무대를 보여줘요.", "https://images.unsplash.com/photo-1485579149621-3123dd979885?auto=format&fit=crop&w=600&q=80"),
    ]

    for name, role, image_url in members:
        with st.container():
            st.image(image_url, width=220)
            st.write(f"**{name}**: {role}")

    st.subheader("🎵 대표곡")
    songs = [
        ("Dynamite", "밝고 신나는 느낌이 특징이에요."),
        ("Butter", "달콤하고 귀여운 분위기의 노래예요."),
        ("Spring Day", "감동적이고 따뜻한 느낌의 노래예요."),
    ]

    for song, description in songs:
        st.write(f"- **{song}**: {description}")


if "questions" not in st.session_state:
    start_game()

st.set_page_config(page_title="영단어와 BTS", page_icon="📚")
st.title("📚 영어 공부 + BTS")
st.write("영단어 게임도 하고 BTS도 소개해 보세요!")

word_tab, bts_tab = st.tabs(["📚 영단어 게임", "🎤 BTS 소개"])

with word_tab:
    render_word_game()

with bts_tab:
    render_bts_page()
