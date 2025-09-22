# PrepPal - A web Application

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
Like many learners in Tech in intensive programs especially those who are self learning, it is hard to kepp track of yor progress and the topics you need to cover eg software engineering, data science or cybersecurity while meeting ceratin deadlines. Without a structured schedule, students often prioritize poorly and missing deadlines leading to burnout or incomplete coursework. A studennt may spend too much time on one topic and negelect another leading to poor skills. My project was to try to create a tool that automates scheduling and integrates to reduce stress and improve focus. It generates a JSON summary and an calendar file to integrate with Google Calendar, Outlook, or Apple Calendar.

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

  