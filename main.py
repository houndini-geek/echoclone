from tkinter import Tk, Frame, Menu, Label, ttk
from tkinter import Toplevel, Button
from tkinter import filedialog, messagebox
from random import randint
import os 

root = Tk()
def clone_handler(clone_choice):
    # Get the list of selected files based on clone_choice
    if clone_choice == 'image':
        files = filedialog.askopenfilenames(title="Select one or more image files", filetypes=[("Image files", '.png .jpg .jpeg')])
    elif clone_choice == 'video':
        files = filedialog.askopenfilenames(title="Select one or more video files", filetypes=[("Video files", '.mp4')])

    # Get the output directory to save cloned files
    output_dir = filedialog.askdirectory(title=f'Where to save cloned {clone_choice}(s)?')

    if not files:
        return
    if not output_dir:
        messagebox.showwarning("Warning", "No output directory selected!")
        return
    # Create a subfolder named after the cloning type (image or video)
    output_dir = os.path.join(output_dir, clone_choice)  # Create folder for images or videos
    os.makedirs(output_dir, exist_ok=True)  # Create the subfolder if it doesn't exist
    # Create progress bar and label to show the process
    progress_label = ttk.Label(root, text=f"Cloning {clone_choice}(s)...")
    progress_label.pack(pady=10)
    progress = ttk.Progressbar(root, length=300, mode='determinate', maximum=len(files))
    progress.pack(pady=10)

    # Process each file
    for i, file in enumerate(files):
        base, ext = os.path.splitext(file)
        
        new_name = f'pyclone-{clone_choice}-{randint(100, 700)}-{os.path.basename(base)}{ext}'

        try:
            with open(file, 'rb') as f:
                with open(os.path.join(output_dir, new_name), 'wb') as cloned:
                    cloned.write(f.read())
                    print(f"Cloned {os.path.basename(file)} to {output_dir}")

            # Update progress bar
            progress['value'] = i + 1
            root.update_idletasks()  # Refresh the UI

        except Exception as e:
            messagebox.showerror("Error", f"Failed to clone {os.path.basename(file)}: {e}")
            break  # Stop cloning on error

    # Finish up after cloning
    progress_label.config(text="Cloning Complete!")
    messagebox.showinfo("Success", f"Cloning complete for all selected {clone_choice}(s)!")

def clone_img_choice():
    clone_handler('image')

def clone_video_choice():
    clone_handler('video')














root.title("EchoClone | Dark Mode Edition 😎")
root.geometry("500x300")
root.configure(bg="#2c2c2c")

# Dark Theme Colors
dark_bg = "#2c2c2c"
dark_fg = "#f0f0f0"
accent_color = "#1f8ef1"







def launch_mini_guide():
    # Create a new top-level window
    guide_window = Toplevel(root)
    guide_window.title("Welcome to EchoClone Guide 😎")
    guide_window.geometry("400x250")
    guide_window.configure(bg=dark_bg)
    
    # Guide content
    guide_label = Label(guide_window, text="Welcome to EchoClone! 🎉\n\nHere's what you can do:\n\n"
                                           "- Clone images and videos effortlessly.\n"
                                           "- Organize files into subfolders.\n"
                                           "- Convert file formats (coming soon!).\n"
                                           "- Batch rename files for easy management.\n\n"
                                           "Click around and explore! 😎",
                                           bg=dark_bg, fg=dark_fg, font=("Helvetica", 12), justify="left")
    guide_label.pack(pady=20, padx=20)
    
    # Close button
    close_button = Button(guide_window, text="Close Guide", command=guide_window.destroy, bg=accent_color, fg=dark_fg)
    close_button.pack(pady=10)

# Frame for content
content_frame = Frame(root, bg=dark_bg)
content_frame.pack(expand=True, fill='both', padx=20, pady=20)

# Menu bar
menu_bar = Menu(root, bg=dark_bg, fg=dark_fg, tearoff=0)
clone_menu = Menu(menu_bar, tearoff=0, bg=dark_bg, fg=dark_fg)
clone_menu.add_command(label="Clone Images", command=clone_img_choice) 
clone_menu.add_command(label="Clone Videos", command=clone_video_choice) 
menu_bar.add_cascade(label="Clone Options", menu=clone_menu)

# Add Exit option
menu_bar.add_command(label="Exit", command=root.quit)

# Label for welcome message
welcome_label = Label(content_frame, text="Welcome to EchoClone 😎", bg=dark_bg, fg=dark_fg, font=("Helvetica", 16, "bold"))
welcome_label.pack(pady=10)

# Placeholder for a button with an accent color
start_button = ttk.Button(content_frame, text="Get Started", command=lambda: None)
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12))
start_button.pack(pady=10)
# Update the 'Get Started' button to launch the guide
start_button.config(command=launch_mini_guide)
# Configure menu
root.config(menu=menu_bar)

# Run the app
root.mainloop()
