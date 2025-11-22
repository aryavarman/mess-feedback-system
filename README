Real-World Problem and Project Objective
 The Problem
Student mess halls often suffer from low engagement in feedback mechanisms. This leads to issues that include:
Delayed Action: Complaints aren't registered quickly or clearly, causing repetitive issues (e.g., poorly cooked food, sanitation issues).
Lack of Quantifiable Data: Mess managers struggle to identify systemic problems or measure improvements because feedback is unstructured (e.g., verbal complaints or notes are hard to analyze).
Low Student Trust: Students feel their feedback is ignored, leading to decreased participation and increased dissatisfaction

Objective Category
Specific Goal
Metric / Success Criterion
Data Integrity
Ensure all collected feedback is structured and valid.
100% of date, rating, and choice inputs pass validation checks.
System Efficiency
Create a fast, simple method for students to submit feedback.
Feedback submission takes less than 60 seconds per entry.
Reporting
Provide immediate, quantifiable reports for mess management.
Average Rating is calculated correctly; all Complaints (rating $\leq 2$) are accurately isolated and displayed.
Maintainability
Decouple the meal data from the core logic.
Use of the MEAL_MENU dictionary allows menu updates without altering core validation code.

Phase 1: Foundation and Initialization (Data Structure and File Setup)
1.1 Goal
Establish the structured data model for the meal menu and ensure the persistent storage file (studentopinion.csv) is correctly initialized.
1.2 Algorithm: file_init()
START
TRY to open the file specified by FILENAME in exclusive creation mode ("x").
If successful: Write the header row: ["date", "meal", "rating", "comment"].
CATCH FileExistsError: Pass (file already exists).
CATCH any other Exception: Print the error and exit the program (sys.exit(1)).
END
1.3 Key Data Structure
MEAL_MENU: A nested dictionary mapping Day $\rightarrow$ Choice $\rightarrow$ Description.

📐 Phase 2: Input and Validation (Ensuring Data Quality)
2.1 Goal
Implement a generic, reusable input loop and specific validation functions to ensure high data integrity, thereby meeting the Data Integrity Objective.
2.2 Algorithm: get_valid_input(prompt, validator_func)
START
LOOP FOREVER:
Get user input based on prompt.
TRY to execute the validator_func on the input.
If valid, RETURN the validated value.
CATCH ValueError: Print the specific error message and loop again.
END
2.3 Key Validation Logic
Date Validation: Use datetime.strptime() to check against the YYYY-MM-DD format.
Rating Validation: Confirm input is an integer $R$ such that $0 \le R \le 10$.

📝 Phase 3: Feedback Submission (give_opinion)
3.1 Goal
Guide the user through the submission process using validated inputs and successfully record the feedback, addressing the System Efficiency Objective.
3.2 Algorithm: give_opinion()
START
Gather the following inputs sequentially using the Phase 2 get_valid_input structure:
Date
Day of Week
Meal Choice (which returns the full meal description).
Rating
Prompt for Comment/Feedback.
TRY to open FILENAME in append mode ("a").
Write the data [date, meal_description, rating, comment] as a new CSV row.
CATCH Exception: Print the file writing error.
Print success message.
END

 Phase 4: Reporting and Analysis
4.1 Goal
Implement the two core reports to give immediate, quantifiable insights to mess management, fulfilling the Reporting Objective.
4.2 Algorithm: view_average_rating()
START
Initialize T=0 (total rating) and C=0 (count).
TRY to read FILENAME, skipping the header.
FOR each row:
TRY to convert the third column (rating) to an integer.
T = T + rating
C = C + 1
CATCH Exception: Continue to the next row (skip malformed data).
If C > 0: Calculate Average = T/C. Print Average.
Else: Print "No feedback yet."
CATCH FileNotFoundError: Print error message.
END
4.3 Algorithm: view_complaints()
START
Initialize complaint_found = False.
TRY to read FILENAME, skipping the header.
FOR each row:
TRY to convert the rating column to an integer.
IF R<2 :
Set complaint_found = True.
Print the full row details (Date, Meal, Rating, Comment).
CATCH Exception: Continue.
If complaint_found is False: Print "No critical complaints found."
END

 Phase 5: Main Menu and Control Flow
5.1 Goal
Provide a simple, looping user interface to tie all functions together.
5.2 Algorithm: main_menu()
START
Execute file_init().
WHILE TRUE (Loop the menu):
Display the four options (1, 2, 3, 4).
Get the user's choice.
Use if/elif statements to call the corresponding Phase 3 or Phase 4 function.
If choice is '4', BREAK the loop.
If invalid choice, print error.
END
