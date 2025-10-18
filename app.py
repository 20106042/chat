from flask import Flask, request, render_template

app = Flask(__name__)
chat = []

# --- Function to get bot response ---
def get_response(user_input):
    user_input = user_input.lower()

    if "hii" in user_input:
        return "Welcome!"
    elif "hello" in user_input:
        return "Hello!"
    elif "convert capital" in user_input:
        capital = user_input.replace("convert capital", "").strip()
        if capital:
            return f"Your capital: {capital.upper()}"
        else:
            return "Please enter text after 'convert capital'"
    else:
        return "Invalid input. Try saying 'hii', 'hello', or 'convert capital <text>'."

# --- Route ---
@app.route('/', methods=['GET', 'POST'])
def chatbot():
    if request.method == "POST":
        user_input = request.form['user_input']
        response = get_response(user_input)
        chat.append(("You", user_input))
        chat.append(("Bot", response))
    return render_template('chat.html', chat=chat)

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
