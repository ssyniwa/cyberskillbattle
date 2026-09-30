import random
import streamlit as st

# ページ設定とサイバーパンク風カスタムCSS
st.set_page_config(
    page_title="CYBER_DECK: 10_STAGES_ENVIRONMENTS", page_icon="⚡", layout="wide"
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0b0f19;
        color: #00ffcc;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button {
        background-color: #1a1a2e;
        color: #00ffcc;
        border: 1px solid #00ffcc;
        border-radius: 4px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ffcc;
        color: #0b0f19;
    }
    .card-box {
        background: #16213e;
        border: 1px solid #ff007f;
        padding: 10px;
        border-radius: 6px;
        margin-bottom: 10px;
    }
    .enemy-box {
        background: #2b131a;
        border: 1px solid #ff3333;
        padding: 10px;
        border-radius: 6px;
    }
    .ally-box {
        background: #13272b;
        border: 1px solid #00ffff;
        padding: 10px;
        border-radius: 6px;
    }
    .env-box {
        background: #1f1a2e;
        border: 1px solid #bd00ff;
        padding: 8px;
        border-radius: 6px;
        margin-bottom: 10px;
        font-size: 0.9em;
    }
    .story-box {
        background: #121826;
        border: 2px solid #00ffcc;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    .enemy-skill-log {
        background: #2b131a;
        border: 1px dashed #ff3333;
        padding: 8px;
        border-radius: 6px;
        margin-top: 5px;
        margin-bottom: 5px;
    }
    .warning-box {
        background: #3d0f15;
        border: 2px solid #ff3333;
        padding: 10px;
        border-radius: 6px;
        color: #ff9999;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .score-box {
        background: #16213e;
        border: 2px solid #00ffcc;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 1. 味方キャラクターデータ (3体×10スキル)
# ==========================================
ALLIES_DATA = [
    {
        "name": "詩音 (サイバーニンジャ)",
        "image_path": "assets/allies/shion.jpg",
        "hp": 110,
        "skills": [
            {"name": "ブレードスラッシュ", "type": "attack", "val": 20, "img": "assets/skills/s1.jpg"},
            {"name": "影分身ステップ", "type": "shield", "val": 15, "img": "assets/skills/s2.jpg"},
            {"name": "クナイ連擲", "type": "attack", "val": 25, "img": "assets/skills/s3.jpg"},
            {"name": "ナノマシン応急処置", "type": "heal", "val": 25, "img": "assets/skills/s4.jpg"},
            {"name": "超感覚アイ", "type": "ram", "val": 2, "img": "assets/skills/s5.jpg"},
            {"name": "プラズマ居合", "type": "attack", "val": 40, "img": "assets/skills/s6.jpg"},
            {"name": "ステルス", "type": "shield", "val": 30, "img": "assets/skills/s7.jpg"},
            {"name": "ファントム", "type": "attack", "val": 55, "img": "assets/skills/s8.jpg"},
            {"name": "自己修復", "type": "heal", "val": 50, "img": "assets/skills/s9.jpg"},
            {"name": "アクセラレート", "type": "ram", "val": 2, "img": "assets/skills/s10.jpg"},
        ],
    },
    {
        "name": "サイファー (スナイパー)",
        "image_path": "assets/allies/cypher.jpg",
        "hp": 85,
        "skills": [
            {"name": "精密ショット", "type": "attack", "val": 22, "img": "assets/skills/c1.jpg"},
            {"name": "カモフラ", "type": "shield", "val": 12, "img": "assets/skills/c2.jpg"},
            {"name": "アーマーピアス", "type": "attack", "val": 30, "img": "assets/skills/c3.jpg"},
            {"name": "メディキット", "type": "heal", "val": 20, "img": "assets/skills/c4.jpg"},
            {"name": "ターゲティング", "type": "ram", "val": 2, "img": "assets/skills/c5.jpg"},
            {"name": "ハイパースナイプ", "type": "attack", "val": 45, "img": "assets/skills/c6.jpg"},
            {"name": "デコイ展開", "type": "shield", "val": 25, "img": "assets/skills/c7.jpg"},
            {"name": "バースト狙撃", "type": "attack", "val": 60, "img": "assets/skills/c8.jpg"},
            {"name": "メディドローン", "type": "heal", "val": 40, "img": "assets/skills/c9.jpg"},
            {"name": "オーバークロック", "type": "ram", "val": 2, "img": "assets/skills/c10.jpg"},
        ],
    },
    {
        "name": "アイリーン (重装アーマー)",
        "image_path": "assets/allies/irene.jpg",
        "hp": 130,
        "skills": [
            {"name": "バルカン", "type": "attack", "val": 18, "img": "assets/skills/i1.jpg"},
            {"name": "バリア", "type": "shield", "val": 20, "img": "assets/skills/i2.jpg"},
            {"name": "マイクロミサイル", "type": "attack", "val": 35, "img": "assets/skills/i3.jpg"},
            {"name": "システムパッチ", "type": "heal", "val": 30, "img": "assets/skills/i4.jpg"},
            {"name": "ジェネレーター", "type": "ram", "val": 2, "img": "assets/skills/i5.jpg"},
            {"name": "プラズマキャノン", "type": "attack", "val": 50, "img": "assets/skills/i6.jpg"},
            {"name": "重装フィールド", "type": "shield", "val": 40, "img": "assets/skills/i7.jpg"},
            {"name": "ストライクボム", "type": "attack", "val": 70, "img": "assets/skills/i8.jpg"},
            {"name": "オーバーホール", "type": "heal", "val": 60, "img": "assets/skills/i9.jpg"},
            {"name": "コアチャージ", "type": "ram", "val": 3, "img": "assets/skills/i10.jpg"},
        ],
    },
]

# ==========================================
# 2. 10ステージ×7種類の個別敵データ＆環境・ストーリー定義
# ==========================================
STAGES_DATA = [
    {
        "stage": 1,
        "env_name": "アンダーシティ・スラム (酸性雨降る底辺街)",
        "env_desc": "視界不良のスラム街。錆びついた治安維持ドローンやギャングが襲い来る。",
        "prev_boss_name": "なし",
        "story_image": "assets/story/stage1.jpg",
        "story_intro": (
            "深夜のアンダーシティ。冷たい酸性雨が降り注ぐ中、治安部隊として夜勤についていた"
            "詩音、サイファー、アイリーンの3人は、無線から不穏な緊急通報を受信した。\n\n"
            "『こちらスラム外縁部……何者かが治安ネットワークをハッキングし、暴徒を扇動している！急行せよ！』\n\n"
            "「夜更けの仕事はこれだから面倒さね」とアイリーンが銃口を点検し、"
            "サイファーが遠方の敵影をスコープにとらえる。詩音は静かに刀の柄に手を掛けた。"
            "3人はサイバーバイクを起動し、事件の渦中へと走り出した。"
        ),
        "enemies": [
            {"name": "スクラップ・ドローン", "image_path": "assets/e/1_1.jpg", "hp": 60, "skills": [{"name": "電撃スパーク", "type": "attack", "val": 10, "pierce": False, "img": "assets/sk/1_1_1.jpg"}, {"name": "体当たり", "type": "attack", "val": 14, "pierce": False, "img": "assets/sk/1_1_2.jpg"}, {"name": "自己防壁", "type": "buff", "val": 5, "img": "assets/sk/1_1_3.jpg"}]},
            {"name": "ストリート・プンク", "image_path": "assets/e/1_2.jpg", "hp": 70, "skills": [{"name": "鉄パイプ殴打", "type": "attack", "val": 12, "pierce": False, "img": "assets/sk/1_2_1.jpg"}, {"name": "飛び蹴り", "type": "attack", "val": 15, "pierce": False, "img": "assets/sk/1_2_2.jpg"}, {"name": "挑発", "type": "buff", "val": 8, "img": "assets/sk/1_2_3.jpg"}]},
            {"name": "ジャンク・ハッカー", "image_path": "assets/e/1_3.jpg", "hp": 65, "skills": [{"name": "ウィルス注入", "type": "attack", "val": 13, "pierce": True, "img": "assets/sk/1_3_1.jpg"}, {"name": "データ抜き", "type": "attack", "val": 16, "pierce": False, "img": "assets/sk/1_3_2.jpg"}, {"name": "隠蔽工作", "type": "buff", "val": 6, "img": "assets/sk/1_3_3.jpg"}]},
            {"name": "スラム・ドッグ", "image_path": "assets/e/1_4.jpg", "hp": 75, "skills": [{"name": "サイバー牙", "type": "attack", "val": 14, "pierce": False, "img": "assets/sk/1_4_1.jpg"}, {"name": "猛ダッシュ", "type": "attack", "val": 18, "pierce": False, "img": "assets/sk/1_4_2.jpg"}, {"name": "遠吠え", "type": "buff", "val": 10, "img": "assets/sk/1_4_3.jpg"}]},
            {"name": "ブラック・ディーラー", "image_path": "assets/e/1_5.jpg", "hp": 80, "skills": [{"name": "毒針発射", "type": "attack", "val": 15, "pierce": True, "img": "assets/sk/1_5_1.jpg"}, {"name": "隠しナイフ", "type": "attack", "val": 19, "pierce": False, "img": "assets/sk/1_5_2.jpg"}, {"name": "煙幕", "type": "buff", "val": 12, "img": "assets/sk/1_5_3.jpg"}]},
            {"name": "アンダー・エンフォーサー", "image_path": "assets/e/1_6.jpg", "hp": 90, "skills": [{"name": "ヘビーショット", "type": "attack", "val": 17, "pierce": False, "img": "assets/sk/1_6_1.jpg"}, {"name": "バットナックル", "type": "attack", "val": 21, "pierce": False, "img": "assets/sk/1_6_2.jpg"}, {"name": "硬質化", "type": "buff", "val": 15, "img": "assets/sk/1_6_3.jpg"}]},
            {"name": "【ボス】スラムの暴力王・ガレオン", "image_path": "assets/e/1_7.jpg", "hp": 150, "skills": [{"name": "ガトリング乱射", "type": "attack", "val": 22, "pierce": False, "img": "assets/sk/1_7_1.jpg"}, {"name": "メガトンプレス", "type": "attack", "val": 28, "pierce": True, "img": "assets/sk/1_7_2.jpg"}, {"name": "狂戦士の咆哮", "type": "buff", "val": 20, "img": "assets/sk/1_7_3.jpg"}]},
        ],
    },
    {
        "stage": 2,
        "env_name": "ネオン・カジノ地区 (欲望と電脳の歓楽街)",
        "env_desc": "きらびやかなホログラムが明滅する歓楽街。マフィアの手先が立ち塞がる。",
        "prev_boss_name": "スラムの暴力王・ガレオン",
        "story_image": "assets/story/stage2.jpg",
        "story_intro": (
            "スラム街の奥深くで「スラムの暴力王・ガレオン」を沈黙させた3人。\n"
            "ガレオンが残した端末のデータから、一連の事件の黒幕がネオン輝く歓楽街の裏で糸を引いていることが判明した。\n\n"
            "「どうやらお次は華やかなカジノ地区のご招待ってわけだ」\n\n"
            "きらびやかなホログラム看板が視界を埋め尽くすカジノ地区へとバイクを飛ばし、"
            "3人はマフィアの支配する不夜城へと潜入を開始する。"
        ),
        "enemies": [
            {"name": "カジノ・セキュリティー", "image_path": "assets/e/2_1.jpg", "hp": 80, "skills": [{"name": "スタンバトン", "type": "attack", "val": 14, "pierce": False, "img": "assets/sk/2_1_1.jpg"}, {"name": "ボディーブロー", "type": "attack", "val": 18, "pierce": False, "img": "assets/sk/2_1_2.jpg"}, {"name": "プロテクト", "type": "buff", "val": 10, "img": "assets/sk/2_1_3.jpg"}]},
            {"name": "シンジケート・ガード", "image_path": "assets/e/2_2.jpg", "hp": 85, "skills": [{"name": "サブマシンガン", "type": "attack", "val": 16, "pierce": False, "img": "assets/sk/2_2_1.jpg"}, {"name": "タックル", "type": "attack", "val": 20, "pierce": False, "img": "assets/sk/2_2_2.jpg"}, {"name": "防弾シールド", "type": "buff", "val": 12, "img": "assets/sk/2_2_3.jpg"}]},
            {"name": "サイバー・ホステス", "image_path": "assets/e/2_3.jpg", "hp": 75, "skills": [{"name": "魅惑のリップ", "type": "attack", "val": 15, "pierce": True, "img": "assets/sk/2_3_1.jpg"}, {"name": "毒入りグラス", "type": "attack", "val": 19, "pierce": False, "img": "assets/sk/2_3_2.jpg"}, {"name": "錯乱フェロモン", "type": "buff", "val": 14, "img": "assets/sk/2_3_3.jpg"}]},
            {"name": "カジノ・ディーラー", "image_path": "assets/e/2_4.jpg", "hp": 90, "skills": [{"name": "カードカッター", "type": "attack", "val": 17, "pierce": False, "img": "assets/sk/2_4_1.jpg"}, {"name": "ルーレットボム", "type": "attack", "val": 22, "pierce": False, "img": "assets/sk/2_4_2.jpg"}, {"name": "イカサマ演算", "type": "buff", "val": 15, "img": "assets/sk/2_4_3.jpg"}]},
            {"name": "アンドロイド・バトラー", "image_path": "assets/e/2_5.jpg", "hp": 95, "skills": [{"name": "シルバーブレード", "type": "attack", "val": 19, "pierce": False, "img": "assets/sk/2_5_1.jpg"}, {"name": "高速刺突", "type": "attack", "val": 24, "pierce": True, "img": "assets/sk/2_5_2.jpg"}, {"name": "精密計算", "type": "buff", "val": 18, "img": "assets/sk/2_5_3.jpg"}]},
            {"name": "マフィア・キャプテン", "image_path": "assets/e/2_6.jpg", "hp": 110, "skills": [{"name": "マグナムショット", "type": "attack", "val": 21, "pierce": False, "img": "assets/sk/2_6_1.jpg"}, {"name": "近接ウィップ", "type": "attack", "val": 26, "pierce": False, "img": "assets/sk/2_6_2.jpg"}, {"name": "組織の号令", "type": "buff", "val": 20, "img": "assets/sk/2_6_3.jpg"}]},
            {"name": "【ボス】カジノの支配人・ドン・バネッサ", "image_path": "assets/e/2_7.jpg", "hp": 180, "skills": [{"name": "ロイヤルストレート", "type": "attack", "val": 25, "pierce": False, "img": "assets/sk/2_7_1.jpg"}, {"name": "黄金の銃撃", "type": "attack", "val": 32, "pierce": True, "img": "assets/sk/2_7_2.jpg"}, {"name": "カジノ・パニック", "type": "buff", "val": 25, "img": "assets/sk/2_7_3.jpg"}]},
        ],
    },
    {
        "stage": 3,
        "env_name": "ハイテク工業プラント (自動化された無人工場)",
        "env_desc": "炎と蒸気が吹き出すメガコープの製造プラント。戦闘用ロボットが徘徊する。",
        "prev_boss_name": "カジノの支配人・ドン・バネッサ",
        "story_image": "assets/story/stage3.jpg",
        "story_intro": (
            "華やかなカジノの奥で「ドン・バネッサ」を追い詰め、組織の隠し口座情報を押さえた3人。\n"
            "資金の流れを追うと、街外れのメガコープ直営プラントへと繋がっていた。\n\n"
            "「ふん、あんな成金マフィアの背後には、でかい企業の影があったってわけね」\n\n"
            "ネオンの街をあとにして、熱気と金属音が響き渡る巨大工業プラントへ足を踏み入れる。"
        ),
        "enemies": [
            {"name": "オート・ワーカー", "image_path": "assets/e/3_1.jpg", "hp": 90, "skills": [{"name": "アームハンマー", "type": "attack", "val": 16, "pierce": False, "img": "assets/sk/3_1_1.jpg"}, {"name": "プラズマ溶接", "type": "attack", "val": 20, "pierce": False, "img": "assets/sk/3_1_2.jpg"}, {"name": "出力上昇", "type": "buff", "val": 12, "img": "assets/sk/3_1_3.jpg"}]},
            {"name": "ファクトリー・ドローン", "image_path": "assets/e/3_2.jpg", "hp": 85, "skills": [{"name": "レーザー照射", "type": "attack", "val": 18, "pierce": True, "img": "assets/sk/3_2_1.jpg"}, {"name": "突撃ドリル", "type": "attack", "val": 22, "pierce": False, "img": "assets/sk/3_2_2.jpg"}, {"name": "光学迷彩", "type": "buff", "val": 15, "img": "assets/sk/3_2_3.jpg"}]},
            {"name": "ウォー・ハウンド", "image_path": "assets/e/3_3.jpg", "hp": 100, "skills": [{"name": "超音波バイト", "type": "attack", "val": 19, "pierce": False, "img": "assets/sk/3_3_1.jpg"}, {"name": "フレイムブレス", "type": "attack", "val": 24, "pierce": False, "img": "assets/sk/3_3_2.jpg"}, {"name": "四肢強化", "type": "buff", "val": 16, "img": "assets/sk/3_3_3.jpg"}]},
            {"name": "セキュリティ・センチネル", "image_path": "assets/e/3_4.jpg", "hp": 110, "skills": [{"name": "パルスキャノン", "type": "attack", "val": 21, "pierce": False, "img": "assets/sk/3_4_1.jpg"}, {"name": "ショックウェーブ", "type": "attack", "val": 26, "pierce": True, "img": "assets/sk/3_4_2.jpg"}, {"name": "重装アーマー", "type": "buff", "val": 20, "img": "assets/sk/3_4_3.jpg"}]},
            {"name": "インダストリアル・ボット", "image_path": "assets/e/3_5.jpg", "hp": 120, "skills": [{"name": "クラッシャー", "type": "attack", "val": 23, "pierce": False, "img": "assets/sk/3_5_1.jpg"}, {"name": "プレスアタック", "type": "attack", "val": 28, "pierce": False, "img": "assets/sk/3_5_2.jpg"}, {"name": "チタンボディ", "type": "buff", "val": 22, "img": "assets/sk/3_5_3.jpg"}]},
            {"name": "プラント・インスペクター", "image_path": "assets/e/3_6.jpg", "hp": 130, "skills": [{"name": "スキャンレーザー", "type": "attack", "val": 25, "pierce": True, "img": "assets/sk/3_6_1.jpg"}, {"name": "高圧電流", "type": "attack", "val": 30, "pierce": False, "img": "assets/sk/3_6_2.jpg"}, {"name": "システム分析", "type": "buff", "val": 24, "img": "assets/sk/3_6_3.jpg"}]},
            {"name": "【ボス】プラント監視AI・アイアン・マザー", "image_path": "assets/e/3_7.jpg", "hp": 210, "skills": [{"name": "オービットレーザー", "type": "attack", "val": 28, "pierce": False, "img": "assets/sk/3_7_1.jpg"}, {"name": "全方位ミサイル", "type": "attack", "val": 35, "pierce": True, "img": "assets/sk/3_7_2.jpg"}, {"name": "無限増産プロトコル", "type": "buff", "val": 30, "img": "assets/sk/3_7_3.jpg"}]},
        ],
    },
    {
        "stage": 4,
        "env_name": "地下下水道網 (汚染物質が流れ込む暗渠)",
        "env_desc": "悪臭と毒ガスが充満する地下水路。ミュータントや廃棄されたサイボーグが潜む。",
        "prev_boss_name": "プラント監視AI・アイアン・マザー",
        "story_image": "assets/story/stage4.jpg",
        "story_intro": (
            "暴走する「アイアン・マザー」の中枢コアを破壊し、プラントの機能を停止させた3人。\n"
            "プラントから排泄される不正廃棄物のルートを辿ると、都市の地下迷宮へと続いていた。\n\n"
            "「機械のクズどもを片付けたら、今度はドブネズミの匂いか。ご苦労なこったね」\n\n"
            "悪臭が鼻をつく地下下水道網へ下降し、汚染された暗渠に潜む脅威を排除するため進軍する。"
        ),
        "enemies": [
            {"name": "下水道のドブネズミ", "image_path": "assets/e/4_1.jpg", "hp": 95, "skills": [{"name": "猛毒かみつき", "type": "attack", "val": 18, "pierce": True, "img": "assets/sk/4_1_1.jpg"}, {"name": "不意打ち", "type": "attack", "val": 22, "pierce": False, "img": "assets/sk/4_1_2.jpg"}, {"name": "素早い身かわし", "type": "buff", "val": 15, "img": "assets/sk/4_1_3.jpg"}]},
            {"name": "廃棄サイボーグ", "image_path": "assets/e/4_2.jpg", "hp": 110, "skills": [{"name": "錆びたソード", "type": "attack", "val": 20, "pierce": False, "img": "assets/sk/4_2_1.jpg"}, {"name": "狂気の突進", "type": "attack", "val": 25, "pierce": False, "img": "assets/sk/4_2_2.jpg"}, {"name": "暴走回路", "type": "buff", "val": 18, "img": "assets/sk/4_2_3.jpg"}]},
            {"name": "ケミカル・スライム", "image_path": "assets/e/4_3.jpg", "hp": 120, "skills": [{"name": "酸の液滴", "type": "attack", "val": 22, "pierce": True, "img": "assets/sk/4_3_1.jpg"}, {"name": "溶解プレス", "type": "attack", "val": 27, "pierce": False, "img": "assets/sk/4_3_2.jpg"}, {"name": "弾力ボディ", "type": "buff", "val": 20, "img": "assets/sk/4_3_3.jpg"}]},
            {"name": "アンダーグラウンド・ゲリラ", "image_path": "assets/e/4_4.jpg", "hp": 115, "skills": [{"name": "ハンドグレネード", "type": "attack", "val": 24, "pierce": False, "img": "assets/sk/4_4_1.jpg"}, {"name": "アサルト射撃", "type": "attack", "val": 29, "pierce": False, "img": "assets/sk/4_4_2.jpg"}, {"name": "闇夜の潜伏", "type": "buff", "val": 22, "img": "assets/sk/4_4_3.jpg"}]},
            {"name": "ミュータント・ブル", "image_path": "assets/e/4_5.jpg", "hp": 135, "skills": [{"name": "猛角突進", "type": "attack", "val": 26, "pierce": False, "img": "assets/sk/4_5_1.jpg"}, {"name": "グランドスマッシュ", "type": "attack", "val": 32, "pierce": True, "img": "assets/sk/4_5_2.jpg"}, {"name": "怒涛の肉体", "type": "buff", "val": 25, "img": "assets/sk/4_5_3.jpg"}]},
            {"name": "トキシック・ストーカー", "image_path": "assets/e/4_6.jpg", "hp": 125, "skills": [{"name": "猛毒ニードル", "type": "attack", "val": 28, "pierce": True, "img": "assets/sk/4_6_1.jpg"}, {"name": "サイコネイル", "type": "attack", "val": 34, "pierce": False, "img": "assets/sk/4_6_2.jpg"}, {"name": "猛毒霧発生", "type": "buff", "val": 28, "img": "assets/sk/4_6_3.jpg"}]},
            {"name": "【ボス】下水道の主・バイオキメラ", "image_path": "assets/e/4_7.jpg", "hp": 240, "skills": [{"name": "アシッドブレス", "type": "attack", "val": 32, "pierce": True, "img": "assets/sk/4_7_1.jpg"}, {"name": "触手乱打", "type": "attack", "val": 38, "pierce": False, "img": "assets/sk/4_7_2.jpg"}, {"name": "超再生能力", "type": "buff", "val": 35, "img": "assets/sk/4_7_3.jpg"}]},
        ],
    },
    {
        "stage": 5,
        "env_name": "データ・サーバータワー (電脳の結界要塞)",
        "env_desc": "無数のサーバーラックが並ぶ仮想と現実の交差点。ネットセキュリティが襲い来る。",
        "prev_boss_name": "下水道の主・バイオキメラ",
        "story_image": "assets/story/stage5.jpg",
        "story_intro": (
            "地下水路の奥で「バイオキメラ」を討伐した3人。\n"
            "その肉片から回収された暗号キーは、都市のデータ通信中枢であるタワーへアクセスするためのものだった。\n\n"
            "「なるほど、地下水路はただの隠れ蓑。本丸のネットワークはここってわけね」\n\n"
            "タワーの防壁を突破するため、3人は電脳の結界要塞へとダイブする。"
        ),
        "enemies": [
            {"name": "アイス・ウォール", "image_path": "assets/e/5_1.jpg", "hp": 120, "skills": [{"name": "ファイアウォール弾", "type": "attack", "val": 23, "pierce": False, "img": "assets/sk/5_1_1.jpg"}, {"name": "データクラッシュ", "type": "attack", "val": 28, "pierce": False, "img": "assets/sk/5_1_2.jpg"}, {"name": "防壁展開", "type": "buff", "val": 25, "img": "assets/sk/5_1_3.jpg"}]},
            {"name": "ネット・スパイダー", "image_path": "assets/e/5_2.jpg", "hp": 110, "skills": [{"name": "ウェブストリング", "type": "attack", "val": 25, "pierce": True, "img": "assets/sk/5_2_1.jpg"}, {"name": "電脳ファング", "type": "attack", "val": 30, "pierce": False, "img": "assets/sk/5_2_2.jpg"}, {"name": "網の張巡り", "type": "buff", "val": 22, "img": "assets/sk/5_2_3.jpg"}]},
            {"name": "セキュリティ・アバター", "image_path": "assets/e/5_3.jpg", "hp": 130, "skills": [{"name": "ホログラムソード", "type": "attack", "val": 27, "pierce": False, "img": "assets/sk/5_3_1.jpg"}, {"name": "ライトニングレイ", "type": "attack", "val": 33, "pierce": True, "img": "assets/sk/5_3_2.jpg"}, {"name": "残像防御", "type": "buff", "val": 28, "img": "assets/sk/5_3_3.jpg"}]},
            {"name": "パケット・スニファー", "image_path": "assets/e/5_4.jpg", "hp": 125, "skills": [{"name": "データパケット", "type": "attack", "val": 29, "pierce": False, "img": "assets/sk/5_4_1.jpg"}, {"name": "情報バースト", "type": "attack", "val": 35, "pierce": False, "img": "assets/sk/5_4_2.jpg"}, {"name": "トラフィック解析", "type": "buff", "val": 30, "img": "assets/sk/5_4_3.jpg"}]},
            {"name": "プロキシ・サーベイヤー", "image_path": "assets/e/5_5.jpg", "hp": 140, "skills": [{"name": "プロキシ砲", "type": "attack", "val": 31, "pierce": True, "img": "assets/sk/5_5_1.jpg"}, {"name": "リダイレクト", "type": "attack", "val": 37, "pierce": False, "img": "assets/sk/5_5_2.jpg"}, {"name": "匿名化シールド", "type": "buff", "val": 32, "img": "assets/sk/5_5_3.jpg"}]},
            {"name": "エリート・ハッカー", "image_path": "assets/e/5_6.jpg", "hp": 150, "skills": [{"name": "ゼロデイアタック", "type": "attack", "val": 33, "pierce": True, "img": "assets/sk/5_6_1.jpg"}, {"name": "システムオーバー", "type": "attack", "val": 40, "pierce": False, "img": "assets/sk/5_6_2.jpg"}, {"name": "ディープクラック", "type": "buff", "val": 35, "img": "assets/sk/5_6_3.jpg"}]},
            {"name": "【ボス】防衛AI・ガーディアン・プライム", "image_path": "assets/e/5_7.jpg", "hp": 270, "skills": [{"name": "マスタージャッジメント", "type": "attack", "val": 36, "pierce": False, "img": "assets/sk/5_7_1.jpg"}, {"name": "ハイパーパルス", "type": "attack", "val": 44, "pierce": True, "img": "assets/sk/5_7_2.jpg"}, {"name": "絶対防壁起動", "type": "buff", "val": 40, "img": "assets/sk/5_7_3.jpg"}]},
        ],
    },
    {
        "stage": 6,
        "env_name": "高級コーポレート街 (富裕層の高層ビル群)",
        "env_desc": "きらびやかな高層ガラス都市。エリート警備部隊と高級ドローンが警護する。",
        "prev_boss_name": "防衛AI・ガーディアン・プライム",
        "story_image": "assets/story/stage6.jpg",
        "story_intro": (
            "データタワーの守護者「ガーディアン・プライム」をハッキングで打ち破った3人。\n"
            "タワーから抽出されたログは、富裕層が暮らす高級コーポレート街のビルへと繋がっていた。\n\n"
            "「いよいよお大尽どものお膝元か。治安部隊の権限を使って踏み込んでやろうじゃないか」\n\n"
            "高級ガラス都市の輝く高層ビル群へ向け、部隊の誇りを胸に歩みを進める。"
        ),
        "enemies": [
            {"name": "コープ・ガードマン", "image_path": "assets/e/6_1.jpg", "hp": 135, "skills": [{"name": "スマートライフル", "type": "attack", "val": 28, "pierce": False, "img": "assets/sk/6_1_1.jpg"}, {"name": "スタンアレスト", "type": "attack", "val": 34, "pierce": True, "img": "assets/sk/6_1_2.jpg"}, {"name": "コーポレート防壁", "type": "buff", "val": 30, "img": "assets/sk/6_1_3.jpg"}]},
            {"name": "エグゼクティブ・ホーク", "image_path": "assets/e/6_2.jpg", "hp": 130, "skills": [{"name": "エナジーボルト", "type": "attack", "val": 30, "pierce": False, "img": "assets/sk/6_2_1.jpg"}, {"name": "急降下爆撃", "type": "attack", "val": 36, "pierce": False, "img": "assets/sk/6_2_2.jpg"}, {"name": "高高度レーダー", "type": "buff", "val": 28, "img": "assets/sk/6_2_3.jpg"}]},
            {"name": "エリート・エンフォーサー", "image_path": "assets/e/6_3.jpg", "hp": 150, "skills": [{"name": "プラズマバースト", "type": "attack", "val": 32, "pierce": True, "img": "assets/sk/6_3_1.jpg"}, {"name": "アサルトチャージ", "type": "attack", "val": 39, "pierce": False, "img": "assets/sk/6_3_2.jpg"}, {"name": "アーマーコート", "type": "buff", "val": 35, "img": "assets/sk/6_3_3.jpg"}]},
            {"name": "コーポレート・スナイパー", "image_path": "assets/e/6_4.jpg", "hp": 140, "skills": [{"name": "ロングレンジ", "type": "attack", "val": 34, "pierce": False, "img": "assets/sk/6_4_1.jpg"}, {"name": "サイレントショット", "type": "attack", "val": 41, "pierce": True, "img": "assets/sk/6_4_2.jpg"}, {"name": "ピンポイント照準", "type": "buff", "val": 33, "img": "assets/sk/6_4_3.jpg"}]},
            {"name": "セキュリティ・アドバイザー", "image_path": "assets/e/6_5.jpg", "hp": 160, "skills": [{"name": "マインドクラッシュ", "type": "attack", "val": 36, "pierce": True, "img": "assets/sk/6_5_1.jpg"}, {"name": "レイザーウィップ", "type": "attack", "val": 43, "pierce": False, "img": "assets/sk/6_5_2.jpg"}, {"name": "リスクヘッジ", "type": "buff", "val": 38, "img": "assets/sk/6_5_3.jpg"}]},
            {"name": "サイボーグ・ボディガード", "image_path": "assets/e/6_6.jpg", "hp": 175, "skills": [{"name": "ヘビーパイル", "type": "attack", "val": 38, "pierce": True, "img": "assets/sk/6_6_1.jpg"}, {"name": "鉄拳制裁", "type": "attack", "val": 46, "pierce": False, "img": "assets/sk/6_6_2.jpg"}, {"name": "不屈の意志", "type": "buff", "val": 42, "img": "assets/sk/6_6_3.jpg"}]},
            {"name": "【ボス】治安維持本部長・ゼネラル・クロウ", "image_path": "assets/e/6_7.jpg", "hp": 310, "skills": [{"name": "オーダードミネーション", "type": "attack", "val": 42, "pierce": False, "img": "assets/sk/6_7_1.jpg"}, {"name": "ジャッジメント砲", "type": "attack", "val": 50, "pierce": True, "img": "assets/sk/6_7_2.jpg"}, {"name": "総司令発令", "type": "buff", "val": 45, "img": "assets/sk/6_7_3.jpg"}]},
        ],
    },
    {
        "stage": 7,
        "env_name": "廃墟の実験施設 (禁忌の研究が行われた地)",
        "env_desc": "放棄された不気味な地下研究所。改造された異形の存在がうごめく。",
        "prev_boss_name": "治安維持本部長・ゼネラル・クロウ",
        "story_image": "assets/story/stage7.jpg",
        "story_intro": (
            "腐敗した治安維持本部長「ゼネラル・クロウ」を撃破した3人。\n"
            "クロウが遺した機密ファイルには、都市の裏で行われていた禁忌の改造実験の記録が記されていた。\n\n"
            "「まさか、本部長自身がこんな悍ましい実験に関わっていたなんてね……」\n\n"
            "真実を暴くため、3人は荒れ果てた廃墟の実験施設へと潜入する。"
        ),
        "enemies": [
            {"name": "プロトタイプ・オブスキュア", "image_path": "assets/e/7_1.jpg", "hp": 150, "skills": [{"name": "異形クロー", "type": "attack", "val": 35, "pierce": True, "img": "assets/sk/7_1_1.jpg"}, {"name": "絶叫波", "type": "attack", "val": 42, "pierce": False, "img": "assets/sk/7_1_2.jpg"}, {"name": "暴走活性", "type": "buff", "val": 38, "img": "assets/sk/7_1_3.jpg"}]},
            {"name": "試作型サイボーグ・ゼロ", "image_path": "assets/e/7_2.jpg", "hp": 160, "skills": [{"name": "バーストブレード", "type": "attack", "val": 37, "pierce": False, "img": "assets/sk/7_2_1.jpg"}, {"name": "超高速突進", "type": "attack", "val": 44, "pierce": True, "img": "assets/sk/7_2_2.jpg"}, {"name": "冷却装置", "type": "buff", "val": 40, "img": "assets/sk/7_2_3.jpg"}]},
            {"name": "バイオ・ホラー", "image_path": "assets/e/7_3.jpg", "hp": 170, "skills": [{"name": "アシッドスピア", "type": "attack", "val": 39, "pierce": True, "img": "assets/sk/7_3_1.jpg"}, {"name": "寄生胞子", "type": "attack", "val": 47, "pierce": False, "img": "assets/sk/7_3_2.jpg"}, {"name": "変異再生", "type": "buff", "val": 42, "img": "assets/sk/7_3_3.jpg"}]},
            {"name": "マッド・ホムンクルス", "image_path": "assets/e/7_4.jpg", "hp": 165, "skills": [{"name": "ケミカルボム", "type": "attack", "val": 41, "pierce": False, "img": "assets/sk/7_4_1.jpg"}, {"name": "ダークパルス", "type": "attack", "val": 49, "pierce": True, "img": "assets/sk/7_4_2.jpg"}, {"name": "狂気の人形劇", "type": "buff", "val": 44, "img": "assets/sk/7_4_3.jpg"}]},
            {"name": "キメラ・ハウンド", "image_path": "assets/e/7_5.jpg", "hp": 180, "skills": [{"name": "トリプルファング", "type": "attack", "val": 43, "pierce": True, "img": "assets/sk/7_5_1.jpg"}, {"name": "ヘルファイヤー", "type": "attack", "val": 52, "pierce": False, "img": "assets/sk/7_5_2.jpg"}, {"name": "獣の咆哮", "type": "buff", "val": 46, "img": "assets/sk/7_5_3.jpg"}]},
            {"name": "アノマリー・エージェント", "image_path": "assets/e/7_6.jpg", "hp": 190, "skills": [{"name": "空間歪曲", "type": "attack", "val": 45, "pierce": True, "img": "assets/sk/7_6_1.jpg"}, {"name": "ダークマター", "type": "attack", "val": 54, "pierce": False, "img": "assets/sk/7_6_2.jpg"}, {"name": "次元障壁", "type": "buff", "val": 48, "img": "assets/sk/7_6_3.jpg"}]},
            {"name": "【ボス】狂気の科学者・ دکتر・サイコ", "image_path": "assets/e/7_7.jpg", "hp": 350, "skills": [{"name": "禁断の改造ビーム", "type": "attack", "val": 48, "pierce": False, "img": "assets/sk/7_7_1.jpg"}, {"name": "オーバードライブ", "type": "attack", "val": 58, "pierce": True, "img": "assets/sk/7_7_2.jpg"}, {"name": "実験体解放", "type": "buff", "val": 52, "img": "assets/sk/7_7_3.jpg"}]},
        ],
    },
    {
        "stage": 8,
        "env_name": "オービタル・ステーション地上発着港 (宇宙へ続くロケット基地)",
        "env_desc": "夜空へ突き出る巨大ロケット発射基地。宇宙防衛軍と重武装ユニットが立ちはだかる。",
        "prev_boss_name": "狂気の科学者・ دکتر・サイコ",
        "story_image": "assets/story/stage8.jpg",
        "story_intro": (
            "実験施設の奥で「Dr.サイコ」の野望を粉砕した3人。\n"
            "研究所のメインモニターには、宇宙へ向けて飛び立つロケットの打ち上げシークエンスが表示されていた。\n\n"
            "「黒幕は地上だけにとどまらず、宇宙へ逃げ込む気ってわけかい！」\n\n"
            "発射管制塔を制圧すべく、3人はオービタル・ステーション地上発着港へと急行する。"
        ),
        "enemies": [
            {"name": "スペース・ガード", "image_path": "assets/e/8_1.jpg", "hp": 170, "skills": [{"name": "ビームライフル", "type": "attack", "val": 42, "pierce": False, "img": "assets/sk/8_1_1.jpg"}, {"name": "グレネードランチャー", "type": "attack", "val": 50, "pierce": True, "img": "assets/sk/8_1_2.jpg"}, {"name": "宇宙服シールド", "type": "buff", "val": 45, "img": "assets/sk/8_1_3.jpg"}]},
            {"name": "エアロ・ファイター", "image_path": "assets/e/8_2.jpg", "hp": 165, "skills": [{"name": "ミサイルポッド", "type": "attack", "val": 44, "pierce": True, "img": "assets/sk/8_2_1.jpg"}, {"name": "超音速アタック", "type": "attack", "val": 52, "pierce": False, "img": "assets/sk/8_2_2.jpg"}, {"name": "ドッジ機動", "type": "buff", "val": 48, "img": "assets/sk/8_2_3.jpg"}]},
            {"name": "ヘビー・メック", "image_path": "assets/e/8_3.jpg", "hp": 200, "skills": [{"name": "ガトリング砲", "type": "attack", "val": 46, "pierce": False, "img": "assets/sk/8_3_1.jpg"}, {"name": "ロケットパンチ", "type": "attack", "val": 55, "pierce": True, "img": "assets/sk/8_3_2.jpg"}, {"name": "チタン装甲", "type": "buff", "val": 52, "img": "assets/sk/8_3_3.jpg"}]},
            {"name": "オフィサー・コマンダー", "image_path": "assets/e/8_4.jpg", "hp": 185, "skills": [{"name": "プラズマサーベル", "type": "attack", "val": 48, "pierce": True, "img": "assets/sk/8_4_1.jpg"}, {"name": "指令ブラスト", "type": "attack", "val": 57, "pierce": False, "img": "assets/sk/8_4_2.jpg"}, {"name": "戦術指揮", "type": "buff", "val": 50, "img": "assets/sk/8_4_3.jpg"}]},
            {"name": "サイバー・スナイパー", "image_path": "assets/e/8_5.jpg", "hp": 175, "skills": [{"name": "レールガン", "type": "attack", "val": 50, "pierce": True, "img": "assets/sk/8_5_1.jpg"}, {"name": "光速スナイプ", "type": "attack", "val": 60, "pierce": False, "img": "assets/sk/8_5_2.jpg"}, {"name": "サーモグラフィ", "type": "buff", "val": 48, "img": "assets/sk/8_5_3.jpg"}]},
            {"name": "ディフェンス・タレット", "image_path": "assets/e/8_6.jpg", "hp": 210, "skills": [{"name": "全方位レーザー", "type": "attack", "val": 52, "pierce": False, "img": "assets/sk/8_6_1.jpg"}, {"name": "高圧パルス", "type": "attack", "val": 62, "pierce": True, "img": "assets/sk/8_6_2.jpg"}, {"name": "エネルギー充填", "type": "buff", "val": 55, "img": "assets/sk/8_6_3.jpg"}]},
            {"name": "【ボス】宇宙港司令官・ヴァルキリー", "image_path": "assets/e/8_7.jpg", "hp": 390, "skills": [{"name": "オービタルストライク", "type": "attack", "val": 56, "pierce": False, "img": "assets/sk/8_7_1.jpg"}, {"name": "アブソリュートレイ", "type": "attack", "val": 66, "pierce": True, "img": "assets/sk/8_7_2.jpg"}, {"name": "ハイパーバリア展開", "type": "buff", "val": 60, "img": "assets/sk/8_7_3.jpg"}]},
        ],
    },
    {
        "stage": 9,
        "env_name": "メガコープ・タワー最上階 (巨大企業の心臓部)",
        "env_desc": "雲を突き抜けた超高層オフィスの最上階。企業の最終防衛システムが待ち構える。",
        "prev_boss_name": "宇宙港司令官・ヴァルキリー",
        "story_image": "assets/story/stage9.jpg",
        "story_intro": (
            "宇宙港で「ヴァルキリー」を退け、発射されたシャトルのアクセス権を奪還した3人。\n"
            "すべての黒幕が潜む、メガコープの本社タワー最上階へと進路を定めた。\n\n"
            "「ここまで来れば、あとはトップを引きずり出すだけだね」\n\n"
            "雲を突き抜ける超高層オフィスの最上階へ向け、最後の地上決戦へ突入する。"
        ),
        "enemies": [
            {"name": "エリート・セキュリティー", "image_path": "assets/e/9_1.jpg", "hp": 190, "skills": [{"name": "ナノブレード", "type": "attack", "val": 50, "pierce": True, "img": "assets/sk/9_1_1.jpg"}, {"name": "パルスライフル", "type": "attack", "val": 60, "pierce": False, "img": "assets/sk/9_1_2.jpg"}, {"name": "絶対防御ネット", "type": "buff", "val": 55, "img": "assets/sk/9_1_3.jpg"}]},
            {"name": "コーポレート・ニンジャ", "image_path": "assets/e/9_2.jpg", "hp": 180, "skills": [{"name": "サイバー手裏剣", "type": "attack", "val": 53, "pierce": False, "img": "assets/sk/9_2_1.jpg"}, {"name": "影渡り斬り", "type": "attack", "val": 63, "pierce": True, "img": "assets/sk/9_2_2.jpg"}, {"name": "隠れ身の術", "type": "buff", "val": 52, "img": "assets/sk/9_2_3.jpg"}]},
            {"name": "アンドロイド・オフィサー", "image_path": "assets/e/9_3.jpg", "hp": 210, "skills": [{"name": "プラズマソード", "type": "attack", "val": 56, "pierce": True, "img": "assets/sk/9_3_1.jpg"}, {"name": "バーストキャノン", "type": "attack", "val": 66, "pierce": False, "img": "assets/sk/9_3_2.jpg"}, {"name": "コープアーマー", "type": "buff", "val": 58, "img": "assets/sk/9_3_3.jpg"}]},
            {"name": "サイバー・ガーディアン", "image_path": "assets/e/9_4.jpg", "hp": 230, "skills": [{"name": "ヘビーハンマー", "type": "attack", "val": 59, "pierce": False, "img": "assets/sk/9_4_1.jpg"}, {"name": "ショックウェーブ", "type": "attack", "val": 69, "pierce": True, "img": "assets/sk/9_4_2.jpg"}, {"name": "要塞化フィールド", "type": "buff", "val": 62, "img": "assets/sk/9_4_3.jpg"}]},
            {"name": "AI・セキュリティエージェント", "image_path": "assets/e/9_5.jpg", "hp": 200, "skills": [{"name": "マインドバースト", "type": "attack", "val": 62, "pierce": True, "img": "assets/sk/9_5_1.jpg"}, {"name": "データストーム", "type": "attack", "val": 72, "pierce": False, "img": "assets/sk/9_5_2.jpg"}, {"name": "自己診断パッチ", "type": "buff", "val": 60, "img": "assets/sk/9_5_3.jpg"}]},
            {"name": "エグゼクティブ・ボディーガード", "image_path": "assets/e/9_6.jpg", "hp": 240, "skills": [{"name": "バイオニック拳", "type": "attack", "val": 65, "pierce": True, "img": "assets/sk/9_6_1.jpg"}, {"name": "超高圧ビーム", "type": "attack", "val": 75, "pierce": False, "img": "assets/sk/9_6_2.jpg"}, {"name": "不屈のシールド", "type": "buff", "val": 68, "img": "assets/sk/9_6_3.jpg"}]},
            {"name": "【ボス】取締役会会長・ゼウス", "image_path": "assets/e/9_7.jpg", "hp": 430, "skills": [{"name": "神罰の稲妻", "type": "attack", "val": 70, "pierce": False, "img": "assets/sk/9_7_1.jpg"}, {"name": "メガコープジャッジ", "type": "attack", "val": 82, "pierce": True, "img": "assets/sk/9_7_2.jpg"}, {"name": "神の絶対領域", "type": "buff", "val": 75, "img": "assets/sk/9_7_3.jpg"}]},
        ],
    },
    {
        "stage": 10,
        "env_name": "最終電脳空間・コア (世界の命運を握る中枢ネット)",
        "env_desc": "現実の物理法則を超越した電脳の深淵。すべての黒幕が待つ最終決戦の地。",
        "prev_boss_name": "取締役会会長・ゼウス",
        "story_image": "assets/story/stage10.jpg",
        "story_intro": (
            "メガコープ会長「ゼウス」の肉体を追い詰めたものの、彼の意識は都市の中枢ネットへ逃走した。\n"
            "物質世界を離れ、現実の物理法則を超越した電脳の深淵へダイブする3人。\n\n"
            "「これが最後の舞台か。……行くよ、二人とも！」\n\n"
            "世界すべての命運を賭け、電脳の神に等しい黒幕を討つための最終決戦が始まる。"
        ),
        "enemies": [
            {"name": "ダーク・プログラム", "image_path": "assets/e/10_1.jpg", "hp": 220, "skills": [{"name": "ブラックホール", "type": "attack", "val": 65, "pierce": True, "img": "assets/sk/10_1_1.jpg"}, {"name": "バグインジェクション", "type": "attack", "val": 75, "pierce": False, "img": "assets/sk/10_1_2.jpg"}, {"name": "暗黒シールド", "type": "buff", "val": 70, "img": "assets/sk/10_1_3.jpg"}]},
            {"name": "ファントム・ウィルス", "image_path": "assets/e/10_2.jpg", "hp": 210, "skills": [{"name": "ファントムエッジ", "type": "attack", "val": 68, "pierce": False, "img": "assets/sk/10_2_1.jpg"}, {"name": "精神崩壊波", "type": "attack", "val": 78, "pierce": True, "img": "assets/sk/10_2_2.jpg"}, {"name": "幻影迷彩", "type": "buff", "val": 68, "img": "assets/sk/10_2_3.jpg"}]},
            {"name": "オメガ・センチネル", "image_path": "assets/e/10_3.jpg", "hp": 250, "skills": [{"name": "オメガキャノン", "type": "attack", "val": 71, "pierce": False, "img": "assets/sk/10_3_1.jpg"}, {"name": "消滅レイ", "type": "attack", "val": 82, "pierce": True, "img": "assets/sk/10_3_2.jpg"}, {"name": "超硬質アーマー", "type": "buff", "val": 75, "img": "assets/sk/10_3_3.jpg"}]},
            {"name": "カオス・エージェント", "image_path": "assets/e/10_4.jpg", "hp": 230, "skills": [{"name": "カオススラッシュ", "type": "attack", "val": 74, "pierce": True, "img": "assets/sk/10_4_1.jpg"}, {"name": "空間崩壊", "type": "attack", "val": 85, "pierce": False, "img": "assets/sk/10_4_2.jpg"}, {"name": "混沌の加護", "type": "buff", "val": 78, "img": "assets/sk/10_4_3.jpg"}]},
            {"name": "シンギュラリティ・ボット", "image_path": "assets/e/10_5.jpg", "hp": 260, "skills": [{"name": "特異点バースト", "type": "attack", "val": 77, "pierce": True, "img": "assets/sk/10_5_1.jpg"}, {"name": "重力プレス", "type": "attack", "val": 88, "pierce": False, "img": "assets/sk/10_5_2.jpg"}, {"name": "重力制御", "type": "buff", "val": 80, "img": "assets/sk/10_5_3.jpg"}]},
            {"name": "ネメシス・ガーディアン", "image_path": "assets/e/10_6.jpg", "hp": 280, "skills": [{"name": "ネメシスソード", "type": "attack", "val": 80, "pierce": False, "img": "assets/sk/10_6_1.jpg"}, {"name": "ジャッジメントレイ", "type": "attack", "val": 92, "pierce": True, "img": "assets/sk/10_6_2.jpg"}, {"name": "絶対神の障壁", "type": "buff", "val": 85, "img": "assets/sk/10_6_3.jpg"}]},
            {"name": "【FINAL BOSS】全知全能のCEO・オーバーライド", "image_path": "assets/e/10_7.jpg", "hp": 550, "skills": [{"name": "ワールド・デリート", "type": "attack", "val": 90, "pierce": True, "img": "assets/sk/10_7_1.jpg"}, {"name": "システム・オーバーロード", "type": "attack", "val": 110, "pierce": True, "img": "assets/sk/10_7_2.jpg"}, {"name": "電脳神の完全無敵化", "type": "buff", "val": 100, "img": "assets/sk/10_7_3.jpg"}]},
        ],
    },
]

# ==========================================
# 3. ゲーム状態の初期化
# ==========================================
if "game_state" not in st.session_state:
  st.session_state.game_state = "TITLE"
  st.session_state.stage = 1
  st.session_state.enemy_index = 0
  st.session_state.ram = 3
  st.session_state.max_ram = 3
  st.session_state.allies = []
  st.session_state.current_enemy = None
  st.session_state.env_info = {}
  st.session_state.hand = []
  st.session_state.battle_log = []
  st.session_state.last_enemy_action = None
  st.session_state.all_three_alive_turns = 0


def start_new_game():
  st.session_state.stage = 1
  st.session_state.enemy_index = 0
  st.session_state.allies = []
  st.session_state.all_three_alive_turns = 0
  for data in ALLIES_DATA:
    st.session_state.allies.append({
        "name": data["name"],
        "image_path": data["image_path"],
        "hp": data["hp"],
        "max_hp": data["hp"],
        "shield": 0,
        "alive": True,
        "skills": data["skills"],
    })
  st.session_state.last_enemy_action = None
  st.session_state.game_state = "STAGE_STORY"


def start_battle():
  s_idx = min(st.session_state.stage - 1, len(STAGES_DATA) - 1)
  stage_data = STAGES_DATA[s_idx]
  
  st.session_state.env_info = {
      "name": stage_data["env_name"],
      "desc": stage_data["env_desc"],
      "story_intro": stage_data["story_intro"],
      "prev_boss_name": stage_data["prev_boss_name"],
  }
  
  e_idx = min(st.session_state.enemy_index, len(stage_data["enemies"]) - 1)
  chosen_enemy_data = stage_data["enemies"][e_idx]
  
  st.session_state.current_enemy = {
      "name": chosen_enemy_data["name"],
      "image_path": chosen_enemy_data["image_path"],
      "hp": chosen_enemy_data["hp"],
      "max_hp": chosen_enemy_data["hp"],
      "shield": 0,
      "skills": chosen_enemy_data["skills"],
  }
  st.session_state.ram = 3
  st.session_state.max_ram = 3
  st.session_state.battle_log = [
      f"--- ステージ {st.session_state.stage} ({stage_data['env_name']}) : 敵 {st.session_state.enemy_index + 1}/7 【{chosen_enemy_data['name']}】出現 ---"
  ]
  st.session_state.last_enemy_action = None
  draw_cards()


def draw_cards():
  pool = []
  for a in st.session_state.allies:
    if a["alive"]:
      for s in a["skills"]:
        sc = s.copy()
        sc["owner"] = a["name"]
        sc["cost"] = 1 if sc["val"] < 35 else 2
        pool.append(sc)
  
  if pool:
    st.session_state.hand = random.sample(pool, min(4, len(pool)))
  else:
    st.session_state.hand = []


def calculate_score():
  stages_cleared = st.session_state.stage if st.session_state.game_state == "VICTORY" else max(0, st.session_state.stage - 1)
  alive_turns = st.session_state.all_three_alive_turns
  
  score = (stages_cleared * 1500) + (alive_turns * 200)
  
  if st.session_state.game_state == "VICTORY":
    score += 5000
    
  if score >= 25000:
    rank = "S (LEGENDARY CYBER RUNNER)"
  elif score >= 18000:
    rank = "A (ELITE HACKER)"
  elif score >= 10000:
    rank = "B (VETERAN OPERATOR)"
  elif score >= 5000:
    rank = "C (SURVIVOR)"
  else:
    rank = "D (ROOKIE)"
    
  return stages_cleared, alive_turns, score, rank


# ==========================================
# 4. 画面描画 (Streamlit)
# ==========================================

if st.session_state.game_state == "TITLE":
  st.title("⚡ CYBER_DECK : ULTIMATE ENVIRONMENTS ⚡")
  st.markdown(
      "味方3体（各10固有スキル）を率い、全10ステージの**異なる環境**を踏破せよ！"
      "各ステージには雑魚6体＋ボス1体（計7体全て）が順番に立ち塞がる本格カードバトル。"
  )
  if st.button("ゲームスタート", use_container_width=True):
    start_new_game()
    st.rerun()

elif st.session_state.game_state == "STAGE_STORY":
  # 各ステージ開始時の物語・導入表示画面
  s_idx = min(st.session_state.stage - 1, len(STAGES_DATA) - 1)
  s_data = STAGES_DATA[s_idx]
  
  st.title(f"📖 STAGE {st.session_state.stage} 開幕ストーリー")
  
  if st.session_state.stage > 1:
    st.markdown(
        f"""<div class="story-box" style="border-color: #ff007f;">
            <b>【前ステージボス撃破 ＆ 移動完了】</b><br><br>
            前ステージにて<b>「{s_data['prev_boss_name']}」</b>を撃破した詩音、サイファー、アイリーンの3人。<br>
            死闘の痕跡を後にし、新たな任務地である<b>「{s_data['env_name']}」</b>へと移動を完了した。
            </div>""",
        unsafe_allow_html=True,
    )
    
  # ストーリー用画像の表示
  if "story_image" in s_data:
    try:
      st.image(s_data["story_image"], use_container_width=True)
    except Exception:
      st.caption(f"[ストーリー画像読み込みエラー: {s_data['story_image']}]")

  st.markdown(
      f"""<div class="story-box">
          <b>🌐 ステージ {st.session_state.stage}: {s_data['env_name']}</b><br><br>
          {s_data['story_intro']}
          </div>""",
      unsafe_allow_html=True,
  )
  
  if st.button("戦闘エリアへ突入する", use_container_width=True):
    start_battle()
    st.session_state.game_state = "BATTLE"
    st.rerun()

elif st.session_state.game_state == "STAGE_CLEAR_REVIVE":
  st.title(f"🎉 ステージ {st.session_state.stage} クリア！ (強化・リペアプロトコル)")
  st.markdown(
      "ボスを撃破しました！次のステージに進む前に、以下のいずれかのオプションを実行できます：<br>"
      "1. **戦闘不能の味方の復活**（該当者がいる場合）<br>"
      "2. **味方キャラ1人を選んでステータス強化**（最大HPアップ ＆ 所持スキルの効果量アップ）",
      unsafe_allow_html=True,
  )

  dead_allies = [a for a in st.session_state.allies if not a["alive"]]
  if dead_allies:
    st.markdown("### 💀 戦闘不能メンバーの復活")
    cols = st.columns(len(dead_allies))
    for idx, a in enumerate(dead_allies):
      with cols[idx]:
        st.markdown(
            f"""<div class="ally-box">
                <b>{a['name']} (DEFEATED)</b><br>
                状態: 戦闘不能
                </div>""",
            unsafe_allow_html=True,
        )
        if st.button(f"{a['name']} を復活", key=f"revive_btn_{idx}"):
          a["alive"] = True
          a["hp"] = max(1, int(a["max_hp"] * 0.5))
          a["shield"] = 0
          st.session_state.battle_log.append(f"✨ {a['name']} がリペアされ、HP {a['hp']} で復活した！")
          
          if st.session_state.stage >= 10:
            st.session_state.game_state = "VICTORY"
          else:
            st.session_state.stage += 1
            st.session_state.enemy_index = 0
            st.session_state.game_state = "STAGE_STORY"
          st.rerun()
    st.markdown("---")

  st.markdown("### 🚀 味方エージェントのステータス強化 (1人選択)")
  st.markdown("お気に入りのキャラを選んで、最大HPと全スキルの威力を底上げしましょう！")
  
  alive_allies = [a for a in st.session_state.allies if a["alive"]]
  if alive_allies:
    cols_buff = st.columns(len(alive_allies))
    for idx, a in enumerate(alive_allies):
      with cols_buff[idx]:
        st.markdown(
            f"""<div class="ally-box">
                <b>{a['name']}</b><br>
                現在 MaxHP: {a['max_hp']}
                </div>""",
            unsafe_allow_html=True,
        )
        if st.button(f"⚡ {a['name']} を強化する", key=f"buff_btn_{idx}"):
          hp_boost = 30
          a["max_hp"] += hp_boost
          a["hp"] = min(a["max_hp"], a["hp"] + hp_boost)
          
          for s in a["skills"]:
            if "val" in s:
              s["val"] = int(s["val"] * 1.25) + 3
          
          st.session_state.battle_log.append(
              f"💪 {a['name']} が強化された！ (MaxHP +{hp_boost} & スキル性能向上)"
          )
          
          if st.session_state.stage >= 10:
            st.session_state.game_state = "VICTORY"
          else:
            st.session_state.stage += 1
            st.session_state.enemy_index = 0
            st.session_state.game_state = "STAGE_STORY"
          st.rerun()

  st.markdown("---")
  if st.button("強化・復活を行わずに次へ進む", use_container_width=True):
    if st.session_state.stage >= 10:
      st.session_state.game_state = "VICTORY"
    else:
      st.session_state.stage += 1
      st.session_state.enemy_index = 0
      st.session_state.game_state = "STAGE_STORY"
    st.rerun()

elif st.session_state.game_state == "BATTLE":
  st.title(f"⚡ STAGE {st.session_state.stage} / 10  (敵 {st.session_state.enemy_index + 1} / 7)")

  env = st.session_state.env_info
  st.markdown(
      f"""<div class="env-box">
          <b>🌐 現在の環境: {env['name']}</b><br>
          <small>{env['desc']}</small>
          </div>""",
      unsafe_allow_html=True,
  )

  e = st.session_state.current_enemy

  has_pierce_skill = any(s.get("type") == "attack" and s.get("pierce", False) for s in e["skills"])
  if has_pierce_skill:
    st.markdown(
        f"""<div class="warning-box">
            ⚠️ 警告: 遭遇中のターゲット「{e['name']}」は、シールド（防御）を無視して直接HPを貫通する危険な攻撃スキルを保有しています！
            </div>""",
        unsafe_allow_html=True,
    )

  col_ally, col_enemy = st.columns(2)

  with col_ally:
    st.markdown("### 🟢 味方エージェント部隊")
    for a in st.session_state.allies:
      if a["alive"]:
        with st.container():
          st.markdown(
              f"""<div class="ally-box">
                  <b>{a['name']}</b><br>
                  HP: {a['hp']} / {a['max_hp']} | シールド: {a['shield']}
                  </div>""",
              unsafe_allow_html=True,
          )
          hp_ratio = max(0.0, min(1.0, a["hp"] / a["max_hp"]))
          st.progress(hp_ratio)
          
          try:
            st.image(a["image_path"], width=200)
          except Exception:
            st.caption(f"[画像読み込みエラー: {a['image_path']}]")
      else:
        st.markdown(f"<s style='color:gray;'>{a['name']} (DEFEATED)</s>", unsafe_allow_html=True)

  with col_enemy:
    st.markdown("### 🔴 遭遇した敵ターゲット")
    if e:
      st.markdown(
          f"""<div class="enemy-box">
              <b>{e['name']}</b><br>
              HP: {e['hp']} / {e['max_hp']} | シールド: {e['shield']}
              </div>""",
              unsafe_allow_html=True,
      )
      enemy_hp_ratio = max(0.0, min(1.0, e["hp"] / e["max_hp"]))
      st.progress(enemy_hp_ratio)

      try:
        st.image(e["image_path"], width=250)
      except Exception:
        st.caption(f"[画像読み込みエラー: {e['image_path']}]")

  st.markdown("---")
  st.markdown(f"### 🔋 RAM (コスト): {st.session_state.ram} / {st.session_state.max_ram}")

  st.markdown("### 🃏 スキルカード (手札)")
  if st.session_state.hand:
    cols = st.columns(len(st.session_state.hand))
    for idx, card in enumerate(st.session_state.hand):
      with cols[idx]:
        st.markdown(
            f"""<div class="card-box">
                <small style="color:#ff007f;">[{card['owner']}]</small><br>
                <b>{card['name']}</b><br>
                コスト: {card['cost']} RAM<br>
                タイプ: {card['type']} ({card['val']})
                </div>""",
            unsafe_allow_html=True,
        )
        try:
          st.image(card["img"], width=200)
        except Exception:
            st.caption(f"[画像エラー: {card['img']}]")

        if st.button("使用", key=f"card_btn_{idx}"):
          if st.session_state.ram >= card["cost"]:
            st.session_state.ram -= card["cost"]

            if card["type"] == "attack":
              e["hp"] -= card["val"]
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！ 敵に {card['val']} のダメージ！"
              )
            elif card["type"] == "shield":
              for a in st.session_state.allies:
                if a["name"] == card["owner"]:
                  a["shield"] += card["val"]
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！ シールド +{card['val']}！"
              )
            elif card["type"] == "heal":
              for a in st.session_state.allies:
                if a["name"] == card["owner"]:
                  a["hp"] = min(a["max_hp"], a["hp"] + card["val"])
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！ HPを {card['val']} 回復！"
              )
            elif card["type"] == "ram":
              st.session_state.ram = min(
                  st.session_state.max_ram, st.session_state.ram + card["val"]
              )
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！ RAMが {card['val']} 回復！"
              )

            st.session_state.hand.pop(idx)

            if e["hp"] <= 0:
              st.session_state.battle_log.append(f"👉 {e['name']} を撃破した！")
              st.session_state.last_enemy_action = None
              
              if st.session_state.enemy_index < 6:
                st.session_state.enemy_index += 1
                start_battle()
              else:
                st.session_state.game_state = "STAGE_CLEAR_REVIVE"
            st.rerun()
          else:
            st.warning("RAMが不足しています！")

  if st.button("ターン終了 (敵の行動へ)", use_container_width=True):
    all_three_alive = all(a["alive"] for a in st.session_state.allies)
    if all_three_alive:
      st.session_state.all_three_alive_turns += 1

    if e["hp"] > 0:
      eskill = random.choice(e["skills"])
      alive_allies = [a for a in st.session_state.allies if a["alive"]]
      if alive_allies:
        min_hp = min(a["hp"] for a in alive_allies)
        lowest_hp_allies = [a for a in alive_allies if a["hp"] == min_hp]
        target = random.choice(lowest_hp_allies)
        
        dmg = eskill["val"]
        is_pierce = eskill.get("type") == "attack" and eskill.get("pierce", False)

        st.session_state.last_enemy_action = {
            "enemy_name": e["name"],
            "skill_name": eskill["name"],
            "skill_type": eskill["type"],
            "skill_val": eskill["val"],
            "skill_img": eskill["img"],
            "pierce": is_pierce,
        }

        pierce_label = " 【⚡防御貫通スキル！】" if is_pierce else ""
        st.session_state.battle_log.append(
            f"🔴 {e['name']} は 【{eskill['name']}】 を使用した！{pierce_label}"
        )

        if eskill["type"] == "attack":
          if is_pierce:
            target["hp"] -= dmg
            st.session_state.battle_log.append(
                f"   -> [最優先標的] {target['name']} は防御を貫通され、直接 {dmg} のダメージを受けた！"
            )
          else:
            if target["shield"] >= dmg:
              target["shield"] -= dmg
              dmg = 0
            else:
              dmg -= target["shield"]
              target["shield"] = 0
              target["hp"] -= dmg
            st.session_state.battle_log.append(
                f"   -> [最優先標的] {target['name']} に {eskill['val']} のダメージ！"
            )
        elif eskill["type"] == "buff":
          e["shield"] += eskill["val"]
          st.session_state.battle_log.append(
              f"   -> {e['name']} のシールドが +{eskill['val']} 強化された！"
          )

        if target["hp"] <= 0:
          target["hp"] = 0
          target["alive"] = False
          st.session_state.battle_log.append(
              f"💀 {target['name']} が戦闘不能になった..."
          )

        if not any(a["alive"] for a in st.session_state.allies):
          st.session_state.game_state = "GAMEOVER"

    st.session_state.ram = st.session_state.max_ram
    draw_cards()
    st.rerun()

  if st.session_state.last_enemy_action:
    la = st.session_state.last_enemy_action
    st.markdown("### 💥 敵の直前スキル発動")
    col_l1, col_l2 = st.columns([2, 1])
    with col_l1:
      pierce_text = "<br><span style='color:#ff3333; font-weight:bold;'>⚡ 【防御貫通攻撃】シールドが無効化されました！</span>" if la.get("pierce") else ""
      st.markdown(
          f"""<div class="enemy-skill-log">
              <b>【敵スキル】 {la['skill_name']}</b><br>
              使用敵: {la['enemy_name']}<br>
              タイプ: {la['skill_type']} (効果量: {la['skill_val']})
              {pierce_text}
              </div>""",
          unsafe_allow_html=True,
      )
    with col_l2:
      try:
        st.image(la["skill_img"], width=200)
      except Exception:
        st.caption(f"[画像エラー: {la['skill_img']}]")

  st.markdown("### 📜 バトルログ")
  st.text("\n".join(reversed(st.session_state.battle_log[-5:])))

elif st.session_state.game_state in ["VICTORY", "GAMEOVER"]:
  is_win = (st.session_state.game_state == "VICTORY")
  st.title("🏆 ミッション完全クリア (VICTORY)" if is_win else "💀 システムクラッシュ (GAME OVER)")
  
  if is_win:
    # 結末の画像を表示
    try:
      st.image("assets/story/end.jpg", use_column_width=True)
    except Exception:
      st.caption("[結末画像読み込みエラー: assets/story/end.jpg]")

    st.markdown(
        """
        <div class="story-box" style="border-color: #00ffcc; margin-bottom: 20px;">
            <h3 style="color: #00ffcc; margin-top: 0;">📖 物語の結末：電脳の夜明け</h3>
            最終電脳空間の深淵にて、全知全能を自称するCEO「オーバーライド」の全システムを粉砕した詩音、サイファー、アイリーン。<br><br>
            暴走していたメガコープの中枢ネットは静まり返り、アンダーシティから高層コーポレート街に至るまで、都市全体を覆っていた悪質な支配プログラムがすべて消去されていった。<br><br>
            「……ふう、ようやく終わったね。長かった夜勤も、これでおしまいさ」<br><br>
            夜明けを迎えたサイバーシティの空に、眩い本当の朝日が昇る。治安部隊として誇り高き戦いをやり遂げた3人のエージェントは、それぞれのバイクに跨がり、新たな日常へと走り出した――。
        </div>
        """,
        unsafe_allow_html=True,
    )
  else:
    st.markdown("エージェント部隊が全滅しました...")

  stages_cleared, alive_turns, score, rank = calculate_score()

  st.markdown(
      f"""
      <div class="score-box">
          <h2>📊 プレイ評価スコア</h2>
          <hr style="border-color: #00ffcc;">
          <h1 style="color: #ff007f; font-size: 2.5em;">{score:,} pt</h1>
          <h3>評価ランク: <span style="color: #ffcc00;">{rank}</span></h3>
          <p style="margin-top: 15px; font-size: 1.1em;">
            クリアステージ数: <b>{stages_cleared} / 10</b> ステージ<br>
            味方3体全員の生存ターン数: <b>{alive_turns}</b> ターン
          </p>
      </div>
      """,
      unsafe_allow_html=True,
  )

  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()
