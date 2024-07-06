import json

def parse_resume(resume_text):
    resume_lines = resume_text.split('\n')
    resume_data = {
        "contact_information": {},
        "summary": "",
        "education": [],
        "skills": [],
        "scholarships": [],
        "experience": [],
        "projects": [],
        "certifications": [],
        "conferences_and_workshops": [],
        "links": [],
        "extra_curricular_activities": [],
        "languages": []
    }

    current_section = None

    for line in resume_lines:
        line = line.strip()

        if not line:
            continue

        if line.startswith("Summary"):
            current_section = "summary"
        elif line.startswith("Education"):
            current_section = "education"
        elif line.startswith("Skills"):
            current_section = "skills"
        elif line.startswith("Scholarships"):
            current_section = "scholarships"
        elif line.startswith("Experience"):
            current_section = "experience"
        elif line.startswith("Projects"):
            current_section = "projects"
        elif line.startswith("Certifications"):
            current_section = "certifications"
        elif line.startswith("Conferences and Workshops"):
            current_section = "conferences_and_workshops"
        elif line.startswith("Links"):
            current_section = "links"
        elif line.startswith("Extra Curricular Activities"):
            current_section = "extra_curricular_activities"
        elif line.startswith("Languages"):
            current_section = "languages"
        else:
            if current_section == "summary":
                resume_data[current_section] += line + " "
            elif current_section in ["skills", "links"]:
                resume_data[current_section].append(line)
            elif current_section in ["education", "experience", "projects", "certifications", "conferences_and_workshops", "extra_curricular_activities", "languages"]:
                if "institution" in line or "organization" in line or "company" in line:
                    resume_data[current_section].append({"name": line})
                else:
                    if resume_data[current_section]:
                        if current_section == "education":
                            field_mapping = ["institution", "location", "degree", "dates", "GPA"]
                        elif current_section == "experience":
                            field_mapping = ["company", "role", "type", "location", "dates", "description"]
                        elif current_section == "projects":
                            field_mapping = ["name", "dates", "organization", "technologies", "description"]
                        elif current_section == "certifications":
                            field_mapping = ["name", "issuer", "dates", "link"]
                        elif current_section == "conferences_and_workshops":
                            field_mapping = ["name", "issuer", "organization", "dates", "link"]
                        elif current_section == "extra_curricular_activities":
                            field_mapping = ["name", "dates"]
                        elif current_section == "languages":
                            field_mapping = ["name", "proficiency"]

                        if isinstance(resume_data[current_section][-1], dict):
                            last_entry = resume_data[current_section][-1]
                            for key in field_mapping:
                                if key not in last_entry:
                                    last_entry[key] = line
                                    break

    return json.dumps(resume_data, indent=4)

# Input resume text
resume_text = """
Pranjali Tiwari
 pt2796@srmist.edu.in   |    6232718108     |     Chennai, India
 Summary
 I'm Pranjali Tiwari, currently pursuing a Bachelor's degree in Computer Science at SRM University. With a GPA of 9.46, I 
prioritize academic excellence. Passionate about frontend development, I've honed my skills through real-time projects 
and internships. My aim is to merge technical expertise with social responsibility, embracing new challenges and seeking 
collaboration for mutual growth.
 Education
 SRM Institute of Science and Technology, Chennai, Tamil Nadu Sep 2021 - Jun 2025
 B.Tech  ·  Computer Science  ·  Chennai, Tamil Nadu 9.47
 Delhi Public School Mar 2019 - Jun 2020
 12th  ·  CBSE  ·  Guna, MP 93.2%
 Delhi Public School Mar 2017 - Apr 2018
 10th  ·  CBSE  ·  Guna, MP 93.8%
 Skills
 C Programming, C++, Python, Java, HTML5, CSS, JavaScript, BootStrap, DBMS, MySql, NODE.Js, OOPS, UI/UX, Figma, 
Adobe Photoshop , Adobe Illustrator , Web Development, React, Cloud Computing
 Scholarships
 Founder's Scholarship 
SRM Institute of Science and Technology, Kattankulathur, Chennai, Tamil Nadu 
Experience
 BootNext Tech Venture Private Limited   |  Link Jul 2023 - Jul 2023
 UI Developer  ·  Internship Indore
 Interned at BootNext Tech Venture, immersing in the UI/UX domain to gain industry experience and hands-on training. 
Became proficient in tools like Figma, Adobe XD, and Sketch, honing skills in wireframing, prototyping, and user interface 
design.
 Bharat Intern  |  Link Jan 2024 - Feb 2024
 Web Developer   ·  Internship Virtual
 Collaborated on projects to build intuitive user interfaces, implement responsive designs, and optimize website 
performance. Acquired proficiency in HTML, CSS, and JavaScript while adhering to industry best practices and design  
principles.
 CodeAlpha  |  Link Mar 2024 - Mar 2024
 Full Stack Web Developer  ·  Internship Virtual
 Engaged in collaborative projects aimed at crafting user-centric interfaces, integrating responsive design elements, and 
enhancing website performance. Cultivated expertise in HTML, CSS, JavaScript, and Node.js through practical application, 
guided by industry standards and design methodologies. Embraced hands-on training to tackle real-world challenges, 
fostering a deep understanding of effective development practices and ensuring the delivery of high-quality digital 
experiences.
Projects
 Social Media Tracker App Mar 2024 - Apr 2024
 CodeAlpha  ·  HTML, CSS, Javascript Frontend
 Crafted a robust Social Media Tracker application, exemplifying full-stack developer capabilities. Employed a blend of 
technologies for seamless integration across frontend, backend, and database components. Noteworthy features include 
advanced user authentication, dynamic data visualization, and realtime updates, reflecting expertise in modern web 
development.
 Expense Tracker Website Mar 2024 - Apr 2024
 CodeAlpha  ·  HTML5, CSS, JavaScript Frontend
 Created a website for an Expense Tracker, utilizing HTML, CSS, JavaScript, and Node.js. Includes features for expense 
recording, categorization, and visualization. Demonstrates skills in frontend design, backend development, and database 
integration for efficient expense management.
 Blog-Website Jan 2024 - Feb 2024
 Bharat Intern  ·  HTML5, CSS, JavaScript, Node.Js Frontend
 Developed a website demonstrating proficiency in HTML, CSS, JavaScript, and Node.js. Features include responsive 
design, dynamic content, user authentication, and MongoDB integration. Emphasizes functionality, aesthetics, and 
scalability in full-stack web development.
 Registration Form Jan 2024 - Feb 2024
 Bharat Intern  ·  HTML5, CSS, JavaScript Frontend
 Attendance Management System using Facial Recognition Jan 2023 - Jul 2024
 SRM University  ·  Python Programming Digital Image Processing OpenCV HTML5 
CSS JScript
 Machine Learning
 Developed an Attendance Management System with Facial Recognition capabilities. Created using HTML, CSS, 
JavaScript, and Node.js, integrating facial recognition technology for secure and efficient attendance tracking. 
Demonstrates proficiency in frontend design, backend development, and advanced biometric authentication.
 Portfolio Website Feb 2022 - 
SRM University  ·  HTML5 CSS Frontend
 My dynamic portfolio website showcases my professional journey, skills, and expertise, allowing visitors to explore my 
qualifications and projects seamlessly. With a sleek interface, it invites prospective employers to engage with my work 
effortlessly, reflecting my dedication to excellence and innovation.
 Election Voting System Feb 2022 - Jun 2022
 SRM University  ·  C C++ Object-Oriented Programming OOPS
 The election voting system provides a secure and transparent method for casting votes, ensuring integrity and fostering 
confidence in democratic principles through robust security measures.
 SITE-to-SITE IPsec VPN Using CLI Topology Jan 2023 - Jun 2023
 SRM University Computer Networks
 Computer Vision- Rock Paper Scissor Aug 2023 - Dec 2023
 SRM University Computer Communication
 Implementing a real-time multiplayer Rock, Paper, Scissors game using UDP ensures efficient data transmission in 
computer networks. Players choose between three shapes with specific outcomes: Rock beats Scissors, Scissors beat 
Paper, and Paper beats Rock.
 Library Management System Jul 2022 - Nov 2022
 SRM University  ·  C++ C Object-Oriented Programming OOPS
 Certifications
 Oracle Cloud Infrastructure 2023 Certified Foundations Associate  |  Link Jun 2024 - Present
 Oracle 
Meta Frontend Developer  |  Link Nov 2023 - 
Coursera
Machine Learning Specialization  |  Link May 2024 - 
Coursera
 Programming in Java  |  Link Nov 2023 - 
NPTEL
 Android Developer Virtual Internship  |  Link Jul 2024 - 
AICTE
 AIML Virtual Internship Aug 2023 - 
AICTE
 Mastering Compiler design  |  Link Apr 2024 - 
Udemy
 Introduction to Automata Theory, Languages and Computation  |  Link Oct 2023 - 
Udemy
 Networking Basics  |  Link Apr 2023 - 
Cisco Networking Academy
 Networking Devices and Initial Configuration Oct 2023 - 
Cisco Networking Academy
 AWS Academy Graduate - AWS Academy Machine Learning Foundations Apr 2023 - 
AWS Academy
 AWS Academy Graduate - AWS Academy Cloud Foundations Jun 2023 - 
AWS Academy
 Conferences and Workshops
 UI/UX Masterclass  |  Link Aug 2023
 Team Gen-Y  ·  SRM University 
Mern Full Stack Development Aug 2023
 Department of Data Science and Business Systems, School of Computing, SRM 
Institute of Science and Technology, Kattankulathur  ·  SRM University 
Links
 GitHub, LinkedIn
 Extra Curricular Activities
 Member of Graphic Designing Domain at a student's based club at SRM 
University 
Jan 2022 - Nov 2023
 Languages
 English [Professional Working Proficiency], Hindi [Professional Working Proficiency]
"""

# Parse the resume text and print the JSON result
resume_json = parse_resume(resume_text)
print(resume_json)
