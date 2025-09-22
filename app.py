import re
import datetime
import random
import json


def get_motivational_quote():
    """ This function returns a random quote from the choices given """

    quotes = [
        "Keep learning, keep growing!",
        "As long as you show up, things will align!",
        "Stay curious, stay coding!"
        "All play with no work makes jack a broke boy"
        ]
    return random.choice(quotes)

def user_input_and_validate():
         """ This function gets the data from the user and validates if it,s in the correct format """
         error =  None
         #Topics
         topics_data = input("Please Enter the topics e.g math, regex, science: ")
         topics_data = [t.strip().lower() for t in topics_data.split(",") if t.strip()]
         if not topics_data:
             return None, None, None, None
         for t in topics_data:
             if not re.match(r"^\w+$", t):
                return None, None, None, None
        #Hours
         hours_data=input(f"\nEnter the number of hours(max 40hrs): ").strip()
         if not re.match(r"^\d+$", hours_data):
             return False, None, None, None, None
         hours = int(hours_data)
         if hours > 40:
              return False, None, None, None, None      
                     
         #Deadline
               
         deadline_data=input(f"\nEnter the deadline date YYYY-MM-DD: ").strip()
         if not re.match(r"^\d{4}-\d{2}-\d{2}$", deadline_data):
            return None, None, None, None
         try:
              deadline_date = datetime.datetime.strptime(deadline_data, "%Y-%m-%d").date()
              if deadline_date <= datetime.datetime.today().date():
                   return None, None, None, None
         except ValueError:
                return None, None, None, None
         
         #Priority
         priorities = {}
         for topic in topics_data:
              p = input(f"Enter priority for {topic} (1-5) 5 is the highest priority: ").strip()
              if not re.match(r"^[1-5]$", p):
                   return None, None, None, None
              priorities[topic] = int(p)


         return(topics_data, hours, deadline_date, priorities)      

def generate_schedule(topics_data, hours, deadline_date, priorities):
        """ This function generates the schedule """
        start_date = datetime.datetime.now().date()
        days = (deadline_date - start_date).days
        weeks = max(days // 7, 1)
        
        total_weight = sum(priorities.values())

        schedule = {}
        for topic in topics_data:
             weight = priorities[topic] / total_weight
             weekly_hours = hours * weight
             schedule[topic] = f"{round(weekly_hours, 2)} hrs/week for {weeks} weeks"

        return schedule      

def save_schedule(schedule, priorities):
     """ This function allows the schedule created to be stored in csv and json format """
     schedule_data = []
     for topic, allocation in schedule.items():
          hours_match = re.search(r'(\d+\.?\d*)', allocation)
          weeks_match = re.search(r'(\d+) weeks', allocation)
          hours = float(hours_match.group(1)) if hours_match else 0
          weeks = int(weeks_match.group(1)) if weeks_match else 1
          schedule_data.append({
                "topic": topic,
                "weekly_hours": hours,
                "weeks": weeks,
                "total_hours": round(hours * weeks, 2),
                "priority": priorities.get(topic, 1)      
          })

     with open("study_schedule.json", "w") as f:
          json.dump(schedule_data, f, indent=2)

     return True, "Schedule saved to study_schedule.json"     
        

def main():
     """ This is the main function where everythin is executed """
     topics_data, hours, deadline_date, priorities = user_input_and_validate()

     if topics_data:
          schedule = generate_schedule(topics_data, hours,deadline_date, priorities)             
        
          print("YOUR PERSONAL STUDY SCHEDULE")
          print("\n-----------------------------------------")
          print(f"Total Weekly Hours: {hours}")
          print(f"Duration: {(deadline_date - datetime.datetime.now().date()).days} days")
          print(f"Topics: {','.join(topics_data)}")
          print("--------------------")

          for topic, allocation in schedule.items():
               priority = priorities[topic]
               print(f"{topic.upper()}: {allocation} (Priority: {priority}/5)")

          save_sucess, save_message = save_schedule(schedule, priorities)
          print(f"\n {save_message}")  

          quote = get_motivational_quote()
          print(f"\n {quote}")   

          print("--------------------------------------------")

          print("Happy Studying")
     else:    
          print("No valid inputs provided")



if __name__ == "__main__":
        main()    
               
            
            
                   
            
            
            
                       

           
                    
           
                    
           
                       
                    
          


            
       



        

