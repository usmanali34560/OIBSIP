import socket
import threading
import tkinter as tk
from tkinter import messagebox, filedialog
from cryptography.fernet import Fernet
from PIL import ImageTk, Image

# Initialize encryption key (in practice, securely exchange keys)
encryption_key = Fernet.generate_key()
cipher_suite = Fernet(encryption_key)

# Client class to handle connection and UI
class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.setup_gui()

        # Socket setup
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 12345))

        # Start receiving messages in a new thread
        threading.Thread(target=self.receive_messages).start()

    def setup_gui(self):
        # Chat area
        self.chat_area = tk.Text(self.root, height=20, width=50)
        self.chat_area.pack()

        # Message input
        self.message_input = tk.Entry(self.root, width=40)
        self.message_input.pack()

        # Send button
        self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
        self.send_button.pack()

        # Multimedia sharing button
        self.media_button = tk.Button(self.root, text="Send Image", command=self.send_image)
        self.media_button.pack()

    def send_message(self):
        message = self.message_input.get()
        self.message_input.delete(0, tk.END)

        # Encrypt message before sending
        encrypted_message = cipher_suite.encrypt(message.encode('utf-8'))
        self.client_socket.send(encrypted_message)

    def receive_messages(self):
        while True:
            message = self.client_socket.recv(1024)
            # Decrypt message
            decrypted_message = cipher_suite.decrypt(message).decode('utf-8')
            self.chat_area.insert(tk.END, f"Friend: {decrypted_message}\n")

    def send_image(self):
        # File dialog to choose an image
        filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png")])
        if filepath:
            img = Image.open(filepath)
            img.show()

# Run the client
if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
