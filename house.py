#!/usr/bin/env python3
from uszipcode import SearchEngine
import pandas as pd
import numpy as np

class County:
    def __init__(self, county):
        self.county = county
        self.solar_install_cost = 0
        self.average_electric_bill = 0
        self.average_number_solar_panels = 0
        self.average_residential_electricity_price = 0
        self.average_energy_produced_per_day = 0

    def set_info(self):
        df = pd.read_csv('solarinfo.csv')
        for i in range(len(df)):
            if df.loc[i, 'County'] == self.county:
                self.solar_install_cost = df.loc[i, 'Solar Installation Cost (of 5kW System)']
                self.average_electric_bill = df.loc[i, 'Average Electric Bill per County']
                self.average_number_solar_panels = df.loc[i, 'Average Number of Solar Panels per Household']
                self.average_residential_electricity_price = df.loc[i, 'Average Residential Electricity Price per County (kWh)']
                self.average_energy_produced_per_day = df.loc[i, 'Average Energy Produced in each County Per Day']
                break

class House:
    def __init__(self, zipcode, num_panels):
        self.zipcode = str(zipcode)
        self.num_panels = num_panels
        self.county = None
        self.state = ""

    def set_county(self):
        sr = SearchEngine(download_url="https://your-private-storage.sqlite")
        zipcode = sr.by_zipcode(self.zipcode)
        county = zipcode.values()[5][:-7]
        self.county = County(county)
        print(self.county)
        self.county.set_info()
        print(self.county.solar_install_cost)

    def set_state(self):
        sr = SearchEngine(download_url="https://your-private-storage.sqlite")
        zipcode = sr.by_zipcode(self.zipcode)
        self.state = zipcode.values()[6]

    def power_estimate(self):
        if self.county == "":
            self.set_county()


class SolarPanel:
    def __init__(self, length = 1.6, width = 1, power = 300):
        self.length = length
        self.width = width
        self.power = power


class SolarSystem:
    def __init__(self, num_panels):
        self.output_peak = 0
        self.sqm = 0
        self.solar_panel_type = None
        self.num_panels = num_panels

    def set_solar_panel_type(self, length = 1.6, width = 1, power = 300):
        solar_panel = SolarPanel(length, width, power)
        self.solar_panel_type = solar_panel

    def set_output_peak:
        if solar_panel_type is None:
            self.set_solar_panel_type()
        self.output_peak = self.num_panels * self.solar_panel_type.power

    def set_sqm(self, solar_panel):
        self.sqm = solar_panel.length*solar_panel.width * self.num_panels

    def estimate(self, num_panels, price_by_state):
        if self.output_peak == 0:
            self.set_output_peak
        ratio = output_peak/5000
        estimate = ratio * price_by_state
        return estimate

def OnlyFunctionYouNeed(zipcode, num_panels):
    house = House(zipcode, num_panels):
    

if __name__ == '__main__':
    myhouse = House("46556", 10000, 30)
    myhouse.set_county()
    myhouse.set_state()
