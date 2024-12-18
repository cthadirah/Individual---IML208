import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# List to simulate database
appointments = []

# Add new appointment (Create)
def add_appointment():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    date = entry_date.get()
    time = entry_time.get()
    location = entry_location.get()
    condition = entry_condition.get()

    if name and age and gender and date and time and location and condition:
        appointment = {
            "id": len(appointments) + 1,
            "patient_name": name,
            "age": age,
            "gender": gender,
            "appointment_date": date,
            "appointment_time": time,
            "clinic_location": location,
            "condition": condition
        }
        appointments.append(appointment)
        messagebox.showinfo('Success', 'Appointment added successfully!')
        clear_entries()
        show_appointments()
    else:
        messagebox.showerror('Error', 'Please fill all fields.')

# Show all appointments (Read)
def show_appointments():
    for row in tree.get_children():
        tree.delete(row)

    for appointment in appointments:
        tree.insert('', tk.END, values=(appointment["id"], appointment["patient_name"], appointment["age"], appointment["gender"], appointment["appointment_date"], appointment["appointment_time"], appointment["clinic_location"], appointment["condition"]))

# Update an appointment
def update_appointment():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select an appointment to update.')
        return
    
    selected_id = tree.item(selected_item, 'values')[0]
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    date = entry_date.get()
    time = entry_time.get()
    location = entry_location.get()
    condition = entry_condition.get()

    if name and age and gender and date and time and location and condition:
        for appointment in appointments:
            if appointment["id"] == int(selected_id):
                appointment.update({
                    "patient_name": name,
                    "age": age,
                    "gender": gender,
                    "appointment_date": date,
                    "appointment_time": time,
                    "clinic_location": location,
                    "condition": condition
                })
        messagebox.showinfo('Success', 'Appointment updated successfully!')
        clear_entries()
        show_appointments()
    else:
        messagebox.showerror('Error', 'Please fill all fields.')

# Delete an appointment
def delete_appointment():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', 'Please select an appointment to delete.')
        return
    
    selected_id = tree.item(selected_item, 'values')[0]
    global appointments
    appointments = [appointment for appointment in appointments if str(appointment["id"]) != selected_id]
    messagebox.showinfo('Success', 'Appointment deleted successfully!')
    show_appointments()

# Clear input fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_time.delete(0, tk.END)
    entry_location.delete(0, tk.END)
    entry_condition.delete(0, tk.END)

# Load selected appointment data into the entry fields
def on_tree_select(event):
    selected_item = tree.selection()
    if selected_item:
        selected_id = tree.item(selected_item, 'values')[0]
        for appointment in appointments:
            if appointment["id"] == int(selected_id):
                entry_name.delete(0, tk.END)
                entry_name.insert(0, appointment["patient_name"])
                entry_age.delete(0, tk.END)
                entry_age.insert(0, appointment["age"])
                gender_var.set(appointment["gender"])
                entry_date.delete(0, tk.END)
                entry_date.insert(0, appointment["appointment_date"])
                entry_time.delete(0, tk.END)
                entry_time.insert(0, appointment["appointment_time"])
                entry_location.delete(0, tk.END)
                entry_location.insert(0, appointment["clinic_location"])
                entry_condition.delete(0, tk.END)
                entry_condition.insert(0, appointment["condition"])

# Main application window
root = tk.Tk()
root.title("Dental Clinic Appointment System")

# Set the background color for a clinic theme
root.configure(bg="#f0f8ff")

# Frame for input fields
frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

# Input fields with styled labels and entries
label_name = tk.Label(frame, text="Patient Name:", bg="#f0f8ff", font=("Arial", 12))
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(frame, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age = tk.Label(frame, text="Age:", bg="#f0f8ff", font=("Arial", 12))
label_age.grid(row=1, column=0, padx=10, pady=5)
entry_age = tk.Entry(frame, font=("Arial", 12))
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_gender = tk.Label(frame, text="Gender:", bg="#f0f8ff", font=("Arial", 12))
label_gender.grid(row=2, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_male = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male", bg="#f0f8ff", font=("Arial", 12))
gender_male.grid(row=2, column=1, padx=10, pady=5)
gender_female = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female", bg="#f0f8ff", font=("Arial", 12))
gender_female.grid(row=2, column=2, padx=10, pady=5)

label_date = tk.Label(frame, text="Appointment Date (YYYY-MM-DD):", bg="#f0f8ff", font=("Arial", 12))
label_date.grid(row=3, column=0, padx=10, pady=5)
entry_date = tk.Entry(frame, font=("Arial", 12))
entry_date.grid(row=3, column=1, padx=10, pady=5)

label_time = tk.Label(frame, text="Appointment Time (HH:MM):", bg="#f0f8ff", font=("Arial", 12))
label_time.grid(row=4, column=0, padx=10, pady=5)
entry_time = tk.Entry(frame, font=("Arial", 12))
entry_time.grid(row=4, column=1, padx=10, pady=5)

label_location = tk.Label(frame, text="Clinic Location:", bg="#f0f8ff", font=("Arial", 12))
label_location.grid(row=5, column=0, padx=10, pady=5)
entry_location = tk.Entry(frame, font=("Arial", 12))
entry_location.grid(row=5, column=1, padx=10, pady=5)

label_condition = tk.Label(frame, text="Condition:", bg="#f0f8ff", font=("Arial", 12))
label_condition.grid(row=6, column=0, padx=10, pady=5)
entry_condition = tk.Entry(frame, font=("Arial", 12))
entry_condition.grid(row=6, column=1, padx=10, pady=5)

# Buttons for CRUD operations
btn_add = tk.Button(root, text="Add Appointment", command=add_appointment, bg="#b0e0e6", font=("Arial", 12), width=20)
btn_add.pack(pady=10)

btn_update = tk.Button(root, text="Update Appointment", command=update_appointment, bg="#b0e0e6", font=("Arial", 12), width=20)
btn_update.pack(pady=10)

btn_delete = tk.Button(root, text="Delete Appointment", command=delete_appointment, bg="#b0e0e6", font=("Arial", 12), width=20)
btn_delete.pack(pady=10)

# Treeview for displaying appointments
tree_frame = tk.Frame(root, bg="#f0f8ff")
tree_frame.pack(pady=20)

columns = ('ID', 'Patient Name', 'Age', 'Gender', 'Appointment Date', 'Appointment Time', 'Clinic Location', 'Condition')
tree = ttk.Treeview(tree_frame, columns=columns, show='headings', height=10)
tree.heading('ID', text='ID')
tree.heading('Patient Name', text='Patient Name')
tree.heading('Age', text='Age')
tree.heading('Gender', text='Gender')
tree.heading('Appointment Date', text='Appointment Date')
tree.heading('Appointment Time', text='Appointment Time')
tree.heading('Clinic Location', text='Clinic Location')
tree.heading('Condition', text='Condition')
tree.pack()

# Bind treeview select event
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Show all appointments on startup
show_appointments()

# Run the Tkinter event loop
root.mainloop() 
