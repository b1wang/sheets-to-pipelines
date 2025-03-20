import streamlit as st

home_page = st.Page("./views/home.py", title="Home")
catalog_page = st.Page("./views/catalog.py", title="Catalog")

pg = st.navigation([home_page, catalog_page])
pg.run()

