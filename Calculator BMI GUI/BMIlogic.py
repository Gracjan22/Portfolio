class BMIlogic:
    def __init__(self):
        self.bmi_value = None

    def calculate_bmi(self, weight, height):
        '''Calculate BMI and set bmi_value.'''
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be greater than zero.")
        self.bmi_value = weight / (height ** 2)

    def calculate_bmi_lbs_ft(self, weight_lbs, height_ft):
        '''Calculate BMI using weight in pounds and height in feet.'''
        # Przeliczanie na kilogramy i metry
        weight_kg = weight_lbs * 0.453592  # 1 lb = 0.453592 kg
        height_m = height_ft * 0.3048  # 1 ft = 0.3048 m
        self.calculate_bmi(weight_kg, height_m)  # Użyj istniejącej metody do obliczenia BMI

    def get_bmi_category(self):
        '''Return the BMI category based on the calculated value.'''
        if self.bmi_value is None:
            raise ValueError("BMI value has not been calculated.")

        if self.bmi_value < 16:
            return 'You are severely underweight'
        elif 16 <= self.bmi_value < 17:
            return 'You are underweight'
        elif 17 <= self.bmi_value < 18.5:
            return 'You are slightly underweight'
        elif 18.5 <= self.bmi_value < 25:
            return 'Your weight is normal'
        elif 25 <= self.bmi_value < 30:
            return 'You are overweight'
        elif 30 <= self.bmi_value < 35:
            return 'You have obesity (Class 1)'
        elif 35 <= self.bmi_value < 40:
            return 'You have obesity (Class 2)'
        else:
            return 'You have obesity (Class 3)'

def reset(self):
    '''Reset the BMI value to None.'''
    self.bmi_value = None
