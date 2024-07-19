import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DeviceControllerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controlador de Dispositivo")
        self.geometry("400x300")
        self.create_widgets()
    
    def create_widgets(self):
        # Estilos
        self.style = ttk.Style(self)
        self.configure_style()

        # Título
        title_label = ttk.Label(self, text="Controlador de Dispositivo", style="Title.TLabel")
        title_label.pack(pady=10)

        # Estado del dispositivo
        self.device_status = tk.StringVar(value="Apagado")
        status_label = ttk.Label(self, text="Estado del Dispositivo:", style="Text.TLabel")
        status_label.pack(pady=5)
        status_value_label = ttk.Label(self, textvariable=self.device_status, style="Status.TLabel")
        status_value_label.pack(pady=5)

        # Botón de Encendido/Apagado
        power_button = ttk.Button(self, text="Encender/Apagar", command=self.toggle_power, style="TButton")
        power_button.pack(pady=10)
        
        # Control de velocidad
        speed_label = ttk.Label(self, text="Velocidad:", style="Text.TLabel")
        speed_label.pack(pady=5)
        self.speed_var = tk.IntVar()
        speed_scale = ttk.Scale(self, from_=0, to=100, orient="horizontal", variable=self.speed_var, command=self.update_speed)
        speed_scale.pack(pady=10)
        
        # Barra de progreso
        self.progress = ttk.Progressbar(self, orient="horizontal", length=200, mode="determinate")
        self.progress.pack(pady=10)

        # Botón de Reinicio
        reset_button = ttk.Button(self, text="Reiniciar", command=self.reset_device, style="TButton")
        reset_button.pack(pady=10)

    def configure_style(self):
        try:
            self.tk.call("source", "azure.tcl")
            self.tk.call("set_theme", "light")
        except tk.TclError:
            print("azure.tcl no encontrado. Usando tema predeterminado.")
            self.style.theme_use("default")

        self.style.configure("Title.TLabel", font=("Helvetica", 16, "bold"))
        self.style.configure("Text.TLabel", font=("Helvetica", 12))
        self.style.configure("Status.TLabel", font=("Helvetica", 12, "bold"))

    def toggle_power(self):
        if self.device_status.get() == "Apagado":
            self.device_status.set("Encendido")
        else:
            self.device_status.set("Apagado")

    def update_speed(self, value):
        self.progress['value'] = self.speed_var.get()

    def reset_device(self):
        self.device_status.set("Apagado")
        self.speed_var.set(0)
        self.progress['value'] = 0
        messagebox.showinfo("Reiniciar", "El dispositivo ha sido reiniciado.")

if __name__ == "__main__":
    app = DeviceControllerApp()
    app.mainloop()


