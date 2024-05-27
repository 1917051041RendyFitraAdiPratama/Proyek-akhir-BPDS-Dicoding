import pandas as pd
import numpy as np
import warnings
from joblib import load
warnings.filterwarnings('ignore')

cat_features_dict = {
    'Daytime_evening_attendance': ['Siang', 'Malam'],
    'Displaced': ['Ya', 'Tidak'],
    'Debtor': ['Tidak', 'Ya'],
    'Tuition_fees_up_to_date': ['Ya', 'Tidak'],
    'Gender': ['Perempuan', 'Laki-laki'],
    'Scholarship_holder': ['Ya', 'Tidak']
}

helper_df = pd.DataFrame(cat_features_dict)

# PCA
pca1 = load("assets/enroll_approve_grade_1st_2nd")
pca2 = load("assets/eval_1st_2nd")

# Transformer
transform_admission_grade = load("assets/Transformed_Admission_grade")
transform_age = load("assets/Transformed_Age_at_enrollment")
transform_pca1_1 = load("assets/Transformed_pca1_1")
transform_pca1_2 = load("assets/Transformed_pca1_2")
transform_pca2 = load("assets/Transformed_pca2")

# Model
RFmodel = load("assets/rf_model.joblib")

transformers = [
    transform_admission_grade,
    transform_age,
    transform_pca1_1,
    transform_pca1_2,
    transform_pca2
]

def data_preprocessing(data_input, df=helper_df):
    # Split between the numeric data and categoric data
    numeric_data = data_input[:10]
    categoric_data = data_input[10:]
    
    # Numerical features preprocessing
    ## PCA
    pca1_result = list(pca1.transform([numeric_data[:6]])[0])
    pca2_result = list(pca2.transform([numeric_data[6:8]])[0])

    ## Power Transformer
    val_to_transformed_list = [*numeric_data[8:], *pca1_result, *pca2_result]
    transformed_vals = []
    for transformer, val in zip(transformers, val_to_transformed_list):
        transformed_val = transformer.transform([[val]])[0][0]
        transformed_vals.append(transformed_val)
    
    # Categorical features preprocessing
    ## Add a new data to the dataframe
    df.loc[len(df)] = categoric_data

    ## Do a One-hot Encoding technique
    new_df = pd.get_dummies(df, dtype="int")

    ## Take the last index of the dataframe
    encoded_data_list = list(new_df.iloc[-1])

    # Concate both numeric processed data and categoric processed data
    # and save it into nummpy array
    preprocessed_data = pd.DataFrame([[*transformed_vals, *encoded_data_list]], columns=['Transformed_Admission_grade',
                                                                                       'Transformed_Age_at_enrollment',
                                                                                       'Transformed_pca1_1',
                                                                                       'Transformed_pca1_2',
                                                                                       'Transformed_pca2',
                                                                                       'Daytime_evening_attendance_Malam',
                                                                                       'Daytime_evening_attendance_Siang',
                                                                                       'Displaced_Tidak',
                                                                                       'Displaced_Ya',
                                                                                       'Debtor_Tidak',
                                                                                       'Debtor_Ya',
                                                                                       'Tuition_fees_up_to_date_Tidak',
                                                                                       'Tuition_fees_up_to_date_Ya',
                                                                                       'Gender_Laki-laki', 
                                                                                       'Gender_Perempuan', 
                                                                                       'Scholarship_holder_Tidak',
                                                                                       'Scholarship_holder_Ya'])
    
    return preprocessed_data

def prediction(preprocessed_data, model=RFmodel):
    array = np.array(preprocessed_data)
    result = model.predict(array)[0]
    return result
