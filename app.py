
import streamlit as st

st.set_page_config(
    page_title="Гайд Інфлюенсера",
    page_icon="✨",
    layout="wide"
)

# Оформлення сайту
st.markdown("""<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
html, body, [class*="css"], button, input, textarea {
    font-family: 'Montserrat', sans-serif !important;
}
.stApp {
    background-color: #f5f7f3;
}
[data-testid="stSidebar"] {
    background-color: #243b35;
}
[data-testid="stSidebar"] * {
    color: #ffffff;
}
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #263e35;
    margin-bottom: 8px;
}
.subtitle {
    color: #718078;
    font-size: 17px;
    margin-bottom: 25px;
}
.info-card {
    background: white;
    padding: 25px;
    border-radius: 16px;
    border: 1px solid #e5ebe4;
    margin-bottom: 15px;
}
.tip {
    background: #e5efe7;
    padding: 18px;
    border-radius: 12px;
    color: #294a3b;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# Зміст гайду
steps = [
    {
        "title": "Твій вік та юридичний статус",
        "intro": "Перш ніж заробляти на контенті, важливо розуміти свої права та обов'язки.",
        "points": [
            "Якщо тобі ще немає 14 років, важливі юридичні питання щодо договорів і доходів мають вирішуватися за участю батьків або опікунів.",
            "У віці 14–18 років ти маєш певні права самостійно розпоряджатися доходами, але для окремих правочинів може бути потрібна згода батьків.",
            "Реєстрація підприємницької діяльності та укладання договорів мають свої вікові вимоги.",
            "Не підписуй документи, яких не розумієш. Обговорюй їх із батьками."
        ],
        "tip": "Порада: залучай дорослих, яким довіряєш, до співпраці з брендами та фінансових питань."
    },
    {
        "title": "Сплачуй податки правильно",
        "intro": "Дохід від блогінгу також може мати податкові наслідки.",
        "points": [
            "Доходом можуть бути рекламні інтеграції, монетизація, донати та оплата за створення контенту.",
            "Навіть подарунки або товари в обмін на рекламу можуть мати податкові наслідки.",
            "Зберігай інформацію про отримані виплати та домовленості з брендами.",
            "Порядок декларування та сплати податків залежить від виду доходу й твого юридичного статусу.",
            "Перед отриманням регулярного доходу проконсультуйся з батьками та фахівцем із податків."
        ],
        "tip": "Порада: веди окремий облік доходів, виплат і витрат. Це допоможе нічого не загубити."
    },
    {
        "title": "Дотримуйся правил реклами",
        "intro": "Реклама має бути чесною, зрозумілою та відповідати законодавству.",
        "points": [
            "Позначай рекламні публікації відповідним чином.",
            "Не видавай оплачений огляд за незалежну рекомендацію.",
            "Не поширюй неправдиві твердження про товари та послуги.",
            "Дотримуйся мовних вимог українського законодавства.",
            "Існують спеціальні обмеження щодо реклами алкоголю, тютюну, азартних ігор та інших категорій товарів."
        ],
        "tip": "Порада: якщо не впевнена, чи можна рекламувати певний продукт, спочатку перевір правила разом із дорослими."
    },
    {
        "title": "Поважай авторське право",
        "intro": "Твій контент має цінність. Але так само потрібно поважати творчість інших.",
        "points": [
            "Не використовуй чужі фотографії, відео та тексти без дозволу або належної правової підстави.",
            "Музика з бібліотек соціальних мереж може мати обмеження щодо комерційного використання.",
            "Для рекламних роликів перевіряй, чи дозволена комерційна ліцензія на музику та інші матеріали.",
            "Якщо використовуєш чужі матеріали, перевір умови ліцензії та необхідність зазначення автора.",
            "Зберігай оригінали своїх робіт і матеріали, що підтверджують авторство."
        ],
        "tip": "Порада: використовуй власні матеріали або перевірені ресурси з відповідними ліцензіями."
    },
    {
        "title": "Домовляйся з брендами письмово",
        "intro": "Навіть невелика рекламна співпраця потребує чітких домовленостей.",
        "points": [
            "Узгоджуй формат реклами: відео, допис, Stories чи інший матеріал.",
            "Обговорюй дату публікації та терміни виконання роботи.",
            "Заздалегідь визначай оплату, спосіб і строки її отримання.",
            "Домовляйся про кількість правок і додаткову оплату за них.",
            "Уточнюй, чи може бренд використовувати твоє відео у власній рекламі.",
            "Зберігай листування та копії домовленостей."
        ],
        "tip": "Порада: не передавай фінальний матеріал і не погоджуйся на незрозумілі умови, доки не обговориш їх із дорослими."
    }
]

# Початковий стан навігації
if "current_step" not in st.session_state:
    st.session_state.current_step = 0

def previous_step():
    st.session_state.current_step = max(
        0, st.session_state.current_step - 1
    )

def next_step():
    st.session_state.current_step = min(
        len(steps) - 1, st.session_state.current_step + 1
    )

# Бокове меню
with st.sidebar:
    st.markdown("## ✨ Гайд Інфлюенсера")
    st.markdown("---")
    st.markdown("### ТВОЄ НАВЧАННЯ")

    selected = st.radio(
        "Обери розділ:",
        options=list(range(len(steps))),
        format_func=lambda i: steps[i]['title'],
        key="current_step",
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.caption("Твій шлях у світі блогінгу ")

# Основна частина
current = steps[selected]

st.markdown(
    '<div class="main-title">✨ Гайд Інфлюенсера</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">Твій путівник у світі контенту, реклами та блогінгу</div>',
    unsafe_allow_html=True
)

st.progress((selected + 1) / len(steps))
st.caption(f"РОЗДІЛ {selected + 1} ІЗ {len(steps)}")

st.markdown(
   f'<div class="info-card"><h2>{current["title"]}</h2>'
    f'<p>{current["intro"]}</p></div>',
    unsafe_allow_html=True
)

st.markdown("### Що потрібно знати?")

for point in current["points"]:
    st.markdown(
        f'<div class="info-card">✓ {point}</div>',
        unsafe_allow_html=True
    )

st.markdown(
    f'<div class="tip"><b>💡 {current["tip"]}</b></div>',
    unsafe_allow_html=True
)

st.markdown("---")

# Навігація
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if selected > 0:
        st.button(
            "← Назад",
            on_click=previous_step,
            use_container_width=True
        )

with col2:
    st.markdown(
        f"<p style='text-align:center;color:#718078;'>"
        f"{selected + 1} / {len(steps)} розділів</p>",
        unsafe_allow_html=True
    )

with col3:
    if selected < len(steps) - 1:
        st.button(
            "Далі →",
            on_click=next_step,
            use_container_width=True
        )
    else:
        st.success("Ти завершила всі п'ять розділів! ")

st.caption(
    "Інформаційний гайд. Правові та податкові правила потрібно "
    "перевіряти за актуальним законодавством України.")
