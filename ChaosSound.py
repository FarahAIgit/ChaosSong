import React, { useState } from 'react';
import { Music, Sparkles, Copy, Check } from 'lucide-react';

const SunoPromptGenerator = () => {
  const [prompt, setPrompt] = useState('');
  const [lyrics, setLyrics] = useState('');
  const [instrumentalMode, setInstrumentalMode] = useState(false);
  const [addMetatags, setAddMetatags] = useState(true);
  const [pureChaosMood, setPureChaosMood] = useState(false);
  const [copied, setCopied] = useState(false);

  // Musical genres and styles
  const GENRES = [
    'ambient', 'experimental', 'ethereal wave', 'dark ambient', 'drone',
    'post-rock', 'shoegaze', 'dream pop', 'downtempo', 'trip-hop',
    'neo-classical', 'avant-garde', 'minimal techno', 'industrial',
    'witch house', 'vaporwave', 'chillwave', 'synthwave', 'darkwave',
    'psychedelic', 'folk', 'chamber pop', 'art pop', 'glitch',
    'noise', 'space music', 'cosmic', 'cinematic', 'orchestral'
  ];

  const MOODS = [
    'melancholic', 'haunting', 'mysterious', 'ethereal', 'dreamy',
    'dark', 'atmospheric', 'hypnotic', 'meditative', 'introspective',
    'surreal', 'nostalgic', 'eerie', 'contemplative', 'twilight',
    'liminal', 'cosmic', 'otherworldly', 'spectral', 'transcendent',
    'somber', 'wistful', 'enigmatic', 'pensive', 'brooding'
  ];

  const INSTRUMENTS = [
    'piano', 'synthesizer', 'strings', 'guitar', 'cello', 'violin',
    'harp', 'flute', 'bells', 'drone', 'pads', 'bass', 'drums',
    'percussion', 'choir', 'vocals', 'keys', 'organ', 'brass',
    'woodwinds', 'electronic', 'analog synth', 'digital synth'
  ];

  const PRODUCTION_STYLES = [
    'reverb-heavy', 'lo-fi', 'high-fidelity', 'distorted', 'clean',
    'layered', 'minimal', 'dense', 'spacious', 'compressed',
    'vintage', 'modern', 'raw', 'polished', 'tape-saturated'
  ];

  // Lyrical themes
  const LYRIC_THEMES = [
    'twilight realm', 'forgotten memories', 'cosmic drift', 'shadow dance',
    'eternal night', 'lost horizons', 'whispered dreams', 'void embrace',
    'silent echoes', 'fading light', 'ancient paths', 'distant stars',
    'mystic journey', 'time dissolving', 'spectral visions', 'endless drift',
    'crystal tears', 'broken mirrors', 'sacred emptiness', 'lunar descent'
  ];

  const LYRIC_FRAGMENTS = [
    'wandering through', 'dissolving into', 'beneath the veil of',
    'lost within', 'echoing across', 'suspended in', 'drifting beyond',
    'wrapped in', 'falling through', 'ascending into', 'merged with',
    'calling from', 'reaching toward', 'bound by', 'freed from'
  ];

  const LYRIC_IMAGES = [
    'silver mist', 'crystal void', 'obsidian sky', 'amber glow',
    'phantom breath', 'twilight haze', 'stardust trail', 'moonlit path',
    'shadow waves', 'frost-touched air', 'velvet darkness', 'golden silence',
    'infinite shore', 'cosmic sea', 'temporal drift', 'ethereal flame'
  ];

  // Chaos word generation (from original)
  const generateChaosWord = () => {
    const consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'w', 'z'];
    const consonantClusters = ['br', 'cr', 'dr', 'fr', 'gr', 'pr', 'tr', 'bl', 'cl', 'fl', 'gl', 'pl', 'sl'];
    const vowels = ['a', 'e', 'i', 'o', 'u', 'ae', 'ea', 'ia', 'io', 'ou'];
    const endings = ['', 'n', 's', 'x', 'r', 'l', 'th', 'sh', 'nt', 'st'];
    
    const numSyllables = Math.random() < 0.7 ? 2 : Math.random() < 0.5 ? 1 : 3;
    let word = '';
    
    for (let i = 0; i < numSyllables; i++) {
      if (Math.random() < 0.4) {
        word += consonantClusters[Math.floor(Math.random() * consonantClusters.length)];
      } else {
        word += consonants[Math.floor(Math.random() * consonants.length)];
      }
      word += vowels[Math.floor(Math.random() * vowels.length)];
      if (i === numSyllables - 1 && Math.random() < 0.6) {
        word += endings[Math.floor(Math.random() * endings.length)];
      }
    }
    return word;
  };

  const generateLyrics = (useChaos) => {
    const lines = [];
    const numVerses = Math.random() < 0.5 ? 2 : 3;
    
    for (let v = 0; v < numVerses; v++) {
      const theme = useChaos ? generateChaosWord() : LYRIC_THEMES[Math.floor(Math.random() * LYRIC_THEMES.length)];
      const fragment = LYRIC_FRAGMENTS[Math.floor(Math.random() * LYRIC_FRAGMENTS.length)];
      const image1 = useChaos ? generateChaosWord() : LYRIC_IMAGES[Math.floor(Math.random() * LYRIC_IMAGES.length)];
      const image2 = useChaos ? generateChaosWord() : LYRIC_IMAGES[Math.floor(Math.random() * LYRIC_IMAGES.length)];
      
      lines.push(`${fragment} ${theme}`);
      lines.push(`where ${image1} meets ${image2}`);
      if (v < numVerses - 1) lines.push('');
    }
    
    return lines.join('\n');
  };

  const generatePrompt = () => {
    const genre1 = GENRES[Math.floor(Math.random() * GENRES.length)];
    let genre2 = GENRES[Math.floor(Math.random() * GENRES.length)];
    while (genre2 === genre1) {
      genre2 = GENRES[Math.floor(Math.random() * GENRES.length)];
    }
    
    const mood = pureChaosMood ? generateChaosWord() : MOODS[Math.floor(Math.random() * MOODS.length)];
    const instrument1 = INSTRUMENTS[Math.floor(Math.random() * INSTRUMENTS.length)];
    const instrument2 = INSTRUMENTS[Math.floor(Math.random() * INSTRUMENTS.length)];
    const production = PRODUCTION_STYLES[Math.floor(Math.random() * PRODUCTION_STYLES.length)];
    
    let promptText = `${genre1}, ${genre2}, ${mood}`;
    
    if (addMetatags) {
      promptText += `, ${instrument1}, ${instrument2}, ${production}`;
      
      // Add some random technical tags
      const bpm = 60 + Math.floor(Math.random() * 80); // 60-140 BPM
      if (Math.random() < 0.5) {
        promptText += `, ${bpm}bpm`;
      }
    }
    
    setPrompt(promptText);
    
    if (!instrumentalMode) {
      setLyrics(generateLyrics(pureChaosMood));
    } else {
      setLyrics('[Instrumental]');
    }
  };

  const copyToClipboard = (text) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div style={{
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #0a0a0f 0%, #1a0a1f 100%)',
      color: '#e8e6e3',
      fontFamily: "'Courier New', monospace",
      padding: '2rem'
    }}>
      <div style={{
        maxWidth: '1200px',
        margin: '0 auto',
        background: 'rgba(0, 0, 0, 0.5)',
        borderRadius: '12px',
        padding: '2rem',
        backdropFilter: 'blur(10px)'
      }}>
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: '1rem', marginBottom: '1rem' }}>
            <Music size={40} color="#c946ff" />
            <h1 style={{ color: '#c946ff', margin: 0 }}>Suno Chaos Generator</h1>
            <Sparkles size={40} color="#c946ff" />
          </div>
          <p style={{ color: '#a8a6a3', fontStyle: 'italic' }}>Surreal music prompt generation for Suno AI</p>
        </div>

        <div style={{ display: 'grid', gridTemplateColumns: '1fr 2fr', gap: '2rem' }}>
          {/* Options Panel */}
          <div>
            <h2 style={{ color: '#ff8c00', fontSize: '1.5rem', marginBottom: '1.5rem' }}>Options</h2>
            
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  checked={instrumentalMode}
                  onChange={(e) => setInstrumentalMode(e.target.checked)}
                  style={{ accentColor: '#c946ff' }}
                />
                <span> Instrumental (no lyrics)</span>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  checked={addMetatags}
                  onChange={(e) => setAddMetatags(e.target.checked)}
                  style={{ accentColor: '#c946ff' }}
                />
                <span>Add detailed metatags</span>
              </label>

              <label style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', cursor: 'pointer' }}>
                <input
                  type="checkbox"
                  checked={pureChaosMood}
                  onChange={(e) => setPureChaosMood(e.target.checked)}
                  style={{ accentColor: '#c946ff' }}
                />
                <span>Pure Chaos Mode (invented words)</span>
              </label>

              <button
                onClick={generatePrompt}
                style={{
                  marginTop: '1rem',
                  padding: '1rem',
                  background: '#c946ff',
                  color: 'white',
                  border: 'none',
                  borderRadius: '8px',
                  cursor: 'pointer',
                  fontSize: '1rem',
                  fontWeight: 'bold',
                  transition: 'all 0.3s'
                }}
                onMouseOver={(e) => e.target.style.background = '#a635d9'}
                onMouseOut={(e) => e.target.style.background = '#c946ff'}
              >
                Generate Suno Prompt
              </button>
            </div>

            <div style={{ marginTop: '2rem', padding: '1rem', background: 'rgba(255, 140, 0, 0.1)', borderRadius: '8px', border: '1px solid #ff8c00' }}>
              <h3 style={{ color: '#ff8c00', fontSize: '1rem', marginBottom: '0.5rem' }}>How to use:</h3>
              <ol style={{ fontSize: '0.9rem', lineHeight: '1.6', paddingLeft: '1.2rem' }}>
                <li>Generate a prompt</li>
                <li>Copy the style tags</li>
                <li>Paste into Suno's "Style of Music" field</li>
                <li>Copy lyrics (if not instrumental)</li>
                <li>Create your surreal track!</li>
              </ol>
            </div>
          </div>

          {/* Output Panel */}
          <div>
            <h2 style={{ color: '#ff8c00', fontSize: '1.5rem', marginBottom: '1.5rem' }}>Output</h2>
            
            {prompt && (
              <>
                {/* Style Tags */}
                <div style={{ marginBottom: '2rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                    <strong style={{ color: '#ff8c00' }}>Style Tags:</strong>
                    <button
                      onClick={() => copyToClipboard(prompt)}
                      style={{
                        padding: '0.5rem 1rem',
                        background: 'rgba(201, 70, 255, 0.2)',
                        border: '1px solid #c946ff',
                        borderRadius: '6px',
                        color: '#c946ff',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem'
                      }}
                    >
                      {copied ? <Check size={16} /> : <Copy size={16} />}
                      {copied ? 'Copied!' : 'Copy'}
                    </button>
                  </div>
                  <div style={{
                    background: 'rgba(10, 10, 12, 0.7)',
                    padding: '1rem',
                    borderRadius: '8px',
                    border: '1px solid #2f2f31',
                    fontFamily: 'monospace',
                    whiteSpace: 'pre-wrap',
                    wordWrap: 'break-word'
                  }}>
                    {prompt}
                  </div>
                </div>

                {/* Lyrics */}
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem' }}>
                    <strong style={{ color: '#ff8c00' }}>Lyrics:</strong>
                    <button
                      onClick={() => copyToClipboard(lyrics)}
                      style={{
                        padding: '0.5rem 1rem',
                        background: 'rgba(201, 70, 255, 0.2)',
                        border: '1px solid #c946ff',
                        borderRadius: '6px',
                        color: '#c946ff',
                        cursor: 'pointer',
                        display: 'flex',
                        alignItems: 'center',
                        gap: '0.5rem'
                      }}
                    >
                      {copied ? <Check size={16} /> : <Copy size={16} />}
                      {copied ? 'Copied!' : 'Copy'}
                    </button>
                  </div>
                  <div style={{
                    background: 'rgba(10, 10, 12, 0.7)',
                    padding: '1rem',
                    borderRadius: '8px',
                    border: '1px solid #2f2f31',
                    fontFamily: 'monospace',
                    whiteSpace: 'pre-wrap',
                    wordWrap: 'break-word',
                    minHeight: '200px'
                  }}>
                    {lyrics || 'Generate a prompt to see lyrics here...'}
                  </div>
                </div>
              </>
            )}

            {!prompt && (
              <div style={{
                background: 'rgba(10, 10, 12, 0.7)',
                padding: '3rem',
                borderRadius: '8px',
                border: '1px solid #2f2f31',
                textAlign: 'center',
                color: '#a8a6a3'
              }}>
                Click "Generate Suno Prompt" to create your surreal music prompt
              </div>
            )}
          </div>
        </div>

        {/* Footer */}
        <div style={{ marginTop: '3rem', textAlign: 'center', color: '#a8a6a3', fontSize: '0.9rem' }}>
          <p>Adapted from ChaosPrompt by <a href="https://x.com/Farah_ai_" style={{ color: '#c946ff' }}>@Farah_ai_</a></p>
          <p style={{ fontStyle: 'italic', marginTop: '0.5rem' }}>~ Let the chaos harmonize ~</p>
        </div>
      </div>
    </div>
  );
};

export default SunoPromptGenerator;



