import PySimpleGUI as sg
from requests import Session

# Window theme set
sg.theme('DarkTeal9')

r = Session()

class layout_one:

    history = []

    def __init__(self):
        self.combo_style = {'size': (19,1)}
        self.items = ['Jne', 'Jnt', 'Shopee Express', 'Pos Indonesia', 'Sicepat', 'AnterAja', 'Ninja Express']

    def windows(self):
        lyt = [
            [sg.Text('Silahkan pilih kurir?', size=(50,1))],
            [sg.Combo(self.items, default_value='Courier', **self.combo_style, key='kurir', pad=(1,1))],
            [sg.Text(size=(1,1))],
            [sg.Text('Masukkan nomor resi', size=(16,1))],
            [sg.InputText(focus=True, key="resi")],
            [sg.Text(size=(1,1))],

            [sg.Button('submit'), sg.Button('cancel')]
        ]

        window = sg.Window('Resi Tracking', lyt)
        return window

    def getData(self):
        while True:
            event, values = self.windows().read()
            if event in (None, 'cancel'):
                break
                
            return values

    def getHTTPrequest(self):
        data = self.getData()
        try:
            kurir = data['kurir'].replace(" ","").lower()
            resi = data['resi']
            url = f'https://api.binderbyte.com/v1/track?api_key=6c0a34b42aee85de65197b0e12c0c613a77c06185d3b016ba508f3012e4a70e9&courier={kurir}&awb={resi}'
            s = r.get(url).json()
            for histori in s['data']['history']:
                self.history.append(histori['desc'])
            return self.history
        except TypeError:
            pass

show_window = layout_one()

class layout_two:

    def __init__(self):
        pass

    def lyt(self):
        layout = [
            [sg.Text('This Result', size=(20,1))],
            [sg.Listbox(values= show_window.getHTTPrequest(),
                    size = (80, 12),
                    key = '_LIST_',
                    enable_events = True)],
            
            [sg.Button('Oke')]
        ]

        window = sg.Window('Result', layout, resizable=True, finalize=True)
        window['_LIST_'].expand(expand_x=True, expand_y=True, expand_row=True)
        window.read()
        window.close()

show_window1 = layout_two()
show_window1.lyt()