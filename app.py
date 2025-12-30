<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate 66 Club Clone</title>
    <style>
        :root { --bg: #0a0e17; --card: #1c222d; --gold: #f3c34d; --accent: #ff4757; }
        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); color: white; margin: 0; padding-bottom: 70px; }
        
        /* Top Bar */
        .top-nav { background: var(--card); padding: 15px; display: flex; justify-content: space-between; align-items: center; position: sticky; top: 0; z-index: 1000; }
        .balance-chip { background: #2d3436; padding: 5px 15px; border-radius: 20px; border: 1px solid var(--gold); }

        /* Banner */
        .banner { width: 95%; height: 150px; background: linear-gradient(45deg, #ff4757, #70a1ff); margin: 10px auto; border-radius: 15px; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: bold; }

        /* Categories */
        .categories { display: flex; gap: 10px; overflow-x: auto; padding: 10px; }
        .cat-btn { background: var(--card); border: none; color: white; padding: 10px 20px; border-radius: 10px; cursor: pointer; white-space: nowrap; }
        .cat-btn.active { background: var(--gold); color: black; }

        /* Game Grid (30 Games Slot) */
        .game-grid { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; padding: 10px; }
        .game-item { background: var(--card); border-radius: 12px; overflow: hidden; text-align: center; border: 1px solid #333; transition: 0.3s; }
        .game-item:hover { border-color: var(--gold); transform: translateY(-5px); }
        .game-img { width: 100%; height: 80px; background: #333; display: flex; align-items: center; justify-content: center; font-size: 30px; }
        .game-name { padding: 8px; font-size: 12px; font-weight: bold; }

        /* Action Buttons */
        .actions { display: flex; gap: 10px; padding: 10px; }
        .btn-pay { flex: 1; padding: 12px; border-radius: 8px; border: none; font-weight: bold; cursor: pointer; }
        .dep { background: #2ed573; color: white; }
        .wit { background: #eccc68; color: black; }

        /* Footer Menu */
        .footer { position: fixed; bottom: 0; width: 100%; background: var(--card); display: flex; justify-content: space-around; padding: 10px 0; border-top: 1px solid #333; }
        .foot-item { font-size: 12px; text-align: center; color: #aaa; }
    </style>
</head>
<body>

<div class="top-nav">
    <div style="font-weight: bold; color: var(--gold);">PREMIUM CLUB</div>
    <div class="balance-chip">₹ <span id="bal">1500.50</span></div>
</div>

<div class="banner">Mega Jackpot: ₹10,00,000</div>

<div class="actions">
    <button class="btn-pay dep" onclick="showPay('Deposit')">Deposit</button>
    <button class="btn-pay wit" onclick="showPay('Withdraw')">Withdraw</button>
</div>

<div class="categories">
    <button class="cat-btn active">All Games</button>
    <button class="cat-btn">Lottery</button>
    <button class="cat-btn">Slots</button>
    <button class="cat-btn">Fishing</button>
    <button class="cat-btn">Casino</button>
</div>

<div class="game-grid" id="game-list">
    </div>

<div class="footer">
    <div class="foot-item">🏠<br>Home</div>
    <div class="foot-item">📊<br>Activity</div>
    <div class="foot-item">🎁<br>Promotion</div>
    <div class="foot-item">👤<br>Account</div>
</div>

<script>
    // 30 Games List
    const games = [
        {name: "Win Go 1m", icon: "🔴"}, {name: "Aviator", icon: "✈️"}, {name: "Dragon Tiger", icon: "🐉"},
        {name: "Mine Game", icon: "💣"}, {name: "7 Up Down", icon: "🎲"}, {name: "Cricket X", icon: "🏏"},
        {name: "Plinko", icon: "🔵"}, {name: "Slots 777", icon: "🎰"}, {name: "Teen Patti", icon: "🃏"},
        {name: "Andar Bahar", icon: "🃏"}, {name: "Fruit Line", icon: "🍎"}, {name: "JILI Slot", icon: "👑"},
        {name: "Fish Hunter", icon: "🐟"}, {name: "Penalty", icon: "⚽"}, {name: "Baccarat", icon: "♠️"},
        {name: "Roulette", icon: "🎡"}, {name: "Color Pred", icon: "🎨"}, {name: "Wheel Fortune", icon: "🎡"},
        {name: "Ludo Pro", icon: "♟️"}, {name: "Car Casino", icon: "🚗"}, {name: "Crazy Time", icon: "⏳"},
        {name: "Mega Ball", icon: "🎱"}, {name: "Spaceman", icon: "👨‍🚀"}, {name: "Dino Run", icon: "🦖"},
        {name: "Money Roll", icon: "💵"}, {name: "Gold Rush", icon: "⛏️"}, {name: "Candy Party", icon: "🍭"},
        {name: "Joker Spin", icon: "🤡"}, {name: "Blackjack", icon: "🃏"}, {name: "Turbo Mines", icon: "💎"}
    ];

    const grid = document.getElementById('game-list');
    games.forEach(g => {
        grid.innerHTML += `
            <div class="game-item" onclick="playGame('${g.name}')">
                <div class="game-img">${g.icon}</div>
                <div class="game-name">${g.name}</div>
            </div>
        `;
    });

    function showPay(type) {
        let amt = prompt(`${type} अमाउंट दर्ज करें (₹):`);
        if(amt) alert(`${type} रिक्वेस्ट ₹${amt} के लिए भेज दी गई है!`);
    }

    function playGame(name) {
        alert(name + " गेम अभी लोड हो रहा है... कृपया इंटरनेट चेक करें।");
    }
</script>

</body>
</html>
