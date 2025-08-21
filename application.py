import tkinter as tk
from tkinter import ttk
import time

import ui_generics as ui
import ui_imageset as imageset_tab
import ui_video as video_tab
import ui_tagger as tagger_tab


class Application(tk.Tk):
    
    imageset_tab = None
    video_tab = None
    tag_editor_tab = None
    

    def __init__(self, geometry):
        super().__init__()
        self.geometry(geometry)
        self.title('Fast Batch Image Crop v1.1.0')
        self.init_ui()
        self.console.write_info('Application v1.1.0 init complete.')

    
    def init_ui(self):
        self.last_configure_time = time.time()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        # console
        self.console = ui.SingleLineConsole(self)
        self.console.grid(column=0, row=1, sticky='news')
        
        # tab widget
        tabs = ttk.Notebook(self)
        tabs.grid(column=0, row=0, sticky='news')
        
        # tabs
        self.imageset_tab = imageset_tab.ImagesetTab(self.console)
        self.video_tab = video_tab.VideoTab(self.console)
        self.tag_editor_tab = tagger_tab.TagEditorTab(self.console)
        
        tabs.add(self.imageset_tab, text='Image Set')
        tabs.add(self.video_tab, text='Video')
        tabs.add(self.tag_editor_tab, text='Tag Editor')
        
        self.bind('<Configure>', self.window_configure_callback)
        self.console.write_info('UI init done.')
    
        
    def window_configure_callback(self, event):
        self.imageset_tab.window_reconfigure(event)
        self.tag_editor_tab.window_reconfigure(event)
        

    