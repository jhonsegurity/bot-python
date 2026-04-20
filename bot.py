import datetime

def saludo():
    print("🤖 Hola, soy JhonBot. Escribe 'ayuda' para ver comandos.")

def mostrar_ayuda():
    print("""
📌 Comandos disponibles:
- hola
- hora
- fecha
- salir
""")

def bot():
    saludo()
    
    while True:
        comando = input("Tú: ").lower()
        
        if comando == "hola":
            print("🤖 Hola 👋 ¿Cómo estás?")
        
        elif comando == "hora":
            hora = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 La hora es: {hora}")
        
        elif comando == "fecha":
            fecha = datetime.datetime.now().strftime("%d/%m/%Y")
            print(f"🤖 Hoy es: {fecha}")
        
        elif comando == "ayuda":
            mostrar_ayuda()
        
        elif comando == "salir":
            print("🤖 Adiós 👋")
            break
        
        else:
            print("🤖 No entiendo ese comando 😅")

if __name__ == "__main__":
    bot()
