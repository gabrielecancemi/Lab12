import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        for y in range(2015, 2019):
            self._view.ddyear.options.append(ft.dropdown.Option(y))

        nazioni = self._model.getNazioni()
        self._view.update_page()


    def handle_graph(self, e):
        pass



    def handle_volume(self, e):
        pass


    def handle_path(self, e):
        pass
