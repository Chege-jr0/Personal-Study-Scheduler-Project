# PrepPal - A Python Web Application

Welcome to Prepal, a personal study planner that helps students manage study hours and meet tight deadlines

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Description
Like many learners in tech-intensive programs, especially those who are self-learning, it’s hard to keep track of your progress and the topics you need to cover e.g, software engineering, data science, or cybersecurity, while meeting certain deadlines. Without a structured schedule, students often prioritize poorly and miss deadlines, leading to burnout or incomplete coursework. A student may spend too much time on one topic and neglect another, leading to poor skills. My project was to create a tool that automates scheduling and integrates to reduce stress and improve focus. It generates a JSON summary and a calendar file to integrate with Google Calendar, Outlook, or Apple Calendar.

## How the Application works
-**Input Your Study Details**
   Enter your topics (e.g, Math, Physics, Regex).
   Specify the number of hours you can study per week(up to 40).
   Set your deadline(date by which you want to complete the study plan)
   Assign a priority level(1-5) for each topic, where 5 = highest priority.

   
<img width="400" height="400" alt="Screenshot 2025-09-23 201104" src="https://github.com/user-attachments/assets/c67b3481-0bfb-4d3c-9e8b-5b6afe83f1fc" />
<img width="400" height="400" alt="Screenshot 2025-09-23 201216" src="https://github.com/user-attachments/assets/3b0bbc63-007b-4fcc-b0af-d62ac689a71c" />



-**Schedule Generation**
   PrepPal calculates how to distribute your weekly hours across topics based on your priorities.
        
    In the function (generate schedule), the app starts with today's date and your chosen deadline date.
      start_date = datetime.datetime.now().date()
    It calculates how many days are remaining.
      days = (deadline_date - start_date).days
    It then converts that into weeks(at least 1 week)  
      weeks = max(days // 7, 1)
    Each subject is assigned a priority value
    Total weight is calculated by the sum of all priorities.  
      total_weight = sum(priorities.values())
    To get the weekly hours, we perform the following operation
      (subject priority ÷ total priorities) × weekly hours for each subject, and it is calculated accordingly
    


   The Schedule ensures higher-priority subjects get more study time.
   The plan spans from the current week until your deadline.
   <img width="1208" height="857" alt="Screenshot 2025-09-23 201239" src="https://github.com/user-attachments/assets/57b9b0cd-b18f-4c5c-84c2-8451659e4a73" />

**View and Download Your Plan**   
   The generated schedule is displayed in a clean table showing topics, hours per week, total hours, and priority.
   You can download the plan in JSON format, and you can export the schedule, which creates weekly recurring study events in your calendar.

**Calendar Intergration**
   Import the .ics file into your Google Calendar.
   Each topic appears as a weekly recurring event starting at 9AM with the allocated study hours.
   This keeps you accountable and reminds you to stay on track.   


## Features
- **Smart Scheduling**: Generate study plans based on deadlines and available hours.
- **Priority Allocation**: Assign importance levels (1–5) for each topic.
- **Calendar Export**: Save schedule as an `.ics` file for calendar apps.
- **Motivational Quotes**: Encouragement messages with every plan.
- **Data Export**: JSON output for storage or sharing.

## Tech Stack
- **Backend**: Python 3.x
- **Libraries**: `ics`, `datetime`, `json`, `re`
- **Storage**: JSON file + ICS file for calendar events
- **Development**: Git and GitHub

## Installation
### Prerequisites
- Python 3.x
- Git

### Steps
1. **Clone the Repository**  
   ```bash
   git clone https://github.com/Chege-jr0/Personal-Study-Schedule-Project.git
   cd Personal-Study-Schedule-Project                
  
2.**Install Dependencies**

    bash
    Copy code
    pip install -r requirements.txt
    Run the App

    bash
    Copy code
    python app.py
    Usage
    Add Study Details: Enter topics, weekly study hours, deadlines, and priorities.

    Generate Schedule: View personalized study plan in the terminal.

    Save Schedule: JSON + ICS files are created for reuse and calendar import.

    Calendar Import: Open study_schedule.ics in Google Calendar, Outlook, or Apple Calendar.


  ## API Endpoints (optional if you expose a Flask/Django API)

    POST /generate_schedule → Generates a schedule with topics and hours.

    GET /download_calendar → Download the .ics calendar file.

  ## Deployment

    Local Deployment: Run with Python as shown above.

    Future Hosting Options: Can be extended to Flask + deployed on Render, Vercel, or Railway.

    Contributing
    Fork the repository.

    Create a new branch (feature/new-feature).

    Commit changes with clear messages.

    Push branch and open a Pull Request.

##  License
    This project is licensed under the MIT License.

    Contact
    Email: paulgikonyo100@gmail.com

    GitHub: Chege-jr0

  
