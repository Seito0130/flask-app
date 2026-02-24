import os
from flask import Flask, render_template, request 

app = Flask(__name__, template_folder=os.path.join(os.getcwd(),'templates'),static_folder=os.path.join(os.getcwd(),'static'))
@app.route('/')
def index():
    return render_template("index.html")

# --- 便利なアプリ ---

@app.route("/apps")

def apps():

    app_list = [

        {"name": "Gemini", "img": "app1.png", "desc": "最強のAIツール！使い勝手抜群。", "stars": "★★★★★", "site_url": "https://gemini.google.com/"},

        {"name": "Capcat", "img": "app2.png", "desc": "動画編集をこれ一本で！", "stars": "★★★★☆", "site_url": "https://www.capcut.com/"}
    ]
    return render_template("apps.html", apps=app_list)
# --- ポイ活ページ ---
@app.route("/poikatu")
def poikatu():
    poi_list = [
        {"name": "LINEポイント", "img": "poi1.png", "desc": "安全で稼ぎやすい！", "stars": "★★★★★", "site_url": "https://pointclub.line.me/"},
        {"name": "QuickPoint", "img": "poi2.jpg", "desc": "PayPay連携が神！", "stars": "★★★★☆", "site_url": "https://qp.vector.co.jp/entry.php"},
        {"name": "TikTokLite", "img": "poi3.png", "desc": "動画を見るだけで貯まる！", "stars": "★★★★☆", "site_url": "https://www.tiktok.com/ja-JP/"}
    ]
    return render_template("poikatu.html", apps=poi_list)
# --- おすすめ商品 ---
@app.route("/items")
def items():
    item_list = [
        {"name": "shiroのwhite lily", "img": "item1.jpg", "desc": "コスパ最強の香水！", "stars": "★★★★★", "site_url": "https://shiro-shiro.jp/item/12722.html?srsltid=AfmBOooH3T9kaMWwxH4q3CHwG_dx7WB3N4WLco9LVAMEslncDUDzRIbB"},
        {"name": "Applewatch", "img": "item2.jpg", "desc": "モチベ上がる！ スマホをいちいち操作しなくてもこれで簡潔！ ","stars": "★★★★★", "site_url": "https://www.amazon.co.jp/Apple-Watch-GPS%E3%83%A2%E3%83%87%E3%83%AB-46mm%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%82%A2%E3%83%AB%E3%83%9F%E3%83%8B%E3%82%A6%E3%83%A0%E3%82%B1%E3%83%BC%E3%82%B9%E3%81%A8%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%84%E3%83%90%E3%83%B3%E3%83%89/dp/B0FQG2B81Z/ref=sr_1_4?dib=eyJ2IjoiMSJ9.9_0YHjvm96XsGaEtxhSjavawmGZEzf1gnoJAvvYOTQehb9AovlMnYeNukmev5gjwONtUcpO02OEUR7ZDgL9j2u9wqzgfbcuE2VPhemWvrcdi13lQfr_2kWqJlxP4EMOLA6bfa0-6CaGlzOiw1pc8UZGhRUaNTKk7-gUHyq-CfGpdHdWksz7npMEmgqI9sx-y76rcBwzakALDM5fUJdOhWZReet_aYhI0w4MEnAbTy66_VgAdxJ4KY6wIzX34CFo2UjQ2_bTS8RAVCEWWBkOUIpYgnN5YI8V8ZEwAemAtaIc.bixoOuBWvEIhZCBMJZS5JrhwmXnKR2cVvEbEZfedoC4&dib_tag=se&keywords=%E3%82%A2%E3%83%83%E3%83%97%E3%83%AB%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81&qid=1771943284&sr=8-4&th=1"}

    ]

    return render_template("items.html", items=item_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # ssl_context='adhoc' でHTTPS化テスト
    app.run(host="0.0.0.0", port=port)