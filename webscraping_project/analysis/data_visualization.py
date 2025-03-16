# # import pandas as pd
# # import plotly.express as px

# # def main():
# #     file_path = r"books.xlsx"
# #     df = pd.read_excel(file_path)
# #     print(df.head())
# #     avg_price_df = (
# #         df.groupby("Category")["Price"]
# #         .mean()
# #         .reset_index()
# #         .sort_values(by="Price", ascending=False)
# #     )
# #     fig_bar = px.bar(
# #         avg_price_df,
# #         x="Category",
# #         y="Price",
# #         color="Category",
# #         text="Price",
# #         color_discrete_sequence=px.colors.qualitative.Plotly,
# #         title="Average Book Price by Category"
# #     )
# #     fig_bar.update_traces(texttemplate='$%{text:.2f}', textposition='outside')
# #     fig_bar.update_layout(
# #         template="plotly_white",
# #         title=dict(text="Average Book Price by Category", y=0.95, x=0.5),
# #         xaxis_title="Book Category",
# #         yaxis_title="Average Price ($)",
# #         font=dict(family="Arial, sans-serif", size=14, color="#333333"),
# #         legend_title="Category",
# #         margin=dict(l=40, r=40, t=80, b=40)
# #     )
# #     fig_bar.update_yaxes(tickprefix="$")
# #     fig_bar.show()

# # if __name__ == "__main__":
# #     main()




# import pandas as pd
# import plotly.express as px

# def main():
#     file_path = r"books.xlsx"
#     df = pd.read_excel(file_path)

#     # Calculate average price by category (for line chart)
#     avg_price_df = (
#         df.groupby("Category")["Price"]
#         .mean()
#         .reset_index()
#         .sort_values(by="Price", ascending=False)
#     )
    
#     # Calculate book count by category (for bar and pie charts)
#     count_df = df.groupby("Category").size().reset_index(name="Count")

#     # 1. Line Chart: Average Price by Category
#     fig_line = px.line(
#         avg_price_df,
#         x="Category",
#         y="Price",
#         markers=True,
#         title="Average Book Price by Category (Line Chart)",
#         template="plotly_white"
#     )
#     fig_line.update_layout(
#         title=dict(font=dict(family="Helvetica", size=20, color="#333"), x=0.5),
#         xaxis_title="Category",
#         yaxis_title="Average Price ($)",
#         font=dict(family="Helvetica", size=14, color="#333"),
#         margin=dict(l=40, r=40, t=80, b=40)
#     )
#     fig_line.update_yaxes(tickprefix="$")
#     fig_line.show()

#     # 2. Bar Chart: Book Count by Category
#     fig_bar = px.bar(
#         count_df,
#         x="Category",
#         y="Count",
#         color="Category",
#         title="Book Count by Category (Bar Chart)",
#         template="plotly_white"
#     )
#     fig_bar.update_layout(
#         title=dict(font=dict(family="Helvetica", size=20, color="#333"), x=0.5),
#         xaxis_title="Category",
#         yaxis_title="Book Count",
#         font=dict(family="Helvetica", size=14, color="#333"),
#         margin=dict(l=40, r=40, t=80, b=40)
#     )
#     fig_bar.show()

#     # 3. Pie Chart: Book Count by Category
#     fig_pie = px.pie(
#         count_df,
#         names="Category",
#         values="Count",
#         title="Book Count by Category (Pie Chart)",
#         template="plotly_white"
#     )
#     fig_pie.update_layout(
#         title=dict(font=dict(family="Helvetica", size=20, color="#333"), x=0.5),
#         font=dict(family="Helvetica", size=14, color="#333"),
#         margin=dict(l=40, r=40, t=80, b=40)
#     )
#     fig_pie.show()

# if __name__ == "__main__":
#     main()




import pandas as pd
import plotly.express as px

def main():
    file_path = r"books.xlsx"
    df = pd.read_excel(file_path)

    # 1) Prepare DataFrames
    # Average price by category (sort descending by price)
    avg_price_df = (
        df.groupby("Category")["Price"]
        .mean()
        .reset_index()
        .sort_values(by="Price", ascending=False)
    )
    
    # Book count by category (sort descending by count)
    count_df = df.groupby("Category")["Price"].count().reset_index(name="Count")
    count_df.sort_values(by="Count", ascending=False, inplace=True)

    # 2) Line Chart: Average Price by Category (descending order)
    fig_line = px.line(
        avg_price_df,
        x="Category",
        y="Price",
        title="Average Book Price by Category"
    )
    # Remove markers so you don’t see points going “upward”
    fig_line.update_traces(mode='lines')
    fig_line.update_layout(
        xaxis_title="Category",
        yaxis_title="Average Price",
        margin=dict(l=40, r=40, t=80, b=40)
    )
    fig_line.show()

    # 3) Bar Chart: Book Count by Category (descending order)
    fig_bar = px.bar(
        count_df,
        x="Category",
        y="Count",
        color="Category",
        title="Book Count by Category"
    )
    fig_bar.update_layout(
        xaxis_title="Category",
        yaxis_title="Count",
        margin=dict(l=40, r=40, t=80, b=40)
    )
    fig_bar.show()

    # 4) Pie Chart: Book Count by Category
    fig_pie = px.pie(
        count_df,
        names="Category",
        values="Count",
        title="Distribution of Books by Category"
    )
    fig_pie.update_layout(
        margin=dict(l=40, r=40, t=80, b=40)
    )
    fig_pie.show()

if __name__ == "__main__":
    main()

