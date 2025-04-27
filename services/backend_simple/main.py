from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    response = {
        'items': [
                   { 'id': 1, 'title': 'Slim Fitness Fashion', 'subtitle': 'Chapéu Panamá Shangtung Casual Unissex Aba Larga', 'source':'https://m.media-amazon.com/images/I/61biqqRtsfL._AC_UL320_.jpg', 'price': 35.90, 'qtd': 0 },
                   { 'id': 2, 'title': 'GEMVIE', 'subtitle': 'Chapéu Panamá de palha verão', 'source':'https://m.media-amazon.com/images/I/81JkyFwqipL._AC_UL320_.jpg', 'price': 45.00, 'qtd': 0 },
                   { 'id': 3, 'title': 'Genérico', 'subtitle': 'Chapéu Pescador Camping Australiano', 'source':'https://m.media-amazon.com/images/I/4152xzA-b6L._AC_UL320_.jpg', 'price': 36.90, 'qtd': 0 },
                   { 'id': 4, 'title': 'HHW', 'subtitle': 'Chapéu Country Rodeio Festa Cowboy Boiadeira Camurça Moda Unissex.', 'source':'https://m.media-amazon.com/images/I/615plFGN8OL._AC_UL320_.jpg', 'price': 38.00, 'qtd': 0 },
                   { 'id': 5, 'title': 'Couros Allas', 'subtitle': 'Chapéu De Palha Carnaúba Natural Country Marcatto.', 'source':'https://m.media-amazon.com/images/I/51KJ33Ts-4L._AC_UL320_.jpg', 'price': 49.90, 'qtd': 0 },
                   { 'id': 6, 'title': 'Adidas', 'subtitle': 'Chapéu Balde Utility Boonie Bucket Hat.', 'source':'https://m.media-amazon.com/images/I/71mRuk8kDYS._AC_UL320_.jpg', 'price': 393.11, 'qtd': 0 },
                   { 'id': 7, 'title': 'Kouk Authentic', 'subtitle': 'Chapéu Fedora Panamá Aveludado Feltro Macio com Faixa Aba Larga.', 'source':'https://m.media-amazon.com/images/I/611uRwBHxwL._AC_UL320_.jpg', 'price': 64.99, 'qtd': 0 },
                   { 'id': 8, 'title': 'Bogu Store', 'subtitle': 'Chapéu De Palha Chinês de Fibra Natural De Bambu Pescador.', 'source':'https://m.media-amazon.com/images/I/71fGO8i7KqL._AC_UL320_.jpg', 'price': 45.00, 'qtd': 0 },
                 ]
    }
    return response


if __name__ == '__main__':
    from uvicorn import run
    run("main:app", reload=True)