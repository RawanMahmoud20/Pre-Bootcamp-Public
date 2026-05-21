# gold_app/views.py
import random
from datetime import datetime
from django.shortcuts import render, redirect

def index(request):
   
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []
        
    context = {
        "gold": request.session["gold"],
        "activities": request.session["activities"]
    }
    return render(request, "ninja_gold.html", context)


def process_money(request):
    if request.method == "POST":
     
        building = request.POST.get("building")
        timestamp = datetime.now().strftime("%B %d, %Y %I:%M %p")
        
        gold_earned = 0
        color = "text-success"
        
      
        if building == "farm":
            gold_earned = random.randint(10, 20)
        elif building == "cave":
            gold_earned = random.randint(10, 20)
        elif building == "house":
            gold_earned = random.randint(10, 20)
        elif building == "quest":
            gold_earned = random.randint(-50, 50) 
            if gold_earned < 0:
                color = "text-danger" 
                
      
        request.session["gold"] += gold_earned
        
       
        if gold_earned >= 0:
            activity_text = f"You entered a {building} and earned {gold_earned} gold. ({timestamp})"
        else:
            activity_text = f"You failed a quest and lost {abs(gold_earned)} gold. Ouch! ({timestamp})"
            
        current_activities = request.session["activities"]
        current_activities.insert(0, {"text": activity_text, "color": color})
        request.session["activities"] = current_activities
        
    return redirect("/")


def reset(request):
    request.session.flush()
    return redirect("/")