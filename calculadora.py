import customtkinter as ctk
from tkinter import messagebox

# configuracion customtkinter
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("dark-blue")

# creacion de la ventana
app = ctk.CTk()
app.title("Calculadora IMC (Praktika)")
app.geometry("600x500")
app.resizable(False, False)
app.iconbitmap("src/descarga.ico")


# cosos dentro de la ventana
titulo = ctk.CTkLabel(
    app,
    text="Calculadora de IMC",
    font=("arial", 16, "bold")
)
titulo.pack(pady=20)

tituloPeso = ctk.CTkLabel(
    app,
    text="Ingrese su peso en kg",
    font=("arial", 12, "bold")
)
tituloPeso.pack()

peso = ctk.CTkEntry(app)
peso.pack(pady=10)

# altura
tituloAltura = ctk.CTkLabel(
    app,
    text="Ingrese su altura",
    font=("arial", 12, "bold")
)
tituloAltura.pack()

altura = ctk.CTkEntry(app)
altura.pack(pady=10)

# funcion calcular IMC
def calcularIMC():
    # Excepciones uwu
    try:
        pesoValor = peso.get()
        pesoFloat = float(pesoValor)

        alturaValor = altura.get()
        alturaFloat = float(alturaValor)

    except ValueError:
        messagebox.showerror(
            "Error",
            "Por favor ingrese un numero válido"
        )
        return

    # Calculo
    imc = pesoFloat / alturaFloat ** 2

    resultados.configure(
        text="Su imc es: " + str(round(imc, 1))
    )

    if imc < 18.5:
        categoria.configure(
            text="Usted está bajo peso"
        )

    elif imc >= 18.5 and imc <= 24.9:
        categoria.configure(
            text="Usted está en un peso normal"
        )

    elif imc >= 25 and imc <= 29.9:
        categoria.configure(
            text="Usted tiene sobrepeso"
        )

    else:
        categoria.configure(
            text="Usted tiene obesidad"
        )

# boton
calculo = ctk.CTkButton(
    app,
    text="Calcular",
    font=("arial", 10, "bold"),
    fg_color="pink",
    text_color="black",
    width=150,
    height=50,
    hover_color="hot pink",
    command=calcularIMC
)
calculo.pack(pady=10)

# muestra de resultados
tituloResultado = ctk.CTkLabel(
    app,
    text="Resultados",
    font=("arial", 12, "bold")
)
tituloResultado.pack(pady=10)

resultados = ctk.CTkLabel(
    app,
    text="",
    font=("arial", 15, "bold")
)
resultados.pack(pady=10)

categoria = ctk.CTkLabel(
    app,
    text="",
    font=("arial", 15, "bold")
)
categoria.pack(pady=10)

app.mainloop()