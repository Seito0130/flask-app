import os
from flask import Flask, render_template, request 

app = Flask(__name__, template_folder=os.path.join(os.getcwd(),'templates'), static_folder=os.path.join(os.getcwd(),'static'))

@app.route('/')
def index():
    return render_template("index.html")

# --- 便利なアプリ ---
@app.route("/apps")
def apps():
    app_list = [
        {"name": "Gemini", "img": "app1.png", "desc": "最強のAIツール！使い勝手抜群。", "stars": "★★★★★", "site_url": "https://gemini.google.com/"},
        {"name": "Capcut", "img": "app2.png", "desc": "動画編集をこれ一本で！", "stars": "★★★★☆", "site_url": "https://www.capcut.com/"}
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
        {"name": "Applewatch", "img": "item2.jpg", "desc": "モチベ上がる！ スマホをいちいち操作しなくてもこれで簡潔！ ","stars": "★★★★★", "site_url": "https://www.amazon.co.jp/Apple-Watch-GPS%E3%83%A2%E3%83%87%E3%83%AB-46mm%E3%82%B8%E3%82%A7%E3%83%83%E3%83%88%E3%83%96%E3%83%A9%E3%83%83%E3%82%AF%E3%82%B9%E3%83%9D%E3%83%BC%E3%83%84%E3%83%90%E3%83%B3%E3%83%89/dp/B0FQG2B81Z/"}
    ]
    return render_template("items.html", items=item_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # 修正ポイント：SSL設定を一旦外し、シンプルに起動させる
    app.run(host="0.0.0.0", port=port)