import os
import cadquery as cq

from models import CADRequest

from shapes import (
    create_box,
    create_cylinder,
    create_sphere,
    create_plate,
    create_hollow_cylinder,
    add_hole
)

EXPORT_FOLDER = "exports"

os.makedirs(EXPORT_FOLDER, exist_ok=True)


# =====================================================
# Validate Parameters
# =====================================================

def validate_parameters(parameters, required):

    missing = []

    for item in required:

        if item not in parameters:
            missing.append(item)

    if missing:

        raise ValueError(
            "Missing parameters: "
            + ", ".join(missing)
        )


# =====================================================
# Generate CAD Model
# =====================================================

def generate_model(request: CADRequest):

    shape = request.shape.upper()

    p = request.parameters

    # -------------------------------------------------
    # BOX
    # -------------------------------------------------

    if shape == "BOX":

        validate_parameters(
            p,
            [
                "length",
                "width",
                "height"
            ]
        )

        model = create_box(

            p["length"],

            p["width"],

            p["height"]

        )

        if request.hole is not None:

            model = add_hole(
                model,
                request.hole
            )

    # -------------------------------------------------
    # CYLINDER
    # -------------------------------------------------

    elif shape == "CYLINDER":

        validate_parameters(
            p,
            [
                "diameter",
                "height"
            ]
        )

        model = create_cylinder(

            p["diameter"],

            p["height"]

        )

    # -------------------------------------------------
    # SPHERE
    # -------------------------------------------------

    elif shape == "SPHERE":

        validate_parameters(
            p,
            [
                "diameter"
            ]
        )

        model = create_sphere(

            p["diameter"]

        )

    # -------------------------------------------------
    # PLATE
    # -------------------------------------------------

    elif shape == "PLATE":

        validate_parameters(
            p,
            [
                "length",
                "width",
                "thickness"
            ]
        )

        model = create_plate(

            p["length"],

            p["width"],

            p["thickness"]

        )

    # -------------------------------------------------
    # HOLLOW CYLINDER
    # -------------------------------------------------

    elif shape == "HOLLOW_CYLINDER":

        validate_parameters(
            p,
            [
                "outer_diameter",
                "inner_diameter",
                "height"
            ]
        )

        model = create_hollow_cylinder(

            p["outer_diameter"],

            p["inner_diameter"],

            p["height"]

        )

    else:

        raise ValueError(
            f"Unsupported Shape: {shape}"
        )

    return model


# =====================================================
# Export STEP
# =====================================================

def export_step(model):

    filename = os.path.join(

        EXPORT_FOLDER,

        "model.step"

    )

    cq.exporters.export(

        model,

        filename

    )

    return filename


# =====================================================
# Export STL
# =====================================================

def export_stl(model):

    filename = os.path.join(

        EXPORT_FOLDER,

        "model.stl"

    )

    cq.exporters.export(

        model,

        filename

    )

    return filename