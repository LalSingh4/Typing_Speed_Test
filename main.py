import tkinter as tk
import time


def start_test():
    global test_started, words, correct_words, start_time

  # Clear any previous results
    result_label.config(text="")
    user_entry.delete(0, tk.END)

  # Generate random words
    words = ["python", "programming", "gui", "interface", "testing"]

  # Initialize variables
    correct_words = 0
    start_time = time.time()
    test_started = True

  # Display first word
    display_word.config(text=words[0])

def check_word(event):
  global test_started, words, correct_words

  if not test_started:
    return

  user_text = user_entry.get().strip()

  # Check if typed word matches displayed word
  if user_text == display_word.cget("text"):
    correct_words += 1

    # Remove typed word and display next word
    user_entry.delete(0, tk.END)
    words = words[1:]
    
    if words:
      display_word.config(text=words[0])
    else:
      end_test()

def end_test():
  global test_started, start_time, correct_words

  # Calculate elapsed time
  end_time = time.time()
  elapsed_time = end_time - start_time

  # Calculate words per minute (wpm)
  total_words = len(words) + correct_words
  wpm = int((correct_words / elapsed_time) * 60)

  # Display results
  result_label.config(text=f"WPM: {wpm}, Accuracy: {correct_words}/{total_words}")
  test_started = False

# Create main window
root = tk.Tk()
root.title("Typing Test")

# Create labels
display_word_label = tk.Label(root, text="Word:")
display_word_label.pack()

display_word = tk.Label(root, text="", font=("Arial", 18))
display_word.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Create entry field
user_entry = tk.Entry(root, width=50)
user_entry.bind("<Return>", check_word)
user_entry.pack()

# Create button to start test
start_button = tk.Button(root, text="Start Test", command=start_test)
start_button.pack()


# Global variables
test_started = False
words = []
correct_words = 0
start_time = 0

# Run the main loop
root.mainloop()
