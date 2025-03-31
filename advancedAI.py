class ExpertSystem:
    def __init__(self):
        self.knowledge_base = {
            "Common Cold": {"cough", "sneezing", "runny nose", "sore throat"},
            "Flu": {"fever", "chills", "body ache", "fatigue", "cough"},
            "Malaria": {"fever", "chills", "sweating", "headache", "nausea"},
            "Typhoid": {"fever", "abdominal pain", "weakness", "loss of appetite", "constipation"},
            "COVID-19": {"fever", "cough", "shortness of breath", "loss of taste", "loss of smell"}
        }

    def diagnose(self, symptoms):
        possible_diseases = {}

        for disease, disease_symptoms in self.knowledge_base.items():
            match_count = len(symptoms.intersection(disease_symptoms))
            if match_count > 0:
                possible_diseases[disease] = match_count

        if not possible_diseases:
            return "No matching disease found. Please consult a doctor."

        diagnosis = max(possible_diseases, key=possible_diseases.get)
        return f"Based on the symptoms, you may have {diagnosis}. Please seek medical advice."


def main():
    system = ExpertSystem()
    print("Welcome to the AI-based Disease Diagnosis System")
    print("Enter your symptoms separated by commas (e.g., fever, cough, headache) Three(3) symptoms please:")

    user_input = input().lower()
    symptoms = set(map(str.strip, user_input.split(",")))

    diagnosis = system.diagnose(symptoms)
    print(diagnosis)


if __name__ == "__main__":
    main()
