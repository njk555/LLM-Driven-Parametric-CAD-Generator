import cadquery as cq


# ======================================================
# BOX
# ======================================================

def create_box(length, width, height):

    return (
        cq.Workplane("XY")
        .box(
            length,
            width,
            height
        )
    )


# ======================================================
# CYLINDER
# ======================================================

def create_cylinder(diameter, height):

    radius = diameter / 2

    return (
        cq.Workplane("XY")
        .circle(radius)
        .extrude(height)
    )


# ======================================================
# SPHERE
# ======================================================

def create_sphere(diameter):

    radius = diameter / 2

    return (
        cq.Workplane("XY")
        .sphere(radius)
    )


# ======================================================
# PLATE
# ======================================================

def create_plate(length, width, thickness):

    return (
        cq.Workplane("XY")
        .box(
            length,
            width,
            thickness
        )
    )


# ======================================================
# HOLLOW CYLINDER
# ======================================================

def create_hollow_cylinder(
    outer_diameter,
    inner_diameter,
    height
):

    outer_radius = outer_diameter / 2
    inner_radius = inner_diameter / 2

    return (
        cq.Workplane("XY")
        .circle(outer_radius)
        .circle(inner_radius)
        .extrude(height)
    )


# ======================================================
# HOLE
# ======================================================

def add_hole(model, hole):

    workplane = (
        model
        .faces(">Z")
        .workplane()
        .center(
            hole.x,
            hole.y
        )
    )

    if hole.type.upper() == "THROUGH":

        return workplane.hole(
            hole.diameter
        )

    elif hole.type.upper() == "BLIND":

        if hole.depth is None:

            raise ValueError(
                "Blind hole requires depth."
            )

        return workplane.hole(
            hole.diameter,
            depth=hole.depth
        )

    return model