# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:13:43 2017

@author: Toan
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
 
 
class ProductListButton(ListItemButton):
    pass
 
 
class ProductDB(BoxLayout):
 
    # Connects the value in the TextInput widget to these
    # fields
    product_code_text_input = ObjectProperty()
    quantity_text_input = ObjectProperty()
    reduction_text_input = ObjectProperty()
    products_list = ObjectProperty()
 
    def submit_product(self):
 
        # Get the product name from the TextInputs
        product_name = self.product_code_text_input.text 
 
        # Add the product to the ListView
        self.products_list.adapter.data.extend([product_name])
 
        # Reset the ListView
        self.products_list._trigger_reset_populate()
 
    def delete_product(self, *args):
 
        # If a list item is selected
        if self.products_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.products_list.adapter.selection[0].text
 
            # Remove the matching item
            self.products_list.adapter.data.remove(selection)
 
            # Reset the ListView
            self.products_list._trigger_reset_populate()
 
    def replace_product(self, *args):
 
        # If a list item is selected
        if self.products_list.adapter.selection:
 
            # Get the text from the item selected
            selection = self.products_list.adapter.selection[0].text
 
            # Remove the matching item
            self.products_list.adapter.data.remove(selection)
 
            # Get the product name from the TextInputs
            product_name = self.product_code_text_input.text 

            # Add the updated data to the list
            self.products_list.adapter.data.extend([product_name])
 
            # Reset the ListView
            self.products_list._trigger_reset_populate()
 
 
class ProductDBApp(App):
    def build(self):
        return ProductDB()
 
 
dbApp = ProductDBApp()
 
dbApp.run()