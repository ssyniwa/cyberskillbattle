import random
import streamlit as st

# ページ設定とサイバーパンク風カスタムCSS
st.set_page_config(
    page_title="CYBER_DECK: 10_STAGES", page_icon="⚡", layout="wide"
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
    </style>
    """,
    unsafe_allow_html=True,
)

# --- ゲームデータの初期化 ---
if "game_state" not in st.session_state:
  st.session_state.game_state = "TITLE"  # TITLE, BATTLE, VICTORY, GAMEOVER
  st.session_state.stage = 1
  st.session_state.ram = 3
  st.session_state.max_ram = 3

  # 味方3体
  st.session_state.allies = [
    {
        "name": "詩音 (サイバーニンジャ)",
        "hp": 100,
        "max_hp": 100,
        "shield": 0,
        "alive": True,
    },
    {
        "name": "サイファー (スナイパー)",
        "hp": 80,
        "max_hp": 80,
        "shield": 0,
        "alive": True,
    },
    {
        "name": "アイリーン (飛行攻撃アーマー)",
        "hp": 130,
        "max_hp": 130,
        "shield": 0,
        "alive": True,
    },
  ]

  # 敵データ生成関数
  st.session_state.current_enemy = None
  st.session_state.hand = []
  st.session_state.battle_log = []


def init_enemy(stage):
  if stage < 10:
    names = [
        "Sec-Drone MK-I",
        "Corpo-Enforcer",
        "Street-Ganger",
        "Net-Assassin",
        "Cyber-Hound",
        "Heavy-Guard",
        "Rogue-AI Agent",
        "Corp-Assassinator",
        "Borg-Commander",
    ]
    name = names[(stage - 1) % len(names)]
    hp = 60 + stage * 15
    return {"name": f"Stage {stage}: {name}", "hp": hp, "max_hp": hp, "attack": 12 + stage * 3}
  else:
    return {
        "name": "FINAL BOSS: CEO 'OVERRIDE'",
        "hp": 300,
        "max_hp": 300,
        "attack": 35,
    }


def draw_cards():
  all_cards = [
      {
          "id": 1,
          "name": "スラッシュ・ブレード",
          "cost": 1,
          "type": "attack",
          "val": 25,
          "desc": "単体に25ダメージ",
      },
      {
          "id": 2,
          "name": "EMPバースト",
          "cost": 2,
          "type": "attack",
          "val": 50,
          "desc": "単体に50ダメージ",
      },
      {
          "id": 3,
          "name": "ファイアウォール",
          "cost": 1,
          "type": "shield",
          "val": 20,
          "desc": "味方全体にシールド20付与",
      },
      {
          "id": 4,
          "name": "リブート・パッチ",
          "cost": 2,
          "type": "heal",
          "val": 30,
          "desc": "味方一人のHPを30回復",
      },
      {
          "id": 5,
          "name": "オーバークロック",
          "cost": 0,
          "type": "ram",
          "val": 2,
          "desc": "RAMを2回復する",
      },
  ]
  # ランダムに4枚手札に加える
  st.session_state.hand = [random.choice(all_cards) for _ in range(4)]


def start_battle():
  st.session_state.game_state = "BATTLE"
  st.session_state.current_enemy = init_enemy(st.session_state.stage)
  st.session_state.ram = 3
  st.session_state.max_ram = 3
  st.session_state.battle_log = [
      f"--- ステージ {st.session_state.stage} 戦闘開始 ---"
  ]
  draw_cards()


# --- 画面描画：タイトル ---
if st.session_state.game_state == "TITLE":
  st.title("⚡ CYBER_DECK : 10_STAGES ⚡")
  st.markdown(
      "西暦2088年のネオン輝くメガシティ。あなたは3人の精鋭エージェントを率い、"
      "全10ステージに及ぶコーポレート・タワーの深部へと潜入する。"
  )
  st.markdown("スキルカードを駆使してすべての敵をハック＆スラッシュで排除せよ。")
  if st.button("ゲームスタート", use_container_width=True):
    # ステータス初期化
    st.session_state.stage = 1
    for a in st.session_state.allies:
      a["hp"] = a["max_hp"]
      a["shield"] = 0
      a["alive"] = True
    start_battle()
    st.rerun()

# --- 画面描画：バトル画面 ---
elif st.session_state.game_state == "BATTLE":
  st.title(f"⚡ STAGE {st.session_state.stage} / 10")

  # ステータス表示エリア
  col_ally, col_enemy = st.columns(2)

  with col_ally:
    st.markdown("### 🟢 味方エージェント")
    for i, a in enumerate(st.session_state.allies):
      if a["alive"]:
        st.markdown(
            f"""<div class="ally-box">
                <b>{a['name']}</b><br>
                HP: {a['hp']} / {a['max_hp']} | シールド: {a['shield']}
                </div>""",
            unsafe_allow_html=True,
        )
        # 回復対象選択などのためのインデックス保存
      else:
        st.markdown(f"<s style='color:gray;'>{a['name']} (DEFEATED)</s>", unsafe_allow_html=True)

  with col_enemy:
    st.markdown("### 🔴 敵ターゲット")
    e = st.session_state.current_enemy
    if e:
      st.markdown(
          f"""<div class="enemy-box">
              <b>{e['name']}</b><br>
              HP: {e['hp']} / {e['max_hp']} | 攻撃力: {e['attack']}
              </div>""",
          unsafe_allow_html=True,
      )

  st.markdown("---")
  st.markdown(f"### 🔋 RAM (コスト): {st.session_state.ram} / {st.session_state.max_ram}")

  # 手札とカードプレイ
  st.markdown("### 🃏 スキルカード (手札)")
  cols = st.columns(len(st.session_state.hand))
  for idx, card in enumerate(st.session_state.hand):
    with cols[idx]:
      st.markdown(
          f"""<div class="card-box">
              <b>{card['name']}</b><br>
              コスト: {card['cost']} RAM<br>
              <small>{card['desc']}</small>
              </div>""",
          unsafe_allow_html=True,
      )
      if st.button("使用", key=f"card_{idx}"):
        if st.session_state.ram >= card["cost"]:
          st.session_state.ram -= card["cost"]
          # カード効果処理
          if card["type"] == "attack":
            e["hp"] -= card["val"]
            st.session_state.battle_log.append(
                f"プレイヤーは {card['name']} を使い、{e['name']} に"
                f" {card['val']} のダメージ！"
            )
          elif card["type"] == "shield":
            for a in st.session_state.allies:
              if a["alive"]:
                a["shield"] += card["val"]
            st.session_state.battle_log.append(
                f"プレイヤーは {card['name']} を使い、全体にシールド"
                f" +{card['val']}！"
            )
          elif card["type"] == "heal":
            # 生きている味方のうち最もHPが減っている者を回復
            alive_allies = [a for a in st.session_state.allies if a["alive"]]
            if alive_allies:
              target = min(alive_allies, key=lambda x: x["hp"])
              target["hp"] = min(target["max_hp"], target["hp"] + card["val"])
              st.session_state.battle_log.append(
                  f"プレイヤーは {card['name']} を使い、{target['name']} のHPを"
                  f" {card['val']} 回復！"
              )
          elif card["type"] == "ram":
            st.session_state.ram = min(
                st.session_state.max_ram, st.session_state.ram + card["val"]
            )
            st.session_state.battle_log.append(
                f"プレイヤーは {card['name']} を使い、RAMが"
                f" {card['val']} 回復した！"
            )

          # 手札から使用したカードを削除して補充
          st.session_state.hand.pop(idx)
          
          # 敵の撃破判定
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

  if st.button("ターン終了 (敵の攻撃へ)", use_container_width=True):
    # 敵のターン
    if e["hp"] > 0:
      alive_allies = [a for a in st.session_state.allies if a["alive"]]
      if alive_allies:
        target_ally = random.choice(alive_allies)
        dmg = e["attack"]
        # シールド計算
        if target_ally["shield"] >= dmg:
          target_ally["shield"] -= dmg
          dmg = 0
        else:
          dmg -= target_ally["shield"]
          target_ally["shield"] = 0
          target_ally["hp"] -= dmg

        st.session_state.battle_log.append(
            f"🔴 {e['name']} の攻撃！ {target_ally['name']} に {e['attack']}"
            " のダメージ！"
        )

        if target_ally["hp"] <= 0:
          target_ally["hp"] = 0
          target_ally["alive"] = False
          st.session_state.battle_log.append(
              f"💀 {target_ally['name']} が戦闘不能になった..."
          )

        # 全滅判定
        if not any(a["alive"] for a in st.session_state.allies):
          st.session_state.game_state = "GAMEOVER"

    # RAM回復＆手札再ドロー
    st.session_state.ram = st.session_state.max_ram
    draw_cards()
    st.rerun()

  # バトルログ表示
  st.markdown("### 📜 バトルログ")
  log_text = "\n".join(reversed(st.session_state.battle_log[-5:]))
  st.text(log_text)

# --- 画面描画：勝利画面 ---
elif st.session_state.game_state == "VICTORY":
  st.title("🏆 勝利！ (MISSION COMPLETE)")
  st.markdown(
      "おめでとうございます！ すべてのステージを突破し、メガコープのCEOを"
      "ハッキングしてネットワークの自由を取り戻しました。"
  )
  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()

# --- 画面描画：ゲームオーバー画面 ---
elif st.session_state.game_state == "GAMEOVER":
  st.title("💀 ゲームオーバー (SYSTEM CRASH)")
  st.markdown("エージェント部隊が全滅しました... サイバー空間の闇に消え去ります。")
  if st.button("リトライ", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()
