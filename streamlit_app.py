import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/all")
st.text(fruityvice_response)
