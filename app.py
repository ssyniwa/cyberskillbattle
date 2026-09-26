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
        "image_path": "assets/allies/shion.png",
        "hp": 110,
        "skills": [
            {"name": "ブレードスラッシュ", "type": "attack", "val": 20, "img": "assets/skills/s1.png"},
            {"name": "影分身ステップ", "type": "shield", "val": 15, "img": "assets/skills/s2.png"},
            {"name": "クナイ連擲", "type": "attack", "val": 25, "img": "assets/skills/s3.png"},
            {"name": "ナノマシン応急処置", "type": "heal", "val": 25, "img": "assets/skills/s4.png"},
            {"name": "超感覚アイ", "type": "ram", "val": 1, "img": "assets/skills/s5.png"},
            {"name": "プラズマ居合", "type": "attack", "val": 40, "img": "assets/skills/s6.png"},
            {"name": "ステルス", "type": "shield", "val": 30, "img": "assets/skills/s7.png"},
            {"name": "ファントム", "type": "attack", "val": 55, "img": "assets/skills/s8.png"},
            {"name": "自己修復", "type": "heal", "val": 50, "img": "assets/skills/s9.png"},
            {"name": "アクセラレート", "type": "ram", "val": 2, "img": "assets/skills/s10.png"},
        ],
    },
    {
        "name": "サイファー (スナイパー)",
        "image_path": "assets/allies/cypher.png",
        "hp": 85,
        "skills": [
            {"name": "精密ショット", "type": "attack", "val": 22, "img": "assets/skills/c1.png"},
            {"name": "カモフラ", "type": "shield", "val": 12, "img": "assets/skills/c2.png"},
            {"name": "アーマーピアス", "type": "attack", "val": 30, "img": "assets/skills/c3.png"},
            {"name": "メディキット", "type": "heal", "val": 20, "img": "assets/skills/c4.png"},
            {"name": "ターゲティング", "type": "ram", "val": 1, "img": "assets/skills/c5.png"},
            {"name": "ハイパースナイプ", "type": "attack", "val": 45, "img": "assets/skills/c6.png"},
            {"name": "デコイ展開", "type": "shield", "val": 25, "img": "assets/skills/c7.png"},
            {"name": "バースト狙撃", "type": "attack", "val": 60, "img": "assets/skills/c8.png"},
            {"name": "メディドローン", "type": "heal", "val": 40, "img": "assets/skills/c9.png"},
            {"name": "オーバークロック", "type": "ram", "val": 2, "img": "assets/skills/c10.png"},
        ],
    },
    {
        "name": "アイリーン (重装アーマー)",
        "image_path": "assets/allies/irene.png",
        "hp": 130,
        "skills": [
            {"name": "バルカン", "type": "attack", "val": 18, "img": "assets/skills/i1.png"},
            {"name": "バリア", "type": "shield", "val": 20, "img": "assets/skills/i2.png"},
            {"name": "マイクロミサイル", "type": "attack", "val": 35, "img": "assets/skills/i3.png"},
            {"name": "システムパッチ", "type": "heal", "val": 30, "img": "assets/skills/i4.png"},
            {"name": "ジェネレーター", "type": "ram", "val": 1, "img": "assets/skills/i5.png"},
            {"name": "プラズマキャノン", "type": "attack", "val": 50, "img": "assets/skills/i6.png"},
            {"name": "重装フィールド", "type": "shield", "val": 40, "img": "assets/skills/i7.png"},
            {"name": "ストライクボム", "type": "attack", "val": 70, "img": "assets/skills/i8.png"},
            {"name": "オーバーホール", "type": "heal", "val": 60, "img": "assets/skills/i9.png"},
            {"name": "コアチャージ", "type": "ram", "val": 3, "img": "assets/skills/i10.png"},
        ],
    },
]

# ==========================================
# 2. 10ステージ×7種類の個別敵データ＆環境定義
# （ボス1体＋雑魚敵6体 ＝ 計7種類 × 10ステージ ＝ 70種類個別定義、各3スキル）
# ==========================================
STAGES_DATA = [
    # --- ステージ 1：アンダーシティ・スラム ---
    {
        "stage": 1,
        "env_name": "アンダーシティ・スラム (酸性雨降る底辺街)",
        "env_desc": "視界不良のスラム街。錆びついた治安維持ドローンやギャングが襲い来る。",
        "enemies": [
            {"name": "スクラップ・ドローン", "image_path": "assets/e/1_1.png", "hp": 60, "skills": [{"name": "電撃スパーク", "type": "attack", "val": 10, "img": "assets/sk/1_1_1.png"}, {"name": "体当たり", "type": "attack", "val": 14, "img": "assets/sk/1_1_2.png"}, {"name": "自己防壁", "type": "buff", "val": 5, "img": "assets/sk/1_1_3.png"}]},
            {"name": "ストリート・プンク", "image_path": "assets/e/1_2.png", "hp": 70, "skills": [{"name": "鉄パイプ殴打", "type": "attack", "val": 12, "img": "assets/sk/1_2_1.png"}, {"name": "飛び蹴り", "type": "attack", "val": 15, "img": "assets/sk/1_2_2.png"}, {"name": "挑発", "type": "buff", "val": 8, "img": "assets/sk/1_2_3.png"}]},
            {"name": "ジャンク・ハッカー", "image_path": "assets/e/1_3.png", "hp": 65, "skills": [{"name": "ウィルス注入", "type": "attack", "val": 13, "img": "assets/sk/1_3_1.png"}, {"name": "データ抜き", "type": "attack", "val": 16, "img": "assets/sk/1_3_2.png"}, {"name": "隠蔽工作", "type": "buff", "val": 6, "img": "assets/sk/1_3_3.png"}]},
            {"name": "スラム・ドッグ", "image_path": "assets/e/1_4.png", "hp": 75, "skills": [{"name": "サイバー牙", "type": "attack", "val": 14, "img": "assets/sk/1_4_1.png"}, {"name": "猛ダッシュ", "type": "attack", "val": 18, "img": "assets/sk/1_4_2.png"}, {"name": "遠吠え", "type": "buff", "val": 10, "img": "assets/sk/1_4_3.png"}]},
            {"name": "ブラック・ディーラー", "image_path": "assets/e/1_5.png", "hp": 80, "skills": [{"name": "毒針発射", "type": "attack", "val": 15, "img": "assets/sk/1_5_1.png"}, {"name": "隠しナイフ", "type": "attack", "val": 19, "img": "assets/sk/1_5_2.png"}, {"name": "煙幕", "type": "buff", "val": 12, "img": "assets/sk/1_5_3.png"}]},
            {"name": "アンダー・エンフォーサー", "image_path": "assets/e/1_6.png", "hp": 90, "skills": [{"name": "ヘビーショット", "type": "attack", "val": 17, "img": "assets/sk/1_6_1.png"}, {"name": "バットナックル", "type": "attack", "val": 21, "img": "assets/sk/1_6_2.png"}, {"name": "硬質化", "type": "buff", "val": 15, "img": "assets/sk/1_6_3.png"}]},
            {"name": "【ボス】スラムの暴力王・ガレオン", "image_path": "assets/e/1_7.png", "hp": 150, "skills": [{"name": "ガトリング乱射", "type": "attack", "val": 22, "img": "assets/sk/1_7_1.png"}, {"name": "メガトンプレス", "type": "attack", "val": 28, "img": "assets/sk/1_7_2.png"}, {"name": "狂戦士の咆哮", "type": "buff", "val": 20, "img": "assets/sk/1_7_3.png"}]},
        ],
    },
    # --- ステージ 2：ネオン・カジノ地区 ---
    {
        "stage": 2,
        "env_name": "ネオン・カジノ地区 (欲望と電脳の歓楽街)",
        "env_desc": "きらびやかなホログラムが明滅する歓楽街。マフィアの手先が立ち塞がる。",
        "enemies": [
            {"name": "カジノ・セキュリティー", "image_path": "assets/e/2_1.png", "hp": 80, "skills": [{"name": "スタンバトン", "type": "attack", "val": 14, "img": "assets/sk/2_1_1.png"}, {"name": "ボディーブロー", "type": "attack", "val": 18, "img": "assets/sk/2_1_2.png"}, {"name": "プロテクト", "type": "buff", "val": 10, "img": "assets/sk/2_1_3.png"}]},
            {"name": "シンジケート・ガード", "image_path": "assets/e/2_2.png", "hp": 85, "skills": [{"name": "サブマシンガン", "type": "attack", "val": 16, "img": "assets/sk/2_2_1.png"}, {"name": "タックル", "type": "attack", "val": 20, "img": "assets/sk/2_2_2.png"}, {"name": "防弾シールド", "type": "buff", "val": 12, "img": "assets/sk/2_2_3.png"}]},
            {"name": "サイバー・ホステス", "image_path": "assets/e/2_3.png", "hp": 75, "skills": [{"name": "魅惑のリップ", "type": "attack", "val": 15, "img": "assets/sk/2_3_1.png"}, {"name": "毒入りグラス", "type": "attack", "val": 19, "img": "assets/sk/2_3_2.png"}, {"name": "錯乱フェロモン", "type": "buff", "val": 14, "img": "assets/sk/2_3_3.png"}]},
            {"name": "カジノ・ディーラー", "image_path": "assets/e/2_4.png", "hp": 90, "skills": [{"name": "カードカッター", "type": "attack", "val": 17, "img": "assets/sk/2_4_1.png"}, {"name": "ルーレットボム", "type": "attack", "val": 22, "img": "assets/sk/2_4_2.png"}, {"name": "イカサマ演算", "type": "buff", "val": 15, "img": "assets/sk/2_4_3.png"}]},
            {"name": "アンドロイド・バトラー", "image_path": "assets/e/2_5.png", "hp": 95, "skills": [{"name": "シルバーブレード", "type": "attack", "val": 19, "img": "assets/sk/2_5_1.png"}, {"name": "高速刺突", "type": "attack", "val": 24, "img": "assets/sk/2_5_2.png"}, {"name": "精密計算", "type": "buff", "val": 18, "img": "assets/sk/2_5_3.png"}]},
            {"name": "マフィア・キャプテン", "image_path": "assets/e/2_6.png", "hp": 110, "skills": [{"name": "マグナムショット", "type": "attack", "val": 21, "img": "assets/sk/2_6_1.png"}, {"name": "近接ウィップ", "type": "attack", "val": 26, "img": "assets/sk/2_6_2.png"}, {"name": "組織の号令", "type": "buff", "val": 20, "img": "assets/sk/2_6_3.png"}]},
            {"name": "【ボス】カジノの支配人・ドン・バネッサ", "image_path": "assets/e/2_7.png", "hp": 180, "skills": [{"name": "ロイヤルストレート", "type": "attack", "val": 25, "img": "assets/sk/2_7_1.png"}, {"name": "黄金の銃撃", "type": "attack", "val": 32, "img": "assets/sk/2_7_2.png"}, {"name": "カジノ・パニック", "type": "buff", "val": 25, "img": "assets/sk/2_7_3.png"}]},
        ],
    },
    # --- ステージ 3：ハイテク工業プラント ---
    {
        "stage": 3,
        "env_name": "ハイテク工業プラント (自動化された無人工場)",
        "env_desc": "炎と蒸気が吹き出すメガコープの製造プラント。戦闘用ロボットが徘徊する。",
        "enemies": [
            {"name": "オート・ワーカー", "image_path": "assets/e/3_1.png", "hp": 90, "skills": [{"name": "アームハンマー", "type": "attack", "val": 16, "img": "assets/sk/3_1_1.png"}, {"name": "プラズマ溶接", "type": "attack", "val": 20, "img": "assets/sk/3_1_2.png"}, {"name": "出力上昇", "type": "buff", "val": 12, "img": "assets/sk/3_1_3.png"}]},
            {"name": "ファクトリー・ドローン", "image_path": "assets/e/3_2.png", "hp": 85, "skills": [{"name": "レーザー照射", "type": "attack", "val": 18, "img": "assets/sk/3_2_1.png"}, {"name": "突撃ドリル", "type": "attack", "val": 22, "img": "assets/sk/3_2_2.png"}, {"name": "光学迷彩", "type": "buff", "val": 15, "img": "assets/sk/3_2_3.png"}]},
            {"name": "ウォー・ハウンド", "image_path": "assets/e/3_3.png", "hp": 100, "skills": [{"name": "超音波バイト", "type": "attack", "val": 19, "img": "assets/sk/3_3_1.png"}, {"name": "フレイムブレス", "type": "attack", "val": 24, "img": "assets/sk/3_3_2.png"}, {"name": "四肢強化", "type": "buff", "val": 16, "img": "assets/sk/3_3_3.png"}]},
            {"name": "セキュリティ・センチネル", "image_path": "assets/e/3_4.png", "hp": 110, "skills": [{"name": "パルスキャノン", "type": "attack", "val": 21, "img": "assets/sk/3_4_1.png"}, {"name": "ショックウェーブ", "type": "attack", "val": 26, "img": "assets/sk/3_4_2.png"}, {"name": "重装アーマー", "type": "buff", "val": 20, "img": "assets/sk/3_4_3.png"}]},
            {"name": "インダストリアル・ボット", "image_path": "assets/e/3_5.png", "hp": 120, "skills": [{"name": "クラッシャー", "type": "attack", "val": 23, "img": "assets/sk/3_5_1.png"}, {"name": "プレスアタック", "type": "attack", "val": 28, "img": "assets/sk/3_5_2.png"}, {"name": "チタンボディ", "type": "buff", "val": 22, "img": "assets/sk/3_5_3.png"}]},
            {"name": "プラント・インスペクター", "image_path": "assets/e/3_6.png", "hp": 130, "skills": [{"name": "スキャンレーザー", "type": "attack", "val": 25, "img": "assets/sk/3_6_1.png"}, {"name": "高圧電流", "type": "attack", "val": 30, "img": "assets/sk/3_6_2.png"}, {"name": "システム分析", "type": "buff", "val": 24, "img": "assets/sk/3_6_3.png"}]},
            {"name": "【ボス】プラント監視AI・アイアン・マザー", "image_path": "assets/e/3_7.png", "hp": 210, "skills": [{"name": "オービットレーザー", "type": "attack", "val": 28, "img": "assets/sk/3_7_1.png"}, {"name": "全方位ミサイル", "type": "attack", "val": 35, "img": "assets/sk/3_7_2.png"}, {"name": "無限増産プロトコル", "type": "buff", "val": 30, "img": "assets/sk/3_7_3.png"}]},
        ],
    },
    # --- ステージ 4：地下下水道網 ---
    {
        "stage": 4,
        "env_name": "地下下水道網 (汚染物質が流れ込む暗渠)",
        "env_desc": "悪臭と毒ガスが充満する地下水路。ミュータントや廃棄されたサイボーグが潜む。",
        "enemies": [
            {"name": "下水道のドブネズミ", "image_path": "assets/e/4_1.png", "hp": 95, "skills": [{"name": "猛毒かみつき", "type": "attack", "val": 18, "img": "assets/sk/4_1_1.png"}, {"name": "不意打ち", "type": "attack", "val": 22, "img": "assets/sk/4_1_2.png"}, {"name": "素早い身かわし", "type": "buff", "val": 15, "img": "assets/sk/4_1_3.png"}]},
            {"name": "廃棄サイボーグ", "image_path": "assets/e/4_2.png", "hp": 110, "skills": [{"name": "錆びたソード", "type": "attack", "val": 20, "img": "assets/sk/4_2_1.png"}, {"name": "狂気の突進", "type": "attack", "val": 25, "img": "assets/sk/4_2_2.png"}, {"name": "暴走回路", "type": "buff", "val": 18, "img": "assets/sk/4_2_3.png"}]},
            {"name": "ケミカル・スライム", "image_path": "assets/e/4_3.png", "hp": 120, "skills": [{"name": "酸の液滴", "type": "attack", "val": 22, "img": "assets/sk/4_3_1.png"}, {"name": "溶解プレス", "type": "attack", "val": 27, "img": "assets/sk/4_3_2.png"}, {"name": "弾力ボディ", "type": "buff", "val": 20, "img": "assets/sk/4_3_3.png"}]},
            {"name": "アンダーグラウンド・ゲリラ", "image_path": "assets/e/4_4.png", "hp": 115, "skills": [{"name": "ハンドグレネード", "type": "attack", "val": 24, "img": "assets/sk/4_4_1.png"}, {"name": "アサルト射撃", "type": "attack", "val": 29, "img": "assets/sk/4_4_2.png"}, {"name": "闇夜の潜伏", "type": "buff", "val": 22, "img": "assets/sk/4_4_3.png"}]},
            {"name": "ミュータント・ブル", "image_path": "assets/e/4_5.png", "hp": 135, "skills": [{"name": "猛角突進", "type": "attack", "val": 26, "img": "assets/sk/4_5_1.png"}, {"name": "グランドスマッシュ", "type": "attack", "val": 32, "img": "assets/sk/4_5_2.png"}, {"name": "怒涛の肉体", "type": "buff", "val": 25, "img": "assets/sk/4_5_3.png"}]},
            {"name": "トキシック・ストーカー", "image_path": "assets/e/4_6.png", "hp": 125, "skills": [{"name": "猛毒ニードル", "type": "attack", "val": 28, "img": "assets/sk/4_6_1.png"}, {"name": "サイコネイル", "type": "attack", "val": 34, "img": "assets/sk/4_6_2.png"}, {"name": "猛毒霧発生", "type": "buff", "val": 28, "img": "assets/sk/4_6_3.png"}]},
            {"name": "【ボス】下水道の主・バイオキメラ", "image_path": "assets/e/4_7.png", "hp": 240, "skills": [{"name": "アシッドブレス", "type": "attack", "val": 32, "img": "assets/sk/4_7_1.png"}, {"name": "触手乱打", "type": "attack", "val": 38, "img": "assets/sk/4_7_2.png"}, {"name": "超再生能力", "type": "buff", "val": 35, "img": "assets/sk/4_7_3.png"}]},
        ],
    },
    # --- ステージ 5：データ・サーバータワー ---
    {
        "stage": 5,
        "env_name": "データ・サーバータワー (電脳の結界要塞)",
        "env_desc": "無数のサーバーラックが並ぶ仮想と現実の交差点。ネットセキュリティが襲い来る。",
        "enemies": [
            {"name": "アイス・ウォール", "image_path": "assets/e/5_1.png", "hp": 120, "skills": [{"name": "ファイアウォール弾", "type": "attack", "val": 23, "img": "assets/sk/5_1_1.png"}, {"name": "データクラッシュ", "type": "attack", "val": 28, "img": "assets/sk/5_1_2.png"}, {"name": "防壁展開", "type": "buff", "val": 25, "img": "assets/sk/5_1_3.png"}]},
            {"name": "ネット・スパイダー", "image_path": "assets/e/5_2.png", "hp": 110, "skills": [{"name": "ウェブストリング", "type": "attack", "val": 25, "img": "assets/sk/5_2_1.png"}, {"name": "電脳ファング", "type": "attack", "val": 30, "img": "assets/sk/5_2_2.png"}, {"name": "網の張巡り", "type": "buff", "val": 22, "img": "assets/sk/5_2_3.png"}]},
            {"name": "セキュリティ・アバター", "image_path": "assets/e/5_3.png", "hp": 130, "skills": [{"name": "ホログラムソード", "type": "attack", "val": 27, "img": "assets/sk/5_3_1.png"}, {"name": "ライトニングレイ", "type": "attack", "val": 33, "img": "assets/sk/5_3_2.png"}, {"name": "残像防御", "type": "buff", "val": 28, "img": "assets/sk/5_3_3.png"}]},
            {"name": "パケット・スニファー", "image_path": "assets/e/5_4.png", "hp": 125, "skills": [{"name": "データパケット", "type": "attack", "val": 29, "img": "assets/sk/5_4_1.png"}, {"name": "情報バースト", "type": "attack", "val": 35, "img": "assets/sk/5_4_2.png"}, {"name": "トラフィック解析", "type": "buff", "val": 30, "img": "assets/sk/5_4_3.png"}]},
            {"name": "プロキシ・サーベイヤー", "image_path": "assets/e/5_5.png", "hp": 140, "skills": [{"name": "プロキシ砲", "type": "attack", "val": 31, "img": "assets/sk/5_5_1.png"}, {"name": "リダイレクト", "type": "attack", "val": 37, "img": "assets/sk/5_5_2.png"}, {"name": "匿名化シールド", "type": "buff", "val": 32, "img": "assets/sk/5_5_3.png"}]},
            {"name": "エリート・ハッカー", "image_path": "assets/e/5_6.png", "hp": 150, "skills": [{"name": "ゼロデイアタック", "type": "attack", "val": 33, "img": "assets/sk/5_6_1.png"}, {"name": "システムオーバー", "type": "attack", "val": 40, "img": "assets/sk/5_6_2.png"}, {"name": "ディープクラック", "type": "buff", "val": 35, "img": "assets/sk/5_6_3.png"}]},
            {"name": "【ボス】防衛AI・ガーディアン・プライム", "image_path": "assets/e/5_7.png", "hp": 270, "skills": [{"name": "マスタージャッジメント", "type": "attack", "val": 36, "img": "assets/sk/5_7_1.png"}, {"name": "ハイパーパルス", "type": "attack", "val": 44, "img": "assets/sk/5_7_2.png"}, {"name": "絶対防壁起動", "type": "buff", "val": 40, "img": "assets/sk/5_7_3.png"}]},
        ],
    },
    # --- ステージ 6：高級コーポレート街 ---
    {
        "stage": 6,
        "env_name": "高級コーポレート街 (富裕層の高層ビル群)",
        "env_desc": "きらびやかな高層ガラス都市。エリート警備部隊と高級ドローンが警護する。",
        "enemies": [
            {"name": "コープ・ガードマン", "image_path": "assets/e/6_1.png", "hp": 135, "skills": [{"name": "スマートライフル", "type": "attack", "val": 28, "img": "assets/sk/6_1_1.png"}, {"name": "スタンアレスト", "type": "attack", "val": 34, "img": "assets/sk/6_1_2.png"}, {"name": "コーポレート防壁", "type": "buff", "val": 30, "img": "assets/sk/6_1_3.png"}]},
            {"name": "エグゼクティブ・ホーク", "image_path": "assets/e/6_2.png", "hp": 130, "skills": [{"name": "エナジーボルト", "type": "attack", "val": 30, "img": "assets/sk/6_2_1.png"}, {"name": "急降下爆撃", "type": "attack", "val": 36, "img": "assets/sk/6_2_2.png"}, {"name": "高高度レーダー", "type": "buff", "val": 28, "img": "assets/sk/6_2_3.png"}]},
            {"name": "エリート・エンフォーサー", "image_path": "assets/e/6_3.png", "hp": 150, "skills": [{"name": "プラズマバースト", "type": "attack", "val": 32, "img": "assets/sk/6_3_1.png"}, {"name": "アサルトチャージ", "type": "attack", "val": 39, "img": "assets/sk/6_3_2.png"}, {"name": "アーマーコート", "type": "buff", "val": 35, "img": "assets/sk/6_3_3.png"}]},
            {"name": "コーポレート・スナイパー", "image_path": "assets/e/6_4.png", "hp": 140, "skills": [{"name": "ロングレンジ", "type": "attack", "val": 34, "img": "assets/sk/6_4_1.png"}, {"name": "サイレントショット", "type": "attack", "val": 41, "img": "assets/sk/6_4_2.png"}, {"name": "ピンポイント照準", "type": "buff", "val": 33, "img": "assets/sk/6_4_3.png"}]},
            {"name": "セキュリティ・アドバイザー", "image_path": "assets/e/6_5.png", "hp": 160, "skills": [{"name": "マインドクラッシュ", "type": "attack", "val": 36, "img": "assets/sk/6_5_1.png"}, {"name": "レイザーウィップ", "type": "attack", "val": 43, "img": "assets/sk/6_5_2.png"}, {"name": "リスクヘッジ", "type": "buff", "val": 38, "img": "assets/sk/6_5_3.png"}]},
            {"name": "サイボーグ・ボディガード", "image_path": "assets/e/6_6.png", "hp": 175, "skills": [{"name": "ヘビーパイル", "type": "attack", "val": 38, "img": "assets/sk/6_6_1.png"}, {"name": "鉄拳制裁", "type": "attack", "val": 46, "img": "assets/sk/6_6_2.png"}, {"name": "不屈の意志", "type": "buff", "val": 42, "img": "assets/sk/6_6_3.png"}]},
            {"name": "【ボス】治安維持本部長・ゼネラル・クロウ", "image_path": "assets/e/6_7.png", "hp": 310, "skills": [{"name": "オーダードミネーション", "type": "attack", "val": 42, "img": "assets/sk/6_7_1.png"}, {"name": "ジャッジメント砲", "type": "attack", "val": 50, "img": "assets/sk/6_7_2.png"}, {"name": "総司令発令", "type": "buff", "val": 45, "img": "assets/sk/6_7_3.png"}]},
        ],
    },
    # --- ステージ 7：廃墟の実験施設 ---
    {
        "stage": 7,
        "env_name": "廃墟の実験施設 (禁忌の研究が行われた地)",
        "env_desc": "放棄された不気味な地下研究所。改造された異形の存在がうごめく。",
        "enemies": [
            {"name": "プロトタイプ・オブスキュア", "image_path": "assets/e/7_1.png", "hp": 150, "skills": [{"name": "異形クロー", "type": "attack", "val": 35, "img": "assets/sk/7_1_1.png"}, {"name": "絶叫波", "type": "attack", "val": 42, "img": "assets/sk/7_1_2.png"}, {"name": "暴走活性", "type": "buff", "val": 38, "img": "assets/sk/7_1_3.png"}]},
            {"name": "試作型サイボーグ・ゼロ", "image_path": "assets/e/7_2.png", "hp": 160, "skills": [{"name": "バーストブレード", "type": "attack", "val": 37, "img": "assets/sk/7_2_1.png"}, {"name": "超高速突進", "type": "attack", "val": 44, "img": "assets/sk/7_2_2.png"}, {"name": "冷却装置", "type": "buff", "val": 40, "img": "assets/sk/7_2_3.png"}]},
            {"name": "バイオ・ホラー", "image_path": "assets/e/7_3.png", "hp": 170, "skills": [{"name": "アシッドスピア", "type": "attack", "val": 39, "img": "assets/sk/7_3_1.png"}, {"name": "寄生胞子", "type": "attack", "val": 47, "img": "assets/sk/7_3_2.png"}, {"name": "変異再生", "type": "buff", "val": 42, "img": "assets/sk/7_3_3.png"}]},
            {"name": "マッド・ホムンクルス", "image_path": "assets/e/7_4.png", "hp": 165, "skills": [{"name": "ケミカルボム", "type": "attack", "val": 41, "img": "assets/sk/7_4_1.png"}, {"name": "ダークパルス", "type": "attack", "val": 49, "img": "assets/sk/7_4_2.png"}, {"name": "狂気の人形劇", "type": "buff", "val": 44, "img": "assets/sk/7_4_3.png"}]},
            {"name": "キメラ・ハウンド", "image_path": "assets/e/7_5.png", "hp": 180, "skills": [{"name": "トリプルファング", "type": "attack", "val": 43, "img": "assets/sk/7_5_1.png"}, {"name": "ヘルファイヤー", "type": "attack", "val": 52, "img": "assets/sk/7_5_2.png"}, {"name": "獣の咆哮", "type": "buff", "val": 46, "img": "assets/sk/7_5_3.png"}]},
            {"name": "アノマリー・エージェント", "image_path": "assets/e/7_6.png", "hp": 190, "skills": [{"name": "空間歪曲", "type": "attack", "val": 45, "img": "assets/sk/7_6_1.png"}, {"name": "ダークマター", "type": "attack", "val": 54, "img": "assets/sk/7_6_2.png"}, {"name": "次元障壁", "type": "buff", "val": 48, "img": "assets/sk/7_6_3.png"}]},
            {"name": "【ボス】狂気の科学者・ دکتر・サイコ", "image_path": "assets/e/7_7.png", "hp": 350, "skills": [{"name": "禁断の改造ビーム", "type": "attack", "val": 48, "img": "assets/sk/7_7_1.png"}, {"name": "オーバードライブ", "type": "attack", "val": 58, "img": "assets/sk/7_7_2.png"}, {"name": "実験体解放", "type": "buff", "val": 52, "img": "assets/sk/7_7_3.png"}]},
        ],
    },
    # --- ステージ 8：オービタル・ステーション地上発着港 ---
    {
        "stage": 8,
        "env_name": "オービタル・ステーション地上発着港 (宇宙へ続くロケット基地)",
        "env_desc": "夜空へ突き出る巨大ロケット発射基地。宇宙防衛軍と重武装ユニットが立ちはだかる。",
        "enemies": [
            {"name": "スペース・ガード", "image_path": "assets/e/8_1.png", "hp": 170, "skills": [{"name": "ビームライフル", "type": "attack", "val": 42, "img": "assets/sk/8_1_1.png"}, {"name": "グレネードランチャー", "type": "attack", "val": 50, "img": "assets/sk/8_1_2.png"}, {"name": "宇宙服シールド", "type": "buff", "val": 45, "img": "assets/sk/8_1_3.png"}]},
            {"name": "エアロ・ファイター", "image_path": "assets/e/8_2.png", "hp": 165, "skills": [{"name": "ミサイルポッド", "type": "attack", "val": 44, "img": "assets/sk/8_2_1.png"}, {"name": "超音速アタック", "type": "attack", "val": 52, "img": "assets/sk/8_2_2.png"}, {"name": "ドッジ機動", "type": "buff", "val": 48, "img": "assets/sk/8_2_3.png"}]},
            {"name": "ヘビー・メック", "image_path": "assets/e/8_3.png", "hp": 200, "skills": [{"name": "ガトリング砲", "type": "attack", "val": 46, "img": "assets/sk/8_3_1.png"}, {"name": "ロケットパンチ", "type": "attack", "val": 55, "img": "assets/sk/8_3_2.png"}, {"name": "チタン装甲", "type": "buff", "val": 52, "img": "assets/sk/8_3_3.png"}]},
            {"name": "オフィサー・コマンダー", "image_path": "assets/e/8_4.png", "hp": 185, "skills": [{"name": "プラズマサーベル", "type": "attack", "val": 48, "img": "assets/sk/8_4_1.png"}, {"name": "指令ブラスト", "type": "attack", "val": 57, "img": "assets/sk/8_4_2.png"}, {"name": "戦術指揮", "type": "buff", "val": 50, "img": "assets/sk/8_4_3.png"}]},
            {"name": "サイバー・スナイパー", "image_path": "assets/e/8_5.png", "hp": 175, "skills": [{"name": "レールガン", "type": "attack", "val": 50, "img": "assets/sk/8_5_1.png"}, {"name": "光速スナイプ", "type": "attack", "val": 60, "img": "assets/sk/8_5_2.png"}, {"name": "サーモグラフィ", "type": "buff", "val": 48, "img": "assets/sk/8_5_3.png"}]},
            {"name": "ディフェンス・タレット", "image_path": "assets/e/8_6.png", "hp": 210, "skills": [{"name": "全方位レーザー", "type": "attack", "val": 52, "img": "assets/sk/8_6_1.png"}, {"name": "高圧パルス", "type": "attack", "val": 62, "img": "assets/sk/8_6_2.png"}, {"name": "エネルギー充填", "type": "buff", "val": 55, "img": "assets/sk/8_6_3.png"}]},
            {"name": "【ボス】宇宙港司令官・ヴァルキリー", "image_path": "assets/e/8_7.png", "hp": 390, "skills": [{"name": "オービタルストライク", "type": "attack", "val": 56, "img": "assets/sk/8_7_1.png"}, {"name": "アブソリュートレイ", "type": "attack", "val": 66, "img": "assets/sk/8_7_2.png"}, {"name": "ハイパーバリア展開", "type": "buff", "val": 60, "img": "assets/sk/8_7_3.png"}]},
        ],
    },
    # --- ステージ 9：メガコープ・タワー最上階 ---
    {
        "stage": 9,
        "env_name": "メガコープ・タワー最上階 (巨大企業の心臓部)",
        "env_desc": "雲を突き抜けた超高層オフィスの最上階。企業の最終防衛システムが待ち構える。",
        "enemies": [
            {"name": "エリート・セキュリティー", "image_path": "assets/e/9_1.png", "hp": 190, "skills": [{"name": "ナノブレード", "type": "attack", "val": 50, "img": "assets/sk/9_1_1.png"}, {"name": "パルスライフル", "type": "attack", "val": 60, "img": "assets/sk/9_1_2.png"}, {"name": "絶対防御ネット", "type": "buff", "val": 55, "img": "assets/sk/9_1_3.png"}]},
            {"name": "コーポレート・ニンジャ", "image_path": "assets/e/9_2.png", "hp": 180, "skills": [{"name": "サイバー手裏剣", "type": "attack", "val": 53, "img": "assets/sk/9_2_1.png"}, {"name": "影渡り斬り", "type": "attack", "val": 63, "img": "assets/sk/9_2_2.png"}, {"name": "隠れ身の術", "type": "buff", "val": 52, "img": "assets/sk/9_2_3.png"}]},
            {"name": "アンドロイド・オフィサー", "image_path": "assets/e/9_3.png", "hp": 210, "skills": [{"name": "プラズマソード", "type": "attack", "val": 56, "img": "assets/sk/9_3_1.png"}, {"name": "バーストキャノン", "type": "attack", "val": 66, "img": "assets/sk/9_3_2.png"}, {"name": "コープアーマー", "type": "buff", "val": 58, "img": "assets/sk/9_3_3.png"}]},
            {"name": "サイバー・ガーディアン", "image_path": "assets/e/9_4.png", "hp": 230, "skills": [{"name": "ヘビーハンマー", "type": "attack", "val": 59, "img": "assets/sk/9_4_1.png"}, {"name": "ショックウェーブ", "type": "attack", "val": 69, "img": "assets/sk/9_4_2.png"}, {"name": "要塞化フィールド", "type": "buff", "val": 62, "img": "assets/sk/9_4_3.png"}]},
            {"name": "AI・セキュリティエージェント", "image_path": "assets/e/9_5.png", "hp": 200, "skills": [{"name": "マインドバースト", "type": "attack", "val": 62, "img": "assets/sk/9_5_1.png"}, {"name": "データストーム", "type": "attack", "val": 72, "img": "assets/sk/9_5_2.png"}, {"name": "自己診断パッチ", "type": "buff", "val": 60, "img": "assets/sk/9_5_3.png"}]},
            {"name": "エグゼクティブ・ボディーガード", "image_path": "assets/e/9_6.png", "hp": 240, "skills": [{"name": "バイオニック拳", "type": "attack", "val": 65, "img": "assets/sk/9_6_1.png"}, {"name": "超高圧ビーム", "type": "attack", "val": 75, "img": "assets/sk/9_6_2.png"}, {"name": "不屈のシールド", "type": "buff", "val": 68, "img": "assets/sk/9_6_3.png"}]},
            {"name": "【ボス】取締役会会長・ゼウス", "image_path": "assets/e/9_7.png", "hp": 430, "skills": [{"name": "神罰の稲妻", "type": "attack", "val": 70, "img": "assets/sk/9_7_1.png"}, {"name": "メガコープジャッジ", "type": "attack", "val": 82, "img": "assets/sk/9_7_2.png"}, {"name": "神の絶対領域", "type": "buff", "val": 75, "img": "assets/sk/9_7_3.png"}]},
        ],
    },
    # --- ステージ 10：最終電脳空間・コア ---
    {
        "stage": 10,
        "env_name": "最終電脳空間・コア (世界の命運を握る中枢ネット)",
        "env_desc": "現実の物理法則を超越した電脳の深淵。すべての黒幕が待つ最終決戦の地。",
        "enemies": [
            {"name": "ダーク・プログラム", "image_path": "assets/e/10_1.png", "hp": 220, "skills": [{"name": "ブラックホール", "type": "attack", "val": 65, "img": "assets/sk/10_1_1.png"}, {"name": "バグインジェクション", "type": "attack", "val": 75, "img": "assets/sk/10_1_2.png"}, {"name": "暗黒シールド", "type": "buff", "val": 70, "img": "assets/sk/10_1_3.png"}]},
            {"name": "ファントム・ウィルス", "image_path": "assets/e/10_2.png", "hp": 210, "skills": [{"name": "ファントムエッジ", "type": "attack", "val": 68, "img": "assets/sk/10_2_1.png"}, {"name": "精神崩壊波", "type": "attack", "val": 78, "img": "assets/sk/10_2_2.png"}, {"name": "幻影迷彩", "type": "buff", "val": 68, "img": "assets/sk/10_2_3.png"}]},
            {"name": "オメガ・センチネル", "image_path": "assets/e/10_3.png", "hp": 250, "skills": [{"name": "オメガキャノン", "type": "attack", "val": 71, "img": "assets/sk/10_3_1.png"}, {"name": "消滅レイ", "type": "attack", "val": 82, "img": "assets/sk/10_3_2.png"}, {"name": "超硬質アーマー", "type": "buff", "val": 75, "img": "assets/sk/10_3_3.png"}]},
            {"name": "カオス・エージェント", "image_path": "assets/e/10_4.png", "hp": 230, "skills": [{"name": "カオススラッシュ", "type": "attack", "val": 74, "img": "assets/sk/10_4_1.png"}, {"name": "空間崩壊", "type": "attack", "val": 85, "img": "assets/sk/10_4_2.png"}, {"name": "混沌の加護", "type": "buff", "val": 78, "img": "assets/sk/10_4_3.png"}]},
            {"name": "シンギュラリティ・ボット", "image_path": "assets/e/10_5.png", "hp": 260, "skills": [{"name": "特異点バースト", "type": "attack", "val": 77, "img": "assets/sk/10_5_1.png"}, {"name": "重力プレス", "type": "attack", "val": 88, "img": "assets/sk/10_5_2.png"}, {"name": "重力制御", "type": "buff", "val": 80, "img": "assets/sk/10_5_3.png"}]},
            {"name": "ネメシス・ガーディアン", "image_path": "assets/e/10_6.png", "hp": 280, "skills": [{"name": "ネメシスソード", "type": "attack", "val": 80, "img": "assets/sk/10_6_1.png"}, {"name": "ジャッジメントレイ", "type": "attack", "val": 92, "img": "assets/sk/10_6_2.png"}, {"name": "絶対神の障壁", "type": "buff", "val": 85, "img": "assets/sk/10_6_3.png"}]},
            {"name": "【FINAL BOSS】全知全能のCEO・オーバーライド", "image_path": "assets/e/10_7.png", "hp": 550, "skills": [{"name": "ワールド・デリート", "type": "attack", "val": 90, "img": "assets/sk/10_7_1.png"}, {"name": "システム・オーバーロード", "type": "attack", "val": 110, "img": "assets/sk/10_7_2.png"}, {"name": "電脳神の完全無敵化", "type": "buff", "val": 100, "img": "assets/sk/10_7_3.png"}]},
        ],
    },
]

# ==========================================
# 3. ゲーム状態の初期化
# ==========================================
if "game_state" not in st.session_state:
  st.session_state.game_state = "TITLE"
  st.session_state.stage = 1
  st.session_state.ram = 3
  st.session_state.max_ram = 3
  st.session_state.allies = []
  st.session_state.current_enemy = None
  st.session_state.env_info = {}
  st.session_state.hand = []
  st.session_state.battle_log = []


def start_new_game():
  st.session_state.stage = 1
  st.session_state.allies = []
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
  start_battle()


def start_battle():
  s_idx = min(st.session_state.stage - 1, len(STAGES_DATA) - 1)
  stage_data = STAGES_DATA[s_idx]
  
  st.session_state.env_info = {
      "name": stage_data["env_name"],
      "desc": stage_data["env_desc"],
  }
  
  # 各ステージのボス1体＋雑魚敵6体（計7種類）の中からランダムに1体選出して戦闘相手にする
  chosen_enemy_data = random.choice(stage_data["enemies"])
  
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
      f"--- ステージ {st.session_state.stage} ({stage_data['env_name']}) 戦闘開始 ---"
  ]
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


# ==========================================
# 4. 画面描画 (Streamlit)
# ==========================================

if st.session_state.game_state == "TITLE":
  st.title("⚡ CYBER_DECK : ULTIMATE ENVIRONMENTS ⚡")
  st.markdown(
      "味方3体（各10固有スキル）を率い、全10ステージの**異なる環境**を踏破せよ！"
      "各ステージにはボス1体と雑魚6体（計7種×10＝70種類の個別敵データ、各3スキル）が待ち受ける本格カードバトル。"
  )
  if st.button("ゲームスタート", use_container_width=True):
    start_new_game()
    st.session_state.game_state = "BATTLE"
    st.rerun()

elif st.session_state.game_state == "BATTLE":
  st.title(f"⚡ STAGE {st.session_state.stage} / 10")

  # 環境情報バナーの表示
  env = st.session_state.env_info
  st.markdown(
      f"""<div class="env-box">
          <b>🌐 現在の環境: {env['name']}</b><br>
          <small>{env['desc']}</small>
          </div>""",
      unsafe_allow_html=True,
  )

  col_ally, col_enemy = st.columns(2)

  # 味方ステータス
  with col_ally:
    st.markdown("### 🟢 味方エージェント部隊")
    for a in st.session_state.allies:
      if a["alive"]:
        st.markdown(
            f"""<div class="ally-box">
                <b>{a['name']}</b><br>
                HP: {a['hp']} / {a['max_hp']} | シールド: {a['shield']}<br>
                <small>Img: <code>{a['image_path']}</code></small>
                </div>""",
            unsafe_allow_html=True,
        )
      else:
        st.markdown(f"<s style='color:gray;'>{a['name']} (DEFEATED)</s>", unsafe_allow_html=True)

  # 敵ステータス
  with col_enemy:
    st.markdown("### 🔴 遭遇した敵ターゲット")
    e = st.session_state.current_enemy
    if e:
      st.markdown(
          f"""<div class="enemy-box">
              <b>{e['name']}</b><br>
              HP: {e['hp']} / {e['max_hp']} | シールド: {e['shield']}<br>
              <small>Img: <code>{e['image_path']}</code></small>
              </div>""",
          unsafe_allow_html=True,
      )

  st.markdown("---")
  st.markdown(f"### 🔋 RAM (コスト): {st.session_state.ram} / {st.session_state.max_ram}")

  # 手札表示
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
                タイプ: {card['type']} ({card['val']})<br>
                <small>Icon: <code>{card['img']}</code></small>
                </div>""",
            unsafe_allow_html=True,
        )
        if st.button("使用", key=f"card_btn_{idx}"):
          if st.session_state.ram >= card["cost"]:
            st.session_state.ram -= card["cost"]

            # 効果処理
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

            # 撃破判定
            if e["hp"] <= 0:
              st.session_state.battle_log.append(f"👉 {e['name']} を撃破した！")
              if st.session_state.stage >= 10:
                st.session_state.game_state = "VICTORY"
              else:
                st.session_state.stage += 1
                start_battle()
            st.rerun()
          else:
            st.warning("RAMが不足しています！")

  if st.button("ターン終了 (敵の行動へ)", use_container_width=True):
    if e["hp"] > 0:
      eskill = random.choice(e["skills"])
      alive_allies = [a for a in st.session_state.allies if a["alive"]]
      if alive_allies:
        target = random.choice(alive_allies)
        dmg = eskill["val"]

        st.session_state.battle_log.append(
            f"🔴 {e['name']} は 【{eskill['name']}】 を使用した！"
        )

        if eskill["type"] == "attack":
          if target["shield"] >= dmg:
            target["shield"] -= dmg
            dmg = 0
          else:
            dmg -= target["shield"]
            target["shield"] = 0
            target["hp"] -= dmg
          st.session_state.battle_log.append(
              f"   -> {target['name']} に {eskill['val']} のダメージ！"
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

  # バトルログ
  st.markdown("### 📜 バトルログ")
  st.text("\n".join(reversed(st.session_state.battle_log[-5:])))

elif st.session_state.game_state == "VICTORY":
  st.title("🏆 ミッション完全クリア (VICTORY)")
  st.markdown("すべての異なる環境を突破し、メガコープの網からサイバーシティを解放しました！")
  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()

elif st.session_state.game_state == "GAMEOVER":
  st.title("💀 システムクラッシュ (GAME OVER)")
  st.markdown("エージェント部隊が全滅しました...")
  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()
