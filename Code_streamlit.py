import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# 페이지 설정
st.set_page_config(page_title="Title", layout="wide")
st.title("Title")

# 버튼
if st.button("Recruit Searching"):
    os.system("jupyter nbconvert --to notebook --execute Code_Saramin.ipynb --inplace")
    os.system("jupyter nbconvert --to notebook --execute Code_Jobkorea.ipynb --inplace")
    st.success("채용공고 수집 완료!")

# 데이터 로딩
def load_data():
    try:
        df_saramin = pd.read_csv("data_tmp/data_saramin.csv")
        df_jobkorea = pd.read_csv("data_tmp/data_jobkorea.csv")
        df = pd.concat([df_saramin, df_jobkorea], ignore_index=True)
        return df
    except:
        st.warning("데이터 파일을 불러올 수 없습니다.")
        return pd.DataFrame()

# 데이터프레임 출력
df_all = load_data()
if not df_all.empty:
    st.dataframe(df_all)

    # 통계 요약
    count_by_site = df_all["Site"].value_counts().reset_index()
    count_by_site.columns = ["Site", "Count"]
    count_by_site["Ratio"] = round(count_by_site["Count"] / count_by_site["Count"].sum() * 100, 2)
    st.table(count_by_site)

    # 파이차트 + 범례
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        count_by_site["Ratio"],
        autopct="%.1f%%",
        startangle=90
    )
    ax.axis("equal")
    ax.legend(wedges, count_by_site["Site"], loc="center left", bbox_to_anchor=(1, 0.5))
    st.markdown("Recruitment Ratio")
    st.pyplot(fig)