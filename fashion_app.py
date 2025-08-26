import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

# --- App Title ---
st.set_page_config(page_title="Fashion Recommender", page_icon="👗", layout="centered")
st.title("👗 Fashion Recommender Based on Skin Tone")
st.caption("Upload a face image to detect your skin tone and get personalized fashion suggestions!")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# Functions
def extract_dominant_color(image, k=3):
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    image = image.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(image)
    return kmeans.cluster_centers_[0]

def classify_skin_tone(rgb):
    brightness = np.mean(rgb)
    if brightness > 200:
        return "Fair"
    elif brightness > 150:
        return "Wheatish"
    elif brightness > 100:
        return "Dusky"
    else:
        return "Deep"

def show_palette(palette):
    """Display color palette as swatches."""
    cols = st.columns(len(palette))
    for col, (hex_code, name) in zip(cols, palette):
        col.markdown(
            f"<div style='background:{hex_code}; padding:30px; border-radius:10px'></div>",
            unsafe_allow_html=True,
        )
        col.caption(f"{name} ({hex_code})")

def fashion_suggestions(tone):
    if tone == "Fair":
        return "✅ Try pastel shades, lavender, soft pinks, and icy blue."
    elif tone == "Wheatish":
        return "✅ Earth tones, mustard, olive green, and maroon suit you well."
    elif tone == "Dusky":
        return "✅ Bold colors like royal blue, purple, and burnt orange are great!"
    elif tone == "Deep":
        return "✅ Vibrant colors like white, yellow, red, and coral look amazing!"
    else:
        return "Could not determine skin tone."

def fashion_suggestions(tone):
    """Return fashion recommendations and color palettes."""
    palettes = {
        "Fair": [("#E6E6FA", "Lavender"), ("#FFB6C1", "Light Pink"), ("#87CEEB", "Sky Blue")],
        "Wheatish": [("#FFDB58", "Mustard"), ("#808000", "Olive"), ("#800000", "Maroon")],
        "Dusky": [("#4169E1", "Royal Blue"), ("#800080", "Purple"), ("#CC5500", "Burnt Orange")],
        "Deep": [("#FFFFFF", "White"), ("#FFD700", "Yellow"), ("#FF4500", "Coral Red")]
    }
    texts = {
        "Fair": "✅ Try pastel shades, lavender, soft pinks, and icy blue.",
        "Wheatish": "✅ Earth tones, mustard, olive green, and maroon suit you well.",
        "Dusky": "✅ Bold colors like royal blue, purple, and burnt orange are great!",
        "Deep": "✅ Vibrant colors like white, yellow, red, and coral look amazing!"
    }
    return texts.get(tone, "Could not determine skin tone."), palettes.get(tone, [])

# Main logic
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📸 Uploaded Image", use_column_width=True)

    # Detect dominant color & tone
    dominant_color = extract_dominant_color(image)
    tone = classify_skin_tone(dominant_color)

    # Display results
    st.subheader("🎨 Detected Skin Tone:")
    st.write(f"**{tone}**")

    # Show color swatch of detected tone
    hex_color = "#{:02x}{:02x}{:02x}".format(
        int(dominant_color[0]), int(dominant_color[1]), int(dominant_color[2])
    )
    st.markdown(f"**Dominant Color:** {hex_color}")
    st.markdown(
        f"<div style='background:{hex_color}; padding:40px; border-radius:10px;'></div>",
        unsafe_allow_html=True,
    )

    # Fashion recommendations
    st.subheader("🛍️ Fashion Recommendations:")
    text, palette = fashion_suggestions(tone)
    st.write(text)

    if palette:
        st.markdown("**Suggested Palette:**")
        show_palette(palette)