"""Welcome to Reflex! This file outlines the steps to create a basic app."""

from turtle import width
import reflex as rx


class State(rx.State):
    # Lista de tareas (cada tarea es un diccionario)
    tareas: list[dict] = [
        {"texto": "Aprender Reflex", "completada": False},
        {"texto": "Construir PyTasks", "completada": False},
        {"texto": "Desplegar a producción", "completada": False},
    ]
    nueva_tarea: str = ""  # Texto del input

    def agregar_tarea(self):
        if self.nueva_tarea.strip():
            self.tareas.append(
                {"texto": self.nueva_tarea, "completada": False})
        self.nueva_tarea = ""  # Lipia el input

    def toggle_tarea(self, index: int):
        tarea = self.tareas[index]
        tarea["completada"] = not tarea["completada"]

    # 👇 NUEVO: handler manual para el input
    def set_nueva_tarea(self, value: str):
        self.nueva_tarea = value


def index() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("📋 PyTasks", size="8"),
            rx.text("Tu gestor de tareas full‑stack con Python puro"),

            # Formulario para añadir nueva tarea
            rx.hstack(
                rx.input(
                    placeholder="¿Qué necesitas hacer?",
                    value=State.nueva_tarea,
                    on_change=State.set_nueva_tarea,
                    width="300px",
                ),
                rx.button("Añadir", on_click=State.agregar_tarea),
                spacing="3",
            ),

            # Lista de tareas
            rx.vstack(
                rx.foreach(
                    State.tareas,
                    lambda tarea, i: rx.card(
                        rx.hstack(
                            rx.checkbox(
                                checked=tarea["completada"],
                                on_change=lambda: State.toggle_tarea(i),
                            ),
                            rx.text(
                                tarea["texto"],
                                text_decoration=rx.cond(
                                    tarea["completada"], "line-through", "none"),

                            ),
                            spacing="3",
                        ),
                        width="400px",
                    ),
                ),
                spacing="3",
            ),

            spacing="5",
            justify="center",
            min_height="85vh",
            align="center",
        ),
    )


app = rx.App()
app.add_page(index)
