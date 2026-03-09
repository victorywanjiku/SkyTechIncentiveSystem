
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

X_train = np.array([[5, 80, 3, 70],
                    [3, 60, 2, 50],
                    [8, 90, 4, 85],
                    [2, 50, 1, 40],
                    [6, 85, 3, 75]])
y_train = np.array(['PASS', 'FAIL', 'PASS', 'FAIL', 'PASS'])

knn = KNeighborsClassifier(n_neighbors=3)   
knn.fit(X_train, y_train)
def get_user_input():
    while True:
        try:
            hours_studied = float(input("Enter hours studied (0-10): "))
            attendance = float(input("Enter attendance percentage (0-100): "))
            assignments_completed = int(input("Enter number of assignments completed (0-5): "))
            past_exam_score = float(input("Enter past exam score (0-100): "))
            
            if (0 <= hours_studied <= 10 and 
                0 <= attendance <= 100 and 
                0 <= assignments_completed <= 5 and 
                0 <= past_exam_score <= 100):
                return np.array([[hours_studied, attendance, assignments_completed, past_exam_score]])
            else:
                print("Please enter values within the specified ranges.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
def predict_pass_fail(user_input):
    prediction = knn.predict(user_input)
    return prediction[0]
if __name__ == "__main__":
    user_input = get_user_input()
    result = predict_pass_fail(user_input)
    print(f"Based on the entered data, the student is likely to {result} the exam.")
