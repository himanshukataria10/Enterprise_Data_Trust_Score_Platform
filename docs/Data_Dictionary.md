# Enterprise Data Trust Score Platform

## Data Dictionary

| Column Name | Data Type | Required | Validation Rule | Example |
|-------------|-----------|----------|-----------------|---------|
| Employee_ID | Integer | Yes | Must be unique | 1001 |
| First_Name | String | Yes | Only alphabets | Rahul |
| Last_Name | String | Yes | Only alphabets | Sharma |
| Email | String | Yes | Must be a valid email address | rahul@gmail.com |
| Phone | String | Yes | Must contain 10 digits | 9876543210 |
| Department | String | Yes | Must match predefined departments | IT |
| Job_Title | String | Yes | Must match predefined job titles | Data Analyst |
| Salary | Integer | Yes | Must be between 25000 and 120000 | 65000 |
| Joining_Date | Date | Yes | Cannot be a future date | 2024-01-15 |
| City | String | Yes | Must match predefined cities | Jaipur |