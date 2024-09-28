import tkinter as tk
from BMIlogic import BMIlogic  # Import the BMIlogic class
from Create_UI import UIelements  # Assuming UIelements is in the Create_UI.py file

class BMIGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('BMI CALCULATOR')
        self.root.geometry('400x400')
        self.root.resizable(False, False)
        self.root.iconbitmap("BMIICO.ico")

        # Create frames for screens
        self.mainScreen = tk.Frame(self.root)
        self.BMICalculatorScreen = tk.Frame(self.root)
        self.BMIStandardsScreen = tk.Frame(self.root)

        self.ui = UIelements(self.root)  # Initialize the UIelements class with root
        self.bmi_logic = BMIlogic()  # Initialize the BMIlogic class

        self.options = ['Select option', 'Kg/Cm', 'Lbs/Ft']
        self.selectedOptions = tk.StringVar(self.mainScreen)
        self.selectedOptions.set(self.options[0])

        # Configure layout for frames
        self.mainScreen.grid_columnconfigure(0, weight=1)
        self.mainScreen.grid_columnconfigure(1, weight=2)
        self.mainScreen.grid_columnconfigure(2, weight=1)
        self.mainScreen.grid_rowconfigure(0, weight=1)
        self.mainScreen.grid_rowconfigure(1, weight=0)
        self.mainScreen.grid_rowconfigure(2, weight=0)
        self.mainScreen.grid_rowconfigure(3, weight=0)
        self.mainScreen.grid_rowconfigure(4, weight=0)
        self.mainScreen.grid_rowconfigure(5, weight=0)
        self.mainScreen.grid_rowconfigure(6, weight=1)

        self.BMICalculatorScreen.grid_columnconfigure(0, weight=1)
        self.BMICalculatorScreen.grid_columnconfigure(1, weight=2)
        self.BMICalculatorScreen.grid_columnconfigure(2, weight=1)

        self.BMIStandardsScreen.grid_columnconfigure(0, weight=0)
        self.BMIStandardsScreen.grid_columnconfigure(1, weight=2)
        self.BMIStandardsScreen.grid_columnconfigure(2, weight=1)

        # Add frames to the main window (root)
        self.mainScreen.grid(row=0, column=0, sticky='nsew')
        self.BMICalculatorScreen.grid(row=0, column=0, sticky='nsew')
        self.BMIStandardsScreen.grid(row=0, column=0, sticky='nsew')

        # Set weights for rows and columns in the main window
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create screens
        self.main_screen()

        # Show initial screen (mainScreen)
        self.mainScreen.tkraise()

    def main_screen(self):
        '''Create the main screen'''
        # Add widgets to mainScreen
        self.ui.create_menuOption(self.mainScreen, self.selectedOptions, self.options, row=2, column=1, pady=10)
        self.ui.create_button(self.mainScreen, 'Accept option', row=3, column=1, pady=10, command=self.show_frame)
        self.ui.create_button(self.mainScreen, 'BMI standards', row=4, column=1, pady=10, command=self.show_bmi_standards)
        self.ui.create_button(self.mainScreen, 'Exit', row=5, column=1, pady=10, command=lambda: self.root.destroy())
        self.MainMessage = self.ui.create_label(self.mainScreen, text='', row=6, column=1, pady=10)

    def show_frame(self):
        '''Change displayed frame based on the selected option'''
        selected_option = self.selectedOptions.get()
        if selected_option == self.options[1]:  # kg/cm
            self.BMI_screen('kg/cm', 'Enter weight (kg):', 'Enter height (cm):')
            self.BMICalculatorScreen.tkraise()
        elif selected_option == self.options[2]:  # lbs/ft
            self.BMI_screen('lbs/ft', 'Enter weight (lbs):', 'Enter height (ft):')
            self.BMICalculatorScreen.tkraise()
        elif selected_option == self.options[0]:
            self.display_message(self.MainMessage, 'Select option', 'error')

    def create_bmi_screen(self, title, weight_label, height_label, unit):
        '''Creates the BMI calculator screen'''
        # Clear previous widgets from the BMI calculator screen
        for widget in self.BMICalculatorScreen.winfo_children():
            widget.destroy()

        self.ui.create_label(self.BMICalculatorScreen, f'BMI Calculator ({unit})', row=0, column=1, pady=10, font=('Arial', 15))
        self.ui.create_label(self.BMICalculatorScreen, weight_label, row=1, column=1, pady=10)

        # Save entry fields for resetting later
        self.entry_weight = self.ui.create_entry(self.BMICalculatorScreen, row=2, column=1, pady=5, placeholder='Enter weight')
        self.ui.create_label(self.BMICalculatorScreen, height_label, row=4, column=1, pady=10)
        self.entry_height = self.ui.create_entry(self.BMICalculatorScreen, row=5, column=1, pady=5, placeholder='Enter height')

        self.ui.create_button(self.BMICalculatorScreen, 'Calculate', row=6, column=1, pady=10,
                              command=lambda: self.calculate_bmi(unit))
        self.ui.create_button(self.BMICalculatorScreen, 'Reset', row=7, column=1, pady=10, command=self.reset)

        self.label_message = self.ui.create_label(self.BMICalculatorScreen, '', row=8, column=1, pady=5)
        self.bmi_message = self.ui.create_label(self.BMICalculatorScreen, '', row=9, column=1, pady=1)

        self.ui.create_button(self.BMICalculatorScreen, 'Back', row=10, column=1, pady=5, command=self.back_to_main_screen)

    def show_bmi_standards(self):
        '''Display BMI standards screen'''
        for widget in self.BMIStandardsScreen.winfo_children():
            widget.destroy()  # Clear previous widgets

        # Create headers
        self.ui.create_label(self.BMIStandardsScreen, 'BMI Standards', row=0, column=1, columnspan=2, pady=10, font=('Arial', 15, 'bold'))

        bmi_standards = [
            'BMI', '<16', '16.0-16.9', '17.0-18.6', '18.5-24.9',
            '25.0-29.9', '30.0-34.9', '35.0-39.9', '>= 40'
        ]

        score_interpreter = [
            'Score Interpreter',
            'Severe Thinness',
            'Moderate Thinness',
            'Mild Thinness',
            'Normal Weight',
            'Overweight',
            'Obesity Class I',
            'Obesity Class II',
            'Obesity Class III'
        ]

        # Create the "BMI" label with bold font
        self.ui.create_label(self.BMIStandardsScreen, bmi_standards[0], row=1, column=1, pady=5, sticky='ew', font=('Arial', 10, 'bold'))

        # Create the "Score Interpreter" label with bold font
        self.ui.create_label(self.BMIStandardsScreen, score_interpreter[0], row=1, column=2, pady=5, sticky='ew', font=('Arial', 10, 'bold'))

        # Create the rest of the labels (regular font)
        for idx, standard in enumerate(bmi_standards[1:], start=2):
            self.ui.create_label(self.BMIStandardsScreen, standard, row=idx, column=1, pady=5, sticky='ew')

        for idx, interpretation in enumerate(score_interpreter[1:], start=2):
            self.ui.create_label(self.BMIStandardsScreen, interpretation, row=idx, column=2, pady=5, sticky='ew')

        self.ui.create_button(self.BMIStandardsScreen, 'Back', columnspan=3, padx=10, row=len(bmi_standards) + len(score_interpreter), column=0, pady=5, command=self.back_to_main_screen)

        # Raise the BMI standards screen
        self.BMIStandardsScreen.tkraise()

    def BMI_screen(self, unit, weight_label, height_label):
        '''Create BMI screen based on the unit'''
        self.create_bmi_screen(unit, weight_label, height_label, unit)

    def calculate_bmi(self, unit):
        '''Calculate BMI based on the selected unit'''
        try:
            if unit == 'kg/cm':
                weight = float(self.entry_weight.get().replace(',', '.'))
                height_cm = float(self.entry_height.get().replace(',', '.'))
                height_m = height_cm / 100  # Convert height to meters
                self.validate_input(weight, height_m, 200, 3, 260)  # Adding max_height = 260
            else:  # lbs/ft
                weight = float(self.entry_weight.get().replace(',', '.')) * 0.453592  # Convert to kg
                height_ft = float(self.entry_height.get().replace(',', '.'))
                height_m = height_ft * 0.3048  # Convert to meters
                self.validate_input(weight, height_m, 490, 10, 260)  # Adding max_height = 260

            self.bmi_logic.calculate_bmi(weight, height_m)

            # Display result
            bmi_category = self.bmi_logic.get_bmi_category()
            self.display_message(self.label_message, bmi_category, message_type='info')  # Info message
            self.display_message(self.bmi_message, f'BMI: {self.bmi_logic.bmi_value:.2f}', message_type='info')  # Info message

        except ValueError as e:
            if 'could not convert string to float' in str(e):
                self.display_message(self.label_message, 'Invalid input! Please enter numbers.', message_type='error')  # Error message
            else:
                self.display_message(self.label_message, str(e), message_type='error')  # Error message

    def validate_input(self, weight, height_m, max_weight, min_height, max_height):
        '''Validate weight and height input'''
        if weight <= 0:
            raise ValueError('Weight must be greater than 0.')
        if height_m <= 0:
            raise ValueError('Height must be greater than 0.')
        if weight > max_weight:
            raise ValueError(f'Weight must be less than or equal to {max_weight} kg.')
        if height_m < min_height / 100:
            raise ValueError(f'Height must be greater than or equal to {min_height} cm.')
        if height_m > max_height / 100:  # Check for maximum height
            raise ValueError(f'Height must be less than or equal to {max_height} cm.')

    def reset(self):
        '''Reset input fields and messages'''
        self.entry_weight.delete(0, tk.END)
        self.entry_height.delete(0, tk.END)
        self.label_message.config(text='')
        self.bmi_message.config(text='')

    def back_to_main_screen(self):
        '''Go back to the main screen'''
        self.mainScreen.tkraise()

    def display_message(self, label, message, message_type='info'):
        '''Display messages in a label'''
        label.config(text=message)
        if message_type == 'error':
            label.config(fg='red')
        else:
            label.config(fg='black')

    def run(self):
        '''Run the main loop'''
        self.root.mainloop()


if __name__ == '__main__':
    app = BMIGUI()
    app.run()
