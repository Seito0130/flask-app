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



        {"name": "LINEポイント", "img": "poi1.png", "desc": "安全で稼ぎやすい！", "stars": "★★★★★", "site_url": "#"},



        {"name": "QuickPoint", "img": "poi2.jpg", "desc": "PayPay連携が神！", "stars": "★★★★☆", "site_url": "#"},



        {"name": "TikTokLite", "img": "poi3.png", "desc": "動画を見るだけで貯まる！", "stars": "★★★★☆", "site_url": "#"}



    ]



    return render_template("poikatu.html", apps=poi_list)







# --- おすすめ商品 ---



@app.route("/items")



def items():



    item_list = [



        {"name": "shiroのwhite lily", "img": "item1.jpg", "desc": "コスパ最強の香水！", "stars": "★★★★★", "https://shiro-shiro.jp/item/12722.html?category_from=250": "#"},



        {"name": "Applewatch", "img": "item2.jpg", "desc": "モチベ上がる！ スマホをいちいち操作しなくてもこれで簡潔！", "stars": "★★★★★", "https://www.amazon.co.jp/dp/B0FQGP2P41/ref=fs_a_w_2?th=1": "#"}

    ]

    return render_template("items.html", items=item_list)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    # ssl_context='adhoc' でHTTPS化テスト
    app.run(host="0.0.0.0", port=port)