from semantic_router import Route
from semantic_router.encoders import HuggingFaceEncoder
from semantic_router.routers import SemanticRouter
from semantic_router.index import LocalIndex

faq = Route(
    name="faq",
    utterances=[
        "What is the return policy?",
        "What is your return policy?",
        "How do I return a product?",
        "Can I return a defective product?",
        "What if my item is damaged?",
        "What is your policy on defective items?",
        "Refund policy for damaged goods",
        "How long does refund take?",
        "How do refunds work?",
        "What happens if I receive a faulty product?"
    ]
)

sql = Route(
    name="sql",
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any other shoes under Rs. 5000?",
        "Do you have formal shoes in size 9?",
        "Are there any puma shoes on sale?",
        "What is the price of puma running shoes?"
    ]
)

routes = [faq,sql]
encoder = HuggingFaceEncoder(name="sentence-transformers/all-MiniLM-L6-v2")
index = LocalIndex()

router = SemanticRouter(encoder=encoder,
                        routes=routes,
                        auto_sync="local",
                        index=index)
# router.sync_

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 10000").name)