import numpy  as np # Importing numpy for numerical operations
import pandas as pd # Importing pandas for data manipulation
import seaborn as sns # Importing seaborn for statistical data visualization
import matplotlib.pyplot as plt # Importing matplotlib for plotting
import streamlit as st # Importing Streamlit for web app development
import os # Importing os for file path operations

st.set_page_config(layout='centered') # Setting the layout of the Streamlit app to centered
st.title('Heart Disease Data Explorer: Learning the Basics with heart.csv') # Setting the title of the app
#file_path = "https://raw.githubusercontent.com/Vinayfsds/streamlitweb/main/heart.csv" # Defining the path to the dataset (raw file URL)
file_path = 'heart.csv' # Defining the path to the dataset (local file)
# Uncomment the above line and comment the below line if you want to use a local file
heart_disease_df = None # Initializing the DataFrame to None

try:
    heart_disease_df = pd.read_csv(file_path) # Attempting to read the dataset (works for both URLs and local files)
    st.success("Dataset loaded successfully!") # Displaying success message if dataset is loaded
except Exception as e:
    st.error(f"Error loading the dataset from '{file_path}': {e}") # Displaying error message if there is an issue loading the dataset
    st.info("You might need to upload 'heart.csv' or ensure the 'file_path' is correct.")

if heart_disease_df is not None: # Checking if the DataFrame is loaded successfully
    data_analysis_option = st.selectbox(
        "Select an analysis view:",
        (
            "--Select an option --",
            "1. Intial Data Overview",
            "2. Understanding Age",
            "3. Understanding Gender (Sex)",
            "4. Understanding Target (Heart Disease Status)",
            "5. Understanding Cholesterol Levels",
            "7. Understanding Chest Pain Type",
            "8. Understanding talach",
            "9. Heat Map",
            "10. Pair Plot",
            "11. Miscellaneous Analysis"
        )
    )
    #st.write(data_analysis_option) # Displaying the selected analysis option
    if data_analysis_option == "1. Intial Data Overview":
        st.header("1. Initial Data Overview")

        st.subheader("1.1. First 5 Rows (df.head())")
        st.dataframe(heart_disease_df.head())
        st.write("**:point_right: What this tells you about `heart.csv`:** You see the column names (like 'age', 'sex', 'cp', 'trestbps', 'chol', 'target'), and the first few values. This gives you a quick feel for the type of data in each column.")

        st.subheader("1.2. Data Dimensions (df.shape)")
        st.write(f"The dataset has **{heart_disease_df.shape[0]} rows** and **{heart_disease_df.shape[1]} columns**.")
        st.write("**:point_right: What this tells you about `heart.csv`:** This tells you the total number of patient records (rows) and the number of features/variables (columns) for each patient. For `heart.csv`, it's usually around (303, 14), meaning 303 patients and 14 pieces of information about each.")

        st.subheader("1.3. Column Information (df.info())")
        # df.info() prints to console, but st.write can show some info.
        # A more Streamlit-friendly way is to display dtypes and non-null counts:
        info_df = pd.DataFrame({
            'Data Type': heart_disease_df.dtypes,
            'Non-Null Count': heart_disease_df.count(),
            'Null Count': heart_disease_df.isnull().sum() # Explicitly show nulls
        })
        st.dataframe(info_df)
        st.write("**:point_right: What this tells you about `heart.csv`:**")
        st.write("- **Data Type (`dtype`):** Tells you if a column contains numbers (`int64`, `float64`) or text (`object`). For `heart.csv`, most are numbers. `age`, `trestbps`, `chol`, `thalach`, `oldpeak` are usually integers or floats.")
        st.write("- **Non-Null Count:** Shows how many actual data points are in each column. If this number is **less than the total number of rows** (from `df.shape[0]`), it means there are **missing values** in that column. `heart.csv` is usually very clean with no missing values, which is great!")

        st.subheader("1.4. Descriptive Statistics for Numerical Columns (heart_disease_df.describe())")
        st.dataframe(heart_disease_df.describe())
        st.write("**:point_right: What this tells you about `heart.csv`:** This table summarizes all your *numerical* columns:")
        st.write("- **`count`**: Same as non-null count.")
        st.write("- **`mean`**: The average value of the column (e.g., average age, average cholesterol).")
        st.write("- **`std`**: Standard deviation, how spread out the data is around the mean.")
        st.write("- **`min` / `max`**: The smallest and largest values. Useful for checking for impossible values (e.g., negative age).")
        st.write("- **`25%`, `50%` (median), `75%`**: Quartiles. They divide the data into quarters. `50%` is the median (middle value). These help understand the distribution without being affected by extreme values.")
        st.write("   - **Example for `age`:** You can see the minimum age, maximum age, and the average age of patients in this dataset.")
    elif data_analysis_option == "2. Understanding Age":
        st.header("2. Understanding the 'age' Column")

        if 'age' in heart_disease_df.columns:
            st.dataframe(heart_disease_df[['age','cp', 'target']]) # Display first few rows of 'age' column
            st.write("**:point_right: What this tells you about `heart.csv`:** The 'age' column contains the age of each patient. It helps us understand the age distribution of patients with heart disease.")
            st.subheader("2.1. Basic Statistics for 'age'")
            st.write(heart_disease_df['age'].describe())
            st.write("**:point_right: What this tells you:** You can quickly see the min, max, average, and spread of ages in your dataset.")

            st.subheader("2.2. Distribution of 'age' (Histogram & KDE)")
            fig, ax = plt.subplots(figsize=(7, 5)) # Create a new figure and axes for this plot
            sns.histplot(data=heart_disease_df, x='age', kde=True, ax=ax)
            ax.set_title("Distribution of Patient Age")
            ax.set_xlabel("Age")
            ax.set_ylabel("Count")
            st.pyplot(fig) # Display the plot
            plt.close(fig) # Close the figure to free memory
            

            st.write("**:point_right: What this tells you:**")
            st.write("- The **histogram (bars)** shows how many patients fall into different age groups.")
            st.write("- The **KDE line (smooth curve)** provides a smoothed estimate of the distribution.")
            st.write("- For `heart.csv`, you'll likely see that most patients are in their **50s and 60s**, with fewer younger or much older patients.")
            st.write("- This plot helps confirm that 'age' looks like a typical age distribution and doesn't have weird spikes or gaps.")
 
            st.subheader("2.3. Age Distribution by Target Variable")
            st.subheader("2.3.1. Age Distribution by Target Variable (0=No Disease, 1=Disease)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.histplot(data=heart_disease_df, x='age', hue='target', multiple='stack', kde=True, ax=ax)
            st.pyplot(fig)
            plt.close(fig) 
        else:
            st.warning("Column 'age' not found in the dataset.")
    elif data_analysis_option == "3. Understanding Gender (Sex)":
        st.header("3. Understanding the 'sex' Column")

        if 'sex' in heart_disease_df.columns:
            st.subheader("3.1. Unique Values and Counts for 'sex'")
            # value_counts() is a great Pandas tool for categorical data
            sex_counts = heart_disease_df['sex'].value_counts().to_frame()
            sex_counts.index = sex_counts.index.map({0: 'Female', 1: 'Male'}) # Map 0/1 to meaningful labels
            st.dataframe(sex_counts)
            st.write("**:point_right: What this tells you:** You can see how many female (0) and male (1) patients are in your dataset. In `heart.csv`, you'll typically find more male patients than female patients.")

            st.subheader("3.2. Distribution of 'sex' (Count Plot)")
            fig, ax = plt.subplots(figsize=(6, 4)) # New figure for this plot
            sns.countplot(data=heart_disease_df, x='sex', ax=ax)
            ax.set_title("Distribution of Patient Gender")
            ax.set_xlabel("Gender (0=Female, 1=Male)")
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['Female', 'Male']) # Make labels readable
            st.pyplot(fig)
            plt.close(fig)

            st.write("**:point_right: What this tells you:**")
            st.write("- The bars visually represent the counts you saw in the table. This confirms the balance (or imbalance) of genders.")
            st.write("- Visuals are often easier to quickly grasp than just numbers.")

            st.subheader("3.3 Distubtion of sex with respect to target variable")
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.countplot(data=heart_disease_df, x='sex', hue='target', ax=ax)
            ax.set_title("Distribution of Patient Gender")
            ax.set_xlabel("Gender (0=Female, 1=Male)")
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['Female', 'Male']) # Make labels readable
            ax.legend(title='Heart Disease', labels=['0 - No Disease', '1 - Disease'])
            st.pyplot(fig)
            plt.close(fig)
            
            st.subheader("Gender-wise Distribution of Heart Disease (Target)")
            # Map 0/1 to Female/Male for clarity
            gender_map = {0: 'Female', 1: 'Male'}
            # Create a crosstab for better display
            gender_target_ct = pd.crosstab(
                heart_disease_df['target'],
                heart_disease_df['sex'].map(gender_map)
            )
            gender_target_ct.index = gender_target_ct.index.map({0: 'No Disease', 1: 'Disease'})
            st.dataframe(gender_target_ct)
            st.write("**:point_right: What this tells you:**")
            st.write("- The bars visually represent the counts you saw in the table. This confirms the balance (or imbalance) of genders.")
            st.write("- Visuals are often easier to quickly grasp than just numbers.")
            st.write("- **Insight:** If you see a much higher bar for one gender, it means your dataset is imbalanced for that gender. For example, if there are more males than females, your analysis and conclusions may be more representative of male patients. This is important to keep in mind when interpreting results or building predictive models.")
        else:
            st.warning("Column 'sex' not found in the dataset.")
    elif data_analysis_option == "4. Understanding Target (Heart Disease Status)":
        st.header("4. Understanding the 'target' Column")

        if 'target' in heart_disease_df.columns:
            st.subheader("4.1. Unique Values and Counts for 'target'")
            target_counts = heart_disease_df['target'].value_counts().to_frame()
            # Ensure the index is integer before mapping
            target_counts.index = target_counts.index.astype(int).map({0: 'No Disease', 1: 'Disease'})
            st.dataframe(target_counts)
            st.write("**:point_right: What this tells you:** This is the most crucial column! `0` typically means the patient **does NOT have heart disease**, and `1` means they **DO have heart disease**. This table shows how many patients fall into each category. In `heart.csv`, the counts are usually quite balanced, which is good for machine learning models.")

            st.subheader("4.2. Distribution of 'target' (Count Plot)")
            fig, ax = plt.subplots(figsize=(6, 4)) # New figure

            # Define the palette dictionary with string keys matching the 'target' column values
            palette = {'0': 'red', '1': 'blue'}

            sns.countplot(data=heart_disease_df, x='target', ax=ax, palette=palette) # Using the corrected palette
            ax.set_title("Distribution of Heart Disease Status")
            ax.set_xlabel("Heart Disease Status (0=No Disease, 1=Disease)")
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['No Disease', 'Disease'])
            st.pyplot(fig)
            plt.close(fig)

            st.write("**:point_right: What this tells you:**")
            st.write("- This plot visually confirms the balance of your main prediction outcome.")
            st.write("- If one category was much, much smaller, it would be an 'imbalanced dataset', which can be tricky for models.")
        else:
            st.warning("Column 'target' not found in the dataset.")
    elif data_analysis_option == "5. Understanding Cholesterol Levels":
        if 'target' in heart_disease_df.columns:
            st.header("5.1. Understanding the 'chol' Column")
            st.dataframe(heart_disease_df[['chol', 'target']]) # Display first few rows of 'chol' column
            st.write("**:point_right: What this tells you about `heart.csv`:** The 'chol' column contains the cholesterol levels of each patient. It helps us understand the cholesterol distribution among patients with heart disease.")

            st.subheader("5.2. Distribution of 'target' (Count Plot)")
            fig, ax = plt.subplots(figsize=(6, 4)) # New figure
            sns.countplot(data=heart_disease_df, x='target', ax=ax)
            ax.set_title("Distribution of Heart Disease Status")
            ax.set_xlabel("Heart Disease Status (0=No Disease, 1=Disease)")
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['No Disease', 'Disease'])
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:** This plot visually confirms the balance of your main prediction outcome.")
            st.subheader("5.3. Basic Statistics for 'chol'")
            st.write(heart_disease_df['chol'].describe())
            st.write("**:point_right: What this tells you:** You can quickly see the min, max, average, and spread of cholesterol levels in your dataset.")
            st.subheader("5.4. Distribution of 'chol' (Histogram & KDE)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.histplot(data=heart_disease_df, x='chol', kde=True, ax=ax)

            ax.set_title("Distribution of Cholesterol Levels")
            ax.set_xlabel("Cholesterol Level")
            ax.set_ylabel("Count")
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- The **histogram (bars)** shows how many patients fall into different cholesterol level ranges.")
            st.write("- The **KDE line (smooth curve)** provides a smoothed estimate of the distribution.")
            st.write("- For `heart.csv`, you'll likely see that most patients have cholesterol levels between **150 and 300 mg/dl**, with fewer patients having very high or very low levels.")

            st.subheader("5.5. Cholesterol Levels by Target Variable")
            st.subheader("5.5.1. Cholesterol Levels by Target Variable (0=No Disease, 1=Disease)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.histplot(data=heart_disease_df, x='chol', hue='target', multiple='stack', kde=True, ax=ax)
            ax.set_title("Distribution of Cholesterol Levels by Heart Disease Status")
            ax.set_xlabel("Cholesterol Level")
            ax.set_ylabel("Count")
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- This plot shows how cholesterol levels differ between patients with and without heart disease.")
            st.write("- You can see if patients with heart disease tend to have higher or lower cholesterol levels compared to those without.")
            st.subheader("5.6. Cholesterol Levels by Target Variable (Box Plot)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.boxplot(data=heart_disease_df, x='target', y='chol', ax=ax)
            ax.set_title("Cholesterol Levels by Heart Disease Status")
            ax.set_xlabel("Heart Disease Status (0=No Disease, 1=Disease)")
            ax.set_ylabel("Cholesterol Level")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['No Disease', 'Disease'])
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- The box plot shows the distribution of cholesterol levels for patients with and without heart disease.")
            st.write("- You can see the median cholesterol level, the interquartile range (IQR), and any potential outliers.")

        else:
            st.warning("Column 'chol' not found in the dataset.")    
    elif data_analysis_option == "7. Understanding Chest Pain Type":
        st.header("7. Understanding the 'cp' Column")
        if 'cp' in heart_disease_df.columns:
            st.dataframe(heart_disease_df[['cp', 'target']]) # Display first few rows of 'cp' column
            st.write("**:point_right: What this tells you about `heart.csv`:** The 'cp' column contains the chest pain type experienced by each patient. It helps us understand the distribution of chest pain types among patients with heart disease.")
            st.subheader("7.1. Unique Values and Counts for 'cp'")
            cp_counts = heart_disease_df['cp'].value_counts().to_frame()
            cp_counts.index = cp_counts.index.map({
                0: 'Typical Angina',
                1: 'Atypical Angina',
                2: 'Non-Anginal Pain',
                3: 'Asymptomatic'
            })
            sns.countplot(data=heart_disease_df, x='cp')
            st.dataframe(cp_counts)      
            st.write("**:point_right: What this tells you:** This table shows how many patients fall into each chest pain type category. In `heart.csv`, you'll typically find a mix of chest pain types, which is important for understanding heart disease symptoms.")
            st.subheader("7.2. Distribution of 'cp' (Count Plot)")
            fig, ax = plt.subplots(figsize=(6, 4))
            palette = {'0': 'red', '1': 'blue', '2' : 'green', '3': 'orange'}
            sns.countplot(data=heart_disease_df, x='cp', ax=ax, palette=palette)
            ax.set_title("Distribution of Chest Pain Types")
            ax.set_xlabel("Chest Pain Type")
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1, 2, 3])
            ax.set_xticklabels(['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- This plot visually confirms the distribution of chest pain types.")
            st.write("- You can see which chest pain types are most common among patients with heart disease.")
            st.subheader("7.3. Chest Pain Types by Target Variable")
            st.subheader("7.3.1. Chest Pain Types by Target Variable (0=No Disease, 1=Disease)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.countplot(data=heart_disease_df, x='cp', hue='target', ax=ax)
            ax.set_title("Distribution of Chest Pain Types by Heart Disease Status")
            ax.set_xlabel("Chest Pain Type (0=Female, 1=Male)")    
            ax.set_ylabel("Count")
            ax.set_xticks([0, 1, 2, 3])           
            ax.legend(title='Heart Disease', labels=['0 - No Disease', '1 - Disease'])
            ax.set_xticklabels(['Typical Angina', 'Atypical Angina', 'Non-Anginal Pain', 'Asymptomatic'])
            st.pyplot(fig)
            plt.close(fig)
    elif data_analysis_option == "8. Understanding talach":
        st.header("8. Understanding the 'thalach' Column")
        if 'thalach' in heart_disease_df.columns:
            st.dataframe(heart_disease_df[['thalach', 'target']]) # Display first few rows of 'thalach' column
            st.write("**:point_right: What this tells you about `heart.csv`:** The 'thalach' column contains the maximum heart rate achieved by each patient. It helps us understand the distribution of heart rates among patients with heart disease.")
            st.subheader("8.1. Basic Statistics for 'thalach'")
            st.write(heart_disease_df['thalach'].describe())
            st.write("**:point_right: What this tells you:** You can quickly see the min, max, average, and spread of heart rates in your dataset.")
            st.subheader("8.2. Distribution of 'thalach' (Histogram & KDE)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.histplot(data=heart_disease_df, x='thalach', kde=True, ax=ax)
            ax.set_title("Distribution of Maximum Heart Rate")
            ax.set_xlabel("Maximum Heart Rate")
            ax.set_ylabel("Count")
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- The **histogram (bars)** shows how many patients fall into different heart rate ranges.")
            st.write("- The **KDE line (smooth curve)** provides a smoothed estimate of the distribution.")
            st.write("- For `heart.csv`, you'll likely see that most patients have maximum heart rates between **100 and 200 bpm**, with fewer patients having very high or very low heart rates.")
            st.subheader("8.3. Maximum Heart Rate by Target Variable")
            st.subheader("8.3.1. Maximum Heart Rate by Target Variable (0=No Disease, 1=Disease)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.histplot(data=heart_disease_df, x='thalach', hue='target', multiple='stack', kde=True, ax=ax)
            ax.set_title("Distribution of Maximum Heart Rate by Heart Disease Status")
            ax.set_xlabel("Maximum Heart Rate")
            ax.set_ylabel("Count")
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- This plot shows how maximum heart rates differ between patients with and without heart disease.")
            st.write("- You can see if patients with heart disease tend to have higher or lower maximum heart rates compared to those without.")
            st.subheader("8.4. Maximum Heart Rate by Target Variable (Box Plot)")
            fig, ax = plt.subplots(figsize=(7, 5))
            sns.boxplot(data=heart_disease_df, x='target', y='thalach', ax=ax)
            ax.set_title("Maximum Heart Rate by Heart Disease Status")
            ax.set_xlabel("Heart Disease Status (0=No Disease, 1=Disease)")
            ax.set_ylabel("Maximum Heart Rate")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['No Disease', 'Disease'])
            st.pyplot(fig)
            plt.close(fig)
            st.write("**:point_right: What this tells you:**")
            st.write("- The box plot shows the distribution of maximum heart rates for patients with and without heart disease.")
            st.write("- You can see the median maximum heart rate, the interquartile range (IQR), and any potential outliers.")

            fig, ax = plt.subplots(figsize=(10, 6))
            x = heart_disease_df['thalach']
            x = pd.Series(x, name="thalach variable")
            sns.distplot(x, bins=10, ax=ax)
            st.pyplot(fig)
            plt.close(fig)
            

            f, ax = plt.subplots(figsize=(10,6))
            x = heart_disease_df['thalach']
            x = pd.Series(x, name="thalach variable")
            sns.kdeplot(x, ax=ax)
            ax.set_title("Distribution of Maximum Heart Rate (thalach)")
            ax.set_xlabel("Count")
            ax.set_ylabel("thalach")
            st.pyplot(f)
            plt.close(f)

            f, ax = plt.subplots(figsize=(10,6))
            x = heart_disease_df['thalach']
            x = pd.Series(x, name="thalach variable")
            sns.kdeplot(x, ax=ax,shade=True,color='r')
            # Shade the area under the KDE curve
            ax.set_title("Distribution of Maximum Heart Rate (thalach)")
            ax.set_xlabel("Count")
            ax.set_ylabel("thalach")
            st.pyplot(f)
            plt.close(f)
            palette = {'0': 'red', '1': 'blue'}
            f, ax = plt.subplots(figsize=(10,6))
            x = heart_disease_df['thalach']
            ax = sns.distplot(x, kde=False, rug=True, bins=10)
            st.pyplot(f)
            plt.close(f)

            f, ax = plt.subplots(figsize=(8, 6))
            sns.stripplot(x="target", y="thalach", data=heart_disease_df, palette=palette, ax=ax)
            ax.set_title("Strip Plot of Maximum Heart Rate by Heart Disease Status")
            st.pyplot(f)
            plt.close(f)

            f, ax = plt.subplots(figsize=(8, 6))
            sns.stripplot(x="target", y="thalach", data=heart_disease_df, jitter = 0.01,palette=palette, ax=ax)
            ax.set_title("Strip Plot of Maximum Heart Rate by Heart Disease Status")
            st.pyplot(f)
            plt.close(f)

            # Note: distplot is deprecated, but if you want to use it vertically:
            fig, ax = plt.subplots(figsize=(10, 6))
            x = heart_disease_df['thalach']
            sns.distplot(x, bins=10, ax=ax, vertical=True)
            ax.set_title("Distribution of Maximum Heart Rate (thalach)")
            ax.set_xlabel("Count")
            ax.set_ylabel("thalach")
            st.pyplot(fig)
            plt.close(fig)
        else:
            st.warning("Column 'thalach' not found in the dataset.")   

    elif data_analysis_option == "9. Heat Map":
        st.header("9. Heat Map of Correlations")
        if heart_disease_df is not None:
            st.subheader("9.1. Correlation Matrix")
            corr = heart_disease_df.corr()  # Calculate the correlation matrix
            st.dataframe(corr)
            st.write("**:point_right: What this tells you:** The correlation matrix shows how strongly each pair of variables is related. Values close to 1 or -1 indicate strong relationships, while values near 0 indicate weak relationships.")
            st.subheader("9.2. Heat Map of Correlations")
            fig, ax = plt.subplots(figsize=(10, 8))
            plt.figure(figsize=(16,12))
            plt.title('Correlation Heatmap of Heart Disease Dataset')
            sns.heatmap(corr, square=True, annot=True, fmt='.2f', linecolor='white', ax=ax)
            ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
            ax.set_yticklabels(ax.get_yticklabels(), rotation=30)
            st.pyplot(fig)
            plt.close(fig)

            
    elif data_analysis_option == "10. Pair Plot":
        st.header("10. Pair Plot of Numerical Variables")   
        if heart_disease_df is not None:
            st.subheader("10.1. Pair Plot")
            num_var = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target' ]
            pairplot_fig = sns.pairplot(heart_disease_df[num_var], kind='scatter', diag_kind='hist')
            st.pyplot(pairplot_fig.fig)
            plt.close(pairplot_fig.fig)
        else:
            st.warning("No numerical variables found in the dataset for pair plot.")
    elif data_analysis_option == "11. Miscellaneous Analysis":  
            st.subheader("11.1. Scatter Plot of Age vs. Resting Blood Pressure")
            st.write("**:point_right: What this tells you about `heart.csv`:** This scatter plot shows the relationship between age and resting blood pressure (trestbps) for patients with and without heart disease. It helps us visualize how these two variables are related.")
            f, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x="age", y="trestbps", data=heart_disease_df, hue="target", ax=ax)
            st.pyplot(f)
            plt.close(f)

            st.subheader("11.2. Scatter Plot of Cholesterol vs. Maximum Heart Rate")
            st.write("**:point_right: What this tells you about `heart.csv`:** This scatter plot shows the relationship between cholesterol levels and maximum heart rate (thalach) for patients with and without heart disease. It helps us visualize how these two variables are related.")
            f, ax = plt.subplots(figsize=(8, 6))
            sns.scatterplot(x="chol", y="thalach", data=heart_disease_df, hue="target", ax=ax)
            st.pyplot(f)
            plt.close(f)
            st.write("**:point_right: What this tells you:**")  
            st.write("- The scatter plot shows individual data points for each patient, colored by heart disease status (target).")
            st.write("- You can see how cholesterol levels and maximum heart rates vary among patients with and without heart disease.")
            st.write("- This helps identify any potential relationships or patterns between these two variables.")
            st.subheader("11.3. Box Plot of Age by Target Variable")
            st.write("**:point_right: What this tells you about `heart.csv`:** This box plot shows the distribution of ages for patients with and without heart disease. It helps us visualize how age varies between these two groups.")
            f, ax = plt.subplots(figsize=(8, 6))
            sns.boxplot(x="target", y="age", data=heart_disease_df, ax=ax)
            ax.set_title("Box Plot of Age by Heart Disease Status")
            ax.set_xlabel("Heart Disease Status (0=No Disease, 1=Disease)")
            ax.set_ylabel("Age")
            ax.set_xticks([0, 1])
            ax.set_xticklabels(['No Disease', 'Disease'])
            st.pyplot(f)
            plt.close(f)
            st.write("**:point_right: What this tells you:**")
            st.write("- The box plot shows the distribution of ages for patients with and without heart disease.")
            st.write("- You can see the median age, the interquartile range (IQR), and any potential outliers.")
            st.subheader("11.4. Distribution of Age by Target Variable")
            st.write("**:point_right: What this tells you about `heart.csv`:** This histogram shows the distribution of ages for patients with and without heart disease. It helps us visualize how age varies between these two groups.")
            f, ax = plt.subplots(figsize=(8, 6))
            sns.histplot(data=heart_disease_df, x='age', hue='target', multiple='stack', kde=True, ax=ax)
            ax.set_title("Distribution of Age by Heart Disease Status")
            ax.set_xlabel("Age")
            ax.set_ylabel("Count")
            st.pyplot(f)
            plt.close(f)
            st.write("**:point_right: What this tells you:**")
            st.write("- The histogram shows how many patients fall into different age groups, colored by heart disease status (target).")
            st.write("- You can see how age is distributed among patients with and without heart disease.")
            st.write("- This helps identify any potential differences in age distribution between these two groups.")
    else:
        st.warning("Please select a valid analysis option from the dropdown menu.")
