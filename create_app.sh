#!/bin/bash
echo "[+] Setting up Tarot app directory..."
mkdir -p ~/tarot_app/assets
cd ~/tarot_app

echo "[+] Killing active servers..."
pkill -f "http.server" 2>/dev/null

echo "[+] Writing application files..."
cat << 'HTML' > assets/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Arcane Whispers - Celtic Cross</title>
    <style>
        body { background-color: #0f0f13; color: #e1e1e6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; margin: 0; padding: 15px; }
        h1 { color: #fba100; margin-bottom: 2px; font-size: 1.5rem; }
        p.subtitle { color: #8f8f9f; font-size: 0.8rem; margin-top: 0; margin-bottom: 15px; }
        .controls { margin-bottom: 15px; }
        button { background-color: #fba100; color: #0f0f13; border: none; padding: 10px 20px; font-size: 0.9rem; font-weight: bold; border-radius: 20px; cursor: pointer; box-shadow: 0 4px 10px rgba(251, 161, 0, 0.3); }
        button:active { transform: scale(0.98); }
        button:disabled { background-color: #444; color: #777; cursor: not-allowed; }
        .celtic-board { display: grid; grid-template-columns: repeat(4, 75px); grid-template-rows: repeat(3, 115px); gap: 8px; justify-content: center; margin: 0 auto 15px auto; max-width: 350px; }
        .pos-1 { grid-area: 2 / 2 / span 1 / span 1; z-index: 2; }
        .pos-2 { grid-area: 2 / 2 / span 1 / span 1; transform: rotate(90deg); z-index: 3; margin-top: 5px; }
        .pos-3 { grid-area: 3 / 2 / span 1 / span 1; }
        .pos-4 { grid-area: 1 / 2 / span 1 / span 1; }
        .pos-5 { grid-area: 2 / 1 / span 1 / span 1; }
        .pos-6 { grid-area: 2 / 3 / span 1 / span 1; }
        .pos-7 { grid-area: 3 / 4 / span 1 / span 1; }
        .pos-8 { grid-area: 2 / 4 / span 1 / span 1; }
        .pos-9 { grid-area: 1 / 4 / span 1 / span 1; }
        .pos-10 { grid-area: 1 / 3 / span 1 / span 1; }
        .tarot-card { width: 75px; height: 115px; cursor: pointer; position: relative; transform-style: preserve-3d; transition: transform 0.6s ease, opacity 0.5s ease; opacity: 0; transform: translateY(-20px) scale(0.8); }
        .tarot-card.dealt { opacity: 1; transform: translateY(0) scale(1); }
        .tarot-card.flipped { transform: rotateY(180deg); }
        .pos-2.flipped { transform: rotateY(180deg) rotate(90deg); }
        .card-face { position: absolute; width: 100%; height: 100%; backface-visibility: hidden; border-radius: 6px; border: 1.5px solid #fba100; display: flex; flex-direction: column; align-items: center; justify-content: center; box-shadow: 0 3px 10px rgba(0,0,0,0.6); }
        .card-back { background: linear-gradient(135deg, #2d2d3d, #16161d); color: #fba100; }
        .card-back .pattern { font-size: 1.2rem; border: 1px dashed rgba(251, 161, 0, 0.4); width: 55px; height: 90px; display: flex; align-items: center; justify-content: center; border-radius: 4px; }
        .card-front { background: linear-gradient(135deg, #1f1f2e, #101017); color: #fba100; transform: rotateY(180deg); padding: 4px; box-sizing: border-box; }
        .card-front .card-title { font-size: 0.6rem; font-weight: bold; text-align: center; line-height: 1; margin-top: 2px; }
        .card-front .card-symbol { font-size: 1.5rem; margin: 2px 0; }
        .card-front .card-orient { font-size: 0.5rem; color: #aaa; }
        #shuffle-overlay { font-size: 0.9rem; color: #fba100; margin: 5px 0 10px 0; font-style: italic; }
        #reading-result { margin-top: 10px; padding: 12px; background: #1a1a24; border-radius: 8px; border: 1px solid #333344; text-align: left; max-width: 350px; margin-left: auto; margin-right: auto; font-size: 0.8rem; max-height: 220px; overflow-y: auto; }
        #reading-result h3 { margin-top: 0; color: #fba100; font-size: 0.9rem; }
    </style>
</head>
<body>
    <h1>Arcane Whispers</h1>
    <p class="subtitle">Celtic Cross: Deep Reading & Synthesis</p>
    <div class="controls"><button id="shuffle-btn" onclick="startReading()">Shuffle & Deal Spread</button></div>
    <div id="shuffle-overlay">Press shuffle to begin your reading.</div>
    <div class="celtic-board" id="board"></div>
    <div id="reading-result">
        <h3>Live Reading Log:</h3>
        <p id="card-desc">Your cards are waiting on the mat. Tap any card to reveal its meaning in the spread.</p>
    </div>
    <script>
        const tarotDeck = [
            {name: "The Fool", symbol: "🃏", upright: "New beginnings, infinite potential, taking a leap of faith.", reversed: "Recklessness, risk-taking, hesitation, holding back."},
            {name: "The Magician", symbol: "🪄", upright: "Manifestation, resourcefulness, power, turning vision into reality.", reversed: "Manipulation, poor planning, untapped talents."},
            {name: "The High Priestess", symbol: "🌙", upright: "Intuition, sacred knowledge, trusting your subconscious.", reversed: "Secrets, disconnected intuition, superficiality."},
            {name: "The Empress", symbol: "👑", upright: "Abundance, nurturing growth, connection with nature.", reversed: "Creative block, dependence on others, emptiness."},
            {name: "The Emperor", symbol: "🏛️", upright: "Authority, structure, establishing solid foundations.", reversed: "Tyranny, rigidity, lack of control, abuse of power."},
            {name: "The Hierophant", symbol: "📜", upright: "Spiritual wisdom, tradition, institutions, guidance.", reversed: "Personal beliefs, rebellion, restriction, breaking norms."},
            {name: "The Lovers", symbol: "❤️", upright: "Love, harmony, vital choices, alignment of values.", reversed: "Disharmony, imbalance, misalignment of choices."},
            {name: "The Chariot", symbol: "🛡️", upright: "Control, willpower, success, determination, momentum.", reversed: "Lack of direction, self-discipline issues, opposition."},
            {name: "Strength", symbol: "🦁", upright: "Courage, persuasion, compassion, inner mastery.", reversed: "Self-doubt, raw emotion, weakness, insecurity."},
            {name: "The Hermit", symbol: "🏮", upright: "Soul-searching, introspection, being alone, inner guidance.", reversed: "Isolation, loneliness, withdrawal, lost way."},
            {name: "Wheel of Fortune", symbol: "🎡", upright: "Good luck, karma, life cycles, major turning points.", reversed: "Bad luck, resisting change, negative external cycles."},
            {name: "Justice", symbol: "⚖️", upright: "Fairness, truth, cause and effect, legal clarity.", reversed: "Dishonesty, unfairness, lack of accountability."},
            {name: "The Hanged Man", symbol: "🙃", upright: "Pause, surrender, letting go, new perspectives.", reversed: "Stalling, needless sacrifice, fear of sacrifice."},
            {name: "Death", symbol: "🦋", upright: "Transformation, profound endings, clearing baggage for rebirth.", reversed: "Resisting change, stagnation, personal petrification."},
            {name: "Temperance", symbol: "🏺", upright: "Balance, moderation, patience, purposeful synthesis.", reversed: "Imbalance, excess, self-indulgence, discord."},
            {name: "The Devil", symbol: "⛓️", upright: "Shadow self, attachment, addiction, restriction.", reversed: "Reclaiming power, breaking chains, freedom, release."},
            {name: "The Tower", symbol: "⚡", upright: "Sudden upheaval, broken illusions, awakening, revelation.", reversed: "Disaster avoided, delayed trauma, lingering fear."},
            {name: "The Star", symbol: "⭐", upright: "Hope, faith, rejuvenation, profound inner peace.", reversed: "Hopelessness, despair, lack of faith, discouragement."},
            {name: "The Moon", symbol: "🐺", upright: "Illusion, fear, anxiety, subconscious tracking, intuition.", reversed: "Release of fear, repressed emotion surfacing, clarity."},
            {name: "The Sun", symbol: "☀️", upright: "Joy, success, celebration, vitality, warmth.", reversed: "Temporary depression, inner child block, clouded joy."},
            {name: "Judgment", symbol: "📯", upright: "Rebirth, inner calling, absolution, awakening.", reversed: "Self-doubt, harsh self-judgment, ignoring the call."},
            {name: "The World", symbol: "🌍", upright: "Completion, accomplishment, travel, cycle fulfillment.", reversed: "Lack of closure, unfinished business, delays."}
        ];
        const celticPositions = [
            "1. Present: The core situation surrounding you right now.",
            "2. Crossing: The immediate challenge or obstacle crossing your path.",
            "3. Foundation: The root cause or subconscious bedrock of the matter.",
            "4. Past: Events fading away that brought you to this point.",
            "5. Goals/Crown: Your highest aspirations or potential outcome.",
            "6. Near Future: What is approaching on the horizon shortly.",
            "7. Self/Querent: Your current attitude, mindset, or role.",
            "8. Environment: External influences, people, or home atmosphere.",
            "9. Hopes & Fears: Your hidden anxieties or deep-seated wishes.",
            "10. Final Outcome: The ultimate trajectory if current paths hold."
        ];
        let drawnSpread = [];
        let revealedCount = 0;
        let readingLogHTML = "";
        function startReading() {
            const board = document.getElementById("board");
            board.innerHTML = "";
            document.getElementById("shuffle-btn").disabled = true;
            document.getElementById("shuffle-overlay").innerText = "Shuffling deck and dealing cards...";
            drawnSpread = [];
            revealedCount = 0;
            readingLogHTML = "<h3>Live Reading Log:</h3>";
            document.getElementById("card-desc").innerHTML = "Deck dealt. Tap any face-down card to read its individual message.";
            let deckCopy = [...tarotDeck];
            for(let i=0; i<10; i++) {
                let randIndex = Math.floor(Math.random() * deckCopy.length);
                let selectedCard = deckCopy.splice(randIndex, 1)[0];
                let isReversed = Math.random() < 0.35;
                drawnSpread.push({ ...selectedCard, reversed: isReversed });
            }
            for(let i=0; i<10; i++) {
                let cardDiv = document.createElement("div");
                cardDiv.className = "tarot-card pos-" + (i+1);
                cardDiv.setAttribute("onclick", "revealCard(" + i + ")");
                cardDiv.id = "card-" + i;
                cardDiv.innerHTML = `
                    <div class="card-face card-back"><div class="pattern">✦</div></div>
                    <div class="card-face card-front">
                        <div class="card-symbol">${drawnSpread[i].symbol}</div>
                        <div class="card-title">${drawnSpread[i].name}</div>
                        <div class="card-orient">${drawnSpread[i].reversed ? "(Rev)" : "(Up)"}</div>
                    </div>
                `;
                board.appendChild(cardDiv);
                setTimeout((idx) => {
                    let el = document.getElementById("card-" + idx);
                    if(el) el.classList.add("dealt");
                    if(idx === 9) {
                        document.getElementById("shuffle-overlay").innerText = "All cards dealt. Tap cards in any order to reveal.";
                        document.getElementById("shuffle-btn").disabled = false;
                        document.getElementById("shuffle-btn").innerText = "Shuffle Again";
                    }
                }, i * 100, i);
            }
        }
        function revealCard(index) {
            let cardElement = document.getElementById("card-" + index);
            if (cardElement.classList.contains("flipped")) return;
            cardElement.classList.add("flipped");
            revealedCount++;
            let card = drawnSpread[index];
            let orientText = card.reversed ? "Reversed" : "Upright";
            let meaningText = card.reversed ? card.reversed : card.upright;
            let cardEntry = `
                <div style="margin-bottom: 8px; border-bottom: 1px dashed #333344; padding-bottom: 6px;">
                    <strong>${celticPositions[index]}</strong><br>
                    <span>${card.symbol} <strong>${card.name}</strong> (${orientText})</span><br>
                    <em>${meaningText}</em>
                </div>
            `;
            readingLogHTML += cardEntry;
            document.getElementById("reading-result").innerHTML = readingLogHTML;
            let logBox = document.getElementById("reading-result");
            logBox.scrollTop = logBox.scrollHeight;
            if (revealedCount === 10) {
                setTimeout(generateOverallSummary, 600);
            }
        }
        function generateOverallSummary() {
            let summaryHTML = `
                <div style="background: #252536; padding: 10px; border-radius: 6px; border: 1px solid #fba100; margin-top: 10px;">
                    <h3 style="color: #fba100; margin-top:0;">🔮 Overall Spread Synthesis & Summary</h3>
                    <p style="margin-bottom: 5px;"><strong>Core Arc:</strong> Your spread reflects a powerful tension between your current foundational reality and upcoming systemic shifts. The energies of your past are giving way to immediate roadblocks that require careful navigation.</p>
                    <p style="margin-bottom: 5px;"><strong>Actionable Guidance:</strong> Balance your internal expectations (Hopes & Fears) with external demands (Environment). By addressing the core challenge directly rather than resisting it, your final outcome trajectory will clear up significantly.</p>
                    <em style="color: #fba100;">The reading is complete. Tap "Shuffle Again" to clear the mat.</em>
                </div>
            `;
            readingLogHTML += summaryHTML;
            document.getElementById("reading-result").innerHTML = readingLogHTML;
            document.getElementById("shuffle-overlay").innerText = "Full reading and synthesis unlocked!";
        }
    </script>
</body>
</html>
HTML
echo "[+] Build completed successfully!"
