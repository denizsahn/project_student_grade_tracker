from storage import load_state, save_state
from roster import add_student
from grades import record_grade, calculate_student_average
# YENİ EKLENEN IMPORT:
from analytics import student_progress_report, export_report 

DATA_DIR = "data"

def main():
    # Load data from JSON files
    students, courses, gradebook, settings = load_state(DATA_DIR)
    print("System ready. Data loaded successfully.")
    
    while True:
        print("\n--- STUDENT GRADE TRACKING SYSTEM ---")
        print("1. Add New Student")
        print("2. Record Grade")
        print("3. View Student Average")
        print("4. Export Progress Report (Analytics)") # YENİ SEÇENEK
        print("5. Save & Exit")
        
        choice = input("Enter choice (1-5): ")
        
        # --- OPTION 1: ADD STUDENT ---
        if choice == "1":
            s_id = input("Student ID (e.g., S101): ")
            name = input("Name: ")
            email = input("Email: ")
            
            new_student = {"id": s_id, "name": name, "email": email}
            add_student(students, new_student)
            print(f"Success: {name} added to the system.")
            
        # --- OPTION 2: RECORD GRADE ---
        elif choice == "2":
            c_id = input("Course Code (e.g., CS101): ")
            s_id = input("Student ID: ")
            a_id = input("Assessment ID (e.g., Midterm): ")
            
            try:
                score = float(input("Score (0-100): "))
                weight = float(input("Weight (%): "))
                
                assessment = {
                    "id": a_id,
                    "name": a_id,
                    "score": score,
                    "weight": weight
                }
                record_grade(gradebook, c_id, s_id, assessment)
                print("Success: Grade recorded.")
                
            except ValueError as e:
                print(f"ERROR: {e}")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")

        # --- OPTION 3: VIEW AVERAGE ---
        elif choice == "3":
            c_id = input("Course Code: ")
            s_id = input("Student ID: ")
            
            try:
                avg = calculate_student_average(gradebook, c_id, s_id)
                print(f"-> Average for student {s_id} in {c_id}: {avg:.2f}")
            except Exception:
                print("Could not calculate average. Student or course might not exist.")

        # --- OPTION 4: ANALYTICS (EXPORT REPORT) ---
        elif choice == "4":
            c_id = input("Course Code: ")
            s_id = input("Student ID: ")
            
            try:
                # Raporu oluştur
                report = student_progress_report(gradebook, c_id, s_id)
                filename = f"{s_id}_{c_id}_report.json"
                # Dosyaya yaz
                export_report(report, filename)
                print(f"Success: Report saved to '{filename}'")
            except Exception as e:
                print(f"Error creating report: {e}")
                
        # --- OPTION 5: SAVE & EXIT ---
        elif choice == "5":
            save_state(DATA_DIR, students, courses, gradebook, settings)
            print("All data saved to 'data/' folder. Exiting...")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


