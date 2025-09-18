#HEADER: Tye Glass - pt. 1 Assignment 3 - Personal Data Portfolio & Git Collaboration - COMP163010.202610 - 9/18/2025
full_name = "Jordan Smith"
student_email = 'jsmith@ncat.edu'
home_town = 'Charlotte, NC'
graduation_semester = 'Spring 2028'
major = 'Computer Science'

current_course_list = ["COMP 163", 'MATH 150', 'ENG 101', 'HIS 105']
completed_course_list = ['Biology', 'Chemistry', 'Calculus', 'Spanish II', 'World History']
credit_hours_list = [3, 3, 3, 3]
gpa_history_list = [3.2, 3.6, 3.4, 3.7]
#this holds jordans full gpa history within a list]

emergency_contact = ("Mom", 'Hannah Smith', '704-555-0199')
Home_address = ('456 Oak Street', 'Charlotte, NC', '28202')
instagram_info = ('Instagram', '@jordan_codes', 312)
twitter_info = ('Twitter', '@jordandev', 127)
birthday_tuple = ('Birthday', '5', '22', '2006')

current_skills = {'Python basics', 'HTML', 'Problem solving', 'Time management','Photography'}
skills_to_learn = {'JavaScript', 'Data structures','Git', 'Web design', 'Public speaking'}
career_interests = {'Software development', 'Web development', 'Data science', 'Game development'}
hobbies = {'Gaming', 'Photography', 'Reading', 'Soccer', 'Music'}
entertainment_backlog = {'One Piece', 'Barry', 'Life', 'Incantation', 'Memento'}
#these dictionaries down below hold the users course information
course_credits = {'COMP 163': 3, 'MATH 150': 3, 'ENG 101': 3, 'HIS 105': 3}
course_professors = {'COMP 163': 'Prof. Rhodes', 'MATH 150': 'Dr. Lee', 'ENG 101': 'Dr. Martinez', 'HIS 105': 'Dr. Brown'}
course_rooms = {'COMP 163': 'M-Eric 300', 'MATH 150': 'Marteena 201', 'ENG 101': 'Crosby 121', 'HIS 105': 'Crosby 210'}
monthly_budget = {'Food': 450, 'Entertainment': 200, 'Books': 125, 'Transportation': 100}
#calculate book cost per study hour, rounded to two decimals
study_hours_per_subject = {'Programming': 10, 'Math': 8, 'English': 4, 'History': 3}
contact_directory = {'Mom': '704-555-0199', 'Roommate': '336-555-7821', 'Academic Advisor': '336-334-5000'}

total_credits = sum(credit_hours_list)
cumulative_gpa = sum(gpa_history_list) / len(gpa_history_list)
count_of_completed_courses = len(completed_course_list)
# Total study hours per week across all the subjects
weekly_study_hours = sum(study_hours_per_subject.values())
academic_load = sum(credit_hours_list) + weekly_study_hours
monthly_budget_total = sum(monthly_budget.values())
#this is daily food budget: divided the food budget by 30 days, rounded to two decimals

daily_food_budget = round(monthly_budget['Food'] / 30, 2)
annual_budget_production = (monthly_budget_total * 12)
study_cost_per_hour = round(monthly_budget['Books'] / weekly_study_hours, 2)
#counting the user current hobbies, contacts, and backlog items for life stats

current_hobbies = len(hobbies)

# plz try to aggregate social-media followers across Instagram and Twitter
total_followers = (instagram_info[2]) + (twitter_info[2])
# thefDifference between desired skills and current skills
skill_count_comparision = len(skills_to_learn) - len(current_skills)
contact_directory_size = len(contact_directory)
entertainment_backlog_management = len(entertainment_backlog)
academic_workload = academic_load

print('================================================================')
print('              PERSONAL ACADEMIC & LIFE PORTFOLIO')
print('================================================================')
print(f'Student: {full_name} | Email: {student_email}')
print(f'From: {home_town} | Graduating: {graduation_semester}')
print(f'Major: {major}')
print()
print('=== ACADEMIC PROFILE ===')
print(f'Current Semester: {total_credits} credits across {len(current_course_list)} courses')
print(f'Cumulative GPA: {cumulative_gpa:.2f}')
print(f'Weekly Study Time: {weekly_study_hours} hours')
print(f'Academic Investment: ${study_cost_per_hour:.1f} per study hour')
print()
print('Current Courses:')
print(f"{current_course_list[0]} - {course_credits[current_course_list[0]]} credits - {course_professors[current_course_list[0]]} - {course_rooms[current_course_list[0]]}")
print(f"{current_course_list[1]} - {course_credits[current_course_list[1]]} credits - {course_professors[current_course_list[1]]} - {course_rooms[current_course_list[1]]}")
print(f"{current_course_list[2]} - {course_credits[current_course_list[2]]} credits - {course_professors[current_course_list[2]]} - {course_rooms[current_course_list[2]]}")
print(f"{current_course_list[3]} - {course_credits[current_course_list[3]]} credits - {course_professors[current_course_list[3]]} - {course_rooms[current_course_list[3]]}")
print()
num_skills_youhave = len(current_skills)
num_skills_youwant = len(skills_to_learn)
print('=== PERSONAL DEVELOPMENT ===')
print(f'Current Skills: {current_skills}')
print(f'Learning Goals: {skills_to_learn}')
print(f'Career Interests: {career_interests}')
print(f'Skills Currently Have: {num_skills_youhave}')
print(f'Skills Want to Learn: {num_skills_youwant}')
print()
print('=== FINANCIAL OVERVIEW ===')
print(f'Monthly Budget: ${int(monthly_budget_total)}')
print(f"Food: ${monthly_budget['Food']} (${daily_food_budget:.1f}/day)")
print(f'Entertainment: ${monthly_budget['Entertainment']}')
print(f'Books: ${monthly_budget['Books']}')
print(f'Transportation: ${monthly_budget['Transportation']}')
print(f'Annual Projection: ${annual_budget_production}')
print()
print('=== CONNECTIONS & CONTACTS ===')
print(f'Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}')
print(f'Home Address: {Home_address[0]}, {Home_address[1]} {Home_address[2]}')
print(f'Social Media Presence: {total_followers} followers across 2 platforms')
print(f'Key Contacts: {contact_directory_size} people in directory')
print()
print('=== LIFE STATISTICS ===')
print(f'Total Courses Completed: {count_of_completed_courses}')
print(f'Current Academic Load: {academic_workload} weekly commitments')
print(f'Entertainment Backlog: {entertainment_backlog_management} items')
print(f'Current Hobbies: {current_hobbies} activities')
print('================================================================')
