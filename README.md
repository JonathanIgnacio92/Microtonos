# Simulador de Microtonos

Un simulador interactivo basado en consola desarrollado en Python. Este programa gestiona un banco de "microtonos" (frecuencias de audio virtuales) y permite la reproducción secuencial de tonos utilizando la API de sonido nativa de Windows. 

*(Nota: Como guiño oculto, la secuencia de frecuencias reproduce una melodía clásica de los videojuegos: ¡el tema de Star Wars!).*

## 🚀 Características

- **Gestión de Recursos:** Control de un límite máximo de 25 microtonos (libres, activos y asignados).
- **Reproducción Dinámica:** Utiliza arreglos cíclicos de frecuencias en Hertz (Hz) y duraciones en milisegundos (ms) para generar melodías articuladas.
- **Validación de Errores:** Control de excepciones (`ValueError`) ante entradas vacías o caracteres no numéricos.
- **Recuperación de Memoria/Sonido:** Capacidad de liberar microtonos activos para volver a utilizarlos desde el menú principal.

## 🛠️ Requisitos del Sistema

- **Sistema Operativo:** Microsoft Windows (requerido debido a la dependencia de la librería nativa `winsound`).
- **Lenguaje:** Python 3.6 o superior.
- **Librerías:** Ninguna externa (usa módulos nativos de la biblioteca estándar de Python: `winsound` y `time`).

## 💻 Estructura del Menú Principal

Al ejecutar el script, se presentará una interfaz de comandos con las siguientes opciones:

1. **Ver cuántos microtonos quedan libres:** Muestra el balance actual de microtonos disponibles de forma informativa.
2. **Activar microtonos:** Solicita la cantidad de microtonos a reproducir. Si el valor es válido y hay disponibilidad, genera la secuencia melódica.
3. **Recuperar microtonos:** Permite restar microtonos al contador de "activos" y devolverlos al pozo de "libres" para simular una liberación de canales o de ambiente sonoro.
4. **Monitorear el sonido actual:** Muestra el recuento instantáneo de microtonos activos que se encuentran "vibrando en el ambiente".
5. **Salir:** Finaliza el ciclo principal (`while`) y cierra el programa limpiamente.

## 📦 Instalación y Ejecución

1. Clona este repositorio o descarga el archivo fuente (ej. `simulador.py`).
2. Abre la consola de comandos de Windows (CMD o PowerShell) en la ruta del archivo.
3. Ejecuta el script con el siguiente comando:

```bash
python simulador.py
