# Urban Routes – Automatización de Pruebas (Sprint 9)

Este proyecto contiene la automatización de pruebas funcionales para la aplicación web **Urban Routes**, desarrollada como parte del Sprint 9 del programa de QA Automation.

El objetivo del proyecto es validar el flujo completo de solicitud de un taxi utilizando Selenium y Pytest, simulando la interacción real de un usuario.

---

## 🧪 Flujo de prueba automatizado

La prueba principal cubre el siguiente escenario:

1. Configurar la dirección de origen y destino
2. Solicitar un taxi
3. Seleccionar la tarifa Comfort
4. Ingresar número de teléfono con validación por código
5. Agregar tarjeta de crédito
6. Escribir mensaje para el conductor
7. Solicitar manta y pañuelos
8. Agregar 2 cubetas de helado
9. Ordenar el taxi
10. Verificar que el pedido se genera correctamente

---

## 🛠 Tecnologías y herramientas utilizadas

- **Python 3.12**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver**
- **PyCharm**
- **Git & GitHub**

---

## 📁 Estructura del proyecto


sprint9/

│

├── data.py                  # Datos de prueba

├── utils.py                 # Funciones auxiliares

├── urban_routes_page.py     # Page Object Model (POM)

├── test_urban_routes.py     # Casos de prueba con Pytest

├── README.md                # Documentación del proyecto

└── .venv/                   # Entorno virtual



## Ejecucion

Instalar Pytest : ` pip install pytest `
Instalar Selenium : ` pip install selenium `
Validar pruebas: ` pytest `

