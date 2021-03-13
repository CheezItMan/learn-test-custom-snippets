# Custom Snippet Attempt

This is my (Chris') attempt to build a multi-container test environment for SQL Exercises.  The idea is that students would enter SQL which goes into "requirements.txt" and Pytest reads in the SQL code and runs it against the Postgresql container.  Then Pytest verifies the results.  

I had intended to do this with transactions to roll back changes after the tests run... but I can't get Learn to work with what I have.

