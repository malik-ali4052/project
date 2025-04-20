import streamlit as st
st.set_page_config(page_title="Mindset Growth Project GIAIC", page_icon="🧠")
st.title("**Mindset Growth Challange Program**")

# Adding text to the sidebar
st.sidebar.title("Mindset Growth Program")
st.sidebar.write("Welcome to the Mindset Growth Program! This program is designed to help you develop a growth mindset and achieve your goals.")

# Adding a button to the sidebar
if st.sidebar.button("Get Started"):
    st.write("Let's get started!")

st.header("**Let's start your mindset growth journey**") 
st.write("**What is a Growth Mindset?**")
st.write("A growth mindset is the belief that your abilities and intelligence can be developed through hard work, perseverance, and learning from your mistakes. This concept was popularized by psychologist Carol Dweck, and it challenges the notion that our skills are fixed from the start. Instead,/n it reminds us that every challenge is an opportunity to learn and improve.")
st.header("Ready for the Challanges")
if st.button("Yes, I'm ready"):
        challanges = [
            "Learn something new every day for a week",
            "Ask for feedback on your work",
            "Take on a new responsibility at work",
            "Teach someone something you know",
            "Set a new goal for yourself",
            "Read a book about a new topic",
            "Take a class or workshop",]
        import random
        challange = random.choice(challanges)
        st.write(f" let's start with {challange}")
else:
        st.write("**Click the button to get a new challenge**")
st.header("Share your Journey")
st.write("Share your progress, thoughts, and experiences with the community. You can also ask for advice, support, or feedback from others who are on the same journey. Remember, we're all in this together!")
response = st.text_area("**Share your thoughts here**")

if st.button("Submit"):
    st.write("Thanks for sharing! Your post has been submitted.")
else:
    st.info("Click the button to submit your post")
st.header("Achivments")
achivments = st.text_input("Check here to see your achivments")
if achivments:
    st.success("Great you achived your goal")
else:
      st.info("Every achivment is a step towards your growth mindset journey")


#footer
st.write("- - -")
st.write("**⛔Developed by Muhammad Ali**")
      