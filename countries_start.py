"""
Contains all the questions and the list of all countries in the world.
"""


def start_question():
    """Contains a list of the initial questions for the Countries theme."""
    START_QUESTIONS = ["Is your country situated in Europe?", "Is your country situated in Asia?",
                       "Is your country situated in Africa?", "Is your country situated in South America?",
                       "Is your country situated in North America or in the Caribbean?",
                       "Is your country situated in Oceania?"]
    return START_QUESTIONS


def countries_question():
    """Contains a list of all the questions for every continent.

    The first set of questions are for Europe, the second for Asia,
    the third for Africa, the fourth for South America,
    the fifth for North America and the last set of questions are for Oceania.
    """
    COUNTRIES_QUESTIONS = [
        ["Is the population of your country over 30 million?", "Is the population of your country over 10 million?",
         "Is the population of your country over 5 million?", "Is Dutch an official language in your country?",
         "Is English an official language in your country?",
         "Is Italian an official language in your country?", "Is French an official language in your country?",
         "Is German an official language in your country?", "Is your country part of the European Union?",
         "Is Euro the official currency of your country?",
         "Is your country situated in the Nordic region?", "Does your country touches The Mediterranean Sea?",
         "Was your country part of Yougoslavia?", "Does the flag of your country has 3 or more colors?",
         "Does the flag of your country has blue cross?", "Does the flag of your country has a cross?",
         "Does the flag of your country contains red?"],
        ["Is the population of your country over 100 million?", "Is the population of your country over 30 million?",
         "Is the population of your country over 10 million?", "Is the population of your country over 5 million?",
         "Is Arabic an official language in your country?", "Is your country situated in Middle East region?",
         "Is Hinduism the most practiced religion in your country?",
         "Is Folk religion the most practiced religion in your country?",
         "Is Christianity the most practiced religion in your country?",
         "Is Buddhism the most practiced religion in your country?",
         "Is Islam the most practiced religion in your religion?",
         "Is your country an island?", "Does your country touches the Indian Ocean?",
         "Does your country touches the Pacific Ocean?",
         "Does the flag of your country contains red?",
         "Does the flag of your country contains blue?", "Does the flag of your country contains green?",
         "Does the flag of your country contains yellow?",
         "Is there a star on the flag of your country?", "Is there a moon on the flag your country?",
         "Is there a circled object or a sun on the flag of your country?"],
        ["Is the population of your country over 30 million?", "Is the population of your country over 10 million?",
         "Is the population of your country over 5 million?",
         "Is French an official language in your country?", "Is English an official language in your country?",
         "Is Arabic an official language in your country?",
         "Is Portuguese an official language in your country?",
         "Is your country an island?", "Is Islam the most practiced religion in your religion?",
         "Is Christianity the most practiced religion in your country?",
         "Does your country touches the Atlantic Ocean?(including The Mediterranean Sea)",
         "Does your country touches the Indian Ocean?(including The Red Sea and The Arabian Sea)",
         "Does the flag of your country contains at least 3 or more colors?",
         "Does the flag of your country contains red?", "Does the flag of your country contains blue?",
         "Does the flag of your country contains green?",
         "Does the flag of your country contains yellow?",
         "Is there a star on the flag of your country?", "Is there a moon on the flag your country?"],
        ["Is the population of your country over 30 million?",
         "Is the population of your country over 10 million?", "Is the population of your country over 5 million?",
         "Is Spanish an official language in your country?", "Is the Amazon forest in your country?",
         "Does your country touches the Atlantic Ocean?",
         "Does your country touches the Pacific Ocean?", "Does the flag of your country contains red?",
         "Does the flag of your country contains blue?",
         "Does the flag of your country contains green?", "Is there a star on the flag of your country?",
         "Is there a circled object or a sun on the flag of your country?"],
        ["Is the population of your country over 30 million?", "Is the population of your country over 10 million?",
         "Is the population of your country over 5 million?", "Is Spanish an official language in your country?",
         "Is English an official language in your country?", "Does your country touches the Atlantic Ocean?",
         "Does your country touches the Pacific Ocean?",
         "Does the flag of your country contains red?", "Does the flag of your country contains blue?",
         "Does the flag of your country contains yellow?",
         "Does the flag of your country contains green?", "Does the flag of your country contains black?",
         "Is there a star on the flag of your country?"],
        ["Is the population of your country over 10 million?", "Is the population of your country over 1 million?",
         "Does the flag of your country contains green?",
         "Does the flag of your country contains blue?", "Does the flag of your country contains red?",
         "Does the flag of your country contains yellow?", "Is there a star on the flag of your country?"]]
    return COUNTRIES_QUESTIONS


def countries_list():
    """Contains a list of all the countries in the world separated by continent.

    The first set of counties are in Europe, the second in Asia,
    the third in Africa, the fourth in South America,
    the fifth in North America and the last set of questions are in Oceania.
    """
    COUNTRIES_LIST = [
        ["Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia",
         "Czech Republic", "Cyprus", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece",
         "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg",
         "Malta",
         "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
         "Romania", "Russia", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland",
         "Turkey", "Ukraine", "United Kingdom"],
        ["Afghanistan", "Armenia", "Azerbaijan", "Bahrain",
         "Bangladesh", "Bhutan", "Brunei", "Cambodia", "China",
         "India", "Indonesia", "Iran", "Iraq", "Israel",
         "Japan", "Jordan", "Kazakhstan", "Kuwait", "Kyrgyzstan",
         "Laos", "Lebanon", "Malaysia", "Maldives",
         "Mongolia", "Myanmar", "Nepal", "North Korea", "Oman",
         "Pakistan", "Philippines", "Qatar", "Saudi Arabia",
         "Singapore", "South Korea", "Sri Lanka", "Palestine", "Syria",
         "Tajikistan", "Thailand", "Timor-Leste",
         "Turkmenistan", "United Arab Emirates", "Uzbekistan",
         "Vietnam", "Yemen"],
        ["Algeria", "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cabo Verde", "Cameroon",
         "Central African Republic", "Chad", "Comoros", "Congo", "Côte d'Ivoire", "Djibouti", "DR Congo",
         "Egypt",
         "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", "Gabon", "Gambia", "Ghana", "Guinea",
         "Guinea-Bissau",
         "Kenya", "Lesotho", "Liberia", "Libya", "Madagascar", "Malawi", "Mali", "Mauritania", "Mauritius",
         "Morocco",
         "Mozambique", "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal",
         "Seychelles",
         "Sierra Leone", "Somalia", "South Africa", "South Sudan", "Sudan", "Tanzania", "Togo", "Tunisia",
         "Uganda",
         "Zambia", "Zimbabwe"],
        ["Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "Guyana", "Paraguay",
         "Peru", "Suriname", "Uruguay", "Venezuela"],
        ["Antigua and Barbuda", "Bahamas", "Barbados", "Belize", "Canada", "Costa Rica", "Cuba",
         "Dominica", "Dominican Republic", "El Salvador", "Grenada", "Guatemala", "Haiti",
         "Honduras", "Jamaica", "Mexico", "Nicaragua", "Panama", "Saint Kitts and Nevis",
         "Saint Lucia", "St. Vincent and Grenadines", "Trinidad and Tobago",
         "United States of America"],
        ["Australia", "Fiji", "Kiribati", "Marshall Islands", "Micronesia", "Nauru", "New Zealand", "Palau",
         "Papua New Guinea", "Samoa", "Solomon Islands", "Tonga", "Tuvalu", "Vanuatu"]]
    return COUNTRIES_LIST
