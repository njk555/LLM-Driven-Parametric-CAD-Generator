import streamlit as st
import plotly.graph_objects as go
from stl import mesh
import numpy as np


def show_3d_model(stl_file):
    """
    Display an interactive STL model using Plotly.
    """

    try:

        stl_mesh = mesh.Mesh.from_file(stl_file)

        vertices = stl_mesh.vectors.reshape(-1, 3)

        x = vertices[:, 0]
        y = vertices[:, 1]
        z = vertices[:, 2]

        triangles = np.arange(len(vertices)).reshape(-1, 3)

        with st.container(border=True):

            st.subheader("🖥 Interactive CAD Viewer")

            st.caption("Rotate • Pan • Zoom")

            fig = go.Figure()

            fig.add_trace(

                go.Mesh3d(

                    x=x,
                    y=y,
                    z=z,

                    i=triangles[:, 0],
                    j=triangles[:, 1],
                    k=triangles[:, 2],

                    color="silver",

                    opacity=1,

                    flatshading=True,

                    lighting=dict(

                        ambient=0.55,

                        diffuse=0.95,

                        specular=0.60,

                        roughness=0.35,

                        fresnel=0.20

                    ),

                    lightposition=dict(

                        x=100,

                        y=200,

                        z=150

                    )

                )

            )

            fig.update_layout(

                height=700,

                margin=dict(

                    l=0,

                    r=0,

                    t=0,

                    b=0

                ),

                paper_bgcolor="#0E1117",

                plot_bgcolor="#0E1117",

                scene=dict(

                    bgcolor="#0E1117",

                    aspectmode="data",

                    camera=dict(

                        eye=dict(

                            x=1.4,

                            y=1.4,

                            z=1.1

                        ),

                        center=dict(

                            x=0,

                            y=0,

                            z=0

                        )

                    ),

                    xaxis=dict(

                        visible=False

                    ),

                    yaxis=dict(

                        visible=False

                    ),

                    zaxis=dict(

                        visible=False

                    )

                )

            )

            st.plotly_chart(

                fig,

                use_container_width=True

            )

    except Exception as e:

        st.error(f"Unable to display 3D model.\n\n{e}")