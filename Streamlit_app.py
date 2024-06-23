from pathlib import Path 

import streamlit as st #pip install streamlit
from PIL import Image #pip install pillow

#----PATH SETTINGS----

THIS_DIR = Path(__file__).parent if __file__ in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

#----GENERAL SETTINGS----

STRIPE_CHECKOUT = "https://donate.stripe.com/test_3csaICf0ieccf5ebII"
CONTACT_EMAIL = "mahajanchirag718@gmail.com"
PRODUCT_VIDEO = "https://youtu.be/YdWNlUiMDhc?si=mYMpJMA2BaMcdYcK"
PRODUCT_NAME = "AquaShine: Rejuvenating Argan Oil Shampoo"
PRODUCT_TAGLINE= "Unveil Your Hair's Elegance"
PRODUCT_DESCRIPTION = """**AquaShine: Rejuvenating Argan Oil Shampoo**

Discover the secret to luxurious, radiant hair with AquaShine Shampoo. Infused with the finest Argan oil and a rich blend of essential nutrients, AquaShine provides your hair with the ultimate nourishment it deserves. This premium formula not only cleanses but also rejuvenates, leaving your hair feeling silky, smooth, and naturally vibrant.

Key Features:

-Argan Oil Enrichment: Deeply hydrates and nourishes, restoring natural shine and softness.

-Essential Nutrients: Fortified with vitamins and minerals to strengthen and revitalize hair from root to tip.

-Gentle Cleansing: Removes impurities without stripping essential moisture, maintaining hair’s natural balance.

-Enhanced Manageability: Reduces frizz and tangles for smoother, more manageable hair.

-Luxurious Lather: Indulge in a rich, creamy lather that pampers your hair with every wash.

-Suitable for All Hair Types: Ideal for daily use on all hair types, including color-treated hair.


**Embrace the elegance of AquaShine Shampoo and transform your hair care routine into a spa-like experience. Let the natural radiance of your hair shine through, beautifully nourished and exquisitely maintained.**"""

def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    

#----PAGE SETTINGS----

st.set_page_config(
page_title = PRODUCT_NAME,
page_icon = ":leaf_fluttering_in_wind:",
layout = "centered",
initial_sidebar_state= "collapsed",)

load_css_file(CSS_FILE)
#----MAIN SECTION----

st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))

with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(f'<a href={STRIPE_CHECKOUT} class="button">👉 Buy The Product</a>',
                unsafe_allow_html=True,)
    
with right_col:
    PRODUCT_IMAGE= Image.open(ASSETS_DIR / "Shampoo.webp")
    st.image(PRODUCT_IMAGE, width=450)   




#----FEATURES SECTION----

st.write("")
st.write("---")
st.header(":seedling: Features")

features = {
    "argan.jpg": ["Nourishing Elixir: Enriched with Argan Oil and Essential Minerals",
                  "Experience the transformative power of AquaShine Shampoo, enriched with luxurious Argan oil and essential minerals. This nourishing elixir deeply hydrates and revitalizes your hair, restoring its natural shine and strength for a truly radiant look.",],
    
    "lather.jpg": ["Luxurious Lather: Indulge in Rich, Creamy Cleansing",
                   "Immerse your hair in the sumptuous lather of AquaShine Shampoo. Our rich, creamy formula ensures a thorough cleanse, enveloping each strand in a luxurious foam that pampers your hair and scalp, leaving them feeling refreshed and rejuvenated.",],
    
    "silky_hair.jpg": ["Silky Smooth: Say Goodbye to Frizz",
                       "Achieve effortlessly silky and smooth hair with AquaShine Shampoo. Our advanced formula tames frizz and flyaways, leaving your hair beautifully sleek and manageable. Experience the ultimate in smoothness, with hair that feels soft to the touch and looks flawlessly polished all day long.",],

}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width = True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


#----DEMO----

st.write("")
st.write("---")
st.subheader(":tv: Demo")
st.video(PRODUCT_VIDEO, format="video/mp4", start_time=0)

#----FAQ----

st.write("")
st.write("---")
st.header(":question: FAQ")

faq = {
    "What makes AquaShine Shampoo different from other shampoos?": "AquaShine Shampoo is enriched with luxurious Argan oil and essential minerals, providing deep hydration and nourishment. Its advanced formula tames frizz, enhances shine, and ensures a silky smooth finish, making it a standout choice for all hair types.",
    "Is AquaShine Shampoo suitable for all hair types?": "Yes, AquaShine Shampoo is designed to be gentle yet effective, making it suitable for all hair types, including color-treated hair. It provides the necessary nutrients and moisture without weighing down your hair.",
    "How often should I use AquaShine Shampoo for the best results?": "For optimal results, AquaShine Shampoo can be used daily. Its gentle formula ensures that it cleanses without stripping essential moisture, keeping your hair healthy and vibrant with regular use.",
    "Does AquaShine Shampoo contain any harsh chemicals?": "No, AquaShine Shampoo is free from harsh chemicals like sulfates and parabens. It is formulated with high-quality, natural ingredients to ensure your hair receives the best care possible.",
    "Can AquaShine Shampoo help with frizzy hair?": "Absolutely! AquaShine Shampoo is specifically designed to combat frizz. Its nourishing ingredients, including Argan oil, work to smooth and tame flyaways, leaving your hair silky, smooth, and manageable."
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

#----CONTACT----

st.write("")
st.write("---")
st.subheader("📧Have a question? Get in touch with us.")

contact_form=f"""<form action="https://formsubmit.co/mahajanchirag718@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your Name" required>
     <input type="email" name="email" placeholder="Your Email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send📧</button>
</form>"""

st.markdown(contact_form, unsafe_allow_html=True)

