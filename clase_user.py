class Usuario:
    # Atributo de clase
    red = "Instagram"

    def __init__(self, nombre_usuario, nombre_completo, correo):
        self._nombre_usuario = nombre_usuario
        self._nombre_completo = nombre_completo
        self._correo = correo
        self._seguidores = []       # lista de Usuario
        self._seguidos = []         # lista de Usuario
        self._publicaciones = []    # lista de Publicacion

    def __str__(self):
        return (
            f"@{self._nombre_usuario} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Publicaciones: {self.cantidad_publicaciones()}"
        )

    # --- Encapsulamiento ---
    def obtener_nombre_usuario(self):
        return self._nombre_usuario

    def obtener_nombre_completo(self):
        return self._nombre_completo

    def obtener_correo(self):
        return self._correo

    def cambiar_nombre_usuario(self, nuevo):
        if not nuevo:
            return False
        self._nombre_usuario = nuevo
        return True

    def cambiar_correo(self, nuevo):
        if not nuevo:
            return False
        self._correo = nuevo
        return True

    def obtener_seguidores(self):
        return self._seguidores

    def obtener_seguidos(self):
        return self._seguidos

    def obtener_publicaciones(self):
        return self._publicaciones

    # --- Reglas ---
    def cantidad_seguidores(self):
        return len(self._seguidores)

    def cantidad_seguidos(self):
        return len(self._seguidos)

    def cantidad_publicaciones(self):
        return len(self._publicaciones)

    def es_influencer(self):
        return self.cantidad_seguidores() >= 1000

    # --- Acciones ---
    def seguir(self, otro):
        if otro is self:
            return False
        if otro in self._seguidos:
            return False
        self._seguidos.append(otro)
        otro._seguidores.append(self)
        return True

    def publicar(self, contenido):
        p = Publicacion(self, contenido)
        self._publicaciones.append(p)
        return p

    def dar_like(self, publicacion):
        return publicacion.dar_like(self)

    def comentar(self, publicacion, texto):
        return publicacion.comentar(self, texto)

    def a_diccionario(self):
        return {
            "red": self.red,
            "nombre_usuario": self._nombre_usuario,
            "nombre_completo": self._nombre_completo,
            "correo": self._correo,
            "seguidores": self.cantidad_seguidores(),
            "seguidos": self.cantidad_seguidos(),
            "publicaciones": self.cantidad_publicaciones(),
            "es_influencer": self.es_influencer()
        }


class UsuarioVIP(Usuario):
    def __init__(self, nombre_usuario, nombre_completo, correo,
                 verificado=True, tasa_ganancia=0.05):
        super().__init__(nombre_usuario, nombre_completo, correo)
        self._verificado = verificado
        self._tasa_ganancia = tasa_ganancia
        self._ganancias = 0.0

    def __str__(self):
        return (
            f"VIP @{self.obtener_nombre_usuario()} | "
            f"Seguidores: {self.cantidad_seguidores()} | "
            f"Ganancias: S/ {self._ganancias:.2f}"
        )

    def obtener_verificado(self):
        return self._verificado

    def obtener_tasa_ganancia(self):
        return self._tasa_ganancia

    def obtener_ganancias(self):
        return self._ganancias

    def cambiar_tasa_ganancia(self, nueva):
        if nueva < 0:
            return False
        self._tasa_ganancia = nueva
        return True

    def calcular_ganancias(self):
        interacciones = 0
        for p in self.obtener_publicaciones():
            interacciones += p.cantidad_likes()
            interacciones += p.cantidad_comentarios()
            interacciones += p.cantidad_compartidos()
        self._ganancias = interacciones * self._tasa_ganancia
        return self._ganancias

    def a_diccionario(self):
        datos = super().a_diccionario()
        datos["tipo"] = "Usuario VIP"
        datos["verificado"] = self._verificado
        datos["tasa_ganancia"] = self._tasa_ganancia
        datos["ganancias"] = self._ganancias
        return datos


class Publicacion:
    def __init__(self, autor, contenido):
        self._autor = autor
        self._contenido = contenido
        self._likes = []          # lista de Usuario
        self._comentarios = []    # lista de textos (str)
        self._compartidos = 0

    def __str__(self):
        return (
            f"@{self._autor.obtener_nombre_usuario()}: {self._contenido} | "
            f"Likes: {self.cantidad_likes()} | "
            f"Comentarios: {self.cantidad_comentarios()} | "
            f"Compartidos: {self.cantidad_compartidos()}"
        )

    def obtener_autor(self):
        return self._autor

    def obtener_contenido(self):
        return self._contenido

    def obtener_likes(self):
        return self._likes

    def obtener_comentarios(self):
        return self._comentarios

    def cambiar_contenido(self, nuevo):
        if not nuevo:
            return False
        self._contenido = nuevo
        return True

    def cantidad_likes(self):
        return len(self._likes)

    def cantidad_comentarios(self):
        return len(self._comentarios)

    def cantidad_compartidos(self):
        return self._compartidos

    def es_viral(self):
        total = self.cantidad_likes() + self.cantidad_comentarios() + self._compartidos
        return total >= 1000

    def dar_like(self, usuario):
        if usuario in self._likes:
            return False
        self._likes.append(usuario)
        return True

    def quitar_like(self, usuario):
        if usuario in self._likes:
            self._likes.remove(usuario)
            return True
        return False

    def comentar(self, usuario, texto):
        comentario = f"@{usuario.obtener_nombre_usuario()}: {texto}"
        self._comentarios.append(comentario)
        return comentario

    def compartir(self):
        self._compartidos += 1

    def a_diccionario(self):
        return {
            "red": self._autor.red,
            "autor": self._autor.obtener_nombre_usuario(),
            "contenido": self._contenido,
            "likes": self.cantidad_likes(),
            "comentarios": self.cantidad_comentarios(),
            "compartidos": self.cantidad_compartidos(),
            "es_viral": self.es_viral()
        }
