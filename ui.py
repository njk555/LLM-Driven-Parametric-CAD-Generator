import streamlit as st


def create_ui():

    # ==================================================
    # PAGE CONFIG
    # ==================================================

    st.set_page_config(
        page_title="LLM Driven Parametric CAD Generator",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # ==================================================
    # SIDEBAR
    # ==================================================

    with st.sidebar:

        st.title("🤖 CAD Generator")

        st.caption("Version 1.1")

        st.divider()

        st.subheader("📦 Supported Models")

        st.write("• Box")
        st.write("• Cylinder")
        st.write("• Sphere")
        st.write("• Plate")
        st.write("• Hollow Cylinder")

        st.divider()

        st.subheader("🕳 Supported Features")

        st.write("• Through Hole")
        st.write("• Blind Hole")

        st.divider()

        st.subheader("⚙ Tech Stack")

        st.write("• Streamlit")
        st.write("• Groq")
        st.write("• CadQuery")
        st.write("• Plotly")
        st.write("• Pydantic")

        st.divider()

        debug_mode = st.checkbox(
            "🐞 Debug Mode",
            value=False
        )

        st.divider()

        st.success("Natural Language ➜ CAD Model")

    # ==================================================
    # HEADER
    # ==================================================

    st.title("🤖 LLM Driven Parametric CAD Generator")

    st.caption(
        "Generate professional 3D CAD models using Natural Language and AI."
    )

    st.divider()

    # ==================================================
    # INPUT
    # ==================================================

    st.subheader("Describe your CAD Model")

    with st.expander("💡 Example Prompts"):

        st.code(
"""
Create a box of length 100 mm width 50 mm height 30 mm

Create a cylinder of diameter 40 mm height 80 mm

Create a sphere of diameter 50 mm

Create a plate of length 120 mm width 80 mm thickness 10 mm

Create a hollow cylinder with outer diameter 60 mm inner diameter 40 mm height 100 mm

Create a box of length 100 mm width 60 mm height 30 mm with a hole of diameter 20 mm

Create a box of length 100 mm width 60 mm height 30 mm with a blind hole of diameter 20 mm depth 10 mm
"""
        )

    prompt = st.text_area(
        "",
        height=180,
        placeholder="Example: Create a box of length 100 mm width 50 mm height 30 mm"
    )

    # ==================================================
    # BUTTONS
    # ==================================================

    col1, col2 = st.columns([5, 1])

    with col1:

        generate = st.button(
            "🚀 Generate CAD",
            type="primary",
            use_container_width=True
        )

    with col2:

        clear = st.button(
            "🗑 Clear",
            use_container_width=True
        )

    if clear:
        st.rerun()

    st.divider()

    # ==================================================
    # OUTPUT COLUMNS
    # ==================================================

    left, right = st.columns(
        [1, 1],
        gap="large"
    )

    # ==================================================
    # FOOTER
    # ==================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:

        st.caption("🤖 AI")

        st.caption("Groq")

    with c2:

        st.caption("⚙ CAD")

        st.caption("CadQuery")

    with c3:

        st.caption("🖥 Viewer")

        st.caption("Plotly")

    st.caption(
        "Developed by Noel JK"
    )

    # ==================================================
    # RETURN
    # ==================================================

    return (
        prompt,
        generate,
        left,
        right,
        debug_mode
    )