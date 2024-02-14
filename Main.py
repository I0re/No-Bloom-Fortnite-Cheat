# Source Generated with Decompyle++
# File: ilusity.pyc (Python 3.7)

from ttkbootstrap import Style
from functionalities import Functionalities, default_profile
from time import sleep
from threading import Thread
from random import randint
import win32con
import psutil
import ctypes
import win32api
import os
import webbrowser
import keyboard
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
user32 = ctypes.windll.user32
functions = Functionalities()
hidden = False
recoil_bool = False
randomizer_bool = True
rapidfire_bool = False
value = 0
data = functions.get_config('config', 'config', 'settings')
activation_type_config = data['activation_type']
switch_gun_config = data['switch_gun_key']
switch_modeup_config = data['switch_mode_up']
switch_modedown_config = data['switch_mode_down']
fire_rate_config = data['fire_rate']
interval_config = data['interval']
list_of_profiles = list(functions.profiles)
current_profile = list_of_profiles[0]
list_of_guns = list(functions.get_config(current_profile, 'guns'))
current_gun = list_of_guns[0]
list_of_modes = (lambda .0: [ item for item in .0 if item not in ('key', 'random') ])(functions.get_config(current_profile, 'guns', current_gun))
current_mode = list_of_modes[0]
current_key = functions.get_config(current_profile, 'guns', current_gun)['key']
autocrouch_bool = False
USUAL_FONT = 'Helvetica'
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def Ilusity():
    '''Ilusity'''
    
    def __init__(self):
        tk.Tk.__init__(self)
        Thread.__init__(self)
        self.title('Ilusity')
        self.current_tab = 'recoil'
        self.iconbitmap('ilusityv09.ico')
        self.attributes('-alpha', 0.9)
        self.resizable(False, False)
        self.attributes('-topmost', True)
        style = Style('cyborg', **('theme',))
        style.configure('custom.TFrame', 'black', **('background',))
        self.options_frame_create()
        self.recoil_tab_create()
        self.grid_remove_all(False)
        self.protocol('WM_DELETE_WINDOW', self.on_closing)

    
    def on_closing():
        if tk.messagebox.askokcancel('Quit', 'Do you want to quit?'):
            root.destroy()
            current_system_pid = os.getpid()
            this_system = psutil.Process(current_system_pid)
            this_system.terminate()

    on_closing = staticmethod(on_closing)
    
    def grid_remove_all(self, all = (True,)):
        if all:
            
            try:
                self.recoil_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err


            
            try:
                self.about_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err


            
            try:
                self.profiles_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err


            
            try:
                self.settings_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err


            
            try:
                self.edit_profiles_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err


        else:
            
            try:
                self.about_tab.grid_remove()
            except Exception:
                err = None
                
                try:
                    pass
                finally:
                    err = None
                    del err



    
    def check_options_pressed(self, btn):
        self.grid_remove_all(True)
        if hidden:
            return None
        if None == 'recoil':
            self.recoil_tab_create()
            self.current_tab = 'recoil'
        elif btn == 'about':
            self.about_tab_create()
            self.current_tab = 'about'
        elif btn == 'profile':
            self.profiles_tab_create()
            self.current_tab = 'profiles'
        elif btn == 'settings':
            self.settings_tab_create()
            self.current_tab = 'settings'

    
    def options_frame_create(self):
        self.options_frame = ttk.Frame(self)
        self.options_frame.grid(0, 0, 1, 'NW', 3, **('row', 'column', 'pady', 'sticky', 'rowspan'))
        recoil_button = None(None, None, None, None, None, (lambda btn = None: self.check_options_pressed(btn)), **('text', 'height', 'width', 'font', 'command'))
        extra_button = None(None, None, None, None, None, (lambda btn = None: self.check_options_pressed(btn)), **('text', 'height', 'width', 'font', 'command'))
        settings_button = None(None, None, None, None, None, (lambda btn = None: self.check_options_pressed(btn)), **('text', 'height', 'width', 'font', 'command'))
        profile_button = None(None, None, None, None, None, (lambda btn = None: self.check_options_pressed(btn)), **('text', 'height', 'width', 'font', 'command'))
        about_button = None(None, None, None, None, None, (lambda btn = None: self.check_options_pressed(btn)), **('text', 'height', 'width', 'font', 'command'))
        buttons = [
            recoil_button,
            extra_button,
            settings_button,
            profile_button,
            about_button]
        recoil_button.grid(0, 0, **('row', 'column'))
        profile_button.grid(1, 0, **('row', 'column'))
        extra_button.grid(2, 0, **('row', 'column'))
        settings_button.grid(3, 0, **('row', 'column'))
        about_button.grid(4, 0, **('row', 'column'))

    
    def about_tab_create(self):
        self.current_tab = 'about'
        
        def callback(url):
            webbrowser.open_new(url)

        self.about_tab = ttk.Frame(self)
        self.about_tab.grid(0, 1, 2, 1, 'NW', **('row', 'column', 'columnspan', 'pady', 'sticky'))
        discord_text = '\n        💬   Discord: \n        '
        youtube_text = '\n        📹   Youtube\n        '
        thankyou_text = '\n        Thank you for using Ilusity, your help throughout\n        the years has helped me develop this software!\n        <3\n        '
        about_label = ttk.Label(self.about_tab, 'Ilusity V0.9', (USUAL_FONT, 18), **('text', 'font'))
        about_label.grid(0, 0, 4, **('row', 'column', 'columnspan'))
        discord_label = ttk.Label(self.about_tab, discord_text, (USUAL_FONT, 10), **('text', 'font'))
        discord_label.grid(1, 0, **('row', 'column'))
        None(None, (lambda e = None: callback('https://discord.gg/Yc2qUEfNny')))
        youtube_label = ttk.Label(self.about_tab, youtube_text, (USUAL_FONT, 10), **('text', 'font'))
        youtube_label.grid(1, 1, **('row', 'column'))
        None(None, (lambda e = None: callback('https://www.youtube.com/channel/UCklvRhP73E0jlO77AfeqeXw')))
        thankyou_label = ttk.Label(self.about_tab, thankyou_text, (USUAL_FONT, 10), **('text', 'font'))
        thankyou_label.grid(1, 4, **('row', 'column'))
        None(None, (lambda e = None: callback('https://paypal.me/kriptaep')))
        separator_vert = ttk.Separator(self.about_tab, 'vertical', **('orient',)).grid(1, 3, 3, 5, **('row', 'column', 'rowspan', 'padx'))

    
    def settings_tab_create(self):
        self.current_tab = 'settings'
        self.settings_tab = ttk.Frame(self)
        self.settings_tab.grid(0, 1, 2, 1, 'NW', **('row', 'column', 'columnspan', 'pady', 'sticky'))
        
        def check_activation(var):
            print(var.get())

        
        def save_values(event = None):
            global switch_gun_config, switch_modeup_config, switch_modedown_config, fire_rate_config, interval_config, activation_type_config
            
            try:
                switch_gun_config = str(self.switch_gun_entry.get())
                switch_modeup_config = str(self.switch_mode_up.get())
                switch_modedown_config = str(self.switch_mode_down.get())
                fire_rate_config = int(self.firerate_entry.get())
                interval_config = float(self.delay_interval_entry.get())
            except Exception:
                err = None
                
                try:
                    self.settings_status_label.configure('Status: Error,\n please check values!', **('text',))
                finally:
                    err = None
                    del err


            self.settings_status_label.configure('Status: Saving...', **('text',))
            if self.activation_type_combo.get() == 'left mouse':
                new_activation_type = 0
            elif self.activation_type_combo.get() == 'right mouse':
                new_activation_type = 1
            elif self.activation_type_combo.get() == 'left and right mouse':
                new_activation_type = 2
            functions.set_config('config', 'config', 'settings', 'activation_type', new_activation_type)
            functions.close('config.json')
            activation_type_config = new_activation_type
            functions.set_config('config', 'config', 'settings', 'interval', float(self.delay_interval_entry.get()))
            functions.close('config.json')
            functions.set_config('config', 'config', 'settings', 'fire_rate', int(self.firerate_entry.get()))
            functions.close('config.json')
            functions.set_config('config', 'config', 'settings', 'switch_gun_key', str(self.switch_gun_entry.get()))
            functions.close('config.json')
            functions.set_config('config', 'config', 'settings', 'switch_mode_up', str(self.switch_mode_up.get()))
            functions.close('config.json')
            functions.set_config('config', 'config', 'settings', 'switch_mode_down', str(self.switch_mode_down.get()))
            functions.close('config.json')
            self.settings_status_label.configure('Status: Saved!', **('text',))

        config_data = functions.get_config('config')['config']
        activation_type = config_data['settings']['activation_type']
        interval_ms = config_data['settings']['interval']
        fire_rate = config_data['settings']['fire_rate']
        switch_gun_key = config_data['settings']['switch_gun_key']
        switch_mode_up = config_data['settings']['switch_mode_up']
        switch_mode_down = config_data['settings']['switch_mode_down']
        settings_title = ttk.Label(self.settings_tab, 'Settings Tab', (USUAL_FONT, 18), **('text', 'font')).grid(0, 0, 'W', **('row', 'column', 'sticky'))
        separator_hoz1 = ttk.Separator(self.settings_tab, 'horizontal', **('orient',)).grid(1, 0, 5, 1, **('row', 'column', 'padx', 'pady'))
        activation_label = ttk.Label(self.settings_tab, 'Activation type:', (USUAL_FONT, 12), **('text', 'font')).grid(2, 0, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.activation_type_var = tk.StringVar()
        self.activation_type_combo = ttk.Combobox(self.settings_tab, self.activation_type_var, 12, 1, 'enabled', [
            'left mouse',
            'right mouse',
            'left and right mouse'], **('textvariable', 'width', 'height', 'state', 'values'))
        self.activation_type_combo.set([
            'left mouse',
            'right mouse',
            'left and right mouse'][activation_type])
        self.activation_type_combo.grid(2, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        firerate_entry_var = fire_rate
        firerate_label = ttk.Label(self.settings_tab, 'Fire rate:', (USUAL_FONT, 12), **('text', 'font')).grid(3, 0, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.firerate_entry = ttk.Entry(self.settings_tab, 12, firerate_entry_var, **('width', 'textvariable'))
        delay_interval_var = interval_ms
        delay_interval_label = ttk.Label(self.settings_tab, 'Interval(ms):', (USUAL_FONT, 12), **('text', 'font')).grid(4, 0, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.delay_interval_entry = ttk.Entry(self.settings_tab, 12, delay_interval_var, **('width', 'textvariable'))
        switch_guns_label = ttk.Label(self.settings_tab, 'Gun Switch Key:', (USUAL_FONT, 12), **('text', 'font')).grid(5, 0, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.switch_gun_entry = ttk.Entry(self.settings_tab, 12, switch_gun_key, **('width', 'textvariable'))
        self.switch_gun_entry.grid(5, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        switch_modeup_label = ttk.Label(self.settings_tab, 'Mode Up switch:', (USUAL_FONT, 12), **('text', 'font')).grid(6, 0, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.switch_mode_up = ttk.Entry(self.settings_tab, 12, switch_mode_up, **('width', 'textvariable'))
        self.switch_mode_up.grid(6, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        switch_modedown_label = ttk.Label(self.settings_tab, 'Mode Down switch:', (USUAL_FONT, 12), **('text', 'font')).grid(7, 0, 1, 1, **('row', 'column', 'padx', 'pady'))
        self.switch_mode_down = ttk.Entry(self.settings_tab, 12, **('width',))
        self.switch_mode_down.grid(7, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        separator_vert1 = ttk.Separator(self.settings_tab, 'vertical', **('orient',)).grid(1, 2, 5, 1, 3, **('row', 'column', 'padx', 'pady', 'rowspan'))
        self.firerate_entry.delete(0, '')
        self.firerate_entry.insert(tk.END, fire_rate)
        self.delay_interval_entry.delete(0, '')
        self.delay_interval_entry.insert(tk.END, interval_ms)
        self.switch_gun_entry.delete(0, '')
        self.switch_gun_entry.insert(tk.END, switch_gun_key)
        self.switch_mode_up.delete(0, '')
        self.switch_mode_up.insert(tk.END, switch_mode_up)
        self.switch_mode_down.insert(0, '')
        self.switch_mode_down.insert(tk.END, switch_mode_down)
        self.delay_interval_entry.grid(4, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        self.firerate_entry.grid(3, 1, 1, 1, 'W', **('row', 'column', 'padx', 'pady', 'sticky'))
        
        def reset_values():
            self.firerate_entry.delete(0, '')
            self.firerate_entry.insert(tk.END, fire_rate)
            self.delay_interval_entry.delete(0, '')
            self.delay_interval_entry.insert(tk.END, interval_ms)
            self.switch_mode_up.delete(0, '')
            self.switch_mode_up.insert(tk.END, switch_mode_up)
            self.switch_mode_down.delete(0, '')
            self.switch_mode_down.insert(tk.END, switch_mode_down)
            self.switch_gun_entry.delete(0, '')
            self.switch_gun_entry.insert(tk.END, switch_gun_key)

        save_button = ttk.Button(self.settings_tab, 'Save', save_values, **('text', 'command'))
        save_button.grid(2, 3, 'W', 1, 1, **('row', 'column', 'sticky', 'padx', 'pady'))
        reset_button = ttk.Button(self.settings_tab, 'Reset', reset_values, **('text', 'command'))
        reset_button.grid(3, 3, 'W', 1, 1, **('row', 'column', 'sticky', 'padx', 'pady'))
        self.settings_status_label = ttk.Label(self.settings_tab, 'Status: -', **('text',))
        self.settings_status_label.grid(4, 3, 'W', 1, 2, **('row', 'column', 'sticky', 'padx', 'pady'))
        warning_label = ttk.Label(self.settings_tab, 'Modifying any values here could result in instability!', (USUAL_FONT, 8), **('text', 'font')).grid(9, 0, 2, 5, 'W', **('row', 'column', 'columnspan', 'pady', 'sticky'))

    
    def get_curr_attr(self, curr_profile, curr_gun_input = (None,)):
        global current_profile, list_of_guns, current_gun, current_gun, list_of_modes, current_mode
        functions.check_if_exists()
        current_profile = curr_profile
        list_of_guns = list(functions.get_config(curr_profile, 'guns'))
        print(list_of_guns)
        print(curr_gun_input)
        if curr_gun_input == None:
            current_gun = list_of_guns[0]
        else:
            current_gun = curr_gun_input
        list_of_modes = (lambda .0: [ item for item in .0 if item not in ('key', 'random') ])(functions.get_config(curr_profile, 'guns', current_gun))
        current_mode = list_of_modes[0]

    
    def edit_profiles_create(self, curr_profile):
        '''
        Profile Editor
        -> Allow user to create, remove or edit modes
        -> Allow user to create, remove or edit guns
        :return None

        '''
        
        def add_config():
            global current_gun, current_mode
            if self.current_edit == 'guns':
                new_gun = self.edit_guns_select.get()
                if new_gun in list_of_guns:
                    self.label_edit_status['text'] = f'''Gun: {new_gun} already exists!'''
                else:
                    functions.set_config(current_profile, 'guns', new_gun, {
                        'basic': [
                            1,
                            2,
                            3,
                            4,
                            5],
                        'key': 'x' })
                    functions.close(current_profile)
                    self.edit_profiles_create(curr_profile)
                    self.label_edit_status['text'] = f'''Gun: {new_gun} added!'''
                    current_gun = new_gun
            elif self.current_edit == 'modes':
                new_mode = self.edit_mode_select.get()
                if new_mode in list_of_modes:
                    self.label_edit_status['text'] = f'''Mode: {new_mode} -> {current_gun}already exists!'''
                else:
                    functions.set_config(current_profile, 'guns', current_gun, new_mode, [
                        1,
                        2,
                        3,
                        4,
                        5])
                    functions.close(current_profile)
                    self.edit_profiles_create(curr_profile)
                    self.label_edit_status['text'] = f'''Mode: {new_mode} -> {current_gun} added!'''
                    current_mode = new_mode
            elif self.current_edit == 'values':
                new_values = self.edit_values_entry.get()
                
                try:
                    new_values = (lambda .0: [ int(i) for i in .0 ])(self.edit_values_entry.get().split())
                except Exception:
                    self.label_edit_status['text'] = 'Failed, please input like: 0 1 2 3 4'

                functions.set_config(current_profile, 'guns', current_gun, current_mode, new_values)
                functions.close(current_profile)
                self.label_edit_status['text'] = f'''Values changed for: {current_mode} -> {current_gun}!'''

        
        def del_config():
            if self.current_edit == 'guns':
                remove_gun = self.edit_guns_select.get()
                if remove_gun not in list_of_guns:
                    self.label_edit_status['text'] = f'''Gun: {remove_gun} not in config!'''
                else:
                    output_return = functions.delete_config(current_profile, 'guns', remove_gun)
                    if output_return:
                        self.label_edit_status['text'] = f'''Gun: {remove_gun} removed!'''
                        functions.close(current_profile)
                    elif output_return == None:
                        self.label_edit_status['text'] = f'''Failed on removing: {remove_gun}!'''
                    elif output_return == False:
                        self.label_edit_status['text'] = 'Critical error, try again!'
                    elif self.current_edit == 'modes':
                        remove_mode = self.edit_mode_select.get()
                        if remove_mode not in list_of_modes:
                            self.label_edit_status['text'] = f'''Mode: {remove_mode} -> {current_gun} not in config!'''
                        else:
                            output_return = functions.delete_config(current_profile, 'guns', current_gun, remove_mode)
                            if output_return:
                                self.label_edit_status['text'] = f'''Mode: {remove_mode} -> {current_gun} removed!'''
                                functions.close(current_profile)
                            elif output_return == None:
                                self.label_edit_status['text'] = f'''Failed on removing: {remove_mode}!'''
                            elif output_return == False:
                                self.label_edit_status['text'] = 'Critical error, try again!'

        
        def reset_config():
            self.edit_profiles_create(current_profile)

        
        def disable_mode_select(event = None):
            self.edit_mode_select['state'] = 'disabled'
            self.current_edit = 'values'
            self.label_edit_status['text'] = f'''Currently editing: {self.current_edit}'''
            list_of_values = list(functions.get_config(current_profile, 'guns', current_gun, current_mode))
            lbl_values = ttk.Label(self.edit_profiles_tab, 'Values:', (USUAL_FONT, 14), **('text', 'font')).grid(5, 0, 'NW', 2, 2, **('row', 'column', 'sticky', 'padx', 'pady'))
            gun_value_input = tk.StringVar()
            self.edit_values_entry = tk.Entry(self.edit_profiles_tab, len(list_of_values) + 6, gun_value_input, **('width', 'textvariable'))
            self.edit_values_entry.insert(tk.END, list_of_values)
            self.edit_values_entry.grid(5, 1, 2, 'NW', **('row', 'column', 'padx', 'sticky'))
            btn_add_edit['text'] = 'Save'
            btn_del_edit['state'] = 'disabled'

        
        def disable_gun_select(event = None):
            global current_gun
            self.edit_guns_select['state'] = 'disabled'
            self.current_edit = 'modes'
            self.label_edit_status['text'] = f'''Currently editing: {self.current_edit}'''
            current_gun = event.widget.get()
            self.get_curr_attr(current_profile, current_gun)
            print('446', current_gun, list_of_modes)
            lbl_modes = ttk.Label(self.edit_profiles_tab, 'Modes:', (USUAL_FONT, 14), **('text', 'font')).grid(4, 0, 'NW', 2, 2, **('row', 'column', 'sticky', 'padx', 'pady'))
            self.edit_mode_select = ttk.Combobox(self.edit_profiles_tab, list_of_modes, 10, 6, **('values', 'width', 'height'))
            self.edit_mode_select.grid(4, 1, 'NW', 2, **('row', 'column', 'sticky', 'padx'))
            self.edit_mode_select.bind('<<ComboboxSelected>>', disable_mode_select)

        self.current_edit = 'guns'
        self.grid_remove_all(True)
        self.get_curr_attr(curr_profile)
        self.edit_profiles_tab = ttk.Frame(self)
        self.edit_profiles_tab.grid(0, 1, 'NW', **('row', 'column', 'sticky'))
        edit_profiles_label = ttk.Label(self.edit_profiles_tab, 'Profile Editor', (USUAL_FONT, 18), **('text', 'font'))
        edit_profiles_label.grid(0, 0, 6, 'W', 2, **('row', 'column', 'columnspan', 'sticky', 'padx'))
        sep_hoz1 = ttk.Separator(self.edit_profiles_tab, 'horizontal', **('orient',)).grid(1, 6, 'W', 2, **('row', 'columnspan', 'sticky', 'padx'))
        selected_profile_label = ttk.Label(self.edit_profiles_tab, f'''Selected profile: {current_profile[:-5]}''', '#2494d4', (USUAL_FONT, 10), **('text', 'foreground', 'font'))
        selected_profile_label.grid(2, 0, 6, 'W', **('row', 'column', 'columnspan', 'sticky'))
        sep_vert1 = ttk.Separator(self.edit_profiles_tab, 'vertical', **('orient',)).grid(3, 6, 2, 5, 5, 'NW', **('row', 'rowspan', 'column', 'padx', 'pady', 'sticky'))
        lbl_guns = ttk.Label(self.edit_profiles_tab, 'Guns:', (USUAL_FONT, 14), **('text', 'font')).grid(3, 0, 'NW', 2, 2, **('row', 'column', 'sticky', 'padx', 'pady'))
        self.edit_guns_select = ttk.Combobox(self.edit_profiles_tab, list_of_guns, 10, 6, **('values', 'width', 'height'))
        self.edit_guns_select.grid(3, 1, 'NW', 2, **('row', 'column', 'sticky', 'padx'))
        self.edit_guns_select.bind('<<ComboboxSelected>>', disable_gun_select)
        btn_add_edit = ttk.Button(self.edit_profiles_tab, 'Add', 5, add_config, **('text', 'width', 'command'))
        btn_add_edit.grid(3, 3, 1, **('row', 'column', 'padx'))
        btn_del_edit = ttk.Button(self.edit_profiles_tab, 'Del', 5, del_config, **('text', 'width', 'command'))
        btn_del_edit.grid(4, 3, 1, **('row', 'column', 'padx'))
        btn_reset_edit = ttk.Button(self.edit_profiles_tab, 'Reset', 5, reset_config, **('text', 'width', 'command'))
        btn_reset_edit.grid(5, 3, 1, **('row', 'column', 'pady'))
        self.label_edit_status = ttk.Label(self.edit_profiles_tab, f'''Currently editing: {self.current_edit}''', (USUAL_FONT, 10), **('text', 'font'))
        self.label_edit_status.grid(7, 0, 3, 2, 2, 'SW', **('row', 'column', 'columnspan', 'padx', 'pady', 'sticky'))

    
    def profiles_tab_create(self):
        self.profiles_tab = ttk.Frame(self)
        self.profiles_tab.grid(0, 1, 'NW', **('row', 'column', 'sticky'))
        self.current_profile = 'profiles'
        profile_label = ttk.Label(self.profiles_tab, 'Profiles Tab', (USUAL_FONT, 18), **('text', 'font'))
        profile_label.grid(0, 0, 2, 'W', **('row', 'column', 'columnspan', 'sticky'))
        separator_vert1 = ttk.Separator(self.profiles_tab, 'horizontal', **('orient',)).grid(1, 0, 2, 5, 5, **('row', 'column', 'columnspan', 'padx', 'pady'))
        profiles = self.retrieve_profile()
        
        def delete_profile():
            global current_profile, current_profile, list_of_guns, current_gun, list_of_modes, current_mode
            if self.select_profile.get() in functions.get_profiles():
                data = functions.delete_profile(self.select_profile.get())
                if data == True:
                    functions.check_if_exists()
                    current_profile = functions.get_profiles()[0]
                    self.status_profile_label['text'] = f'''Success! {self.select_profile.get()} deleted!'''
                else:
                    self.status_profile_label['text'] = 'Error, please delete it manually.'
            else:
                self.status_profile_label['text'] = 'Profile not found!'
            functions.check_if_exists()
            current_profile = functions.get_profiles()[0]
            list_of_guns = list(functions.get_config(current_profile, 'guns'))
            current_gun = list_of_guns[0]
            list_of_modes = (lambda .0: [ item for item in .0 if item not in ('key', 'random') ])(functions.get_config(current_profile, 'guns', current_gun))
            current_mode = list_of_modes[0]

        
        def load_profile(event = None):
            global current_profile, list_of_guns, current_gun, list_of_modes
            data = self.retrieve_profile(event.widget.get())
            if data:
                if 'guns' in data.keys():
                    pass
                else:
                    return None
                current_profile = None.widget.get()
                list_of_guns = list(functions.get_config(current_profile, 'guns'))
                current_gun = list_of_guns[0]
                list_of_modes = (lambda .0: [ item for item in .0 if item not in ('key', 'random') ])(functions.get_config(current_profile, 'guns', current_gun))
                current_mode = list_of_modes[0]

        
        def create_profile():
            if self.selected_profile_var.get() in functions.get_profiles():
                self.status_profile_label['text'] = 'Status: Error, profile exists'
            else:
                self.status_profile_label['text'] = 'Status: Creating profile!'
                if '.json' in self.selected_profile_var.get():
                    file_name = self.selected_profile_var.get()
                else:
                    file_name = self.selected_profile_var.get() + '.json'
                if functions.create_profile(default_profile, file_name):
                    self.status_profile_label['text'] = 'Status: Profile created!'
                else:
                    self.status_profile_label['text'] = 'Status: Unknown Error'
                functions.check_if_exists()
                self.select_profile['values'] = functions.get_profiles()

        
        def edit_profile():
            if self.select_profile.get() in functions.get_profiles():
                self.edit_profiles_create(self.select_profile.get())

        choose_profile = ttk.Label(self.profiles_tab, 'Profile:', (USUAL_FONT, 14), **('text', 'font')).grid(2, 0, 'W', **('row', 'column', 'sticky'))
        self.selected_profile_var = tk.StringVar()
        self.select_profile = ttk.Combobox(self.profiles_tab, self.selected_profile_var, 12, 4, 'enabled', self.retrieve_profile(), **('textvariable', 'width', 'height', 'state', 'values'))
        self.select_profile.bind('<<ComboboxSelected>>', load_profile)
        self.select_profile.grid(2, 1, 'W', **('row', 'column', 'sticky'))
        self.select_profile.insert(tk.END, current_profile)
        self.status_profile_label = ttk.Label(self.profiles_tab, 'Status: 🗘 Waiting', (USUAL_FONT, 12), **('text', 'font'))
        self.status_profile_label.grid(8, 0, 5, 1, 1, 'W', **('row', 'column', 'columnspan', 'padx', 'pady', 'sticky'))
        separator_hoz = ttk.Separator(self.profiles_tab, 'horizontal', **('orient',)).grid(3, 0, 2, 'N', 5, **('row', 'column', 'columnspan', 'sticky', 'pady'))
        separator_vert = ttk.Separator(self.profiles_tab, 'vertical', **('orient',)).grid(3, 2, 3, 3, 'N', **('row', 'column', 'padx', 'rowspan', 'sticky'))
        button_create = ttk.Button(self.profiles_tab, '➕', create_profile, **('text', 'command'))
        button_create.grid(2, 3, 'W', 2, 1, **('row', 'column', 'sticky', 'padx', 'pady'))
        button_delete = ttk.Button(self.profiles_tab, '➖', delete_profile, **('text', 'command'))
        button_delete.grid(3, 3, 'W', 2, 2, **('row', 'column', 'sticky', 'padx', 'pady'))
        button_settings = ttk.Button(self.profiles_tab, '⚙️', edit_profile, **('text', 'command'))
        button_settings.grid(4, 3, 'W', 2, 1, **('row', 'column', 'sticky', 'padx', 'pady'))

    
    def extra_tab_create(self):
        pass

    
    def recoil_extension_tab(self):
        '''
                Settings Options:
                - Select weapon
                - Select Mode
                - Able to change each value: input
                    > Show in a textbox
                    > Save into a local directory
                - Save button, write to the config file
                - Reset to original values from file
                '''
        profile_label = ttk.Label(self.recoil_tab, 'Profile', (USUAL_FONT, 18), **('text', 'font'))
        profile_label.grid(0, 0, 2, 'W', 5, **('row', 'column', 'columnspan', 'sticky', 'pady'))
        profile_gun_label = ttk.Label(self.recoil_tab, 'Select Gun:', (USUAL_FONT, 11), **('text', 'font'))
        profile_gun_label.grid(1, 0, 'W', **('row', 'column', 'sticky'))
        profile_gun_selected_var = tk.StringVar()
        profile_gun_select = ttk.Combobox(self.recoil_tab, profile_gun_selected_var, 'readonly', list_of_guns, 6, 1, **('textvariable', 'state', 'values', 'width', 'height'))
        profile_gun_select.grid(1, 1, **('row', 'column'))
        profile_mode_label = ttk.Label(self.recoil_tab, 'Select Mode:', (USUAL_FONT, 11), **('text', 'font'))
        profile_mode_label.grid(2, 0, 'W', 5, **('row', 'column', 'sticky', 'pady'))
        profile_mode_selected_var = tk.StringVar()
        profile_mode_select = ttk.Combobox(self.recoil_tab, profile_mode_selected_var, 'readonly', list_of_modes, 6, 1, **('textvariable', 'state', 'values', 'width', 'height'))
        profile_mode_select['state'] = 'disabled'
        profile_mode_select.grid(2, 1, **('row', 'column'))
        separator_vert1 = ttk.Separator(self.recoil_tab, 'vertical', **('orient',)).grid(1, 3, 4, 2, **('row', 'column', 'rowspan', 'padx'))
        
        def generate_attributes():
            profile_gun_label = ttk.Label(self.recoil_tab, 'Gun attributes', (USUAL_FONT, 14), **('text', 'font'))
            profile_gun_label.grid(0, 4, 2, 5, 10, 'E', **('row', 'column', 'columnspan', 'padx', 'pady', 'sticky'))
            gun_key_input = tk.StringVar()
            gun_key_label = ttk.Label(self.recoil_tab, 'Gun Keybind:', (USUAL_FONT, 11), **('text', 'font'))
            self.gun_key_entry = tk.Entry(self.recoil_tab, 4, gun_key_input, **('width', 'textvariable'))
            if self.gun_attributes['key']:
                self.gun_key_entry.insert(tk.END, self.gun_attributes['key'])
            gun_key_label.grid(2, 4, 2, 'W', **('row', 'column', 'padx', 'sticky'))
            self.gun_key_entry.grid(2, 5, 1, 'E', **('row', 'column', 'padx', 'sticky'))
            
            def profile_save():
                self.gun_attributes[current_mode] = (lambda .0: [ int(i) for i in .0 ])(self.gun_values_entry.get().split())
                self.gun_attributes['key'] = self.gun_key_entry.get()
                functions.set_config(current_profile, 'guns', current_gun, self.gun_attributes)
                functions.close(current_profile)
                status_profile['text'] = 'Status: Saved'

            
            def profiles_reset():
                self.gun_attributes = { }

            separator_vert2 = ttk.Separator(self.recoil_tab, 'vertical', **('orient',)).grid(1, 6, 4, 2, **('row', 'column', 'rowspan', 'padx'))
            gun_values_label = ttk.Label(self.recoil_tab, 'Values:', (USUAL_FONT, 11), **('text', 'font')).grid(1, 4, 10, 'W', **('row', 'column', 'padx', 'sticky'))
            gun_value_input = tk.StringVar()
            self.gun_values_entry = tk.Entry(self.recoil_tab, len(self.gun_attributes[current_mode]) + 10, gun_value_input, **('width', 'textvariable'))
            self.gun_values_entry.insert(tk.END, self.gun_attributes[current_mode])
            self.gun_values_entry.grid(1, 5, 2, 'W', **('row', 'column', 'padx', 'sticky'))
            status_profile = ttk.Label(self.recoil_tab, 'Status: Waiting', (USUAL_FONT, 12), **('text', 'font'))
            status_profile.grid(0, 8, **('row', 'column'))
            save_profile_btn = tk.Button(self.recoil_tab, 'Save', 1, 16, ('Segoe UI', 9), profile_save, **('text', 'height', 'width', 'font', 'command'))
            save_profile_btn.grid(2, 8, 'W', **('row', 'column', 'sticky'))
            reset_profile_btn = tk.Button(self.recoil_tab, 'Reset', 1, 16, ('Segoe UI', 9), self.recoil_tab_create, **('text', 'height', 'width', 'font', 'command'))
            reset_profile_btn.grid(1, 8, 'W', **('row', 'column', 'sticky'))

        
        def check_random_var(var = None):
            if var.get():
                self.gun_attributes['random'] = 1
            else:
                self.gun_attributes['random'] = 0

        
        def get_selected_gun(event = None):
            global current_gun, current_gun
            if event:
                current_gun = event.widget.get()
                if current_gun in list(functions.get_config('recoil', 'guns')):
                    current_gun = profile_gun_selected_var.get()
                    profile_mode_select.configure('readonly', **('state',))
                    profile_gun_select.configure('disabled', **('state',))
                    self.gun_attributes = functions.get_config('recoil', 'guns', current_gun)

        
        def get_selected_mode(event = None):
            global current_mode
            if event:
                current_mode = event.widget.get()
                list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config('recoil', 'guns', self.selected_gun_var.get()).keys()))
                if current_mode in list_of_modes:
                    profile_gun_select.configure('disabled', **('state',))
                    profile_mode_select.configure('disabled', **('state',))
                    generate_attributes()

        profile_gun_select.bind('<<ComboboxSelected>>', get_selected_gun)
        profile_mode_select.bind('<<ComboboxSelected>>', get_selected_mode)

    
    def retrieve_profile(self, profile = (None,)):
        if profile is None:
            return functions.get_profiles()
        return None.get_profiles(profile)

    
    def recoil_tab_create(self):
        '''
        Creates the recoil frame

        To do #
        + Add more stuff!


        :return:
        '''
        self.current_tab = 'recoil'
        self.recoil_tab = ttk.Frame(self)
        self.recoil_tab.grid(0, 1, 1, 'NW', **('row', 'column', 'pady', 'sticky'))
        
        def check_recoil_var(recoil_var = None):
            global current_gun, list_of_modes, current_mode, list_of_modes, current_gun, list_of_modes, current_gun, recoil_bool, recoil_bool
            if self.selected_gun_var.get() == '':
                self.selected_gun_var.set(list(functions.get_config(current_profile, 'guns'))[0])
                current_gun = list(functions.get_config(current_profile, 'guns'))[0]
                list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config(current_profile, 'guns', self.selected_gun_var.get()).keys()))
                self.select_mode['values'] = (lambda .0: [ mode for mode in .0 ])(list_of_modes)
                self.select_mode.set(list_of_modes[0])
                current_mode = list_of_modes[0]
            elif self.selected_gun_var.get() in list(functions.get_config(current_profile, 'guns')):
                list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config(current_profile, 'guns', self.selected_gun_var.get()).keys()))
                current_gun = self.selected_gun_var.get()
            else:
                list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config(current_profile, 'guns', self.selected_gun_var.get()).keys()))
                current_gun = list(functions.get_config(current_profile, 'guns'))[0]
                self.selected_gun_var.set(list(functions.get_config(current_profile, 'guns'))[0])
            if recoil_var.get():
                recoil_bool = True
            else:
                recoil_bool = False

        
        def check_rapidfire_var(rapidfire_var):
            global rapidfire_bool, rapidfire_bool
            if rapidfire_var.get():
                rapidfire_bool = True
            else:
                rapidfire_bool = False

        
        def check_autocrouch_var(autocrouch_var = None):
            global autocrouch_bool, autocrouch_bool
            if autocrouch_var.get():
                autocrouch_bool = True
            else:
                autocrouch_bool = False

        
        def check_autobreathhold(autobreathhold = None):
            global autobreathhold_bool, autobreathhold_bool
            if autobreathhold.get():
                autobreathhold_bool = True
            else:
                autobreathhold_bool = False

        
        def check_random_var(random_toggle_var = None):
            global randomizer_bool, randomizer_bool
            if random_toggle_var.get():
                randomizer_bool = True
            else:
                randomizer_bool = False

        self.recoil_var = tk.IntVar()
        self.recoil_title = tk.Label(self.recoil_tab, 'Recoil Tab', (USUAL_FONT, 18), **('text', 'font')).grid(0, 0, 2, 'W', **('row', 'column', 'columnspan', 'sticky'))
        self.current_profile = tk.Label(self.recoil_tab, f'''Profile ➝ {current_profile[:-5]}''', (USUAL_FONT, 14), **('text', 'font')).grid(0, 6, 4, 'W', **('row', 'column', 'columnspan', 'sticky'))
        self.recoil_label = tk.Label(self.recoil_tab, 'Enable:', (USUAL_FONT, 11), **('text', 'font')).grid(1, 0, 'W', **('row', 'column', 'sticky'))
        self.recoil_toggle = None(None, None, (lambda : check_recoil_var(self.recoil_var)), **('variable', 'command'))
        self.recoil_toggle.grid(1, 1, 'W', **('row', 'column', 'sticky'))
        self.random_toggle_var = tk.IntVar()
        self.random_toggle_label = tk.Label(self.recoil_tab, 'Randomizer:', (USUAL_FONT, 11), **('text', 'font')).grid(2, 0, 'W', **('row', 'column', 'sticky'))
        self.random_toggle = None(None, None, None, (lambda : check_random_var(self.random_toggle_var)), **('variable', 'font', 'command'))
        self.random_toggle.grid(2, 1, 'W', **('row', 'column', 'sticky'))
        self.random_toggle.select()
        self.auto_crouch_var = tk.IntVar()
        self.auto_crouch_label = tk.Label(self.recoil_tab, 'Auto Crouch:', (USUAL_FONT, 11), **('text', 'font')).grid(3, 0, 'W', **('row', 'column', 'sticky'))
        self.auto_crouch_toggle = None(None, None, None, (lambda : check_autocrouch_var(self.auto_crouch_var)), **('variable', 'font', 'command'))
        self.auto_crouch_toggle.grid(3, 1, 'W', **('row', 'column', 'sticky'))
        
        def get_modes(event = None):
            global list_of_modes
            list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config('recoil', 'guns', self.selected_gun_var.get()).keys()))
            self.select_mode['values'] = (lambda .0: [ mode for mode in .0 ])(list_of_modes)

        
        def get_selected_mode(event = None):
            global current_mode
            if event:
                current_mode = event.widget.get()
                self.gun_values_entry.delete(0, tk.END)
                self.gun_values_entry.insert(tk.END, self.gun_attributes[current_mode])

        
        def get_selected_gun(event = None):
            global current_gun, current_gun
            if event:
                current_gun = event.widget.get()
                if current_gun in list(functions.get_config(current_profile, 'guns')):
                    current_gun = self.selected_gun_var.get()
                    self.gun_attributes = functions.get_config(current_profile, 'guns', current_gun)
                    self.gun_values_entry.delete(0, tk.END)
                    
                    try:
                        self.gun_values_entry.insert(tk.END, self.gun_attributes[current_mode])
                    except Exception:
                        err = None
                        
                        try:
                            pass
                        finally:
                            err = None
                            del err



        self.select_gun_label = tk.Label(self.recoil_tab, 'Select Gun:', (USUAL_FONT, 11), **('text', 'font'))
        self.selected_gun_var = tk.StringVar()
        self.select_gun = ttk.Combobox(self.recoil_tab, self.selected_gun_var, 'readonly', list(functions.get_config(current_profile, 'guns')), 6, 4, **('textvariable', 'state', 'values', 'width', 'height'))
        self.select_mode_label = tk.Label(self.recoil_tab, 'Select Mode:', (USUAL_FONT, 11), **('text', 'font'))
        self.selected_mode_var = tk.StringVar()
        self.select_mode = ttk.Combobox(self.recoil_tab, self.selected_mode_var, 'readonly', list_of_modes, 6, 4, **('textvariable', 'state', 'values', 'width', 'height'))
        self.select_gun.bind('<<ComboboxSelected>>', get_selected_gun)
        self.select_mode.bind('<<ComboboxSelected>>', get_selected_mode)
        separator_vert = ttk.Separator(self.recoil_tab, 'vertical', **('orient',)).grid(1, 5, 2, **('row', 'column', 'rowspan'))
        self.select_gun_label.grid(1, 6, 'W', **('row', 'column', 'sticky'))
        self.select_gun.grid(1, 7, 'W', **('row', 'column', 'sticky'))
        self.select_mode_label.grid(2, 6, 'W', **('row', 'column', 'sticky'))
        self.select_mode.grid(2, 7, 'W', **('row', 'column', 'sticky'))
        separator_vert = ttk.Separator(self.recoil_tab, 'vertical', **('orient',)).grid(1, 8, 2, 2, **('row', 'column', 'rowspan', 'padx'))
        self.recoil_status_label = ttk.Label(self.recoil_tab, f'''Recoil Status: {recoil_bool}''', (USUAL_FONT, 11), **('text', 'font'))
        self.recoil_status_label.grid(1, 9, 5, 'W', **('row', 'column', 'padx', 'sticky'))
        self.current_status = ttk.Label(self.recoil_tab, f'''{current_gun} / {current_mode} / {value}''', (USUAL_FONT, 11), **('text', 'font'))
        self.current_status.grid(2, 9, 5, **('row', 'column', 'padx'))
        separator_vert1 = ttk.Separator(self.recoil_tab, 'horizontal', **('orient',)).grid(3, 6, 1, 2, **('row', 'column', 'columnspan', 'padx'))
        self.get_curr_attr(current_profile)
        print(current_profile, current_gun)
        self.gun_attributes = functions.get_config(current_profile, 'guns', current_gun)
        profile_gun_label = ttk.Label(self.recoil_tab, 'Gun attributes', (USUAL_FONT, 14), **('text', 'font')).grid(4, 6, 'W', **('row', 'column', 'sticky'))
        gun_key_input = tk.StringVar()
        gun_key_label = ttk.Label(self.recoil_tab, 'Gun Keybind:', (USUAL_FONT, 11), **('text', 'font'))
        self.gun_key_entry = tk.Entry(self.recoil_tab, 4, gun_key_input, **('width', 'textvariable'))
        print('Self.gun_attributes ( 916 line):', self.gun_attributes)
        if self.gun_attributes['key']:
            self.gun_key_entry.insert(tk.END, self.gun_attributes['key'])
        gun_key_label.grid(5, 6, 2, 'W', **('row', 'column', 'padx', 'sticky'))
        self.gun_key_entry.grid(5, 7, 1, 'W', **('row', 'column', 'padx', 'sticky'))
        gun_values_label = ttk.Label(self.recoil_tab, 'Values:', (USUAL_FONT, 11), **('text', 'font')).grid(6, 6, 2, 'W', **('row', 'column', 'padx', 'sticky'))
        gun_value_input = tk.StringVar()
        self.gun_values_entry = tk.Entry(self.recoil_tab, len(self.gun_attributes[current_mode]) + 5, gun_value_input, **('width', 'textvariable'))
        self.gun_values_entry.insert(tk.END, self.gun_attributes[current_mode])
        self.gun_values_entry.grid(6, 7, 2, 'W', **('row', 'column', 'padx', 'sticky'))
        
        def profile_save():
            self.gun_attributes[current_mode] = (lambda .0: [ int(i) for i in .0 ])(self.gun_values_entry.get().split())
            self.gun_attributes['key'] = self.gun_key_entry.get()
            functions.set_config(current_profile, 'guns', current_gun, self.gun_attributes)
            functions.close(current_profile)

        
        def profiles_reset():
            self.gun_values_entry.delete(0, tk.END)
            self.gun_values_entry.insert(tk.END, self.gun_attributes[current_mode])
            self.gun_key_entry.delete(0, tk.END)
            self.gun_key_entry.insert(tk.END, self.gun_attributes['key'])

        
        def check_random_var(var = None):
            if var.get():
                self.gun_attributes['random'] = 1
            else:
                self.gun_attributes['random'] = 0

        save_profile_btn = tk.Button(self.recoil_tab, 'Save', 1, 16, ('Segoe UI', 9), profile_save, **('text', 'height', 'width', 'font', 'command'))
        save_profile_btn.grid(5, 9, 'W', **('row', 'column', 'sticky'))
        reset_profile_btn = tk.Button(self.recoil_tab, 'Reset', 1, 16, ('Segoe UI', 9), profiles_reset, **('text', 'height', 'width', 'font', 'command'))
        reset_profile_btn.grid(6, 9, 'W', **('row', 'column', 'sticky'))
        if current_mode is not None and current_gun is not None:
            self.select_mode.set(current_mode)
            self.select_gun.set(current_gun)
            if recoil_bool:
                self.recoil_toggle.select()
            else:
                self.recoil_toggle.deselect()


Ilusity = <NODE:27>(Ilusity, 'Ilusity', tk.Tk, Thread)

def check_toggle_pressed():
    '''
    Checks if the toggle key was pressed: Numpad = 0
    If yes then
        select checkbox for recoil
    else:
        deselect checkbox for recoil
    '''
    global recoil_bool
    if win32api.GetAsyncKeyState(96) and win32api.GetAsyncKeyState(144):
        recoil_bool = not recoil_bool
        if recoil_bool == False:
            root.recoil_toggle.deselect()
        else:
            root.recoil_toggle.select()
            root.select_gun.set(current_gun)
            root.select_mode.set(current_mode)
    root.recoil_status_label.configure(f'''Recoil Status: {'On' if recoil_bool else 'Off'}''', **('text',))
    root.current_status.configure(f'''{current_gun} - {current_mode} - {value}''', **('text',))


def check_mode_changes():
    '''"
    Checks if user pressed PAGE UP or PAGE Down to change Modes
    Check if mode can be changed based on list_of_modes
    Modifies the combobox for modes to the current_mode
    and Modifies the variable current_mode to the new selected mode!

    '''
    global list_of_modes, current_mode, current_mode, current_mode, current_mode, current_mode, current_mode
    list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config(current_profile, 'guns', current_gun).keys()))
    if current_mode is not None and current_gun is not None:
        if current_mode in list_of_modes:
            if keyboard.is_pressed(switch_modeup_config):
                if len(list_of_modes) > list_of_modes.index(current_mode) + 1:
                    current_mode = list_of_modes[int(list_of_modes.index(current_mode)) + 1]
                    root.gun_values_entry.delete(0, tk.END)
                    root.gun_values_entry.insert(tk.END, root.gun_attributes[current_mode])
                else:
                    current_mode = list_of_modes[0]
                    root.gun_values_entry.delete(0, tk.END)
                    root.gun_values_entry.insert(tk.END, root.gun_attributes[current_mode])
            if keyboard.is_pressed(switch_modedown_config):
                if len(list_of_modes) > list_of_modes.index(current_mode) - 1:
                    
                    try:
                        current_mode = list_of_modes[int(list_of_modes.index(current_mode)) - 1]
                        root.gun_values_entry.delete(0, tk.END)
                        root.gun_values_entry.insert(tk.END, root.gun_attributes[current_mode])
                    except Exception:
                        current_mode = list_of_modes[0]

                else:
                    current_mode = list_of_modes[0]
                    root.gun_values_entry.delete(0, tk.END)
                    root.gun_values_entry.insert(tk.END, root.gun_attributes[current_mode])
            root.select_mode['values'] = (lambda .0: [ mode for mode in .0 ])(list_of_modes)
            root.select_mode.set(current_mode)
        else:
            current_mode = (lambda .0: [ mode for mode in .0 ])(list_of_modes)[0]
            root.select_mode.set((lambda .0: [ mode for mode in .0 ])(list_of_modes)[0])
        root.gun_attributes = functions.get_config(current_profile, 'guns', current_gun)


def key_check(key):
    if keyboard.is_pressed(key):
        return True
    return None


def check_key(key = None):
    '''Checks if key is pressed == True'''
    global hidden
    if win32api.GetAsyncKeyState(45) != 0:
        hidden = not hidden
        if hidden and root.current_tab == 'recoil':
            hide_ui()
        else:
            hide_ui()


def hide_ui():
    if hidden:
        root.grid_remove_all()
        root.attributes('-alpha', 0.3)
        root.attributes('-topmost', True)
        root.overrideredirect(True)
    else:
        root.recoil_tab_create()
        root.attributes('-alpha', 0.95)
        root.attributes('-topmost', True)
        root.overrideredirect(False)


def check_gun_changes():
    '''"
    Checks if user pressed CAPSLOCK to change guns
    Check if user can change guns, checks list
    Modifies the combobox for guns to the current_gun
    and Modifies the variable current_gun to the new selected gun!

    Also if gun key was pressed then activate specific gun
    '''
    global current_gun, current_gun, current_key, current_gun, current_key, list_of_modes, current_mode, current_mode, current_key
    if keyboard.is_pressed(switch_gun_config):
        current_gun = root.selected_gun_var.get()
        if len(list_of_guns) > list_of_guns.index(current_gun) + 1:
            current_gun = list_of_guns[int(list_of_guns.index(current_gun)) + 1]
            current_key = functions.get_config(current_profile, 'guns', current_gun)['key']
            root.gun_attributes = functions.get_config(current_profile, 'guns', current_gun)
        else:
            current_gun = list_of_guns[0]
            root.gun_attributes = functions.get_config(current_profile, 'guns', current_gun)
            current_key = functions.get_config(current_profile, 'guns', current_gun)['key']
        list_of_modes = (lambda .0: [ key for key in .0 if key not in ('key', 'random') ])(list(functions.get_config(current_profile, 'guns', current_gun).keys()))
        current_mode = list_of_modes[0]
        root.gun_key_entry.delete(0, tk.END)
        root.gun_key_entry.insert(tk.END, current_key)
        root.gun_values_entry.delete(0, tk.END)
        root.gun_values_entry.insert(tk.END, root.gun_attributes[current_mode])
        root.select_gun.set(current_gun)
        current_mode = list_of_modes[0]
    
    try:
        current_key = functions.get_config(current_profile, 'guns', current_gun)['key']
    except Exception:
        e = None
        
        try:
            pass
        finally:
            e = None
            del e


    root.select_mode['values'] = (lambda .0: [ mode for mode in .0 ])(list_of_modes)
    if current_mode not in (lambda .0: [ mode for mode in .0 ])(list_of_modes):
        check_mode_changes()
    root.current_status.configure(f'''{current_gun} - {current_mode} - {value}''', **('text',))


def recoil_movement():
    '''
    Function responsible for recoil movement
    uses Thread to work with Tkinter


    # NEEDS WORK 10/04

    '''
    global recoil_bool, current_key, recoil_bool, recoil_bool, current_key, recoil_bool, value, value, value
    crouch = False
    
    def get_numlock_state():
        '''
        Gets Numlock key state
        1 = On
        0 = Off

        :returns
        1 or 0
        '''
        import ctypes
        hllDll = ctypes.WinDLL('User32.dll')
        VK_CAPITAL = 144
        return hllDll.GetKeyState(VK_CAPITAL)

    while None:
        count = 0
        fire_rate = 0
        check_gun_changes()
        check_mode_changes()
        check_toggle_pressed()
        if not root.current_tab == 'recoil':
            recoil_bool = False
        if check_key('insert') and root.current_tab == 'recoil':
            hide_ui()
        if not current_key:
            current_key = 'x'
        if keyboard.is_pressed(current_key):
            recoil_bool = not recoil_bool
            if recoil_bool:
                root.recoil_toggle.select()
            else:
                root.recoil_toggle.deselect()
        while recoil_bool == True:
            if not root.current_tab == 'recoil':
                recoil_bool = False
            sleep(0.15)
            check_gun_changes()
            check_mode_changes()
            check_toggle_pressed()
            if check_key('insert') and root.current_tab == 'recoil':
                hide_ui()
            if not current_key:
                current_key = 'x'
            if keyboard.is_pressed(current_key):
                recoil_bool = not recoil_bool
                if recoil_bool:
                    root.recoil_toggle.select()
                else:
                    root.recoil_toggle.deselect()
            gun = functions.get_config(current_profile, 'guns', current_gun)
            list_of_values = gun[current_mode]
            count = 0
            if autocrouch_bool and keyboard.is_pressed('c'):
                crouch = not crouch
                if not crouch:
                    keyboard.release('c')
                else:
                    print(crouch)
            if activation_type_config == 0:
                while win32api.GetAsyncKeyState(1):
                    if autocrouch_bool and keyboard.is_pressed('c') == False:
                        keyboard.press('c')
                        crouch = True
                    check_toggle_pressed()
                    gun = functions.get_config(current_profile, 'guns', current_gun)
                    list_of_values = gun[current_mode]
                    if rapidfire_bool:
                        pass
                    if count > len(list_of_values) - 1:
                        count = 0
                    value = list_of_values[count]
                    if randomizer_bool:
                        win32api.mouse_event(1, 0, int(randint(abs(value - 1), value + 1)))
                    else:
                        win32api.mouse_event(1, 0, int(value))
                    if int(fire_rate) % 1000 == 0:
                        count += 1
                    fire_rate += fire_rate_config
                    sleep(interval_config)
            if activation_type_config == 1:
                while win32api.GetAsyncKeyState(2) < 0:
                    if autocrouch_bool and keyboard.is_pressed('c') == False:
                        keyboard.press('c')
                    check_toggle_pressed()
                    gun = functions.get_config(current_profile, 'guns', current_gun)
                    list_of_values = gun[current_mode]
                    if rapidfire_bool:
                        pass
                    if count > len(list_of_values) - 1:
                        count = 0
                    value = list_of_values[count]
                    if randomizer_bool:
                        win32api.mouse_event(1, 0, int(randint(abs(value - 1), value + 1)))
                    else:
                        win32api.mouse_event(1, 0, int(value))
                    if int(fire_rate) % 1000 == 0:
                        count += 1
                    fire_rate += fire_rate_config
                    sleep(interval_config)
            if activation_type_config == 2:
                while win32api.GetAsyncKeyState(1) < 0 and win32api.GetAsyncKeyState(2) < 0:
                    if autocrouch_bool and keyboard.is_pressed('c') == False and crouch == False:
                        crouch = not crouch
                        keyboard.press_and_release('c')
                        print('Pressed Crouch')
                    check_toggle_pressed()
                    gun = functions.get_config(current_profile, 'guns', current_gun)
                    list_of_values = gun[current_mode]
                    if rapidfire_bool:
                        pass
                    if count > len(list_of_values) - 1:
                        count = 0
                    value = list_of_values[count]
                    if randomizer_bool:
                        win32api.mouse_event(1, 0, int(randint(abs(value - 1), abs(value + 1))))
                    else:
                        win32api.mouse_event(1, 0, int(value))
                    if int(fire_rate) % 1000 == 0:
                        count += 1
                    fire_rate += fire_rate_config
                    sleep(interval_config)
        return None

root = Ilusity()
root.run()
recoil_thread = Thread(recoil_movement, **('target',))
recoil_thread.start()
root.mainloop()
