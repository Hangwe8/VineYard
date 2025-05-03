import tkinter as tk
import webbrowser

# Creating the window
window = tk.Tk()
window.title("Chomi")
window.geometry("600x600")
window.configure(bg="#94AEFE")

icon = photo_image = tk.PhotoImage(file="vineyard.png")
window.iconphoto(True, icon)


#WhatsApp Hotlines
KEYWORD_NUMBERS = {
    "mental health": "27871632050",  # SADAG contact
    "mental": "27871632050",         # SADAG contact
    "depression": "27871632050",     # SADAG contact
    "depressed": "27871632050",      # SADAG contact
    "sad": "27871632050",            # SADAG contact
    "sadness": "27871632050",        # SADAG contact
    "stress": "27871632050",         # SADAG contact
    "stressed": "27871632050",       # SADAG contact
    "anxious": "27871632050",        # SADAG contact
    "anxiousness": "27871632050",    # SADAG contact
    "anxiety": "27637092620",        # SADAG contact
    "self harm": "27871632050",     # SADAG contact
    "sh": "27871632050",         # SADAG contact
    "help": "27664353108",      # TEARS contact
    "HIV": "27849228808",         # HIV contact
    "HIV/AIDS": "27849228808",     # HIV contact
    "AIDS": "27849228808",        # HIV contact
    "hiv": "27849228808",         # HIV contact"
    "aids": "27849228808",        # HIV contact
    "abuse": "27800150150",     # Lifeline (GBV) contact
    "gbv": "27800150150",       # Lifeline (GBV) contact
    "domestic violence": "27800150150",  # Lifeline (GBV) contact
    "dv": "27800150150",  # Lifeline (GBV) contact
    "shelter": "27820578600",   # Shelter contact
    "haven": "27820578600",    # Shelter contact
    "escape": "27820578600",   # Shelter contact
    "rape": "27832225164",  # CT Rape Crisis contact
    "sexual assault": "27832225164", #CT Rape Crisis contact
    "sexual violence": "27832225164" #CT Rape Crisis contact
}

# WhatsApp Click-to-Chat Function 
def send_whatsapp_message(phone_number):
    wa_url = f"https://wa.me/{phone_number}"
    webbrowser.open(wa_url)  # Open WhatsApp chat without a message

# Input handling
def handle_input(event=None):
    user_message = message_entry.get().lower().strip()  # Normalize input
    response = "Chomi: I'm sorry, I didn't understand that."

    # Determine correct phone number based on user input
    phone_number = KEYWORD_NUMBERS.get(user_message)  # Get matching number
    
    if phone_number:
        response = f"Chomi: Opening WhatsApp chat with {phone_number}..."
        send_whatsapp_message(phone_number)
    
    output_label.config(text=response)

# Tkinter UI
tk.Label(window, text="Hi! I'm Chomi. What do you need help with?", bg="#94AEFE").pack()
message_entry = tk.Entry(window, width=80)
message_entry.pack(pady=10)
message_entry.bind("<Return>", handle_input)  # Allow pressing Enter

submit_button = tk.Button(window, text="Send Message", command=handle_input)
submit_button.pack(pady=5)

output_label = tk.Label(window, text="", wraplength=400, justify="center", bg="#94AEFE")
output_label.pack(pady=30)

window.mainloop()