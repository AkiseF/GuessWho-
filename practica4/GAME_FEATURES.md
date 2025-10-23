# Guess Who - Attack on Titan Edition

Un juego de adivinanzas basado en los personajes de Attack on Titan (Shingeki no Kyojin) desarrollado en Flutter.

## 🎮 Características del Juego

### Modos de Juego
- **Un Jugador**: Juega contra la IA
- **Dos Jugadores**: Conexión por Bluetooth (próximamente)

### Niveles de Dificultad
El juego ahora incluye cuatro niveles de dificultad diferentes:

#### 🟢 Fácil
- **Grid**: 2×2 (4 personajes)
- **Ideal para**: Principiantes y niños
- **Descripción**: Un reto sencillo para familiarizarse con el juego

#### 🟡 Medio  
- **Grid**: 3×3 (9 personajes)
- **Ideal para**: Jugadores casuales
- **Descripción**: Un poco más de desafío con más opciones

#### 🔴 Difícil
- **Grid**: 4×4 (16 personajes)
- **Ideal para**: Jugadores experimentados
- **Descripción**: El nivel clásico con buena variedad de personajes

#### 🟣 Experto
- **Grid**: Dos grids de 4×4 (32 personajes en total)
- **Ideal para**: Verdaderos expertos
- **Descripción**: El máximo desafío con todos los personajes disponibles
- **Característica especial**: Navegación entre grids con carrusel

## 🎯 Cómo Jugar

### Objetivo
Adivina el personaje secreto de tu oponente antes de que él adivine el tuyo.

### Flujo del Juego
1. **Selección de Dificultad**: Elige entre Fácil, Medio, Difícil o Experto
2. **Selección de Personaje**: Cada jugador elige secretamente su personaje
3. **Hacer Preguntas**: Usa el carrusel de preguntas para obtener información
4. **Eliminar Personajes**: Basándote en las respuestas, elimina personajes manualmente
5. **Adivinanza Final**: Cuando estés seguro, haz tu adivinanza final

### Controles del Juego
- **Tocar un personaje**: Abrir opciones (eliminar o adivinar)
- **Carrusel de preguntas**: Deslizar para ver diferentes preguntas
- **Modo Experto**: Usar flechas para navegar entre grids

## 🏗️ Arquitectura del Proyecto

### Estructura de Archivos
```
lib/
├── main.dart                          # Punto de entrada de la aplicación
├── models/                            # Modelos de datos
│   ├── character.dart                 # Modelo de personaje
│   ├── game_session.dart              # Sesión de juego y dificultades
│   └── question.dart                  # Modelo de preguntas
├── providers/                         # Estado de la aplicación
│   ├── game_provider.dart             # Lógica principal del juego
│   └── theme_provider.dart            # Gestión de temas
├── screens/                           # Pantallas de la aplicación
│   ├── home_screen.dart               # Pantalla principal
│   ├── difficulty_selection_screen.dart # Selección de dificultad
│   ├── game_screen.dart               # Pantalla del juego
│   └── bluetooth_setup_screen.dart    # Configuración Bluetooth (futuro)
├── services/                          # Servicios
│   ├── character_service.dart         # Gestión de personajes
│   └── ai_service.dart                # Lógica de la IA
└── widgets/                           # Componentes reutilizables
    ├── character_card.dart            # Tarjeta de personaje
    ├── custom_logo.dart               # Logo personalizado
    ├── game_status_bar.dart           # Barra de estado del juego
    ├── question_carousel.dart         # Carrusel de preguntas
    ├── theme_selector.dart            # Selector de tema
    └── difficulty_selector.dart       # Selector de dificultad
```

### Características Técnicas

#### Gestión de Estado
- **Provider Pattern**: Para el manejo de estado reactivo
- **GameProvider**: Controla toda la lógica del juego
- **ThemeProvider**: Gestiona los temas visuales

#### Niveles de Dificultad
- **DifficultyLevel Enum**: Define los cuatro niveles
- **GridDimensions**: Calcula automáticamente las dimensiones del grid
- **Dynamic Character Loading**: Carga el número correcto de personajes según la dificultad

#### Modo Experto
- **Dual Grid System**: Maneja dos grids de 4×4 simultáneamente
- **Grid Navigation**: Sistema de carrusel para cambiar entre grids
- **Visual Indicators**: Indicadores de grid actual y navegación

## 🎨 Diseño Visual

### Temas
- **Tema claro y oscuro**: Adaptable automáticamente al sistema
- **Colores por dificultad**:
  - 🟢 Verde: Fácil
  - 🟡 Naranja: Medio  
  - 🔴 Rojo: Difícil
  - 🟣 Morado: Experto

### Responsive Design
- **Grid adaptativo**: Se ajusta automáticamente a diferentes tamaños
- **Carrusel de preguntas**: Navegación fluida por gestos
- **Interfaz intuitiva**: Iconografía clara y comprensible

## 📱 Instalación y Ejecución

### Prerrequisitos
- Flutter SDK (versión 3.0 o superior)
- Dart SDK
- Android Studio / VS Code con extensiones de Flutter

### Pasos de Instalación
```bash
# Clonar el repositorio
git clone [repository-url]

# Navegar al directorio
cd practica4

# Instalar dependencias
flutter pub get

# Ejecutar la aplicación
flutter run
```

### Dependencias Principales
```yaml
dependencies:
  flutter:
    sdk: flutter
  provider: ^6.0.0      # Gestión de estado
  # Otras dependencias...
```

## 🤖 Sistema de IA

### Comportamiento de la IA
- **Toma de decisiones inteligente**: Basada en probabilidades y estrategia
- **Preguntas estratégicas**: Optimiza las preguntas para eliminar más personajes
- **Tiempo de respuesta**: Simula tiempo de pensamiento humano
- **Adaptabilidad**: Se ajusta a diferentes niveles de dificultad

### Algoritmos
- **Eliminación por características**: Basada en las respuestas a preguntas
- **Estrategia óptima**: Intenta minimizar el número de personajes restantes
- **Adivinanza final**: Evalúa cuándo es mejor adivinar vs seguir preguntando

## 🔄 Próximas Funcionalidades

### En Desarrollo
- [ ] **Modo Multijugador Bluetooth**: Conexión real entre dispositivos
- [ ] **Estadísticas de Juego**: Seguimiento de victorias y derrotas
- [ ] **Logros**: Sistema de logros y recompensas
- [ ] **Modo Torneos**: Competencias eliminatorias
- [ ] **Personalización**: Selección de sets de personajes

### Mejoras Planificadas
- [ ] **Animaciones mejoradas**: Transiciones más fluidas
- [ ] **Sonidos**: Efectos de sonido y música temática
- [ ] **Tutorial interactivo**: Guía paso a paso para nuevos jugadores
- [ ] **Modo offline**: Guardado de progreso sin conexión

## 🐛 Problemas Conocidos

- Los errores de compilación de Android requieren Java 17
- Algunas animaciones pueden ser lentas en dispositivos antiguos

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Por favor:
1. Fork el proyecto
2. Crea una rama para tu característica (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## 🎌 Créditos

- **Tema**: Attack on Titan (Shingeki no Kyojin) de Hajime Isayama
- **Desarrollo**: Proyecto educativo en Flutter
- **Datos de personajes**: Basados en el anime y manga oficial

---

¡Disfruta jugando y que gane el mejor estratega! 🎮⚔️