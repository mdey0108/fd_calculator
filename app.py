from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page with the input form
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the form
        principal = float(request.form["principal"])
        interest_rate = float(request.form["rate"]) / 100  # Convert to decimal
        tenure = int(request.form["tenure"])
        compound_frequency = int(request.form["frequency"])

        # Calculate maturity amount using compound interest formula
        maturity_amount = principal * (1 + interest_rate / compound_frequency) ** (compound_frequency * tenure)
        interest_earned = maturity_amount - principal

        # Pass the results to the result page
        return render_template("result.html", principal=principal, interest_rate=interest_rate * 100,
                               tenure=tenure, frequency=compound_frequency, maturity_amount=maturity_amount,
                               interest_earned=interest_earned)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
