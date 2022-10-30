from secrets import choice
from django.forms import *
from products.models import Product
from .models import Categories

decode = {
    'Processor': 
        {
            'Intel Core i5 Processor (10th Gen)': 22,
            'Intel Core i3 Processor (11th Gen)': 18,
            'Intel Pentium Quad Core Processor': 37,
            'AMD Athlon Dual Core Processor': 2,
            'AMD Ryzen 5 Quad Core Processor': 9,
            'Intel Core i7 Processor (10th Gen)': 27,
            'Intel Core i3 Processor (10th Gen)': 17,
            'AMD Ryzen 3 Dual Core Processor': 4,
            'Intel Core i5 Processor (9th Gen)': 26,
            'Intel Core i5 Processor (11th Gen)': 23,
            'Intel Celeron Dual Core Processor': 16,
            'Intel Core i7 Processor (9th Gen)': 31,
            'AMD Ryzen 7 Octa Core Processor': 12,
            'AMD Ryzen 5 Hexa Core Processor': 7,
            'Intel Core i7 Processor (11th Gen)': 28,
            'AMD Ryzen 3 Quad Core Processor': 5,
            'Intel Core i5 Processor (8th Gen)': 25,
            'AMD Ryzen 9 Octa Core Processor': 15,
            'AMD Ryzen 5 Quad Core Processor (3rd Gen)': 10,
            'Intel Core i9 Processor (9th Gen)': 34,
            'AMD Ryzen 7 Quad Core Processor': 14,
            'AMD Dual Core Processor': 3,
            'Intel Core i9 Processor (10th Gen)': 32,
            'Intel Core i7 Processor (8th Gen)': 30,
            'AMD Ryzen 5 Dual Core Processor': 6,
            'AMD APU Dual Core A6 Processor': 1,
            'Intel Core i7 Processor (7th Gen)': 29,
            'Microsoft Core i5 Processor (11th Gen)': 38,
            'Intel Core i5 Processor (7th Gen)': 24,
            'Intel Core i9 Processor (8th Gen)': 33,
            'AMD Ryzen 5 Hexa Core Processor (5th Gen)': 8,
            'AMD Ryzen 7 Hexa Core Processor': 11,
            'AMD Ryzen 7 Octa Core Processor (5th Gen)': 13,
            'Intel Evo platform feat 11th Gen Intel Core i5 processor': 35,
            'Intel Evo platform feat 11th Gen Intel Core i7 processor': 36,
            'Intel Core i3 Processor (7th Gen)': 20,
            'Intel Core i3 Processor (5th Gen)': 19,
            'AMD APU Dual Core A4 Processor': 0,
            'Intel Core i3 Processor (8th Gen)': 21
        },
    'RAM': 
        {
            '8 GB DDR4 RAM': 10,
            '4 GB DDR4 RAM': 8,
            '16 GB DDR4 RAM': 2,
            '8 GB LPDDR4X RAM': 12,
            '8 GB LPDDR3 RAM': 11,
            '32 GB LPDDR4X RAM': 6,
            '16 GB LPDDR4X RAM': 4,
            '16 GB LPDDR3 RAM': 3,
            '8 GB DDR3 RAM': 9,
            '16 GB DDR3 RAM': 1,
            '32 GB DDR4 RAM': 5,
            'Upgradable SSD Upto 512 GB and RAM Upto 32 GB': 13,
            '4 GB DDR3 RAM': 7,
            '12 GB DDR4 RAM': 0
        },
    'Operating System': 
        {
            '64 bit Windows 10 Operating System': 1,
            'Mac OS Operating System': 3,
            'Windows 10 Operating System': 5,
            'Pre-installed Genuine Windows 10 Operating System (Includes Built-in Security, Free Automated Updates, Latest Features)': 4,
            'DOS Operating System': 2,
            '64 bit Chrome Operating System': 0
        },
    'Storage':
        {
            '1 TB HDD': 0,
            '256 GB SSD': 8,
            '1 TB HDD|256 GB SSD': 2,
            '512 GB SSD': 10,
            '1 TB SSD': 4,
            'M.2 Slot for SSD Upgrade': 12,
            '128 GB NVMe PCIe 3.0 x4 SSD': 5,
            '1 TB HDD|128 GB SSD': 1,
            '128 GB SSD': 6,
            '512 GB SSD for Reduced Boot Up Time and in Game Loading': 11,
            '1 TB HDD|512 GB SSD': 3,
            '128 GB SSD for Reduced Boot Up Time and in Game Loading': 7,
            '512 GB HDD|512 GB SSD': 9
        },
    'Display': 
        {
            '39.62 cm (15.6 inch) Display': 22,
                '35.56 cm (14 Inch) Display': 14,
                '35.56 cm (14 inch) Display': 16,
                'Matrix Display, Dragon Center, Cooler Boost 5, Nahimic 3': 28,
                '29.46 cm (11.6 inch) Touchscreen Display': 4,
                '33.78 cm (13.3 inch) Display': 9,
                '15.6 inches Full HD IPS Thin Bezel Display (144Hz, 45% NTSC Color Gamut)': 0,
                'SHIFT, SteelSeries Engine 3, Matrix Display (Extend), Dragon Center, GamingMode, VR Ready, Cooler Boost 5, Nahimic 3, Nahimic VR, Giant Speaker': 29,
                '33.78 cm (13.3 inch) Touchscreen Display': 10,
                '15.6 inches Full HD IPS Thin Bezel Display (60Hz, 45% NTSC Color Gamut)': 1,
                '35.56 cm (14 inch) Touchscreen Display': 17,
                '33.02 cm (13 inch) Display': 7,
                '39.62 cm (15.6 Inch) Display': 21,
                '34.04 cm (13.4 inch) Touchscreen Display': 11,
                '40.64 cm (16 inch) Display': 24,
                '31.24 cm (12.3 inch) Touchscreen Display': 6,
                '35.56 cm (14 inches) Touchscreen Display': 19,
                '39.62 cm (15.6 inch) Touchscreen Display': 23,
                '38.1 cm (15 inch) Display': 20,
                '34.54 cm (13.6 inch) Touchscreen Display': 13,
                '43.94 cm (17.3 inch) Display': 25,
                '34.29 cm (13.5 inch) Touchscreen Display': 12,
                '33.78 cm (13.3 Inch) Display': 8,
                'Full HD LED Backlit Display': 27,
                '30.48 cm (12 inch) Touchscreen Display': 5,
                '35.56 cm (14 inches) Display': 18,
                '25.65 cm (10.1 inch) Touchscreen Display': 3,
                'Full HD LED Backlit Anti-glare Display for Better Visual Experience': 26,
                '35.56 cm (14 Inch) Touchscreen Display': 15,
                '25.4 cm (10 inch) Touchscreen Display': 2
        },
    'Warranty': 
        {
            '1 Year Onsite Warranty': 15,
            '2 Year Warranty': 21,
            '1 Year International Travelers Warranty (ITW)': 6,
            '24 Months Warranty': 27,
            '2 Years Carry In Warranty': 24,
            '1 Year Warranty': 18,
            '2 Year Warranty Term for Gaming & Content Creation (EU-WE)': 23,
            '2 Year Warranty Term for Gaming': 22,
            '1 Year International Travelers Warranty': 5,
            '1 Year Domestic Brand Warranty on Device': 4,
            '1 Year Carry-In Warranty': 2,
            '18 Months Warranty + 6 Months Extended Warranty (6 Months Extended Warranty Upon Online Product Registration on www.avita-india.com)': 19,
            '1 Year Limited Warranty': 11,
            '1 Year Limited Hardware Warranty': 7,
            '3 Years Manufacturer Warranty': 33,
            '3 Years Limited Hardware Warranty, In Home Service After Remote Diagnosis - Retail': 32,
            '1 Year Limited Hardware Warranty, In Home Service After Remote Diagnosis - Retail': 8,
            '1 Year Standard Warranty': 17,
            'One-year International Travelers Warranty (ITW)': 35,
            '2 Year Carry-In Warranty': 20,
            '1 Year Onsite Warranty Commencing from the Date of Purchase': 16,
            '1 Year Manufacturer Warranty on the Device from the Date of Purchase': 13,
            '2 Years Onsite Warranty': 25,
            '1 Year Carry In Warranty': 0,
            '3 Year Limited Warranty': 28,
            '3 Year Manufacturer Warranty on the Device and 6 Months Manufacturer Warranty on Included Accessories from the Date of Purchase': 29,
            '1 Year Carry in Warranty': 1,
            '1 Year Manufacturer Warranty on the Device and 6 Months Manufacturer Warranty on Included Accessories from the Date of Purchase': 12,
            '1 Year Limited International Hardware Warranty': 10,
            '3 Years Onsite Warranty': 34,
            '3 Year Premier Support Warranty': 30,
            '1 Year Complete Cover Warranty': 3,
            '3 Years Domestic and 1 Year International Travelers Warranty (ITW)': 31,
            '2 Years Warranty': 26,
            '1 Year Onsite Manufacturing Warranty': 14,
            '1 Year Limited Hardware Warranty, In Home Service After Remote Diagnosis-Retail': 9,
            'Onsite Global Warranty': 36
        }
    }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("user_id","Pin_No")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
            self.fields[i].widget.attrs['placeholder'] = ' '.join([i.capitalize() for i in i.split('_')])
        
        self.fields['catagory'].queryset = Categories.objects.filter(is_approved=True)



class LaptopForm(Form):
    processor = ChoiceField(label='Processor', choices=[(i, i) for i in decode["Processor"].keys()])
    ram = ChoiceField(label='RAM', choices=[(i, i) for i in decode["RAM"].keys()])
    os = ChoiceField(label='Operating System', choices=[(i, i) for i in decode["Operating System"].keys()])
    storage = ChoiceField(label='Storage', choices=[(i, i) for i in decode["Storage"].keys()])
    display = ChoiceField(label='Display', choices=[(i, i) for i in decode["Display"].keys()])
    warranty = ChoiceField(label='Warranty', choices=[(i, i) for i in decode["Warranty"].keys()])

    def __init__(self, *args, **kwargs):
        super(LaptopForm, self).__init__( *args, **kwargs)

        for i in self.fields:
            self.fields[i].widget.attrs['placeholder'] =  self.fields[i].label #' '.join([i.capitalize() for i in i.split('_')])
            # self.fields[i].label = False
            self.fields[i].widget.attrs['class'] = 'form-control'
