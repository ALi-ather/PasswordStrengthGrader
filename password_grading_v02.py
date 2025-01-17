import tkinter as tk
from tkinter import messagebox

class PasswordGraderApp:
    def __init__(self, root):
        self.root = root

        # Set the window to fullscreen
        self.root.title("Password Strength Grader")
        self.root.attributes('-fullscreen', True)  # Enable fullscreen mode
        self.root.configure(bg="#000000")  # Change the background color to black

        # Program header (appears at the top)
        self.header = tk.Label(
            root, text="Password Strength Grader", font=("Courier New", 24, "bold"), 
            fg="#00FF00", bg="#000000"
        )
        self.header.pack(pady=20)  # Add spacing between the title and other elements

        # Label for password input
        self.input_label = tk.Label(
            root, text="Enter your password:", font=("Courier New", 16), 
            fg="#00FF00", bg="#000000"
        )
        self.input_label.pack(pady=10)

        # Password entry field (with "*" to hide the text)
        self.password_entry = tk.Entry(
            root, show="*", font=("Courier New", 16), width=30, 
            bg="#222222", fg="#00FF00", insertbackground="#00FF00"
        )
        self.password_entry.pack(pady=10)

        # Button to evaluate the password
        self.submit_button = tk.Button(
            root, text="Evaluate Password", font=("Courier New", 16), 
            bg="#444444", fg="#00FF00", activebackground="#555555", command=self.evaluate_password
        )
        self.submit_button.pack(pady=20)

        # Text box to display results and tips for the user
        self.output_text = tk.Text(
            root, font=("Courier New", 14), height=15, width=70, 
            bg="#111111", fg="#00FF00", insertbackground="#00FF00", state="disabled"
        )
        self.output_text.pack(pady=10)

        # Button to close the application
        self.close_button = tk.Button(
            root, text="Close Application", font=("Courier New", 16), 
            bg="#444444", fg="#FF0000", activebackground="#555555", command=root.quit
        )
        self.close_button.pack(pady=20)

    # Function to evaluate the password
    def evaluate_password(self):
        # Get the password entered by the user
        password = self.password_entry.get()
        
        # Check if the field is not empty
        if not password:
            messagebox.showwarning("Warning", "Please enter a password!")
            return

        # Evaluate the password strength and provide feedback
        score, feedback = self.grade_password(password)
        result = f"Password Strength: {score}/100\n\nTips:\n{feedback}"

        # Display the result inside the text box
        self.output_text.config(state="normal")  # Enable editing in the text box
        self.output_text.delete(1.0, tk.END)  # Clear previous text
        self.output_text.insert(tk.END, result)  # Insert the new result
        self.output_text.config(state="disabled")  # Disable editing to prevent changes

    # Function to grade the password and provide points and tips
    def grade_password(self, password):
        # Default score and feedback
        score = 0
        feedback = []

        # Check the password length
        if len(password) >= 8:
            score += 20  # Add points if the password is at least 8 characters long
        else:
            feedback.append("- Password should be at least 8 characters long.")

        # Check for uppercase and lowercase letters
        if any(char.islower() for char in password) and any(char.isupper() for char in password):
            score += 20  # Add points if it contains both uppercase and lowercase letters
        else:
            feedback.append("- Use a mix of uppercase and lowercase letters.")

        # Check for numbers
        if any(char.isdigit() for char in password):
            score += 20  # Add points if it contains numbers
        else:
            feedback.append("- Add at least one number.")

        # Check for special characters
        if any(char in "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|" for char in password):
            score += 20  # Add points if it contains special characters
        else:
            feedback.append("- Add special characters such as @, #, $.")
        
        # Check if the password is not one of the common passwords
        common_passwords = ["password", "123456", "qwerty", "letmein"]
        if password.lower() in common_passwords:
            feedback.append("- Avoid using common passwords.")
        else:
            score += 20  # Add points if the password is not common

        # If there are no feedback messages, the password is very strong
        if not feedback:
            feedback.append("Your password is very strong! Great job.")

        return score, "\n".join(feedback)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGraderApp(root)
    root.mainloop()
