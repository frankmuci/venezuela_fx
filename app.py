import streamlit as st
import requests
import pandas as pd
import numpy as np
import base64
from venezuela_fx.app_ready import Model


st.set_page_config(
    page_title="Quick reference", # => Quick reference - Streamlit
    page_icon="🐍",
    layout="wide", # wide
    initial_sidebar_state="auto") # collapsed




st.sidebar.title(f"""
    Venezuela FX
    """)

font_size = st.sidebar.markdown('Menu')
nav_size = st.sidebar.radio('Select a page',('Home','What We Do','FX Prediction','About Us','My Account'))
link = '[Data Source](https://tradingeconomics.com/venezuela/inflation-cpi)'
st.sidebar.markdown(link, unsafe_allow_html=True)

FONT_SIZE_CSS = f"""
<style>
h1 {{
    font-size: {font_size}px !important;
}}
</style>
"""
st.write(FONT_SIZE_CSS, unsafe_allow_html=True)

#st.write(nav_size)

if nav_size == 'Home':
    st.markdown("""
    <style>
    .big-font {
    font-size:50px !important;
    color: White;
    font: 'monospace'
    }
    </style>
    """,
            unsafe_allow_html=True)


    st.markdown(""" <style> .big-font {
        font-size:80px ; font-family: 'monospace'; color: ##FFFFFF;}
            </style> """,
                unsafe_allow_html=True)

    st.markdown(
        '<p class="big-font">Our mission is to predict the FX rate of the Venezuelan Bolívar for the next 30 days</p>'                                                                                                                                                                                                                                                                                        ,

        unsafe_allow_html=True)

    button_trial = st.button('Free Trial', key = 'button_1')
    ('{color: #4F8BF9;\
    border-radius: 20%;\
    backgroud-color: #00FF00;\
    height: 3em;\
    width: 3em;\
    }')

    if button_trial:
        st.write('button has been clicked')

    CSS = """
    h1 {
        color: #00247D;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638265996/Screenshot_2021-11-30_at_09.45.10.png);
        background-size: cover;
    }
    """


    st.write(f'<style>{CSS}</style>', unsafe_allow_html=True)
elif nav_size == 'What We Do':
    st.subheader('Background Context')
    st.markdown("""Despite Venezuela’s breathtaking economic collapse, life goes on. Millions of people and tens of thousands of firms continue to exchange goods and services daily -- many of them imported from abroad. Although the economy is rapidly dollarizing, a significant subset of businesses continues to price goods and services in Bolivars, the local currency.\

Venezuela officially entered hyperinflation in 2017, with monthly inflation peaking around 200% in 2018/19 and slowing to around 10% per month in late 2021. The foreign exchange or FX rate loosely tracks consumer price inflation, although the latter has greatly outpaced the former in recent years, leading to higher living costs when measured in USD."""                                                                                                                                                                                                                                                                                                                                                                             )
    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638352631/image.png',
             caption=None,
             width=None,
             use_column_width=None,
             clamp=False,
             channels="RGB",
             output_format="auto")

    st.subheader('Our Aim')
    st.markdown('Pricing merchandise imported in USD in Bolivars poses significant challenges due to the volatility of the FX rate. If firms charge too high a markup in local currency, their inventory turnover and sales slow. If firms charge too low a markup in local currency, their “profits” in Bolivars are rapidly diluted by FX depreciation and their balance sheet in USD shrinks.\ Having accurate forecasts for the FX rate can help businesses price products in Bolivars correctly -- high enough so that they make money (in USD), and low enough to ensure robust sales and inventory turnover. Our FX forecast gives firms more confidence about the time-value of the Bolivar and how to price their products.'                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  )

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
elif nav_size == 'FX Prediction':
    st.title("Modeling the FX rate of Venezula")
    # @st.cache
    # def get_line_chart_data():

    #     return pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])


    # df = get_line_chart_data()

    # st.line_chart(df)

    st.image(
        'https://res.cloudinary.com/julioeq29/image/upload/v1638369332/image_7.png',
        caption=
        "Our Machine Learning model compared to the actual Bolívar-USD FX rate",
        width=None,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto")

    st.image(
        'https://res.cloudinary.com/julioeq29/image/upload/v1638369336/Screen_Shot_2021-12-01_at_1.22.04_PM.png',
        caption="Due to the scale of the data, a logorithmic tranformation was required for our models to work",
        width=None,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto")

    CSS2 = """
    h1 {
        color: #00247D;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638270556/Screenshot_2021-11-30_at_11.07.04.png);
        background-size: cover;
    }
    """



    # st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)

    # model = Model()
    # model.set_experiment_name('Tester')
    # model.sort_data()
    # model.splitting_data()
    # model.flattening_test()
    # model.flattening_train()
    # model.fixing_logged_data()
    # model.set_pipeline()
    # model.run()
    # model.evaluate()
    # model.show_metrics()
    # xyz = model.plt_prediction_graph()
    # st.line_chart(xyz)
    # abc = model.sexy_plot()
    # st.altair_chart(abc)



elif nav_size == 'About Us':


    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638354394/image_1.png',
            caption=None,
            width=None,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="auto")

    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638354394/image_3.png',
            caption=None,
            width=None,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="auto")


    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638354394/image_2.png',
            caption=None,
            width=None,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="auto")


    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638354394/image_4.png',
            caption=None,
            width=None,
            use_column_width=None,
            clamp=False,
            channels="RGB",
            output_format="auto")



    CSS2 = """
    h1 {
        color: #00247D;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638265996/Screenshot_2021-11-30_at_09.45.10.png);
        background-size: cover;
    }
    """

    st.write(f'<style>{CSS2}</style>', unsafe_allow_html=True)

elif nav_size == 'My Account':
    CSS2 = """
    h1 {
        color: #00247D;
    }
    .stApp {
        background-image: url(https://res.cloudinary.com/julioeq29/image/upload/v1638265996/Screenshot_2021-11-30_at_09.45.10.png);
        background-size: cover;
    }
    """

    st.image('https://res.cloudinary.com/julioeq29/image/upload/v1638358418/image_6.png',
        caption=None,
        width=None,
        use_column_width=None,
        clamp=False,
        channels="RGB",
        output_format="auto")

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
