from flask import Flask, render_template, request
import os
import re
import datetime


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "a1b2c3d4e5f67890a1b2c3d4e5f67890") 


    
@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    schedule = None
    if request.method == 'POST':

        topics_data = request.form["topics"]
        topics_data= [t.strip() for t in topics_data.split(",") if t.strip()]

        if not topics_data:
            error = "Please enter at least one topic"
        else:
            for t in topics_data:
                if not re.match(r"^\w+$",  t):
                    error = "Invalid topic. Kindly use alphanumrica names "    

        if not error:
            hours_data = request.form.get("hours", "").strip()
            if not re.match(r"^\d+$", hours_data):
                error = "Hours must be a number"
            else:
                hours = int(hours_data)
                if hours > 40:
                    error = "Hours must not exceed 40"
        
        
        if not error:
            deadline_data = request.form.get("deadline", "")
            if not re.match(r"^\d{4}-\d{2}-\d{2}$", deadline_data):
                error = "Deadline must be in the format YYYY-MM-DD"
            else:
                try: 
                    deadline = datetime.datetime.strptime(deadline_data, "%Y-%m-%d")
                    if deadline <= datetime.datetime.today():
                        error = "Deadline cannot be in the past"
                except ValueError:
                    error = "Invalid data entered"    

        priorities = []
        if not error:
            for t in topics_data:
                val = request.form.get(f"priority_{t}", "").strip()
                if val.isdigit():
                    val = int(val)
                priorities.append(val)                
    
        if not error:
                total_priority = sum(priorities)
                weeks = max((deadline - datetime.today()).days // 7, 1)
                schedule = {
                    t: f"{round(hours * (p/total_priority), 2)} hrs/week for {weeks} weeks"
                    for t, p in zip(topics_data, priorities)
                }

               

        
        
    return render_template("index.html", error=error, schedule=schedule)        

    
 


   
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

    