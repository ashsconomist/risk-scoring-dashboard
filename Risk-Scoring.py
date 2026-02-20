import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Load the original data
df = pd.read_excel('Risk_Scoring_Profile_Simulation_1.xlsx', sheet_name=0)

# Clean the data
df = df[[col for col in df.columns if not col.startswith('Unnamed')]]
df = df[df['Student_ID'].notna()]
df = df.sort_values(['Student_ID', 'Year']).reset_index(drop=True)

print("IMPLEMENTING DROPOUT SIMULATION")
print("="*60)
print("\nDropout Probabilities:")
print("Risk 0: 2% per year")
print("Risk 1: 15% per year")
print("Risk 2: 40% per year")
print("Risk 3: 60% per year")
print("\nSPECIAL RULE: Risk 3 at Grade 11 → 70% dropout rate")
print("Grade 12 students: 50% reduced dropout rates (close to graduation)")

# Step 1: Add realistic risk to Grade 12 students
# (Original dataset had all Grade 12 students at Risk 0)
for student_id in df['Student_ID'].unique():
    student_mask = df['Student_ID'] == student_id
    student_data = df[student_mask].copy()
    
    if 12 in student_data['Grade'].values:
        earlier_risks = student_data[student_data['Grade'] < 12]['Risk Intensity'].values
        
        if len(earlier_risks) > 0:
            avg_risk = np.mean(earlier_risks)
            max_risk = np.max(earlier_risks)
            
            # 70% chance of maintaining some risk if they had risk before
            if max_risk > 0:
                if np.random.random() < 0.7:
                    if avg_risk >= 2.5:
                        new_risk = 3
                    elif avg_risk >= 1.5:
                        new_risk = 2
                    elif avg_risk >= 0.5:
                        new_risk = 1
                    else:
                        new_risk = 0
                    
                    grade_12_mask = student_mask & (df['Grade'] == 12)
                    df.loc[grade_12_mask, 'Risk Intensity'] = new_risk

print("\nRisk distribution by grade BEFORE dropout:")
risk_by_grade = pd.crosstab(df['Grade'], df['Risk Intensity'], margins=True)
print(risk_by_grade)

# Step 2: Implement dropout simulation
DROPOUT_PROBS = {
    0: 0.02,   # 2%
    1: 0.15,   # 15%
    2: 0.40,   # 40%
    3: 0.60    # 60%
}

# Reduced rates for Grade 12 (50% reduction - close to graduation)
DROPOUT_PROBS_GRADE12 = {
    0: 0.01,   # 1%
    1: 0.075,  # 7.5%
    2: 0.20,   # 20%
    3: 0.30    # 30%
}

dropped_students = {}
records_to_keep = []

for student_id in df['Student_ID'].unique():
    student_records = df[df['Student_ID'] == student_id].sort_values('Year')
    
    dropped = False
    for idx, row in student_records.iterrows():
        records_to_keep.append(idx)
        
        if not dropped:
            risk = row['Risk Intensity']
            grade = row['Grade']
            
            # SPECIAL RULE: Risk 3 at Grade 11 has 70% dropout rate
            if grade == 11 and risk == 3:
                dropout_prob = 0.70
            elif grade == 12:
                dropout_prob = DROPOUT_PROBS_GRADE12.get(risk, 0)
            else:
                dropout_prob = DROPOUT_PROBS.get(risk, 0)
            
            # Simulate dropout
            if np.random.random() < dropout_prob:
                dropped = True
                dropped_students[student_id] = {
                    'last_grade': grade,
                    'last_year': row['Year'],
                    'risk_at_dropout': risk
                }

df_with_dropout = df.loc[records_to_keep].copy()

# Remove future records for dropped students
final_records = []
for student_id in df_with_dropout['Student_ID'].unique():
    student_data = df_with_dropout[df_with_dropout['Student_ID'] == student_id]
    
    if student_id in dropped_students:
        last_year = dropped_students[student_id]['last_year']
        student_data = student_data[student_data['Year'] <= last_year]
    
    final_records.append(student_data)

df_final = pd.concat(final_records, ignore_index=True)

# Print results
print(f"\n\nDROPOUT RESULTS:")
print("="*60)
print(f"Total dropouts: {len(dropped_students)}")
print(f"Students remaining: {df_final['Student_ID'].nunique()}")
print(f"Records remaining: {len(df_final)}")

if len(dropped_students) > 0:
    dropout_df = pd.DataFrame.from_dict(dropped_students, orient='index')
    print(f"\nDropouts by risk level at time of dropout:")
    print(dropout_df['risk_at_dropout'].value_counts().sort_index())
    print(f"\nDropouts by last grade completed:")
    print(dropout_df['last_grade'].value_counts().sort_index())

# Check Grade 12
grade_12_after = df_final[df_final['Grade'] == 12]
print(f"\n\nGrade 12 Analysis AFTER Dropout:")
print(f"Total Grade 12 students: {len(grade_12_after)}")
print(f"Unique Grade 12 students: {grade_12_after['Student_ID'].nunique()}")
print(f"Risk distribution in Grade 12:")
print(grade_12_after['Risk Intensity'].value_counts().sort_index())

# Calculate graduation rate
grade_9_students = df['Student_ID'].nunique()
grade_12_students = grade_12_after['Student_ID'].nunique()
graduation_rate = (grade_12_students / grade_9_students) * 100
print(f"\n4-Year Graduation Rate: {graduation_rate:.1f}%")

# Save the modified dataset
output_file = 'Risk_Scoring_Profile_With_Dropout.xlsx'
df_final.to_excel(output_file, index=False)
print(f"\n✅ Modified dataset saved to: {output_file}")
