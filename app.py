import random
import streamlit as st

# ページ設定とサイバーパンク風カスタムCSS
st.set_page_config(
    page_title="CYBER_DECK: 10_STAGES_ULTIMATE", page_icon="⚡", layout="wide"
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

# ==========================================
# 1. 味方キャラクター & スキルデータリストの定義 (3体 × 10スキル)
# ==========================================
ALLIES_DATA = [
    {
        "name": "詩音 (サイバーニンジャ)",
        "image_path": "assets/allies/shion.png",
        "hp": 110,
        "skills": [
            {
                "name": "ブレードスラッシュ",
                "type": "attack",
                "val": 20,
                "img": "assets/skills/shion_1.png",
            },
            {
                "name": "影分身ステップ",
                "type": "shield",
                "val": 15,
                "img": "assets/skills/shion_2.png",
            },
            {
                "name": "クナイ連擲",
                "type": "attack",
                "val": 25,
                "img": "assets/skills/shion_3.png",
            },
            {
                "name": "ナノマシン応急処置",
                "type": "heal",
                "val": 25,
                "img": "assets/skills/shion_4.png",
            },
            {
                "name": "超感覚サイバーアイ",
                "type": "ram",
                "val": 1,
                "img": "assets/skills/shion_5.png",
            },
            {
                "name": "プラズマ居合斬り",
                "type": "attack",
                "val": 40,
                "img": "assets/skills/shion_6.png",
            },
            {
                "name": "ステルス・フィールド",
                "type": "shield",
                "val": 30,
                "img": "assets/skills/shion_7.png",
            },
            {
                "name": "ファントム・ストライク",
                "type": "attack",
                "val": 55,
                "img": "assets/skills/shion_8.png",
            },
            {
                "name": "完全自己修復",
                "type": "heal",
                "val": 50,
                "img": "assets/skills/shion_9.png",
            },
            {
                "name": "アクセラレートRAM",
                "type": "ram",
                "val": 2,
                "img": "assets/skills/shion_10.png",
            },
        ],
    },
    {
        "name": "サイファー (スナイパー)",
        "image_path": "assets/allies/cypher.png",
        "hp": 85,
        "skills": [
            {
                "name": "精密ショット",
                "type": "attack",
                "val": 22,
                "img": "assets/skills/cypher_1.png",
            },
            {
                "name": "カモフラージュネット",
                "type": "shield",
                "val": 12,
                "img": "assets/skills/cypher_2.png",
            },
            {
                "name": "アーマーピアシング",
                "type": "attack",
                "val": 30,
                "img": "assets/skills/cypher_3.png",
            },
            {
                "name": "フィールド・メディキット",
                "type": "heal",
                "val": 20,
                "img": "assets/skills/cypher_4.png",
            },
            {
                "name": "ターゲティング支援",
                "type": "ram",
                "val": 1,
                "img": "assets/skills/cypher_5.png",
            },
            {
                "name": "ハイパースナイプ",
                "type": "attack",
                "val": 45,
                "img": "assets/skills/cypher_6.png",
            },
            {
                "name": "デコイ展開",
                "type": "shield",
                "val": 25,
                "img": "assets/skills/cypher_7.png",
            },
            {
                "name": "バースト・狙撃",
                "type": "attack",
                "val": 60,
                "img": "assets/skills/cypher_8.png",
            },
            {
                "name": "メディカル・ドローン",
                "type": "heal",
                "val": 40,
                "img": "assets/skills/cypher_9.png",
            },
            {
                "name": "オーバークロックCPU",
                "type": "ram",
                "val": 2,
                "img": "assets/skills/cypher_10.png",
            },
        ],
    },
    {
        "name": "アイリーン (飛行攻撃アーマー)",
        "image_path": "assets/allies/irene.png",
        "hp": 130,
        "skills": [
            {
                "name": "エアリアル・バルカン",
                "type": "attack",
                "val": 18,
                "img": "assets/skills/irene_1.png",
            },
            {
                "name": "エナジー・バリア",
                "type": "shield",
                "val": 20,
                "img": "assets/skills/irene_2.png",
            },
            {
                "name": "マイクロミサイル",
                "type": "attack",
                "val": 35,
                "img": "assets/skills/irene_3.png",
            },
            {
                "name": "応急システムパッチ",
                "type": "heal",
                "val": 30,
                "img": "assets/skills/irene_4.png",
            },
            {
                "name": "ジェネレーター稼働",
                "type": "ram",
                "val": 1,
                "img": "assets/skills/irene_5.png",
            },
            {
                "name": "プラズマ・キャノン",
                "type": "attack",
                "val": 50,
                "img": "assets/skills/irene_6.png",
            },
            {
                "name": "重装甲フィールド",
                "type": "shield",
                "val": 40,
                "img": "assets/skills/irene_7.png",
            },
            {
                "name": "ストライク・ボム",
                "type": "attack",
                "val": 70,
                "img": "assets/skills/irene_8.png",
            },
            {
                "name": "全回路オーバーホール",
                "type": "heal",
                "val": 60,
                "img": "assets/skills/irene_9.png",
            },
            {
                "name": "コア・ジェネレーター",
                "type": "ram",
                "val": 3,
                "img": "assets/skills/irene_10.png",
            },
        ],
    },
]

# ==========================================
# 2. 敵キャラクター & スキルデータリストの定義 (計9種類：雑魚8体 ＋ ボス1体)
# 各敵キャラは異なる5種類のスキルを所持
# ==========================================
def make_enemy_skills(tag, base):
  return [
      {"name": f"{tag}・アタック1", "type": "attack", "val": base, "img": f"assets/enemies/{tag}_s1.png"},
      {"name": f"{tag}・アタック2", "type": "attack", "val": int(base * 1.3), "img": f"assets/enemies/{tag}_s2.png"},
      {"name": f"{tag}・バースト", "type": "attack", "val": int(base * 1.6), "img": f"assets/enemies/{tag}_s3.png"},
      {"name": f"{tag}・チャージ", "type": "buff", "val": int(base * 0.8), "img": f"assets/enemies/{tag}_s4.png"},
      {"name": f"{tag}・フィニッシュ", "type": "attack", "val": int(base * 2.0), "img": f"assets/enemies/{tag}_s5.png"},
  ]

ENEMIES_DATA = [
    # ステージ1〜8: 雑魚敵8体
    {"name": "Sec-Drone MK-I", "image_path": "assets/enemies/drone.png", "hp": 70, "skills": make_enemy_skills("drone", 10)},
    {"name": "Street-Ganger", "image_path": "assets/enemies/ganger.png", "hp": 90, "skills": make_enemy_skills("ganger", 13)},
    {"name": "Corpo-Enforcer", "image_path": "assets/enemies/enforcer.png", "hp": 110, "skills": make_enemy_skills("enforcer", 16)},
    {"name": "Net-Assassin", "image_path": "assets/enemies/assassin.png", "hp": 130, "skills": make_enemy_skills("assassin", 19)},
    {"name": "Cyber-Hound", "image_path": "assets/enemies/hound.png", "hp": 150, "skills": make_enemy_skills("hound", 22)},
    {"name": "Heavy-Guard", "image_path": "assets/enemies/guard.png", "hp": 180, "skills": make_enemy_skills("guard", 25)},
    {"name": "Rogue-AI Agent", "image_path": "assets/enemies/ai.png", "hp": 210, "skills": make_enemy_skills("ai", 28)},
    {"name": "Borg-Commander", "image_path": "assets/enemies/commander.png", "hp": 250, "skills": make_enemy_skills("commander", 32)},
    # ステージ9・10用（ステージ10はFINAL BOSS）
    {"name": "Corp-Director", "image_path": "assets/enemies/director.png", "hp": 300, "skills": make_enemy_skills("director", 38)},
    {"name": "FINAL BOSS: CEO 'OVERRIDE'", "image_path": "assets/enemies/boss.png", "hp": 450, "skills": make_enemy_skills("boss", 45)},
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
  # ステージに応じた敵を設定 (ステージ1〜10)
  idx = min(st.session_state.stage - 1, len(ENEMIES_DATA) - 1)
  edata = ENEMIES_DATA[idx]
  st.session_state.current_enemy = {
      "name": f"Stage {st.session_state.stage}: {edata['name']}",
      "image_path": edata["image_path"],
      "hp": edata["hp"],
      "max_hp": edata["hp"],
      "shield": 0,
      "skills": edata["skills"],
  }
  st.session_state.ram = 3
  st.session_state.max_ram = 3
  st.session_state.battle_log = [
      f"--- ステージ {st.session_state.stage} バトル開始 ---"
  ]
  draw_cards()


def draw_cards():
  # 生きている味方の全スキルからランダムに4枚を手札として配る（コストは仮で1〜2に設定）
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
# 4. 画面描画ロジック (Streamlit)
# ==========================================

if st.session_state.game_state == "TITLE":
  st.title("⚡ CYBER_DECK : 10_STAGES ⚡")
  st.markdown(
      "味方3体（各10種類の固有スキル）を率い、全10ステージ（雑魚8体＋ボス2体、各5種類のスキル所持）を"
      "突破する本格スキルカードバトル！"
  )
  if st.button("ゲームスタート", use_container_width=True):
    start_new_game()
    st.session_state.game_state = "BATTLE"
    st.rerun()

elif st.session_state.game_state == "BATTLE":
  st.title(f"⚡ STAGE {st.session_state.stage} / 10")

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
                <small>Image: <code>{a['image_path']}</code></small>
                </div>""",
            unsafe_allow_html=True,
        )
      else:
        st.markdown(f"<s style='color:gray;'>{a['name']} (DEFEATED)</s>", unsafe_allow_html=True)

  # 敵ステータス
  with col_enemy:
    st.markdown("### 🔴 敵ターゲット")
    e = st.session_state.current_enemy
    if e:
      st.markdown(
          f"""<div class="enemy-box">
              <b>{e['name']}</b><br>
              HP: {e['hp']} / {e['max_hp']} | シールド: {e['shield']}<br>
              <small>Image: <code>{e['image_path']}</code></small>
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

            # スキル効果処理
            if card["type"] == "attack":
              e["hp"] -= card["val"]
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！"
                  f" 敵に {card['val']} のダメージ！"
              )
            elif card["type"] == "shield":
              for a in st.session_state.allies:
                if a["name"] == card["owner"]:
                  a["shield"] += card["val"]
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！"
                  f" シールド +{card['val']}！"
              )
            elif card["type"] == "heal":
              for a in st.session_state.allies:
                if a["name"] == card["owner"]:
                  a["hp"] = min(a["max_hp"], a["hp"] + card["val"])
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！"
                  f" HPを {card['val']} 回復！"
              )
            elif card["type"] == "ram":
              st.session_state.ram = min(
                  st.session_state.max_ram, st.session_state.ram + card["val"]
              )
              st.session_state.battle_log.append(
                  f"{card['owner']} の 【{card['name']}】！"
                  f" RAMが {card['val']} 回復！"
              )

            st.session_state.hand.pop(idx)

            # 敵撃破判定
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
      # 敵が所持する5種類のスキルからランダムに1つ選択して発動
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

        # 味方の生存確認
        if target["hp"] <= 0:
          target["hp"] = 0
          target["alive"] = False
          st.session_state.battle_log.append(
              f"💀 {target['name']} が戦闘不能になった..."
          )

        # 全滅判定
        if not any(a["alive"] for a in st.session_state.allies):
          st.session_state.game_state = "GAMEOVER"

    # ターン終了処理
    st.session_state.ram = st.session_state.max_ram
    draw_cards()
    st.rerun()

  # ログ
  st.markdown("### 📜 バトルログ")
  st.text("\n".join(reversed(st.session_state.battle_log[-5:])))

elif st.session_state.game_state == "VICTORY":
  st.title("🏆 ミッションクリア (VICTORY)")
  st.markdown("全10ステージを制覇し、サイバーシティの平穏を取り戻しました！")
  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()

elif st.session_state.game_state == "GAMEOVER":
  st.title("💀 システムクラッシュ (GAME OVER)")
  st.markdown("エージェント部隊が全滅しました...")
  if st.button("タイトルに戻る", use_container_width=True):
    st.session_state.game_state = "TITLE"
    st.rerun()
