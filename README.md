# Project Overview
This project automates the process of downloading and analyzing 10-K filings from the SEC's EDGAR database for specified companies. It involves two main Python scripts: download_sc_file.py for retrieving the filings and georgia.py for analyzing a specific year's data.

# download_sc_file.py
1. Purpose: Downloads 10-K filings for a specified company using its ticker symbol.

2. How It Works:

  a. The user inputs the ticker symbol of the company.
  b. The script accesses the SEC EDGAR database and retrieves the 10-K filings.
  c. It downloads the filings and extracts all text, storing the content in the sec-edgar-filings directory.

# georgia.py
1. Purpose: Analyzes the downloaded 10-K filings for a given year to provide insights into the company's financial and operational performance.

2. Output Example: The script outputs a detailed analysis of the company's revenue, profitability, costs, and other financial insights for the specified fiscal year. The analysis includes trends in net sales, gross margin, net income, R&D spending, and more, with specific percentage changes and influential factors highlighted.

3. Analysis Workflow:

  a. Extract data for the specified year from the sec-edgar-filings directory.
  b. Analyze various financial metrics such as revenue growth, profitability, and expenditure trends.
  c. Summarize findings in a structured format, providing context and insights into the data.

# Sample Output Structure

Analysis of Apple Computer Inc.'s 10-K Filing (Fiscal Year Ended September 29, 1995)

The provided text is a portion of Apple Computer Inc.'s 10-K filing for the fiscal year ended September 29, 1995. Here's an analysis of the company's financial performance based on the information provided:

**Revenue:**

* **Net Sales Growth:** Apple experienced significant net sales growth in both 1995 (20%) and 1994 (15%) compared to the previous years. This growth was primarily driven by:
    * **Unit Sales Growth:** Strong sales of Power Macintosh products and newer offerings within the Performa and Powerbook families contributed to increased unit sales.
    * **Higher Average Selling Prices:** A shift in product mix towards newer, higher-margin products like the Power Macintosh line led to an increase in average revenue per unit.
* **International Sales:** International sales played a crucial role, representing 48% of net sales in 1995. Strong growth was observed in the Pacific region, particularly Japan, aided by favorable currency exchange rates.

**Profitability:**

* **Gross Margin:**
    * **1995:** Gross margin increased both in amount and as a percentage of net sales compared to 1994. This was primarily due to a shift in product mix towards newer, high-margin products and favorable currency exchange rate changes.  
    * **1994:** Gross margin declined compared to 1993 due to pricing actions taken in response to industry-wide competitive pressures and slightly unfavorable currency exchange rate changes.
    * **Future Outlook:** The company anticipates continued pressure on gross margins due to ongoing industry-wide pricing pressures, increased competition, and compressed product life cycles.
* **Net Income:** Net income increased significantly in 1995 (37%) compared to 1994, reflecting the growth in sales and improved gross margin.

**Costs:**

* **Research and Development (R&D):** R&D expenditures increased in 1995 compared to 1994 due to higher project headcount and related spending. However, as a percentage of net sales, R&D expenses decreased due to revenue growth and focused spending efforts.
* **Selling, General, and Administrative (SG&A):** SG&A expenses increased in amount but decreased as a percentage of net sales in 1995 compared to 1994. The increase was primarily due to higher advertising and channel marketing program spending to expand market share.
* **Restructuring Costs:** Apple incurred significant restructuring costs in 1993 and 1994 as part of a plan to address competitive conditions and improve efficiency. These costs decreased significantly in 1995 as the restructuring plan neared completion.

**Other Financial Insights:**

* **Backlog:** While the backlog decreased slightly in 1995, it primarily consisted of higher-end Power Macintosh products. The company expected most of these orders to be shipped or canceled in fiscal 1996.
* **Competition:** The filing highlights the intensely competitive nature of the personal computer industry, with rapid technological advancements, frequent new product introductions, and aggressive pricing practices. Apple faces competition from companies like Microsoft and IBM, particularly in the operating system and microprocessor segments.
* **Research and Development:** Apple emphasizes the importance of continued R&D investment for future growth and competitiveness.
* **Global Market Risks:** The company acknowledges risks associated with its significant international operations, such as fluctuations in foreign currency exchange rates and economic conditions in foreign markets.
* **Inventory and Supply:** Apple identifies the availability of key components, such as microprocessors and ASICs, as a potential constraint on its ability to meet product demand.
* **Liquidity and Capital Resources:** Apple believes its cash, cash equivalents, short-term investments, and borrowing capabilities are sufficient to meet its operating cash requirements in the short and long term.


**Overall, Apple's financial performance in fiscal year 1995 was strong, driven by successful new product introductions and growth in both domestic and international markets. However, the company faces challenges from intense competition, potential supply constraints, and managing its exposure to global market risks.**

--------------------------------------------------

# Constraints
1. Token Limitation: The major constraint in this project is the token limit imposed by the LLM. Some 10-K filings are extensive and contain a large amount of text, which may exceed the token limit of the model during analysis. This issue can lead to incomplete analysis or the need to truncate the text, potentially omitting important information.
2. Potential Solutions:
   a. Implement a method to selectively extract and preprocess key sections of the 10-K filings to reduce input size.
   b. Split the analysis into smaller subsections and sequentially process each part to stay within the token limit.

# Conclusion
This project leverages the power of language models to provide an automated, in-depth analysis of company 10-K filings, helping users quickly understand complex financial documents. While the token limit poses a challenge, strategic data handling can mitigate this issue, ensuring comprehensive coverage of the filings.
