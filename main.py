import streamlit as st
from PIL import Image

st.set_page_config(page_title="Valentine Quiz ❤️", layout="centered", page_icon="❤️", initial_sidebar_state="collapsed")

# Custom CSS for Valentine's theme
st.markdown("""
<style>
    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #ffe5ec 0%, #fff0f5 50%, #ffe5ec 100%);
    }
    
    /* Text styling */
    h1, h2, h3, h4 {
        color: #d63384 !important;
        font-weight: 600 !important;
        letter-spacing: 0.5px;
    }
    
    p {
        color: #555 !important;
        font-size: 16px !important;
    }
    
    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #ff69b4 0%, #ff1493 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        font-size: 16px !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 12px 30px !important;
        box-shadow: 0 4px 15px rgba(255, 20, 147, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(255, 20, 147, 0.4) !important;
    }
    
    /* Success and error messages */
    .stSuccess, .stError, .stInfo {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border-left: 5px solid #ff1493 !important;
        border-radius: 8px !important;
        padding: 15px !important;
    }
    
    .stSuccess {
        border-left-color: #ff69b4 !important;
    }
    
    .stError {
        border-left-color: #d63384 !important;
    }
    
    .stInfo {
        border-left-color: #ffc0cb !important;
    }
    
    /* Slider styling */
    .stSlider {
        padding: 20px 0;
    }
    
    /* Input field */
    .stTextInput > div > div > input {
        border: 2px solid #ffc0cb !important;
        border-radius: 10px !important;
        background-color: white !important;
        font-size: 16px !important;
        color: black;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #ff69b4 !important;
        box-shadow: 0 0 10px rgba(255, 105, 180, 0.2) !important;
    }
            
    [data-testid="stElementToolbarButton"] {
        display: none !important;
    }
            
</style>
""", unsafe_allow_html=True)


@st.cache_data
def load_image(image_path):
    """Cache images to avoid reloading on every rerun"""
    return Image.open(image_path)


# --- Initialize session state ---
if "stage" not in st.session_state:
    st.session_state.stage = "name_input"  
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "answer_correct" not in st.session_state:
    st.session_state.answer_correct = None
if "name_valid" not in st.session_state:
    st.session_state.name_valid = None
if "slider_value" not in st.session_state:
    st.session_state.slider_value = 0
if "heart_fill" not in st.session_state:
    st.session_state.heart_fill = 0




# Define questions
questions = [
    {
        "prompt": "Who makes you smile the most?",
        "images": ["images/frank.jpg", "images/chalamet.jpg"],
        "labels": ["Frank💙", "Timothee Chalamet"],
        "answers": [True, False]
    },
    {
        "prompt": "Who would you swipe right on?",
        "images": ["images/jordan.jpg", "images/frank.jpg"],
        "labels": ["Michalel B. Jordan", "Frank💙"],
        "answers": [False, True]
    },
    {
        "prompt": "Who gives the best cuddles?",
        "images": ["images/efron.jpg", "images/frank.jpg"],
        "labels": ["Zac Efron", "Frank💙"],
        "answers": [False, True]
    },
    {
        "prompt": "Who’s the real MVP?⚾",
        "images": ["images/frank.jpg", "images/volpe.jpg"],
        "labels": ["Frank💙", "Anthony Volpe"],
        "answers": [True, False]
    },
    {
        "prompt": "Who’s your all-time favorite guy to laugh with? 😄💙",
        "images": ["images/sandler.jpg", "images/frank.jpg"],
        "labels": ["Adam Sandler", "Frank💙"],
        "answers": [False, True]
    },
]

def show_image_question(question_data):
    # Centered question
    st.markdown(f"<h3 style='text-align:center'>{question_data['prompt']}</h3>", unsafe_allow_html=True)
    
    # Display messages at the top, right after question - no scrolling needed
    if st.session_state.answer_correct is True:
        st.success("💖 Great Pick! You Got Good Taste! 💖")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next ➡️", key=f"next_{st.session_state.question_index}", use_container_width=True):
                st.session_state.question_index += 1
                st.session_state.answer_correct = None
                st.rerun()
        return
    elif st.session_state.answer_correct is False:
        st.error("❌ Sorry, he's not available! Try again!")
        st.markdown("")

    # Simple two column layout for mobile
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(load_image(question_data["images"][0]), width=350)
        if st.button(question_data["labels"][0], key=f"{st.session_state.question_index}_0", use_container_width=True):
            if question_data["answers"][0]:
                st.session_state.answer_correct = True
            else:
                st.session_state.answer_correct = False
            st.rerun()

    with col2:
        st.image(load_image(question_data["images"][1]), width=350)
        if st.button(question_data["labels"][1], key=f"{st.session_state.question_index}_1", use_container_width=True):
            if question_data["answers"][1]:
                st.session_state.answer_correct = True
            else:
                st.session_state.answer_correct = False
            st.rerun()


def show_name_input():
    st.markdown("<h1 style='text-align: center;'>💝 Who's Your Crush? 💝</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Enter the first name of your crush below</p>", unsafe_allow_html=True)
    
    names = ['frank']
    
    # Center the input and button
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        question = st.text_input('Enter a name:', placeholder="Type here...")
        
        if st.button('Check Compatability', use_container_width=True):
            valid = question.lower() in names
            st.session_state.name_valid = valid

    # Display messages based on validation - full width
    if st.session_state.name_valid is True:
        st.success('💖 Congrats Your a Match! 💖')
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next ➡️", key="name_next", use_container_width=True):
                st.session_state.stage = "quiz"
                st.session_state.name_valid = None
                st.rerun()
    elif st.session_state.name_valid is False:
        st.error('❌ Sorry, that name is not a match. Try again!')


def show_slider_question():
    st.markdown("<h1 style='text-align: center;'>💕 How Much Do You Love Frank? 💕</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Drag the slider all the way to the right to proceed</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.5, 3, 0.5])
    
    with col2:
        st.session_state.slider_value = st.slider(
            "Love Level",
            min_value=0,
            max_value=100,
            value=st.session_state.slider_value,
            label_visibility="collapsed"
        )
    
    st.markdown("")  # Add spacing
    
    # Show Next button only when slider is at max
    if st.session_state.slider_value == 100:
        st.success("❤️ Maximum Love Detected! You're ready for the final challenge! ❤️")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next ➡️", key="slider_next", use_container_width=True):
                st.session_state.stage = "heart"
                st.session_state.slider_value = 0
                st.rerun()
    else:
        st.info(f"💭 Current Love Level: {st.session_state.slider_value}% - Drag all the way to 100%!")


def show_heart_game():
    st.markdown("<h1 style='text-align: center;'>💖 Fill Your Heart With Love 💖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Frank wants to fill your heart with love 💖 Click to fill it!</p>", unsafe_allow_html=True)
    
    st.markdown("")  # Add spacing
    
    # Display heart fill percentage with visual representation
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # Visual heart meter
        filled_hearts = int(st.session_state.heart_fill / 10)
        empty_hearts = 10 - filled_hearts
        heart_display = "❤️" * filled_hearts + "🤍" * empty_hearts
        st.markdown(f"<h2 style='text-align: center;'>{heart_display}</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center;'>{st.session_state.heart_fill}%</h3>", unsafe_allow_html=True)
        
        st.markdown("")
        
        if st.button("Click to Fill Heart ❤️", use_container_width=True, key="heart_click"):
            st.session_state.heart_fill += 10
            if st.session_state.heart_fill > 100:
                st.session_state.heart_fill = 100
            st.rerun()
    
    st.markdown("")  # Add spacing
    
    # Show Next button only when heart is full
    if st.session_state.heart_fill == 100:
        st.success("💖 Your heart is completely full of love! 💖")
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("Next ➡️", key="heart_next", use_container_width=True):
                st.session_state.stage = "valentine_question"
                st.session_state.heart_fill = 0
                st.rerun()
    else:
        st.info(f"Keep clicking to fill your heart! {st.session_state.heart_fill}% filled")


def show_valentine_question():
    st.markdown("<h1 style='text-align: center;'>💝 Will You Be My Valentine? 💝</h1>", unsafe_allow_html=True)
    
    st.markdown("")  # Add spacing
    st.markdown("")  # Add spacing
    
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("YES ❤️", use_container_width=True, key="valentine_yes"):
            st.balloons()
            st.success("🥰 YES! I love you SO MUCH! 🥰")
            st.markdown("")
            st.image("images/final.jpg", width=500)
            st.session_state.stage = "complete"


    
# --- Main logic ---
if st.session_state.stage == "name_input":
    show_name_input()
elif st.session_state.stage == "quiz":
    if st.session_state.question_index < len(questions):
        show_image_question(questions[st.session_state.question_index])
    else:
        st.session_state.stage = "slider"
        st.rerun()
elif st.session_state.stage == "slider":
    show_slider_question()
elif st.session_state.stage == "heart":
    show_heart_game()
elif st.session_state.stage == "valentine_question":
    show_valentine_question()