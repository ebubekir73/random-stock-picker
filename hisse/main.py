from flask import Flask, render_template
app = Flask(__name__)
import random

bist100_symbols = [
    "AKBNK", "ARCLK", "ASELS", "BIMAS", "DOHOL", "EKGYO", "EREGL", "FROTO", "GARAN", "GUBRF",
    "HALKB", "HEKTS", "ISCTR", "KRDMD", "KOZAA", "KOZAL", "KCHOL", "OTKAR", "PETKM", "PGSUS",
    "SAHOL", "SISE", "SOKM", "TCELL", "THYAO", "TOASO", "TUPRS", "VAKBN", "YKBNK", "ZOREN",
    "AGHOL", "AKSEN", "ALARK", "ALBRK", "ARCLK", "AVISA", "AYGAZ", "BIZIM", "BRSAN", "CCOLA",
    "CIMSA", "CMBTN", "DEVA", "ENKAI", "ENJSA", "GENTS", "GSDHO", "INDES", "ISFIN", "ISGYO",
    "IZMDC", "KARTN", "KLMSN", "KORDS", "KZBGY", "LOGO", "MGROS", "NETAS", "ODAS", "OTOKAR",
    "PINSU", "PRKME", "SELEC", "SEKUR", "SODA", "TATGD", "TOASO", "TRCAS", "TRGYO", "TSKB",
    "TTKOM", "TURSG", "TURTT", "ULKER", "VESTL", "YATAS", "YKGYO"
]


@app.route('/')
def index():
    def get_random_stock_symbol():
        return random.choice(bist100_symbols)

    output = get_random_stock_symbol()

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
