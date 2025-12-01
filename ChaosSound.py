import streamlit as st
import random

st.set_page_config(page_title="Suno Chaos Generator", layout="wide")

# ---------------------------
# Dark styling with purple accents
# ---------------------------
st.markdown(
    """
    <style>
    body { background-color: #0a0a0f; color: #e8e6e3; font-family: 'Courier New', monospace; }
    .stApp { 
        min-height: 100vh; 
        background: linear-gradient(135deg, #0a0a0f 0%, #1a0a1f 100%);
    }
    .stTextArea textarea { background: rgba(10,10,12,0.7); color: #e8e6e3; border: 1px solid #2f2f31; }
    .stButton>button { 
        background-color:#c946ff; 
        color:#ffffff; 
        border-radius:8px; 
        padding:12px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #a635d9;
    }
    .block-container { 
        padding: 2rem; 
        background: rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(10px);
        border-radius: 12px;
        max-width: 1200px;
    }
    h1 { color: #c946ff; font-family: 'Courier New', monospace; }
    h2,h3 { color: #ff8c00; font-family: 'Courier New', monospace; }
    .footer { color:#a8a6a3; font-size:12px; margin-top:8px; }
    .stCodeBlock { background: rgba(10,10,12,0.7); }
    .stCodeBlock code { 
        white-space: pre-wrap !important; 
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    .stCodeBlock pre {
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
    }
    .stCheckbox input[type="checkbox"]:checked {
        background-color: #c946ff !important;
        border-color: #c946ff !important;
    }
    .stCheckbox [data-testid="stCheckbox"] input:checked ~ span {
        background-color: #c946ff !important;
        border-color: #c946ff !important;
    }
    .info-box {
        background: rgba(255, 140, 0, 0.1);
        border: 1px solid #ff8c00;
        border-radius: 8px;
        padding: 1rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div style="text-align:center;">
        <h1>🎵 Suno Chaos Generator ✨</h1>
        <p style="color: #a8a6a3; font-style: italic;">Surreal music prompt generation for Suno AI</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------------------
# Musical genres and styles
# ---------------------------
GENRES = [
    'ambient', 'experimental', 'ethereal wave', 'dark ambient', 'drone',
    'post-rock', 'shoegaze', 'dream pop', 'downtempo', 'trip-hop',
    'neo-classical', 'avant-garde', 'minimal techno', 'industrial',
    'witch house', 'vaporwave', 'chillwave', 'synthwave', 'darkwave',
    'psychedelic', 'folk', 'chamber pop', 'art pop', 'glitch',
    'noise', 'space music', 'cosmic', 'cinematic', 'orchestral'
]

MOODS = [
    'melancholic', 'haunting', 'mysterious', 'ethereal', 'dreamy',
    'dark', 'atmospheric', 'hypnotic', 'meditative', 'introspective',
    'surreal', 'nostalgic', 'eerie', 'contemplative', 'twilight',
    'liminal', 'cosmic', 'otherworldly', 'spectral', 'transcendent',
    'somber', 'wistful', 'enigmatic', 'pensive', 'brooding'
]

INSTRUMENTS = [
    'piano', 'synthesizer', 'strings', 'guitar', 'cello', 'violin',
    'harp', 'flute', 'bells', 'drone', 'pads', 'bass', 'drums',
    'percussion', 'choir', 'vocals', 'keys', 'organ', 'brass',
    'woodwinds', 'electronic', 'analog synth', 'digital synth'
]

PRODUCTION_STYLES = [
    'reverb-heavy', 'lo-fi', 'high-fidelity', 'distorted', 'clean',
    'layered', 'minimal', 'dense', 'spacious', 'compressed',
    'vintage', 'modern', 'raw', 'polished', 'tape-saturated'
]

# Lyrical themes
LYRIC_THEMES = [
    'twilight realm', 'forgotten memories', 'cosmic drift', 'shadow dance',
    'eternal night', 'lost horizons', 'whispered dreams', 'void embrace',
    'silent echoes', 'fading light', 'ancient paths', 'distant stars',
    'mystic journey', 'time dissolving', 'spectral visions', 'endless drift',
    'crystal tears', 'broken mirrors', 'sacred emptiness', 'lunar descent'
]

LYRIC_FRAGMENTS = [
    'wandering through', 'dissolving into', 'beneath the veil of',
    'lost within', 'echoing across', 'suspended in', 'drifting beyond',
    'wrapped in', 'falling through', 'ascending into', 'merged with',
    'calling from', 'reaching toward', 'bound by', 'freed from'
]

LYRIC_IMAGES = [
    'silver mist', 'crystal void', 'obsidian sky', 'amber glow',
    'phantom breath', 'twilight haze', 'stardust trail', 'moonlit path',
    'shadow waves', 'frost-touched air', 'velvet darkness', 'golden silence',
    'infinite shore', 'cosmic sea', 'temporal drift', 'ethereal flame'
]

# ---------------------------
# Chaos word generation
# ---------------------------
def generate_chaos_word():
    """Generate a mystical-sounding made-up word using syllable patterns"""
    consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'z']
    consonant_clusters = ['br', 'cr', 'dr', 'fr', 'gr', 'pr', 'tr', 'bl', 'cl', 'fl', 'gl', 'pl', 'sl']
    vowels = ['a', 'e', 'i', 'o', 'u', 'ae', 'ea', 'ia', 'io', 'ou']
    endings = ['', 'n', 's', 'x', 'r', 'l', 'th', 'sh', 'nt', 'st']
    
    num_syllables = random.choice([1, 2, 2, 3])  # Weighted toward 2 syllables
    word = ''
    
    for i in range(num_syllables):
        if random.random() < 0.4:
            word += random.choice(consonant_clusters)
        else:
            word += random.choice(consonants)
        
        word += random.choice(vowels)
        
        if i == num_syllables - 1 and random.random() < 0.6:
            word += random.choice(endings)
    
    return word

def generate_lyrics(use_chaos):
    """Generate surreal, atmospheric lyrics"""
    lines = []
    num_verses = random.choice([2, 2, 3])  # Weighted toward 2 verses
    
    for v in range(num_verses):
        theme = generate_chaos_word() if use_chaos else random.choice(LYRIC_THEMES)
        fragment = random.choice(LYRIC_FRAGMENTS)
        image1 = generate_chaos_word() if use_chaos else random.choice(LYRIC_IMAGES)
        image2 = generate_chaos_word() if use_chaos else random.choice(LYRIC_IMAGES)
        
        lines.append(f"{fragment} {theme}")
        lines.append(f"where {image1} meets {image2}")
        if v < num_verses - 1:
            lines.append('')
    
    return '\n'.join(lines)

def generate_prompt(instrumental_mode, add_metatags, pure_chaos_mood):
    """Generate Suno prompt with style tags"""
    genre1 = random.choice(GENRES)
    genre2 = random.choice([g for g in GENRES if g != genre1])
    
    mood = generate_chaos_word() if pure_chaos_mood else random.choice(MOODS)
    instrument1 = random.choice(INSTRUMENTS)
    instrument2 = random.choice(INSTRUMENTS)
    production = random.choice(PRODUCTION_STYLES)
    
    prompt_text = f"{genre1}, {genre2}, {mood}"
    
    if add_metatags:
        prompt_text += f", {instrument1}, {instrument2}, {production}"
        
        # Add some random technical tags
        if random.random() < 0.5:
            bpm = random.randint(60, 140)
            prompt_text += f", {bpm}bpm"
    
    if instrumental_mode:
        lyrics_text = "[Instrumental]"
    else:
        lyrics_text = generate_lyrics(pure_chaos_mood)
    
    return prompt_text, lyrics_text

# ---------------------------
# Streamlit UI
# ---------------------------
if "prompt" not in st.session_state:
    st.session_state.prompt = ""
    st.session_state.lyrics = ""

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Options")
    
    instrumental_mode = st.checkbox("Instrumental (no lyrics)", value=False)
    add_metatags = st.checkbox("Add detailed metatags", value=True)
    pure_chaos_mood = st.checkbox("Pure Chaos Mode (invented words)", value=False)
    
    if st.button("Generate Suno Prompt"):
        st.session_state.prompt, st.session_state.lyrics = generate_prompt(
            instrumental_mode, add_metatags, pure_chaos_mood
        )
    
    st.markdown(
        """
        <div class="info-box">
            <h3 style="color: #ff8c00; font-size: 1rem; margin-bottom: 0.5rem;">How to use:</h3>
            <ol style="font-size: 0.9rem; line-height: 1.6; padding-left: 1.2rem;">
                <li>Generate a prompt</li>
                <li>Copy the style tags</li>
                <li>Paste into Suno's "Style of Music" field</li>
                <li>Copy lyrics (if not instrumental)</li>
                <li>Create your surreal track!</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.header("Output")
    
    if st.session_state.prompt:
        st.markdown("**Style Tags** _(click the copy icon in the top-right corner):_")
        st.code(st.session_state.prompt, language=None)
        
        st.markdown("**Lyrics** _(click the copy icon in the top-right corner):_")
        st.code(st.session_state.lyrics, language=None)
    else:
        st.markdown(
            """
            <div style="background: rgba(10,10,12,0.7); padding: 3rem; border-radius: 8px; 
                        border: 1px solid #2f2f31; text-align: center; color: #a8a6a3;">
                Click "Generate Suno Prompt" to create your surreal music prompt
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #a8a6a3; font-size: 0.9rem;">
        <p>Adapted from <a href="https://chaosprompt.streamlit.app/" style="color: #c946ff;">ChaosPrompt</a> by <a href="https://x.com/Farah_ai_" style="color: #c946ff;">@Farah_ai_</a></p>
        <p style="font-style: italic; margin-top: 0.5rem;">~ Let the chaos harmonize ~</p>
    </div>
    """,
    unsafe_allow_html=True
)

