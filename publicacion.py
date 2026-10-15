# Archivo: publicacion.py
class Publicacion:
    def __init__(self, autor, contenido):
        self.autor = autor
        self.contenido = contenido
        self.likes = []  # ¡Cambio clave! Ahora es una lista en lugar de un número (0)
        self.comentarios = []

    def dar_like(self, usuario):
        nombre = usuario.obtener_nombre_usuario()
        # Verificamos que el usuario no le haya dado like antes
        if nombre not in self.likes:
            self.likes.append(nombre)
            return True
        return False # Retorna Falso si ya le había dado like

    def comentar(self, usuario, texto):
        self.comentarios.append(f"@{usuario.obtener_nombre_usuario()}: {texto}")
        return True

    def __str__(self):
        # Usamos len(self.likes) para contar cuántos elementos hay en la lista
        return f"📝 '{self.contenido}' | ❤️ Likes: {len(self.likes)} | 💬 Comentarios: {len(self.comentarios)}"