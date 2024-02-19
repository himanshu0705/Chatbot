import nltk
from nltk.chat.util import Chat, reflections

patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you', ['I am doing well, thank you!', 'I\'m good, thanks for asking.']),
    (r'what is your name', ['I am a chatbot.', 'You can call me Chatbot.']),
    (r'I need help|can you help me', ['Yes, how may I help you?', 'For sure', 'I\'ll be glad to do that']),
    (r'my name is (.*)', ['Nice to meet you, %1.']),
    (r'(.*) (good|great)', ['I\'m glad to hear that!']),
    (r'(.*) (bad|sad)', ['I\'m sorry to hear that.']),
    (r'((.*) thanks|thankyou)|thanks|thankyou', ['You\'re always welcome', 'Glad I could help']),
    (r'((.*) college|university)|college|university', ['Sure, what aspect of college are you curious about? Admissions, courses, or something else?']),
    (r'((.*) admission|admissions)|admission|admissions', ['For admission details, check the college website or contact the admissions office.']),
    (r'((.*) scholarship|scholarships)|scholarship|scholarships', ['Many colleges offer scholarships based on the Merit Score. Check the college website or contact the financial aid office.']),
    (r'((.*) campus|facilities)|campus|facilities', ['Colleges have facilities like libraries and labs. Explore the college website for more information.']),
    (r'((.*) courses)|courses', ['The courses provided by the college may differ for every college. Check out the college website for details.']),
    (r'((.*) fee|fees)|fee|fees', ['The fee structure differ from college to college depending upon the category you are belonging.']),
    (r'((.*) sports|games|athletics)|sports|games|athletics', ['Every college have their sports programs. Explore th ecollege site to know more.']),
    (r'((.*) extracurricular|clubs)|extracurricular|clubs', ['Both Technical and Non-Technical clubs are formed in the college. Various events are held under the clubs to enhance the learning process. Visit the college website for detailed information'])
]

chatbot = Chat(patterns, reflections)

print("Hi! I'm a Friday, a simple chatbot. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Goodbye!")
        break
    response = chatbot.respond(user_input)
    print("Bot:",response)