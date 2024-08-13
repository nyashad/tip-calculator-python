from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the form
        bill = float(request.form["bill"])
        tip = int(request.form["tip"])
        people = int(request.form["people"])
        
        # Calculate the tip and total bill per person
        tip_as_percentage = tip / 100
        tip_amount = bill * tip_as_percentage
        total_bill = bill + tip_amount
        bill_per_person = total_bill / people
        bill_per_person = round(bill_per_person, 2)

        return render_template("index.html", result=bill_per_person)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
