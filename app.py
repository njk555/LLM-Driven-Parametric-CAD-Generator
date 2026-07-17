import time
import streamlit as st

from ui import create_ui
from llm import generate_cad

from cad import (
    generate_model,
    export_step,
    export_stl
)

from viewer import show_3d_model


# ==========================================================
# MAIN
# ==========================================================

def main():

    (
        prompt,
        generate,
        left,
        right,
        debug_mode
    ) = create_ui()

    step_file = None
    stl_file = None

    if generate:

        if not prompt.strip():

            st.warning(
                "Please enter a CAD description."
            )

            st.stop()

        start = time.time()

        with st.spinner(
            "Generating CAD Model..."
        ):

            try:

                # ==========================================
                # LLM
                # ==========================================

                request = generate_cad(prompt)

                # ==========================================
                # TERMINAL OUTPUT
                # ==========================================

                print("\n" + "=" * 70)
                print("LLM GENERATED JSON")
                print("=" * 70)

                print(
                    request.model_dump_json(
                        indent=4
                    )
                )

                print("=" * 70 + "\n")

                # ==========================================
                # CAD GENERATION
                # ==========================================

                model = generate_model(request)

                step_file = export_step(model)

                stl_file = export_stl(model)

                elapsed = round(
                    time.time() - start,
                    2
                )

                st.success(
                    f"✅ CAD Model Generated in {elapsed} seconds"
                )

                # ==========================================
                # SUMMARY
                # ==========================================

                with left:

                    st.subheader(
                        "📊 CAD Summary"
                    )

                    c1, c2, c3 = st.columns(3)

                    c1.metric(
                        "Shape",
                        request.shape
                    )

                    c2.metric(
                        "Units",
                        request.units
                    )

                    c3.metric(
                        "Parameters",
                        len(request.parameters)
                    )

                    st.divider()

                    st.subheader(
                        "Dimensions"
                    )

                    for key, value in request.parameters.items():

                        st.metric(

                            key.replace(
                                "_",
                                " "
                            ).title(),

                            f"{value} mm"

                        )

                    # ======================================
                    # HOLE
                    # ======================================

                    if request.hole is not None:

                        st.divider()

                        st.subheader(
                            "🕳 Hole Information"
                        )

                        hole = request.hole

                        h1, h2 = st.columns(2)

                        h1.metric(
                            "Type",
                            hole.type
                        )

                        h2.metric(
                            "Diameter",
                            f"{hole.diameter} mm"
                        )

                        if hole.type.upper() == "BLIND":

                            st.metric(
                                "Depth",
                                f"{hole.depth} mm"
                            )

                        st.caption(
                            f"Position : ({hole.x} mm, {hole.y} mm)"
                        )

                # ==========================================
                # DEBUG MODE
                # ==========================================

                if debug_mode:

                    with right:

                        st.subheader(
                            "📄 AI Response"
                        )

                        st.json(
                            request.model_dump()
                        )

                # ==========================================
                # VIEWER
                # ==========================================

                st.divider()

                show_3d_model(
                    stl_file
                )
            except Exception as e:

                st.error(
                    "❌ Error while generating CAD model."
                )

                if debug_mode:
                    st.exception(e)
                else:
                    st.error(str(e))

    else:

        st.info(
            "💡 Enter a CAD prompt above and click **Generate CAD**."
        )

    # ==========================================================
    # DOWNLOADS
    # ==========================================================

    st.divider()

    st.subheader("📦 Export Files")

    col1, col2 = st.columns(2)

    # ==========================================================
    # STEP
    # ==========================================================

    with col1:

        with st.container(border=True):

            st.markdown("### 📄 STEP")

            st.caption(
                "Standard CAD exchange format "
                "(SolidWorks, Fusion 360, CATIA, NX, Creo)"
            )

            if step_file:

                with open(step_file, "rb") as file:

                    st.download_button(
                        label="⬇ Download STEP",
                        data=file.read(),
                        file_name="model.step",
                        mime="application/octet-stream",
                        use_container_width=True
                    )

            else:

                st.button(
                    "⬇ Download STEP",
                    disabled=True,
                    use_container_width=True
                )

    # ==========================================================
    # STL
    # ==========================================================

    with col2:

        with st.container(border=True):

            st.markdown("### 🖨 STL")

            st.caption(
                "3D Printing format "
                "(Cura, PrusaSlicer, Bambu Studio)"
            )

            if stl_file:

                with open(stl_file, "rb") as file:

                    st.download_button(
                        label="⬇ Download STL",
                        data=file.read(),
                        file_name="model.stl",
                        mime="application/octet-stream",
                        use_container_width=True
                    )

            else:

                st.button(
                    "⬇ Download STL",
                    disabled=True,
                    use_container_width=True
                )

    # ==========================================================
    # FOOTER
    # ==========================================================

    st.divider()

    c1, c2, c3 = st.columns(3)

    with c1:
        st.caption("🤖 AI")
        st.caption("Groq LLM")

    with c2:
        st.caption("⚙ CAD")
        st.caption("CadQuery")

    with c3:
        st.caption("🖥 Viewer")
        st.caption("Plotly")

    st.caption(
        "Developed by Noel JK"
    )


# ==========================================================
# ENTRY POINT
# ==========================================================

if __name__ == "__main__":

    main()