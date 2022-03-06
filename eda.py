import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt


st.title('Food Demand Forecasting - Analytics Vidhya')

@st.cache
def load_data(nrows):
    data = pd.read_csv('train.csv', nrows=nrows)
    return data

@st.cache
def load_center_data(nrows):
    data = pd.read_csv('fulfilment_center_info.csv',nrows=nrows)
    return data

@st.cache
def load_meal_data(nrows):
    data = pd.read_csv('meal_info.csv',nrows=nrows)
    return data


weekly_data = load_data(1000)
center_info_data = load_center_data(1000)
meal_data = load_meal_data(1000)


#WeeklyDemand Data
st.subheader('Weekly Demand Data')
st.write(weekly_data)

st.bar_chart(weekly_data['num_orders'])
df = pd.DataFrame(weekly_data[:200], columns = ['num_orders','checkout_price','base_price'])
df.hist()

fig, ax = plt.subplots()
ax.scatter([1, 2, 3], [1, 2, 3])

st.pyplot(fig)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.line_chart(df)

chart_data = pd.DataFrame(weekly_data[:40], columns=['num_orders', 'base_price'])
st.area_chart(chart_data)

#Center Information
st.subheader('Center Information')
if st.checkbox('Show Center Information data'):
    st.subheader('Center Information data')
    st.write(center_info_data)

st.bar_chart(center_info_data['region_code'])
st.bar_chart(center_info_data['center_type'])

hist_data = [center_info_data['center_id'],center_info_data['region_code']]
group_labels = ['Center Id', 'Region Code']
fig = ff.create_distplot(hist_data, group_labels, bin_size=[10, 25])
st.plotly_chart(fig, use_container_width=True)

st.subheader('Meal Information')
st.write(meal_data)
st.bar_chart(meal_data['cuisine'])
agree = st.button('Click to see Categories of Meal')
if agree:
    st.bar_chart(meal_data['category'])


import streamlit.components.v1 as components
st.title('Streamlit Components')
components.html(
    """
     
    <div class="container">
  <h2>HackerShrine</h2>
 
    <div class="card" style="width:400px">
     
    <div class="card-body ">
      <form action="/upload" method="post" enctype="multipart/form-data">
      <p class="card-text">Custom HTML </p>
        <input type="file" name="file" value="file">
        <hr>
      <input type="submit" name="upload" value="Upload" class="btn btn-success">
      </form>
     
    </div>
  </div>
  <br>
</div>
    """,
    height=600,
)
