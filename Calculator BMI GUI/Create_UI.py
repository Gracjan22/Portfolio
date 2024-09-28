import tkinter as tk
from tkinter import ttk

class UIelements:
    def __init__(self, root):
        self.root = root  # Główna ramka do przechowywania wszystkich elementów
        self.max_length = 5  # Możesz zmienić wartość w razie potrzeby

    def create_button(self, frame, text, row, column, columnspan=1, sticky='nsew', pady=5, padx=None, command=None, font=('Arial', 11)):
        button = tk.Button(frame, text=text, command=command, font=font)
        button.grid(row=row, column=column, sticky=sticky, pady=pady, columnspan=columnspan, padx=padx)
        return button

    def create_label(self, frame, text, row, column, borderwidth=None, columnspan=1, sticky='nsew', pady=5, font=('Arial', 11)):
        label = tk.Label(frame, text=text, font=font, borderwidth=borderwidth)
        label.grid(row=row, column=column, sticky=sticky, pady=pady, columnspan=columnspan)
        return label

    def create_entry(self, frame, row, column, columnspan=1, sticky='nsew', pady=5, placeholder=''):
        """Tworzy pole Entry z opcjonalnym placeholderem."""
        entry = tk.Entry(frame)
        entry.grid(row=row, column=column, sticky=sticky, pady=pady, columnspan=columnspan)

        # Ustawia placeholder jako domyślny tekst
        if placeholder:
            entry.insert(0, placeholder)  # Ustawia placeholder jako domyślny tekst
            entry.config(fg='grey')  # Ustawia kolor na szary dla placeholdera

            # Zdarzenie, które usunie placeholder, gdy użytkownik kliknie w Entry
            def on_click(event):
                if entry.get() == placeholder:
                    entry.delete(0, tk.END)  # Czyści tekst
                    entry.config(fg='black')  # Zmienia kolor na czarny

            # Zdarzenie, które przywróci placeholder, gdy pole jest puste
            def on_focusout(event):
                if entry.get() == '':
                    entry.insert(0, placeholder)  # Przywraca placeholder
                    entry.config(fg='grey')  # Ustawia kolor na szary

            # Dodaj zdarzenia do Entry
            entry.bind('<FocusIn>', on_click)
            entry.bind('<FocusOut>', on_focusout)

        # Funkcja limitująca ilość znaków
        def limit_entry(event):
            current_text = entry.get()
            
            # Pozwól na cofanie przy użyciu Backspace
            if event.keysym == 'BackSpace':
                return
            
            # Jeśli ilość znaków przekracza limit, przerwij wstawianie nowych znaków
            if len(current_text) >= self.max_length:
                return 'break'

        # Dodaj zdarzenie ograniczające liczbę znaków
        entry.bind('<KeyPress>', limit_entry)

        return entry
    
    def create_menuOption(self, frame, variable, options, row, column, columnspan=1, sticky='nsew', pady=5):
        menuOption = ttk.OptionMenu(frame, variable, *options)
        menuOption.grid(row=row, column=column, columnspan=columnspan, sticky=sticky, pady=pady)
        return menuOption
