import streamlit as st
import pandas as pd
import mysql.connector
import matplotlib.pyplot as plt

# my sql connection

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Muni@1995",
    database="phonepe_db"

)

# load data

query = "SELECT * FROM aggregated_transaction"
df = pd.read_sql(query, conn)

# Streamlit page config

st.set_page_config(page_title="phonepe Dashboard", layout="wide")

st.title("phonepe Transaction Insights Dashboard")

# Sidebar Filters

st.sidebar.header("Filters")

selected_state = st.sidebar.selectbox(
    "Select State",
    sorted(df["state"].unique())
)

selected_year = st.sidebar.selectbox(
    "Select year",
    sorted(df["year"].unique())
)

# filter data

filtered_df = df[
       (df["state"] == selected_state) &
       (df["year"] == selected_year)
]

# Metrics

total_amount =
filtered_df["transaction_amount"].sum()
total_count =
filtered_df["transaction_count"].sum()

col1, col2 = st.columns(2)

col1.metric(" Total Transaction Amount",
            f"{total_amount:,.0f}")
col2.metric(" Total Transaction Count",
            f"{total_count:,.0f}")

# Charts

st.subheader("Transaction Type Analysis")

type_data = (

filteres_df.groupby("transaction_type")
    ["transaction_amount"]
         .sum()
)

fig, ax = plt.subplots()
type_data.plot(kind="bar", ax=ax)
plt.xticks(roration=45)
plt.ylabel("Transaction Amount")

st.pyplot(fig)

# yearly Trend

st.subheader("Yearly Transaction Trend (State Level)")

yearly_data = (
    df[df["state"] == selected_state]
    .groupby("year")["transaction_amount"]
    .sum()
)

fig2, ax2 = plt.subplots()
yearly_data.plot(kind="line", marker="o",ax=ax2)
plt.ylabel("Transaction Amount")

st.pyplot(fig2)




































