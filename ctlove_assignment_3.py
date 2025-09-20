#Personal Information Storage
full_name = "Cameron Love"
student_email = "ctlove@ncat.edu"
hometown_charlotte =  "Hampton, VA"
graduation_semester = "Spring 2029"
major = "Computer Science"

#Academic Data Organization
current_courses_list = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses_list = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours_list = [3, 3, 3, 3]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]

#Contact Information Storage
emergency_contact_tuple = ("Mom", "Hannah Smith", "704-555-0199" )
home_address_tuple = ("456 Oak Street", "Charlotte", "NC", "28202")
instagram_info_tuple = ("Instagram", "@jordan_codes", 312)
twitter_info_tuple = ("Twitter", "@jordandev", 127)
birthday_tuple = ("Birthday", "5", "22", "2006")

#Interest Tracking
current_skills_set = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn_set = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests_set = {"Software development", "Web development" , "Data science", "Game development"}
hobbies_set = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog_set = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

#Organizational Mapping
course_credits_dictionary = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors_dictionary = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms_dictionary = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget_dictionary = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hrs_per_subject_dictionary = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory_dictionary = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

total_credit_hours =  sum(credit_hours_list) # Adds all the values in the credit hours list
cumulative_gpa = sum(gpa_history_list) / 4 # Adds all the values in the gpa history list then divides them by 4
cumulative_gpa_rounded = round(cumulative_gpa, 2)  # Rounds the answer to 2 decimal points
completed_courses_count = len(completed_courses_list) # Counts the values in the list in the len() function
weekly_study_hours = study_hrs_per_subject_dictionary["Programming"] + study_hrs_per_subject_dictionary["Math"] + study_hrs_per_subject_dictionary["English"] + study_hrs_per_subject_dictionary["History"] # Adds all the values in the study hours per subject dictionary
academic_load = total_credit_hours + weekly_study_hours
monthly_budget_total = monthly_budget_dictionary["Food"] + monthly_budget_dictionary["Entertainment"] + monthly_budget_dictionary["Books"] + monthly_budget_dictionary["Transportation"] # Adds all the values in the monthly dictionary
daily_food_budget = monthly_budget_dictionary["Food"] / 30
daily_food_budget_rounded = round(daily_food_budget, 2) # Rounds the answer to 2 decimal points
annual_budget_projection = monthly_budget_total * 12
study_cost_prhr = monthly_budget_dictionary["Books"] / weekly_study_hours 
study_cost_prhr_rounded = round(study_cost_prhr, 2) # Rounds the answer to 2 decimal points
social_media_followers = instagram_info_tuple[2] +twitter_info_tuple[2] # Add the value in the third position of the instagram tuple to the 3rd value in the twitter tuple
skills_count_comparison = len(current_skills_set) / len(skills_to_learn_set) # Divides the number of strings in current list by the strings in skills to learn
contact_directory_size = len(contact_directory_dictionary) # Counts the values in the list in the len() function
entertainment_backlog_count = len(entertainment_backlog_set) # Counts the values in the list in the len() function
academic_load_count = academic_load







print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown_charlotte} | Graduating: {graduation_semester}")
print(f"Major: {major}")
print("")
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credit_hours} credits across {len(current_courses_list)} courses")
print(f"Cumulative GPA: {cumulative_gpa_rounded}")
print(f"Weekly Study Time: {weekly_study_hours} hours")
print(f"Academic Investment: ${study_cost_prhr_rounded} per study hour")
print("")
print(f"Current Courses:")
print(f"{current_courses_list[0]} - {course_credits_dictionary["COMP 163"]} credits - {course_professors_dictionary["COMP 163"]} - {course_rooms_dictionary["COMP 163"]}")
print(f"{current_courses_list[1]} - {course_credits_dictionary["MATH 150"]} credits - {course_professors_dictionary["MATH 150"]} - {course_rooms_dictionary["MATH 150"]}")
print(f"{current_courses_list[2]} - {course_credits_dictionary["ENG 101"]} credits - {course_professors_dictionary["ENG 101"]} - {course_rooms_dictionary["ENG 101"]}")
print(f"{current_courses_list[3]} - {course_credits_dictionary["HIS 105"]} credits - {course_professors_dictionary["HIS 105"]} - {course_rooms_dictionary["HIS 105"]}")
print("")
print(f"=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills_set}")
print(f"Learning Goals: {skills_to_learn_set}")
print(f"Career Interests: {career_interests_set}")
print(f"Skills Currently Have: {len(current_skills_set)}")
print(f"Skills Want to Learn: {len(skills_to_learn_set)}")
print("")
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget_dictionary["Food"]} (${daily_food_budget_rounded}/day)")
print(f"Entertainment: ${monthly_budget_dictionary["Entertainment"]}")
print(f"Books: ${monthly_budget_dictionary["Books"]}")
print(f"Transportation: ${monthly_budget_dictionary["Transportation"]}")
print(f"Annual Projection: ${annual_budget_projection}")
print("")
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact_tuple[1]} ({emergency_contact_tuple[0]}) - {emergency_contact_tuple[2]}")
print(f"Home Address: {home_address_tuple[0]}, {home_address_tuple[1]}, {home_address_tuple[2]} {home_address_tuple[3]}")
print(f"Social Media Presence: {social_media_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_directory_size} people in directory")
print("")
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_courses_count}")
print(f"Current Academic Load: {academic_load_count} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_count} items")
print(f"Current Hobbies: {len(hobbies_set)} activities")
print("================================================================")
