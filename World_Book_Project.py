#!/usr/bin/env python
# coding: utf-8

# In[16]:


import plotly.express as px
import pandas as pd
import numpy as np


# In[3]:


#Getting used to plotly express
df = px.data.gapminder()
fig = px.choropleth(df, locations="iso_alpha", color="lifeExp", hover_name="country", animation_frame="year", range_color=[20,80])
fig.show()


# In[21]:


#Manual input books - limited countries
data = {
    "Country": ["United States", "Canada", "France", "Germany", "Russia", "China", "India", "Brazil", "Australia"],
    "Books": [500, 150, 300, 250, 200, 600, 450, 350, 100]
}
df = pd.DataFrame(data)
fig = px.choropleth(
    df, 
    locations="Country", 
    locationmode="country names", 
    color="Books",
    hover_name="Country", 
    color_continuous_scale="blackbody", 
    title="Books by Country"
)
fig.update_layout(
    geo=dict(
        showframe=False, 
        projection_type='orthographic' 
    )
)
fig.show()


# In[18]:


fig = px.colors.sequential.swatches_continuous()
fig.show()


# In[26]:


#Fixing up country options with random inputs for book amount
countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
    "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", 
    "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", 
    "Congo, Republic of the", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", 
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", 
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", 
    "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", 
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
    "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", 
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", 
    "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", 
    "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", 
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", 
    "South Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", 
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

books = np.random.randint(0, 20, size=len(countries))

data = {
    "Country": countries,
    "Books": books
}
df = pd.DataFrame(data)

fig = px.choropleth(
    df, 
    locations="Country", 
    locationmode="country names", 
    color="Books", 
    hover_name="Country", 
    color_continuous_scale="electric", 
    title="Books by Country"
)

fig.update_layout(
    geo=dict(
        showframe=False, 
        projection_type='orthographic'
    )
)

fig.show()


# In[27]:


#Credit
#https://www.britannica.com/topic/list-of-countries-1993160 for world countries list


# In[ ]:


#User input for each country's book value
#Reset = Blank Map
#Show Map = Shows World Chloropleth Map
#Exit = escape
import plotly.express as px
import pandas as pd
import numpy as np

countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", "Antigua and Barbuda", "Argentina", "Armenia", 
    "Australia", "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", 
    "Belgium", "Belize", "Benin", "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", 
    "Brunei", "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
    "Central African Republic", "Chad", "Chile", "China", "Colombia", "Comoros", "Congo, Democratic Republic of the", 
    "Congo, Republic of the", "Costa Rica", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", 
    "Denmark", "Djibouti", "Dominica", "Dominican Republic", "East Timor (Timor-Leste)", "Ecuador", "Egypt", 
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini", "Ethiopia", "Fiji", "Finland", 
    "France", "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", "Greece", "Grenada", "Guatemala", 
    "Guinea", "Guinea-Bissau", "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", 
    "Iran", "Iraq", "Ireland", "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan", "Kenya", 
    "Kiribati", "Korea, North", "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", "Laos", "Latvia", 
    "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", 
    "Malawi", "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius", 
    "Mexico", "Micronesia, Federated States of", "Moldova", "Monaco", "Mongolia", "Montenegro", "Morocco", 
    "Mozambique", "Myanmar (Burma)", "Namibia", "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", "Pakistan", "Palau", "Panama", "Papua New Guinea", 
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Qatar", "Romania", "Russia", "Rwanda", 
    "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa", "Spain", "Sri Lanka", "Sudan", 
    "South Sudan", "Suriname", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Togo", "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
    "Uganda", "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay", "Uzbekistan", 
    "Vanuatu", "Vatican City", "Venezuela", "Vietnam", "Yemen", "Zambia", "Zimbabwe"
]

books = [0] * len(countries)

data = {
    "Country": countries,
    "Books": books
}
df = pd.DataFrame(data)

def update_books(country_name, count=1):
    if country_name in df['Country'].values:
        df.loc[df['Country'] == country_name, 'Books'] += count
        print(f"Added {count} books to {country_name}. Total now: {df.loc[df['Country'] == country_name, 'Books'].values[0]}")
    else:
        print("Country not found. Please try again.")

def reset_books():
    df['Books'] = 0
    print("All book counts have been reset to 0.")

def display_map():
    fig = px.choropleth(
        df, 
        locations="Country", 
        locationmode="country names", 
        color="Books", 
        hover_name="Country", 
        color_continuous_scale="blackbody", 
        title="Books by Country"
    )
    fig.update_layout(
        geo=dict(
            showframe=False, 
            projection_type='orthographic'
        )
    )
    fig.show()

while True:
    print("\nEnter the name of a country and a number to add books (e.g., 'United States 5'), type 'reset' to reset counts, 'show map' to display map, or 'exit' to quit:")
    user_input = input()

    if user_input.lower() == "exit":
        break
    elif user_input.lower() == "show map":
        display_map()
    elif user_input.lower() == "reset":
        reset_books()
    else:
        try:
            if " " in user_input:
                country_name, count = user_input.rsplit(" ", 1)
                count = int(count)
            else:
                country_name = user_input
                count = 1

            update_books(country_name, count)
        except ValueError:
            print("Invalid input. Please enter a valid country name and number (e.g., 'United States 5').")


# In[ ]:




