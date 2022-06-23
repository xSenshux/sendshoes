import streamlit
import typing_extensions
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My Parents New Healty Diner')

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page
streamlit.dataframe(fruits_to_show)

streamlit.header ('The fruit load list contains:')
#Snowflake-related functions
def get_fruit_load_list():
	with my_cnx.cursor() as my_cur:
		my_cur.execute("select * from_fruit_load_list")
		return my_cur.fetchall()
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
	my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
	my_data _rows = get_fruit_load_list()
	streamlit.dataframe(my_data_rows)
   
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thank you for adding', add_my_fruit)

#don't run anything past here while we troubleshoot
