import re
import string
from collections import Counter


class UniversityChatbot:
    def __init__(self):
        self.knowledge_base = {
            "admissions": "You can apply online through our university portal. The application deadline is June 30.",
            "programs": "We offer undergraduate and postgraduate programs in Engineering, Business, Arts, and Science.",
            "tuition fees": "The tuition fees vary by program. Please visit the university website for a detailed breakdown.",
            "scholarships": "We offer merit-based and need-based scholarships. Check the financial aid section on our website.",
            "student services": "We provide counseling, career guidance, and student support services to assist you during your studies."
        }
        self.stop_words = set(
            "i me my myself we our ours ourselves you your yours yourself yourselves he him his himself she her hers herself it its itself they them their theirs themselves what which who whom this that these those am is are was were be been being have has had having do does did doing a an the and but if or because as until while of at by for with about against between into through during before after above below to from up down in out on off over under again further then once here there when where why how all any both each few more most other some such no nor not only own same so than too very s t can will just don should now".split())

    def preprocess(self, query):
        query = query.lower().translate(str.maketrans('', '', string.punctuation))
        tokens = query.split()
        filtered_tokens = [word for word in tokens if word not in self.stop_words]
        return filtered_tokens

    def get_response(self, query):
        tokens = self.preprocess(query)

        for keyword, response in self.knowledge_base.items():
            if any(re.search(rf'\b{word}\b', keyword) for word in tokens):
                return response

        return "I'm sorry, I couldn't find an answer to your question. Please visit the university website for more information."


def main():
    bot = UniversityChatbot()
    print("Welcome to the University Chatbot! Type 'exit' to end the chat.")

    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        response = bot.get_response(user_query)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()
