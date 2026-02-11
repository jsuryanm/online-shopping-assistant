#  Online Shopping Assistant

An AI-powered e-commerce chatbot that understands natural language user
queries, routes them to the correct handler (FAQ or SQL product
database), and responds with helpful answers using semantic search and
chain logic.

------------------------------------------------------------------------

## 🚀 Features

-   Semantic intent routing (FAQ vs SQL)
-   FAQ support using RAG
-   SQL-based product search
-   Interactive Streamlit chat UI
-   Modular and extensible architecture

------------------------------------------------------------------------

## 🧠 How It Works

1.  User enters a query in the Streamlit interface.
2.  A semantic router classifies the query (FAQ or SQL).
3.  Based on the route:
    -   FAQ queries use contextual retrieval.
    -   SQL queries search the product database.
4.  The assistant returns a relevant response.

------------------------------------------------------------------------

## 📦 Installation

``` bash
git clone https://github.com/jsuryanm/online-shopping-assistant.git
cd online-shopping-assistant
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ Run the App

``` bash
streamlit run app/main.py
```

------------------------------------------------------------------------

## 📁 Project Structure

    ├── app/                  # Streamlit UI
    ├── router.py             # Semantic router
    ├── faq.py                # FAQ ingestion + chain
    ├── sql.py                # SQL query chain
    ├── resources/            # Data files
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

##  Customization

-   Expand `resources/faq_data.csv` to improve FAQ routing.
-   Add more routes to scale the assistant (e.g., orders, complaints,
    recommendations).

------------------------------------------------------------------------

## License

MIT License
