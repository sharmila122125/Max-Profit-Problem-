import streamlit as st
from max_profit import max_profit_schedule_with_tiebreak

st.set_page_config(page_title="Max Profit Gallery", layout="wide")

# ---------- HEADER ----------
st.markdown(
    """
    <div style='text-align:center; padding-top:10px;'>
      <h1 style='margin:0; font-size:34px; color:#f5c542;'>🏗️ Max Profit Visual Gallery</h1>
      <p style='margin:4px 0; color:#e5e5e5;'>Optimal building mix for given time</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------- INPUT ----------
col_a, col_b = st.columns([3,1])
with col_a:
    n = st.number_input("Time units (n)", min_value=1, value=15, step=1)
with col_b:
    clicked = st.button(
        "Calculate",
        use_container_width=True,
        help="Compute best profit mix"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------- RESULT ----------
if clicked:
    profit, t, p, c = max_profit_schedule_with_tiebreak(int(n))

    # Main card
    st.markdown(
        f"""
        <div style="
          background:#0d0d0d;
          color:#f5c542;
          padding:20px;
          border-radius:12px;
          border: 1px solid #f5c542;
          box-shadow:0 0 18px rgba(245,197,66,0.3);
        ">
          <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;">
            <div style="font-size:22px; font-weight:600;">Optimal Plan • n = {int(n)}</div>
            <div style="text-align:right;">
              <div style="font-size:14px; color:#f0e6c5;">Total Earnings</div>
              <div style="font-size:30px; font-weight:700;">${profit:,}</div>
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Building Cards (Premium Gold Theme) ----------
    cards = [
        ("Theatre (T)", "🎭", t, "#f5c542"),
        ("Pub (P)", "🍺", p, "#f5c542"),
        ("Commercial (C)", "🏢", c, "#f5c542")
    ]

    col1, col2, col3 = st.columns(3)

    for col, (title, icon, count, gold) in zip([col1, col2, col3], cards):
        with col:
            st.markdown(
                f"""
                <div style="
                  border-radius:12px;
                  padding:16px;
                  background:#111111;
                  color:white;
                  border:1px solid {gold};
                  box-shadow:0 0 12px rgba(245,197,66,0.25);
                ">
                  <div style="display:flex; align-items:center; gap:12px;">
                    <div style="font-size:32px; background:{gold}; width:56px; height:56px;
                                display:flex; align-items:center; justify-content:center;
                                border-radius:10px; color:black;">
                      {icon}
                    </div>
                    <div>
                      <div style="font-weight:600; font-size:18px; color:{gold};">{title}</div>
                    </div>
                  </div>

                  <div style="margin-top:14px;">
                    <div style="font-size:13px; color:#dddddd;">Count</div>
                    <div style="font-size:24px; font-weight:700; color:{gold};">{count}</div>
                  </div>
                </div>
                """,
                unsafe_allow_html=True
            )
