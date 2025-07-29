import streamlit as st
import random
import re
import webbrowser

st.set_page_config(page_title="Tech Fest Chatbot")
st.title("🤖 TechFest Chatbot - JNTUH UCEJ")

# Sidebar with coordinator info and a random joke
st.sidebar.header("🎓 Coordinators")
st.sidebar.markdown("""
**HOD (CSE):** Dr. Sateesh Kumar  
**Prompt Fusion:** Akshaya - 📞 9234567890  
**Tech Trivia:** Abhiram - 📞 9492921565  
**Vision Board:** Vardhan - 📞 94925621180  
**Project Prism:** Vinay Vardhan - 📞 9876543770  
**Treasure Hunt:** Srujana - 📞 9876463211  
**Ideathon:** Srilatha - 📞 9826565412  
""")

jokes = [
    "Why did the computer get cold? Because it left its Windows open! 😄",
    "Why do Java developers wear glasses? Because they don't see sharp! 😂",
    "How do you comfort a JavaScript bug? You console it. 😆"
]
st.sidebar.subheader("😂 Joke of the Chat")
st.sidebar.write(random.choice(jokes))

# Chat history setup
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me something about the fest:")

responses = {
    "greeting": [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊 Ready to explore the fest details?",
        "Hey! Ask me anything about the events at JNTUH UCEJ."
    ],
    "how_are_you": [
        "I'm just a bot, but I'm excited about TechVeda 2K25! 🤖🎉",
        "Doing great! Ready to guide you through the CreScencE 2K25 technical details!"
    ],
    "technical_events": [
        "There are 6 exciting technical events at TechVeda 2K25! 🛠️\n\n1. Prompt Fusion\n2. Tech Trivia\n3. Vision Board\n4. Project Prism\n5. Treasure Hunt\n6. Ideathon\n\nAsk me about any event for more details!"
    ],
    "prompt_fusion": [
        "🎯 Prompt Fusion – Where words ignite innovation!\n🧠 Challenge: Craft the most clever AI prompt.\n📲 Criteria: Creativity + Clarity\n🏆 Prizes worth ₹1000 + Certificates\n📅 Deadline: April 10\n💸 Fee: ₹30\n📍 Online\n🔗 Submit here: [Prompt Fusion Form](https://forms.gle/XkhPA7ZhpW2MtkMr7)\n📞 Contact: Akshaya - 1234567890"
    ],
    "tech_trivia": [
        "🧠 Tech Trivia – Test your tech smarts!\n🧩 Round 1: Quiz\n💻 Round 2: Code It!\n📅 April 7 & 8 | 🕙 10 AM – 5 PM\n💸 Fee: ₹30\n📍 Academic Block 1 (CSE)\n🏆 Prizes worth ₹1500 + Certificates\n🔗 Register: [Tech Trivia Form](https://forms.gle/PFCgBKfUiDWA2NEi6)\n📞 Contact: Abhiram - 9492921180"
    ],
    "vision_board": [
        "🎨 Vision Board – Turn your tech dreams into art!\n🧠 Theme: Tech Innovation\n📅 April 10 | 🕙 10 AM – 5 PM\n💸 Fee: ₹30\n📍 Academic Block 1 (CSE)\n🏆 Prizes worth ₹800 + Certificates\n📞 Contact: Vardhan - 9492921180"
    ],
    "project_prism": [
        "🚀 Project Prism – Let your project shine!\n💡 Present your working prototype\n👥 Team Size: 2–4\n📅 April 10\n📍 Venue: Academic Block\n🏆 Prizes worth ₹2000 + Certificates\n📞 Contact: Vinay Vardhan - 9876543210"
    ],
    "treasure_hunt": [
        "🗺️ Treasure Hunt – Decode. Discover. Dash!\n💻 Solve C puzzles and find hidden clues\n📅 April 8 | 🕘 9 AM onwards\n📍 Campus-wide\n🏆 Winner gets ₹1000\n📞 Contact: Srujana - 9876543211"
    ],
    "ideathon": [
        "📢 Ideathon – Think. Pitch. Win!\n🌍 Solve real-world problems with your ideas\n👥 Team Size: 2–4\n📅 April 9 | 🕙 10 AM – 1 PM\n📍 Academic Block 1 (CSE)\n💸 Fee: ₹50 per team\n📅 Register by April 6\n🏆 Prizes worth ₹2500\n📞 Contact: Srilatha - 9876543212"
    ],
    "hod_info": [
        "👨‍🏫 Dr. Sateesh Kumar is the Head of the Department (HOD) for CSE at JNTUH UCEJ."
    ],
    "coordinator_info": [
        "🎯 Fest Coordinator: P. Sreenivasa Rao – Reach out for overall fest queries."
    ],
    "certificates": [
        "🏅 All participants receive participation certificates! Winners get special winning certificates too!"
    ],
    "techveda_info": [
        "🌟 TechVeda 2K25 – A Concept-Based Technical Fest on Generative AI!\n🚀 Organized by the Department of CSE, JNTUH UCEJ\n🧠 Dive into cutting-edge AI innovation\n🗓️ April 9–11, 2025\n🎯 Explore events like Prompt Fusion, Ideathon, and more!\nDon't miss this celebration of technology and creativity! 💡"
    ],
    "college_info": [
        "🏫 JNTUH College of Engineering Jagtial is a prestigious institution affiliated with Jawaharlal Nehru Technological University Hyderabad.\n🌐 Visit official website: https://jntuhcej.ac.in"
    ],
    "silly": [
        "Uhh... I would answer that, but I'm only trained in fest awesomeness! 😅 Try asking me about Prompt Fusion or Treasure Hunt!",
        "That's a fun question! But my brain is wired for TechVeda 2K25. 😄 Ask me about technical events instead!",
        "LOL, good one! But I only specialize in our cool tech fest. Ask me about Ideathon or Project Prism! 😎"
    ]
}

event_keywords = {
    "prompt fusion": "prompt_fusion",
    "tech trivia": "tech_trivia",
    "vision board": "vision_board",
    "project prism": "project_prism",
    "treasure hunt": "treasure_hunt",
    "ideathon": "ideathon"
}

if user_input:
    normalized_input = user_input.lower().strip()
    response = ""

    matched_event = next((event for event in event_keywords if event in normalized_input), None)

    if re.search(r'hi|hello|hey', normalized_input):
        response = random.choice(responses["greeting"])
    elif re.search(r'how are you', normalized_input):
        response = random.choice(responses["how_are_you"])
    elif re.search(r'technical events|events list|fest events', normalized_input):
        response = random.choice(responses["technical_events"])
    elif matched_event:
        key = event_keywords[matched_event]
        if re.search(r'(register|registration|link)', normalized_input):
            links = re.findall(r'https?://\S+', responses[key][0])
            response = f"🔗 Registration/Submission Link: {links[0]}" if links else "No link found."
        elif re.search(r'(submit|submission)', normalized_input):
            links = re.findall(r'https?://\S+', responses[key][0])
            response = f"📤 Submission Link: {links[0]}" if links else "No submission link provided."
        elif re.search(r'(contact|coordinator|phone|phone number)', normalized_input):
            phone = re.findall(r'\b\d{10}\b', responses[key][0])
            names = re.findall(r'Contact: ([A-Za-z ]+)', responses[key][0])
            if phone and names:
                response = f"📞 Contact {names[0]} - {phone[0]}"
            else:
                response = "Coordinator details not found."
        else:
            response = responses[key][0]
    elif re.search(r'hod|head of department|cse hod', normalized_input):
        response = responses["hod_info"][0]
    elif re.search(r'coordinator|fest coordinator|organising', normalized_input):
        response = responses["coordinator_info"][0]
    elif re.search(r'certificate|certificates|participation', normalized_input):
        response = responses["certificates"][0]
    elif re.search(r'techveda|tech veda|about fest|more text|more info|about technical fest', normalized_input):
        response = responses["techveda_info"][0]
    elif re.search(r'jntu|ucej|jntuh ucej|college', normalized_input):
        response = responses["college_info"][0]
        webbrowser.open("https://jntuhcej.ac.in")
    else:
        response = random.choice(responses["silly"])

    st.session_state.chat_history.append((user_input, response))

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if user_input and not st.session_state.submitted:
    st.session_state.submitted = True
    st.rerun()
elif not user_input:
    st.session_state.submitted = False

# Display chat history
if st.session_state.chat_history:
    st.subheader("💬 Chat History")
    for i, (question, answer) in enumerate(reversed(st.session_state.chat_history), 1):
        st.markdown(f"**You:** {question}")
        st.markdown(f"**Bot:** {answer}")
        st.markdown("---")
