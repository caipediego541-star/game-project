# Game Project

## Trabajo Práctico Nº2 - Programación II

### Integrantes

- Serena Vargas
- Uriel Martinez
- Tomas Caballero
- Diego Caipe
- 
---

# Descripción del juego

IES Fight es un videojuego de pelea en 2D desarrollado en Python utilizando la biblioteca Pygame.

El juego está basado en combates uno contra uno, donde los jugadores pueden controlar distintos personajes, realizar ataques, defenderse, utilizar objetos y participar en torneos.

El proyecto fue desarrollado aplicando conceptos de programación orientada a objetos, arquitectura modular y patrones de diseño, buscando crear un sistema organizado, escalable y fácil de mantener.

---

# Historia

En una institución donde la tecnología y la programación forman parte del día a día, surge una competencia diferente: IES Fight.

Los estudiantes, profesores y bedeles se enfrentan en intensos combates para demostrar sus habilidades, utilizando sus conocimientos y herramientas como sus principales armas.

Cada batalla representa un desafío donde la estrategia, los reflejos y el uso inteligente de los recursos pueden definir al ganador.

---

# Tecnologías utilizadas

Las principales tecnologías utilizadas en el desarrollo fueron:

- **Python:** lenguaje principal utilizado para la programación del juego.
- **Pygame:** biblioteca utilizada para la creación de la ventana, manejo de eventos, gráficos, sonidos y animaciones.
- **MySQL:** utilizado para almacenar la información persistente de los torneos.
- **Git / GitHub:** utilizados para el control de versiones y organización del trabajo en equipo.

---
## Configuración de la app

Antes de ejecutar la aplicación, debes configurar las siguientes variables de entorno:

```env
DB_USER=<tu_usuario>
DB_PASSWORD=<tu_contraseña>
DB_NAME=<nombre_de_la_base>
DB_HOST=<host_de_mysql>
DB_PORT=<puerto_de_mysql>
```
---

## Requisitos

- Python 3.10 o superior
- MySQL

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/caipediego541-star/game-project.git
```

### 2. Ingresar al repositorio
```bash
cd game-project
code .
```

### 3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación
```bash
python main.py
```
