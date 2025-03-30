import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

st.set_page_config(page_title="Title", layout="wide")
st.title("Title")

if st.button("Recruit Searching"):
    os.system("jupyter nbconvert --to notebook --execute Code_Saramin.ipynb --inplace")
    os.system("jupyter nbconvert --to notebook --execute Code_Jobkorea.ipynb --inplace")

    try:
        df_saramin = pd.read_csv("data_tmp/data_saramin.csv")
        df_jobkorea = pd.read_csv("data_tmp/data_jobkorea.csv")
        df_all = pd.concat([df_saramin, df_jobkorea], ignore_index=True)

        st.dataframe(df_all)

        count_by_site = df_all["Site"].value_counts().reset_index()
        count_by_site.columns = ["Site", "Count"]
        count_by_site["Ratio"] = round(count_by_site["Count"] / count_by_site["Count"].sum() * 100, 2)
        count_by_site["Ratio"] = count_by_site["Ratio"].map("{:.2f}".format)
        st.table(count_by_site)

        fig, ax = plt.subplots()
        wedges, texts, autotexts = ax.pie(
            count_by_site["Count"], 
            autopct="%.1f%%",
            startangle=90
        )
        ax.axis("equal")
        ax.legend(wedges, count_by_site["Site"], loc="center left", bbox_to_anchor=(1, 0.5))
        st.markdown("Recruitment Ratio")
        st.pyplot(fig)

    except:
        st.warning("데이터 파일을 불러올 수 없습니다.")