import plotly.express as px
import pandas as pd

wide_df = pd.DataFrame(dict(Month=["Jan", "Feb", "Mar"], London=[1,2,3], Paris=[3,1,2]))
tidy_df = wide_df.melt(id_vars="Month")

# print(wide_df)

# print(tidy_df)


df = px.data.iris()

print(df)




fig = px.bar(tidy_df, x="Month", y="value", color="variable", barmode="group")
# fig.show()

