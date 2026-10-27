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
