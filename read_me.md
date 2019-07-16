## Predicting gender

*In this Project I want to implement (more than) one Machine Learning algorithm to suspect the gender of a person.*


In the first few steps I preprocessed the data:

**Step 1:**       
Deleting all rows with unknown gender.
Because of problems with the laptop's RAM, I had to chunk the data and create short csvs, which had to be reappended together at the end.

**Step 2:**     
Detecting NaN values and replacing them at first with 0. Some columns, where useful, were replaced by the columns mean.

**Step 3.0:**   
Sorting the dataframe based on sessions in the column SESSION_ID

**Step 3.1:**   
Data formatting:
Searching for gender specific words in column 'CONTENT_NAME' and filling added column
GENDER_CLOTHING' with matching numbers.

            0: masculine clothing
            1: feminine clothing
            2: gender non-specific clothing

**Step 3.2.1:**   
Here are two different functions trying to solve the same problem. I want to fill a new column named 'GENDER_CLOTHING_UNIQUE'.
 Basically it's the same idea as in Step 3.2, but the rows belonging to the same session should get the same number. This time
it's not about the specific row, but the session as a whole.

            0: looked only at masculine or gender non-specific clothes
            1: looked only at feminine or gender non-specific clothes
            2: looked only at gender non-specific clothes
            3: looked at both feminine and masculine clothes

 Added two new columns. The same is happening, but this time for the content in 'SEACH_QUERY'.

**Step 3.2.2:** 
Combining all four new columns in one.

            0: looked only at masculine or gender non-specific clothes
            1: looked only at feminine or gender non-specific clothes
            2: looked only at gender non-specific clothes
            3: looked at both feminine and masculine clothes

**Step 3.3:**  
Creating a new dataframe with only numeric and important columns. (This step can be done much earlier to save time and disk space. I simply didn't know the dataset well enough.)

**Step 4:**    
Normalizing the data and deleting outliers.

**Step 5:**     
Creating a dataframe with equal men and women rows.
*Data preprocessing done.*

**Step 6:**     
Algorithm and prediction.
          

