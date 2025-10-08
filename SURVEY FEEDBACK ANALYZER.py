feedback_data = {
"S_No" : [1,2,3,4,5,6,7,8,9,10],
"Name" : ["Ravi","Meera","Sam","Anu","Raj","Divya","Arjun","Kiran","Leela","Nisha"],
"Feedback" : [
    "Very GOOD SErvice!!!",
    "poor support, not happy ",
    "GREAT experience! will come again.",
    "okay okay...",
    "not BAD",
    "Excellent care, excellent staff!",
    "good food and good ambience!",
    "Poor response and poor handling of issue",
    "Satisfied. But could be better.",
    "Good support...quick service."
    ],
    "Rating": [5,2,5,3,2,5,4,1,3,4]
    }

num_new = int(input("How many feedbacks do you want to add? "))

for i in range(num_new):
    name = input("Enter name: ")
    feedback = input("Enter feedback: ")
    rating = int(input("Enter rating (1-5): "))

    s_no = len(feedback_data["S_No"]) + 1
    feedback_data["S_No"].append(s_no)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(feedback)
    feedback_data["Rating"].append(rating)

import string
cleaned_feedback = []
for fb in feedback_data["Feedback"]:
    fb = fb.replace(".","").replace(",","").replace("!","").replace("?","")
    fb = " ".join(fb.split())
    fb = fb.lower()
    cleaned_feedback.append(fb)

feedback_data["Feedback"] = cleaned_feedback

def count_word_in_feedbacks(word):
    count = 0
    for fb in feedback_data["Feedback"]:
        if word.lower() in fb:
            count += 1
    return count
print("Word Count Insights:")
print("Feedbacks containing 'good':",count_word_in_feedbacks("good"))
print("Feedbacks containing 'poor':", count_word_in_feedbacks("poor"))
print("Feedbacks containing 'excellent':", count_word_in_feedbacks("excellent"))

print("Final Cleaned Feedback Data:")
for i in range(len(feedback_data["S_No"])):
    print(feedback_data["S_No"][i], "|", feedback_data["Name"][i], "|", feedback_data["Feedback"][i], "| Rating:", feedback_data["Rating"][i])
    

avg_rating = sum(feedback_data["Rating"]) / len(feedback_data["Rating"])
print("Average Rating:", round(avg_rating,2))

longest_feedback = max(feedback_data["Feedback"], key = lambda x: len(x.split()))
print("Feedback with the longest comment:", longest_feedback)

all_words = set()
for fb in feedback_data["Feedback"]:
    all_words.update(fb.split())
print("Unique words in all feedbacks:", all_words)

sorted_data = sorted(
    zip(feedback_data["S_No"], feedback_data["Name"], feedback_data["Feedback"], feedback_data["Rating"]),
    key = lambda x: x[3],
    reverse = True
    )
print("Feedbacks Sorted by Rating (High to Low):")
for entry in sorted_data:
    print(entry[0], "|",entry[1], "|", entry[2], "|", "Rating:", entry[3])













    
 
