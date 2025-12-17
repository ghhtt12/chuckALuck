from chuck_a_luck import ChuckALuckGame
from flask import Flask, render_template_string, request, jsonify
import threading
import webbrowser
import os

# HTML шаблон
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Chuck-A-Luck Web</title>
    <style>
        body { font-family: monospace; background: #000; color: #0f0; padding: 20px; }
        .game { max-width: 600px; margin: auto; }
        #output { 
            background: #111; border: 1px solid #0f0; padding: 15px; 
            height: 300px; overflow-y: auto; white-space: pre-wrap; margin: 10px 0;
        }
        input, button { 
            padding: 10px; margin: 5px; background: #000; color: #0f0; 
            border: 1px solid #0f0; font-family: monospace;
        }
        button:hover { background: #222; }
    </style>
</head>
<body>
    <div class="game">
        <h2>CHUCK-A-LUCK (Web)</h2>
        <div id="output">{{ initial_output }}</div>

        {% if not game_over %}
        <form id="gameForm" onsubmit="return submitForm()">
            <input type="text" id="inputField" name="input" placeholder="Enter command..." autofocus>
            <button type="submit">Submit</button>
        </form>
        <div>
            <button onclick="newGame()">New Game</button>
            <button onclick="showHelp()">Help</button>
        </div>
        {% else %}
        <button onclick="newGame()">Play Again</button>
        {% endif %}
    </div>

    <script>
        function submitForm() {
            fetch('/play', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({input: document.getElementById('inputField').value})
            })
            .then(response => response.json())
            .then(data => {
                document.getElementById('output').innerHTML = data.output;
                document.getElementById('inputField').value = '';
                if (data.game_over) {
                    document.getElementById('gameForm').style.display = 'none';
                }
            });
            return false;
        }

        function newGame() {
            fetch('/new_game')
            .then(() => location.reload());
        }

        function showHelp() {
            alert("Enter bet amount, then number 1-6. Game will roll dice automatically.");
        }

        document.getElementById('inputField').focus();
    </script>
</body>
</html>
'''

app = Flask(__name__)
game_instance = ChuckALuckGame()
state = "bet"  # "bet" или "number"


def get_game_output():
    """Получить текущее состояние игры для вывода"""
    output = " " * 22 + "CHUCK-A-LUCK\n"
    output += " " * 19 + "CREATIVE COMPUTING\n"
    output += " " * 17 + "MORRISTOWN, NEW JERSEY\n\n\n"
    output += "CHOOSE A NUMBER FROM 1 TO 6. I WILL ROLL 3 DICE.\n"
    output += "IF YOUR NUMBER MATCHES 1 DIE, I PAY OFF EVEN MONEY.\n"
    output += "TWO DICE, 2:1    3 DICE, 3:1\n\n"
    output += f"YOU HAVE ${game_instance.get_money()}. MAKE A BET."
    return output


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE,
                                  initial_output=get_game_output(),
                                  game_over=game_instance.is_game_over())


@app.route('/play', methods=['POST'])
def play():
    global state

    user_input = request.json.get('input', '').strip()
    output = get_game_output()

    if state == "bet":
        success, message = game_instance.make_bet(user_input)
        if success:
            output += f"\n> {user_input}\nCHOOSE A NUMBER"
            state = "number"
        else:
            output += f"\n> {user_input}\n{message}\nYOU HAVE ${game_instance.get_money()}. MAKE A BET."
    elif state == "number":
        success, message = game_instance.choose_number(user_input)
        if success:
            output += f"\n> {user_input}"
            result = game_instance.roll_dice()
            output += f"\n{game_instance.get_dice_output()}"
            output += f"\nYOU'VE MATCHED {game_instance.matches} TIMES."
            output += f"\n{result}"
            state = "bet"
        else:
            output += f"\n> {user_input}\n{message}\nCHOOSE A NUMBER"

    return jsonify({
        'output': output,
        'game_over': game_instance.is_game_over(),
        'state': state
    })


@app.route('/new_game')
def new_game():
    global game_instance, state
    game_instance = ChuckALuckGame()
    state = "bet"
    return '', 204


def run_web():
    """Запуск веб-сервера"""
    port = 5000
    print(f"Starting web server at http://localhost:{port}")
    print("Opening browser...")
    webbrowser.open(f"http://localhost:{port}")
    app.run(debug=False, port=port, use_reloader=False)


if __name__ == "__main__":
    run_web()