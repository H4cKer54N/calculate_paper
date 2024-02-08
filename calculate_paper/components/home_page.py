import reflex as rx

class StateHome(rx.State):
    mm_etiqueta: float = 0
    cantidad_etiquetas: float = 0
    margen_vertical: float = 0
    total_metros: str = 0

    def update_total(self):
        suma = float(self.mm_etiqueta) + float(self.margen_vertical)
        self.total_metros = (suma * float(self.cantidad_etiquetas)) / 1000
        self.total_metros = "{:,.2f}".format(self.total_metros)

    def on_mm_etiqueta_change(self, value: float):
        if value == "":
            value = 0
        self.mm_etiqueta = value
        self.update_total()

    def on_cantidad_etiquetas_change(self, value: int):
        if value == "":
            value = 0
        self.cantidad_etiquetas = value
        self.update_total()

    def on_margen_vertical_change(self, value: float):
        if value == "":
            value = 0
        self.margen_vertical = value
        self.update_total()

@rx.page(route="/", title="Calculador de metros de etiquetas", description="Calcula los metros de etiquetas")
def home() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.heading("Calculador de metros de etiquetas", size="lg", weight="bold", align="center",
                       mx="20px",  justify_content="center"),
            rx.button(
                rx.icon(tag="moon"),
                on_click=rx.toggle_color_mode,
            ),
            mt="100px", 
            my="3em",
            mx="2em"
        ),
        rx.vstack(
            rx.text("Ingresa milimetros de etiqueta"),
            rx.number_input(type="number", default_value=0, on_change=StateHome.on_mm_etiqueta_change,
                            value=StateHome.mm_etiqueta, placeholder="mm."),
            rx.text("Ingresa cantidad de etiquetas"),
            rx.number_input(type="number", default_value=0, on_change=StateHome.on_cantidad_etiquetas_change,
                            value=StateHome.cantidad_etiquetas, placeholder="Cantidad"),
            rx.text("Ingresa un margen vertical en milimetros"),
            rx.number_input(type="number", default_value=0, on_change=StateHome.on_margen_vertical_change,
                            value=StateHome.margen_vertical, placeholder="Cantidad"),
            rx.divider(mt="20px"),
            rx.text("Total"),
            rx.code(rx.hstack(
                    rx.heading(StateHome.total_metros, size="md"),
                    rx.heading("Metros", size="md"),),
                    px="10px",
                    py="5px",
                    ),
        ),
        h="100%"
    )
