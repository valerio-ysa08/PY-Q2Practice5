from pyscript import document, display


def check_country (e):
    document.getElementById("output1").innerHTML = ""
    countries = {
        "PH" : "Philippines",
        "JP" : "Japan",
        "SG" : "Singapore",
        "FR" : "France",
        "AU" : "Australia"
    }

    country_code = document.getElementById("countries").value

    # Add a country
    countries["CA"] = "Canada"

    display(countries.get(country_code, "Country code not found"), target="output1") 

def show_country (e):
    document.getElementById("output1").innerHTML = ""
    countries = {
        "PH" : "Philippines",
        "JP" : "Japan",
        "SG" : "Singapore",
        "FR" : "France",
        "AU" : "Australia"
    }

    country_code = document.getElementById("countries").value
    
    # CHECK the countries
    show_country = country_code in countries

    # SHOW ALL the countries
    list_country = list(countries.values())

    display("The number of countries is... ", len(countries), target="output1")
    display("Is it in the dictionary?", show_country, target="output1")
    display("What are the countries in the list?", list_country, target="output1")

