import pandas as pd
from fpdf import FPDF

df = pd.read_csv("articles.csv", dtype={"id": str})  # Ensure all data is read as strings
print(df)

class Article:
    def __init__(self, article_id):
        self.article_id = article_id
        self.name = df.loc[df["id"] == self.article_id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.article_id, "price"].squeeze()

    def available(self):
        """Check if the article is available for purchase."""
        in_stock = df.loc[df["id"] == self.article_id, "in stock"].squeeze()
        return in_stock
    
class Receipt:
    def __init__(self, article):
        self.article = article
    
    def generate_receipt(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr. {self.article.article_id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")

article_ID = input("Enter the article ID: ")
article = Article(article_id=article_ID)
if article.available():
    receipt = Receipt(article)
    receipt.generate_receipt()
else:
    print(f"Article with ID {article_ID} is not available for purchase.")

    
       


