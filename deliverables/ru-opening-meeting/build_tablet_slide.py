#!/usr/bin/env python3
"""Opening-meeting slide: Chidamide Tablets manufacturing flow.

Redraws the source figure. Does not add or remove steps, feeds, equipment,
in-process controls, specification tests, or the moisture limit. Step codes
aa and SS are kept as written. English follows CS Terminology 20260721 where
an exact entry exists.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Emu

import build_flow_slide as base

BLUE = base.BLUE
ON_BLUE = base.ON_BLUE
INK = base.INK
SECONDARY = base.SECONDARY
MUTED = base.MUTED
WHITE = base.WHITE
ENV = base.ENV
GPA = "E6E8EB"
PAGE = base.PAGE


def slide_deck():
    prs = Presentation()
    prs.slide_width = Emu(base.SLIDE_W)
    prs.slide_height = Emu(base.SLIDE_H)
    prs.core_properties.title = "西达本胺片生产流程"
    prs.core_properties.subject = "Manufacturing flow of Chidamide Tablets"
    prs.core_properties.category = "Opening meeting"
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    slide.background.fill.solid()
    slide.background.fill.fore_color.rgb = base.rgb(PAGE)
    return prs, slide


def textbox(slide, x, y, w, h, lines, align="center", anchor="ctr", margins=(0.06, 0.06, 0.02, 0.02)):
    box = slide.shapes.add_textbox(base.inches(x), base.inches(y), base.inches(w), base.inches(h))
    box.fill.background()
    base.no_line(box)
    base.write_lines(box, lines, align=align, anchor=anchor, margins=margins)
    return box


def blue_card(slide, x, y, w, h, lines, pill=False):
    card = base.round_rect(slide, x, y, w, h, 0.5 if pill else 0.14)
    base.fill_rgb(card, BLUE)
    base.no_line(card)
    base.write_lines(
        card,
        lines,
        align="center",
        margins=(0.08, 0.08, 0.02, 0.02),
    )
    return card


def ipc_card(slide, x, y, w, h, lines, name):
    card = base.round_rect(slide, x, y, w, h, 0.12)
    base.fill_rgb(card, WHITE)
    base.border(card, base.LINE, 1.0)
    card.name = name
    base.write_lines(card, lines, align="left", margins=(0.16, 0.08, 0.03, 0.02))
    rail = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE,
        base.inches(x + 0.06),
        base.inches(y + 0.10),
        base.inches(0.04),
        base.inches(max(0.16, h - 0.20)),
    )
    base.fill_rgb(rail, BLUE)
    base.no_line(rail)
    return card


def build():
    prs, slide = slide_deck()

    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Emu(base.SLIDE_W), base.inches(0.05))
    base.fill_rgb(bar, BLUE)
    base.no_line(bar)

    textbox(
        slide, 0.42, 0.10, 12.4, 0.36,
        [("西达本胺片生产流程", 26, INK, True, "zh-CN")],
        align="left", margins=(0.02, 0.02, 0.0, 0.0),
    ).name = "Title"
    textbox(
        slide, 0.42, 0.44, 12.4, 0.22,
        [("Manufacturing flow of Chidamide Tablets", 15, BLUE, False, "en-US")],
        align="left", margins=(0.02, 0.02, 0.0, 0.0),
    ).name = "Subtitle"
    textbox(
        slide, 0.42, 0.64, 12.4, 0.20,
        [("Технологическая схема производства таблеток хидамида", 12, MUTED, False, "ru-RU")],
        align="left", margins=(0.02, 0.02, 0.0, 0.0),
    ).name = "Russian subtitle"

    panel_x, panel_y, panel_w, panel_h = 0.30, 0.96, 9.42, 5.96
    panel_r = panel_x + panel_w
    panel_b = panel_y + panel_h
    panel = base.round_rect(slide, panel_x, panel_y, panel_w, panel_h, 0.012)
    base.fill_rgb(panel, ENV)
    base.border(panel, BLUE, 1.5)
    panel.name = "Building 4"

    textbox(
        slide, 0.46, panel_y + 0.04, 8.8, 0.36,
        [
            ("4号楼  ·  D级洁净区与一般生产区", 13, BLUE, True, "zh-CN"),
            ("Building 4  ·  Grade D cleanroom and general production area", 11, BLUE, False, "en-US"),
        ],
        align="left",
        margins=(0.02, 0.02, 0.0, 0.0),
    ).name = "Building label"

    # Geometry. Two wider channels keep the specification branches
    # after final blending and after tableting, as on the source figure.
    flow_top = panel_y + 0.46
    flow_bottom = panel_b - 0.08
    # Wider channels after final blending and after tableting.
    gaps_after = [0.08, 0.08, 0.08, 0.08, 0.24, 0.24, 0.08]
    count = 8
    card_h = (flow_bottom - flow_top - sum(gaps_after)) / count
    rows = []
    cursor = flow_top
    for i in range(count):
        rows.append(cursor)
        if i < count - 1:
            cursor += card_h + gaps_after[i]

    step_x, step_w = 2.28, 2.52
    step_r = step_x + step_w
    spine = step_x + step_w / 2
    feed_x, feed_w = 0.44, 1.68
    equip_x, equip_w = 4.90, 1.88
    ipc_x, ipc_w = 6.86, 2.72
    spec_x, spec_w = 9.92, 3.08

    # General production area is only the outer-packaging row.
    gpa_top = rows[7] - 0.08
    gpa = base.round_rect(slide, panel_x + 0.08, gpa_top, panel_w - 0.16, panel_b - gpa_top - 0.08, 0.04)
    base.fill_rgb(gpa, GPA)
    base.border(gpa, "C5CAD1", 1.0)
    gpa.name = "General production area"

    feeds = {
        1: ("物料", "Materials"),
        2: ("纯化水", "Purified water"),
        4: ("物料", "Materials"),
    }
    equipment = {
        1: ("高效湿法混合制粒机", "High-Shear Wet Granulator", "right"),
        2: ("摇摆颗粒机", "Oscillating Granulator", "right"),
        3: ("热风循环烘箱", "Hot Air Circulating Oven", "left"),
        4: ("三维运动混合机", "Three-Dimensional Mixer", "right"),
        5: ("压片机", "Tablet Press", "left"),
    }
    steps = [
        ([("固体分散体", 15, WHITE, True, "zh-CN"), ("Solid dispersion", 11, ON_BLUE, False, "en-US")], True),
        ([("aa", 18, WHITE, True, "en-US")], False),
        ([("SS", 18, WHITE, True, "en-US")], False),
        ([("干燥", 15, WHITE, True, "zh-CN"), ("Drying", 11, ON_BLUE, False, "en-US")], False),
        ([("总混", 15, WHITE, True, "zh-CN"), ("Final blending", 11, ON_BLUE, False, "en-US")], False),
        ([("压片", 15, WHITE, True, "zh-CN"), ("Tableting", 11, ON_BLUE, False, "en-US")], False),
        ([("内包装", 15, WHITE, True, "zh-CN"), ("Primary packaging", 11, ON_BLUE, False, "en-US")], False),
        ([("外包装", 15, WHITE, True, "zh-CN"), ("Secondary packaging", 11, ON_BLUE, False, "en-US")], False),
    ]

    for index, ((lines, pill), y) in enumerate(zip(steps, rows)):
        card = blue_card(slide, step_x, y, step_w, card_h, lines, pill=pill)
        card.name = f"Step {index}"
        if index < count - 1 and index not in (4, 5):
            base.add_connector(slide, spine, y + card_h, spine, rows[index + 1], tail=True)

    for index, (cn, en) in feeds.items():
        y = rows[index] + (card_h - 0.40) / 2
        pill = blue_card(
            slide, feed_x, y, feed_w, 0.40,
            [(cn, 13, WHITE, True, "zh-CN"), (en, 10, ON_BLUE, False, "en-US")],
            pill=True,
        )
        pill.name = f"Feed {cn} {index}"
        base.add_connector(slide, feed_x + feed_w, y + 0.20, step_x, y + 0.20, tail=True)

    for index, (cn, en, side) in equipment.items():
        y = rows[index]
        if side == "right":
            label = textbox(
                slide, equip_x, y, equip_w, card_h,
                [(cn, 12, INK, False, "zh-CN"), (en, 10, SECONDARY, False, "en-US")],
                align="left",
                margins=(0.04, 0.02, 0.02, 0.02),
            )
        else:
            label = textbox(
                slide, feed_x, y, feed_w, card_h,
                [(cn, 12, INK, False, "zh-CN"), (en, 10, SECONDARY, False, "en-US")],
                align="right",
                margins=(0.02, 0.06, 0.02, 0.02),
            )
        label.name = f"Equipment {cn}"

    textbox(
        slide, feed_x, rows[6], feed_w, card_h,
        [
            ("401口服固体制剂车间", 10, BLUE, True, "zh-CN"),
            ("D级洁净区", 10, BLUE, True, "zh-CN"),
            ("OSD Workshop 401", 9, SECONDARY, False, "en-US"),
        ],
        align="right",
        margins=(0.02, 0.04, 0.0, 0.0),
    ).name = "Workshop 401 Grade D"

    textbox(
        slide, feed_x, rows[7], feed_w, card_h,
        [
            ("401口服固体制剂车间", 10, INK, True, "zh-CN"),
            ("一般生产区", 10, INK, True, "zh-CN"),
            ("General production area", 9, SECONDARY, False, "en-US"),
        ],
        align="right",
        margins=(0.02, 0.04, 0.0, 0.0),
    ).name = "Workshop 401 GPA"

    def spec_card(y, lines, name):
        return ipc_card(slide, spec_x, y, spec_w, 0.58, lines, name)

    # After final blending, before tableting: tablet-granule specification.
    junction_granule = rows[4] + card_h + gaps_after[4] / 2
    dot_r = 0.034
    base.add_connector(slide, spine, rows[4] + card_h, spine, junction_granule - dot_r, tail=False)
    base.add_connector(slide, spine, junction_granule + dot_r, spine, rows[5], tail=True)
    base.add_connector(slide, spine + dot_r, junction_granule, spec_x, junction_granule, tail=True)
    dot = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        base.inches(spine - dot_r), base.inches(junction_granule - dot_r),
        base.inches(dot_r * 2), base.inches(dot_r * 2),
    )
    base.fill_rgb(dot, BLUE)
    base.no_line(dot)
    spec_card(
        junction_granule - 0.29,
        [
            ("按片颗粒质量标准检测", 13, INK, True, "zh-CN"),
            ("Tablet granule quality specification", 11, SECONDARY, False, "en-US"),
        ],
        "Spec tablet granules",
    )

    # After tableting, before primary packaging: uncoated-tablet specification.
    junction_core = rows[5] + card_h + gaps_after[5] / 2
    base.add_connector(slide, spine, rows[5] + card_h, spine, junction_core - dot_r, tail=False)
    base.add_connector(slide, spine, junction_core + dot_r, spine, rows[6], tail=True)
    base.add_connector(slide, spine + dot_r, junction_core, spec_x, junction_core, tail=True)
    dot2 = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        base.inches(spine - dot_r), base.inches(junction_core - dot_r),
        base.inches(dot_r * 2), base.inches(dot_r * 2),
    )
    base.fill_rgb(dot2, BLUE)
    base.no_line(dot2)
    spec_card(
        junction_core - 0.29,
        [
            ("按素片质量标准检测", 13, INK, True, "zh-CN"),
            ("Uncoated tablet quality specification", 11, SECONDARY, False, "en-US"),
        ],
        "Spec uncoated tablets",
    )

    ipc_card(
        slide, ipc_x, rows[3] + (card_h - 0.50) / 2, ipc_w, 0.50,
        [
            ("过程控制：水分 < 5.0%", 12, INK, True, "zh-CN"),
            ("In-process control: Moisture < 5.0%", 10, SECONDARY, False, "en-US"),
        ],
        "IPC moisture",
    )
    base.add_connector(slide, step_r, rows[3] + card_h / 2, ipc_x, rows[3] + card_h / 2, tail=True)

    ipc_card(
        slide, ipc_x, rows[5], ipc_w, card_h,
        [
            ("过程控制：a) 片重；b) 硬度", 10, INK, True, "zh-CN"),
            ("c) 崩解时限；d) 分散时限", 10, INK, False, "zh-CN"),
            ("a) Tablet weight; b) Hardness", 9, SECONDARY, False, "en-US"),
            ("c) Disintegration time; d) Dispersion time", 9, SECONDARY, False, "en-US"),
        ],
        "IPC tableting",
    )
    base.add_connector(slide, step_r, rows[5] + card_h / 2, ipc_x, rows[5] + card_h / 2, tail=True)

    for index, name in ((6, "IPC primary"), (7, "IPC secondary")):
        mid = rows[index] + card_h / 2
        ipc_card(
            slide, ipc_x, mid - 0.25, ipc_w, 0.50,
            [
                ("过程控制：包装气密性", 12, INK, True, "zh-CN"),
                ("In-process control: Package integrity", 10, SECONDARY, False, "en-US"),
            ],
            name,
        )
        base.add_connector(slide, step_r, mid, ipc_x, mid, tail=True)

    # Finished-product specification leaves outer packaging along the bottom
    # of the general production area, as drawn, and does not cross the IPC card.
    spec_h = 0.58
    spec_y = rows[7] + (card_h - spec_h) / 2
    route_y = spec_y + spec_h + 0.06
    base.add_connector(slide, step_r, rows[7] + card_h, step_r, route_y, tail=False)
    base.add_connector(slide, step_r, route_y, spec_x + spec_w / 2, route_y, tail=False)
    base.add_connector(
        slide, spec_x + spec_w / 2, route_y, spec_x + spec_w / 2, spec_y + spec_h, tail=True
    )
    spec_card(
        spec_y,
        [
            ("按西达本胺片质量标准检测", 13, INK, True, "zh-CN"),
            ("Chidamide Tablets quality specification", 10, SECONDARY, False, "en-US"),
        ],
        "Spec Chidamide Tablets",
    )

    textbox(
        slide, 0.36, 7.04, 12.6, 0.36,
        [
            (
                "浅蓝为 D 级洁净区    ·    灰色为一般生产区    ·    深蓝为工艺步骤    ·    框内为过程控制    ·    框外为质量标准检测",
                11,
                MUTED,
                False,
                "zh-CN",
            ),
            (
                "Blue field: Grade D    ·    Gray field: general production area    ·    Deep blue: process steps    ·    Controls inside    ·    Specification tests outside",
                10,
                MUTED,
                False,
                "en-US",
            ),
        ],
        align="center",
        margins=(0.0, 0.0, 0.0, 0.0),
    ).name = "Legend"

    notes = slide.notes_slide.notes_text_frame
    notes.text = (
        "本页按原图重绘西达本胺片从固体分散体到包装的流程，供首次会议使用。"
        "没有增加或删减步骤、投入、设备、过程控制、质量标准检测和水分限度。\n\n"
        "建议讲解顺序：\n"
        "1. 全页在 4 号楼。浅蓝色区域为 D 级洁净区，灰色区域为一般生产区。\n"
        "2. 固体分散体与物料进入 aa，设备为高效湿法混合制粒机。纯化水进入 SS，设备为摇摆颗粒机。"
        "aa、SS 是原图上的步骤代号，本页不另作解释。\n"
        "3. 干燥使用热风循环烘箱，过程控制为水分 < 5.0%。\n"
        "4. 物料进入总混，设备为三维运动混合机。总混之后、压片之前，按片颗粒质量标准检测。\n"
        "5. 压片使用压片机。过程控制为片重、硬度、崩解时限、分散时限。压片之后、内包装之前，按素片质量标准检测。\n"
        "6. 内包装位于 401 口服固体制剂车间 D 级洁净区，过程控制为包装气密性。\n"
        "7. 外包装位于 401 口服固体制剂车间一般生产区，过程控制为包装气密性。"
        "外包装之后按西达本胺片质量标准检测。原图中该连线沿一般生产区下沿引出，本页保持这一接法。\n"
        "8. 过程控制画在环境框内，三项质量标准检测画在框外，与原图一致。"
        "这是版式位置，不是对检测地点的结论。\n\n"
        "受控术语：Solid dispersion、Drying、Final blending、Tableting、"
        "High-Shear Wet Granulator、Oscillating Granulator、Hot Air Circulating Oven、"
        "Three-Dimensional Mixer、Grade D cleanroom、General Production Area、"
        "Oral Solid Dosage Form Workshop、Chidamide Tablets、uncoated tablet。\n"
        "纯化水译为 Purified Water，包装气密性译为 Package integrity，"
        "片重、硬度、崩解时限、分散时限分别译为 Tablet weight、Hardness、"
        "Disintegration time、Dispersion time。术语库没有这些条目的单独词条，按药典和专业用语处理。"
        "压片机译为 Tablet Press，不写入原图没有的设备型号。"
    )

    print(f"card_h={card_h:.3f}")
    print("rows", [round(y, 3) for y in rows])
    print(f"granule_y={junction_granule:.3f} core_y={junction_core:.3f} gpa_top={gpa_top:.3f} panel_b={panel_b:.3f}")
    print(f"route_y={route_y:.3f} spec_bottom={spec_y + spec_h:.3f}")
    return prs


if __name__ == "__main__":
    output = Path(__file__).resolve().parent / "chidamide-tablet-manufacturing-flow.pptx"
    build().save(output)
    print(output)
