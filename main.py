# =========================================================
# 1. DEFINICIÓN DE LA CLASE (Esqueleto completo sin usar import)
# =========================================================
class Usuario:
    red = "Instagram"

    def __init__(self, nombre_usuario, nombre_completo, correo):
        self._nombre_usuario = nombre_usuario
        self._nombre_completo = nombre_completo
        self._correo = correo
        self._seguidores = []       
        self._seguidos = []         
        self._publicaciones = []    

    def __str__(self):
        return (
            f"@{self._nombre_usuario} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )

    def obtener_nombre_usuario(self):
        return self._nombre_usuario

    def obtener_nombre_completo(self):
        return self._nombre_completo

    def obtener_correo(self):
        return self._correo

    def cantidad_seguidores(self):
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        return self.cantidad_seguidores() >= 1000

    def seguir(self, otro):
        if otro is self:
            return False
        if otro in self._seguidos:
            return False
        self._seguidos.append(otro)
        otro._seguidores.append(self)
        return True


# =========================================================
# 2. FUNCIONES DEL MENÚ
# =========================================================
def mostrar_menu():
    print("\n" + "="*60)
    print("      SIMULACIÓN DE USUARIOS DE INSTAGRAM DEFINIDOS")
    print("="*60)
    print("1. Ver lista de usuarios registrados con sus estadísticas")
    print("2. Ver detalles completos de una cuenta (Perfil)")
    print("3. Simular un 'Follow' (Hacer que alguien siga a otro)")
    print("4. Salir de la simulación")
    print("="*60)

def main():
    # Diccionario central para guardar los OBJETOS
    red_social = {}
    
    print("\n========== INFORMACIÓN DE REGISTRO PREVIO ==========")
    
    # Aquí están tus datos definidos tal cual tu imagen
    datos_usuarios = [
        ["valedies_1", "Valeria Guadalupe Diestra Vuelot", "valediestra@gmail.com"],
        ["gbustillos_2", "Gustavo Enrique Bustillos Semeler", "gbustillos@gmail.com"],
        ["stayci_3", "Stayci Marisol Ovalle Muñoz", "sovalle@gmail.com"],
        ["sebastian_4", "Sebastián Mauricio Díaz Pasache", "sdiaz@gmail.com"]
    ]

    # PROCESAMIENTO: Convertimos los datos crudos en objetos Usuario
    for datos in datos_usuarios:
        username = datos[0]
        nombre_completo = datos[1]
        correo = datos[2]
        
        # Imprimimos la lista cruda tal cual pediste en la terminal
        print(datos)
        
        # Instanciamos la clase y lo guardamos en el diccionario
        red_social[username] = Usuario(username, nombre_completo, correo)
        
    print("====================================================")
    print("✅ Todos los usuarios han sido convertidos a objetos exitosamente.")

    # =========================================================
    # 3. BUCLE DEL MENÚ INTERACTIVO
    # =========================================================
    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-4): ")

        if opcion == '1':
            print("\n========== INFORMACIÓN DE CUENTA INSTAGRAM ==========")
            for usuario_definido in datos_usuarios:
                print(usuario_definido) 
                
        elif opcion == '2':
            print("\n--- BUSCAR PERFIL ---")
            buscar = input("Ingresa el @nombre_usuario que quieres revisar (ej. valedies_1): ")
            
            if buscar in red_social:
                perfil = red_social[buscar]
                print(f"\n--- 👤 Perfil de @{buscar} ---")
                print(f"📛 Nombre Completo: {perfil.obtener_nombre_completo()}")
                print(f"📧 Correo: {perfil.obtener_correo()}")
                print(f"👥 Seguidores: {perfil.cantidad_seguidores()}")
                print(f"👣 Seguidos: {perfil.cantidad_seguidos()}")
                print(f"📸 Publicaciones: {perfil.cantidad_publicaciones()}")
                print(f"🌟 ¿Es Influencer?: {'Sí' if perfil.es_influencer() else 'No'}")
            else:
                print("❌ Ese usuario no existe en la simulación.")
                
        elif opcion == '3':
            print("\n--- SIMULACIÓN DE FOLLOW ---")
            seguidor = input("¿Quién va a seguir? (Ingresa su @usuario): ")
            seguido = input("¿A quién va a seguir? (Ingresa su @usuario): ")
            
            if seguidor in red_social and seguido in red_social:
                # Se usa la acción de la clase
                exito = red_social[seguidor].seguir(red_social[seguido])
                if exito:
                    print(f"✅ ¡Confirmado! @{seguidor} empezó a seguir a @{seguido}.")
                else:
                    print("❌ No se pudo realizar la acción (Ya lo sigue o se eligió a sí mismo).")
            else:
                print("❌ Error: Verifica que escribiste bien los nombres de usuario.")

        elif opcion == '4':
            print("\nSaliendo de la simulación del Grupo 3... ¡Hasta luego!")
            break
            
        else:
            print("\n❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()