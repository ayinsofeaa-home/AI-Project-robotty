from datetime import datetime
import pytz

print("Hi! I'm your partner.")

# The loop keeps the chatbot running continuously
while True:
    # 1. Ask the question inside the loop
    user = input("\nHow can I help you princess? (or type 'exit' to stop): ").lower().strip()
    
    # 2. Check if the user wants to leave first
    if user in ["exit", "quit", "bye"]:
        print("Goodbye! Have a great day!")
        break # This breaks the loop and stops the script
        
    # 3. Update the live Malaysia time every single turn
    malaysia_time = datetime.now(pytz.timezone('Asia/Kuala_Lumpur'))
    
    # 4. Your original logic
    if user in ["weather", "cuaca"]:
        print("The weather today is sunny!")
    elif user in ["time", "masa", "pukul berapa"]:
        print(f"Malaysia Time: {malaysia_time.strftime('%I:%M:%S %p')}")
    elif "pretty" in user:
        print("YES PRINCESS URE SOOOOO PRETTY AND CUTE")
    else:
        print("Sorry, I don't understand.")
