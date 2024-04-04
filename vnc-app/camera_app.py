import tkinter as tk
from tkinter import messagebox
import subprocess
import datetime
import os
import logging

logging.basicConfig(filename='./camera_app.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# if os.environ.get('DISPLAY','') == '':
#     print('no display found. Using :0.0')
#     os.environ.__setitem__('DISPLAY', '1')

def capture_image(folder_path):
    # Ensure the folder exists
    os.makedirs(folder_path, exist_ok=True)
    
    # Get the current time for a unique image filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"image_{timestamp}.jpg"
    
    # Specify the full path for the image
    full_path = os.path.join(folder_path, filename)
    
    # Capture an image using libcamera-still and save it in the specified folder
    command = f"libcamera-still -o {full_path}"
    try:
        subprocess.run(command, shell=True, check=True)
        messagebox.showinfo("Success", "Image captured successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to capture image: {e}")

def create_gui():
    folder_path = "/app/output"
    
    # Create the main window
    root = tk.Tk()
    root.title("Image Capture App")
    root.geometry("300x100")
    
    # Add a button to capture an image
    capture_btn = tk.Button(root, text="Capture Image", command=lambda: capture_image(folder_path))
    capture_btn.pack(pady=20)
    
    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    create_gui()
    
