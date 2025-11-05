# Simple Expert System for Disease Diagnosis

def diagnose():
    print("=== Welcome to the Medical Expert System ===\n")
    print("Answer the following questions with 'yes' or 'no'.\n")

    fever = input("Do you have a fever? ").lower()
    cough = input("Do you have a cough? ").lower()
    headache = input("Do you have a headache? ").lower()
    sore_throat = input("Do you have a sore throat? ").lower()
    runny_nose = input("Do you have a runny nose? ").lower()
    body_pain = input("Do you have body pain? ").lower()
    fatigue = input("Do you feel tired or weak? ").lower()

    # Rules (Knowledge Base)
    if fever == "yes" and cough == "yes" and sore_throat == "yes":
        print("\n👉 You may have the **Flu**. Please rest and stay hydrated.")
    elif cough == "yes" and runny_nose == "yes" and fever == "no":
        print("\n👉 You may have a **Common Cold**. Drink warm fluids and rest.")
    elif headache == "yes" and fever == "yes" and body_pain == "yes":
        print("\n👉 You may have **Dengue or Viral Fever**. Consult a doctor immediately.")
    elif fatigue == "yes" and body_pain == "yes" and fever == "no":
        print("\n👉 You may be experiencing **Fatigue or Stress**. Get rest and eat well.")
    else:
        print("\n❓ Unable to diagnose based on the given symptoms. Please consult a doctor.")

    print("\n=== Thank you for using the Expert System ===")

# Run the system
diagnose()
