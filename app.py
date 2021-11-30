import streamlit as st
import requests
import pandas as pd
import numpy as np
import base64
from venezuela_fx.app_ready import Model


st.set_page_config(
    page_title="Quick reference", # => Quick reference - Streamlit
    page_icon="🐍",
    layout="centered", # wide
    initial_sidebar_state="auto") # collapsed




st.sidebar.markdown(f"""
    # Venezuela FX
    """)

font_size = st.sidebar.markdown('This is a test')
nav_size = st.sidebar.radio('Select a page',('Home','What We Do','FX Prediction','About Us','My Account'))
link = '[Data Source](https://tradingeconomics.com/venezuela/inflation-cpi)'
st.sidebar.markdown(link, unsafe_allow_html=True)
st.sidebar.subheader("This is a subheader")

FONT_SIZE_CSS = f"""
<style>
h1 {{
    font-size: {font_size}px !important;
}}
</style>
"""
st.write(FONT_SIZE_CSS, unsafe_allow_html=True)

st.write(nav_size)

if nav_size == 'Home':
    st.header('**Bolívar to USD**')
    st.markdown("""
<style>
.big-font {
    font-size:30px !important;
    color: White
}
</style>
""",
            unsafe_allow_html=True)

    st.markdown('<p class="big-font">Our mission is .... !!</p>', unsafe_allow_html=True)
    CSS = """
    h1 {
        color: red;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638265996/Screenshot_2021-11-30_at_09.45.10.png);
        background-size: cover;
    }
    """


    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
elif nav_size == 'What We Do':
    st.subheader('Background')
    st.markdown("Venezuela’s ongoing economic collapse likens episodes of state collapse or war. In the five\
                years between 2013 and 2018, GDP has almost halved, oil production has fallen by two thirds, and\
                imports per capita have collapsed over 85%. Inflation has climbed to 1.6 million percent while the\
                real value of the money supply has fallen over 99% since 2013. Minimum wages measured in\
                terms of the cheapest food calorie have declined from 52,000 to under 2,700 calories per month,\
                implying that households that earn minimum wages cannot afford basic sustenance, not to mention\
                health, transportation or other expenditures. Survey data shows that over two thirds of Venezuelans\
                have lost weight involuntarily for two consecutive years. Between 10% and 16% of the population\
                has left Venezuela, many as refugees, and the flow of outward migration is increasing. Recent\
                sanctions on the oil sector and the current standoff for the presidency between Juan Guaidó and\
                Nicolas Maduro suggest the situation will continue to deteriorate rapidly."                                                                                            )
    st.subheader('Our Aim')
    st.markdown('Filler words...')
    CSS2 = """
    h1 {
        color: red;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638270556/Screenshot_2021-11-30_at_11.07.04.png);
        background-size: cover;
    }
    """

    st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)
elif nav_size == 'FX Prediction':
    st.title("Our prediction for the Venezuelan FX rate over the next 30 days")
    # @st.cache
    # def get_line_chart_data():

    #     return pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


    # df = get_line_chart_data()

    # st.line_chart(df)

    CSS2 = """
    h1 {
        color: #00247D;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638270556/Screenshot_2021-11-30_at_11.07.04.png);
        background-size: cover;
    }
    """

    st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)

    model = Model()
    model.set_experiment_name('Tester')
    model.sort_data()
    model.splitting_data()
    model.flattening_test()
    model.flattening_train()
    model.fixing_logged_data()
    model.set_pipeline()
    model.run()
    model.evaluate()
    model.show_metrics()
    xyz = model.plt_prediction_graph()
    st.line_chart(xyz)
    model.save_model_locally()


elif nav_size == 'About Us':

    st.subheader("Meet the team!")


    CSS2 = """
    h1 {
        color: red;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638270556/Screenshot_2021-11-30_at_11.07.04.png);
        background-size: cover;
    }
    """

    st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)

elif nav_size == 'My Account':
    st.write('Working on this...be patient!')
    CSS2 = """
    h1 {
        color: red;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638270556/Screenshot_2021-11-30_at_11.07.04.png);
        background-size: cover;
    }
    """

    st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)

    # model = Model()
    # model.set_experiment_name('Tester')
    # if train == True:
    #     model.sort_data()
    #     model.splitting_data()
    #     model.flattening_test()
    #     model.flattening_train()
    #     model.fixing_logged_data()
    #     model.set_pipeline()
    #     model.run()
    # else:
    #     # read processed csv
    #     # load model
    #     pass
    # model.evaluate()
    # model.show_metrics()
    # xyz = model.prediction_graph()
    # st.line_chart(xyz)
    # model.save_model_locally()
