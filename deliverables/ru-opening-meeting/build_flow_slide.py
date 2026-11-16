#!/usr/bin/env python3
"""Opening-meeting slide: solid-dispersion manufacturing flow.

Redraws the source flowchart. Does not add or remove unit operations,
equipment, tests, or the stated moisture limit. English follows the
company terminology snapshot (CS Terminology 20260721).
"""

from __future__ import annotations

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.oxml.ns import qn
from pptx.util import Emu, Inches, Pt

# Widescreen 16:9, the size PowerPoint uses for a new on-screen deck.
SLIDE_W = 12192000
SLIDE_H = 6858000
EMU_IN = 914400

# Deck blue sampled from the existing opening-meeting header: RGB(0, 70, 155).
BLUE = "00469B"
INK = "1B2833"
SECONDARY = "5C6B78"
MUTED = "6E7C88"
LINE = "D5DEE6"
HAIR = "E4E9EE"
PAGE = "F4F6F8"
WHITE = "FFFFFF"
TINT = "E7F0F8"
ARROW = "8E9DAB"

LATIN = "Arial"
EA = "Microsoft YaHei"


def inches(value: float) -> Emu:
    return Emu(int(round(value * EMU_IN)))


def rgb(value: str) -> RGBColor:
    return RGBColor.from_string(value)


def _set_run(run, text, size, color, bold, lang):
    run.text = text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = False
    run.font.color.rgb = rgb(color)
    run.font.name = LATIN
    r_pr = run._r.get_or_add_rPr()
    r_pr.set("lang", lang)
    r_pr.set("b", "1" if bold else "0")
    r_pr.set("i", "0")
    for tag in ("a:latin", "a:ea", "a:cs"):
        face = EA if tag == "a:ea" else LATIN
        node = r_pr.find(qn(tag))
        if node is None:
            node = etree.SubElement(r_pr, qn(tag))
        node.set("typeface", face)


def write_lines(shape, lines, align="center", anchor="ctr", margins=(0.08, 0.08, 0.02, 0.02)):
    """lines: sequence of (text, size_pt, color, bold, lang)."""
    tf = shape.text_frame
    tf.clear()
    tf.word_wrap = True
    left, right, top, bottom = margins
    tf.margin_left = inches(left)
    tf.margin_right = inches(right)
    tf.margin_top = inches(top)
    tf.margin_bottom = inches(bottom)
    body = tf._txBody.find(qn("a:bodyPr"))
    body.set("anchor", anchor)
    align_map = {
        "center": PP_ALIGN.CENTER,
        "left": PP_ALIGN.LEFT,
        "right": PP_ALIGN.RIGHT,
    }
    for index, (text, size, color, bold, lang) in enumerate(lines):
        paragraph = tf.paragraphs[0] if index == 0 else tf.add_paragraph()
        paragraph.alignment = align_map[align]
        paragraph.space_before = Pt(0)
        paragraph.space_after = Pt(0)
        paragraph.line_spacing = 0.95
        run = paragraph.add_run()
        _set_run(run, text, size, color, bold, lang)
    return tf


def fill_rgb(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(color)


def no_line(shape):
    shape.line.fill.background()


def border(shape, color, width_pt):
    shape.line.color.rgb = rgb(color)
    shape.line.width = Pt(width_pt)


def round_rect(slide, x, y, w, h, radius_ratio):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, inches(x), inches(y), inches(w), inches(h)
    )
    # adj is the corner radius as a fraction of the shorter side.
    shape.adjustments[0] = radius_ratio
    return shape


def style_connector(shape, color, width_pt, tail=False):
    shape.line.color.rgb = rgb(color)
    shape.line.width = Pt(width_pt)
    if not tail:
        return
    ln = shape.line._get_or_add_ln()
    end = ln.find(qn("a:tailEnd"))
    if end is None:
        end = etree.SubElement(ln, qn("a:tailEnd"))
    end.set("type", "triangle")
    end.set("w", "sm")
    end.set("len", "sm")


def add_connector(slide, x1, y1, x2, y2, color=ARROW, width=1.25, tail=True):
    shape = slide.shapes.add_connector(
        MSO_CONNECTOR.STRAIGHT, inches(x1), inches(y1), inches(x2), inches(y2)
    )
    style_connector(shape, color, width, tail=tail)
    return shape


def build():
    prs = Presentation()
    prs.slide_width = Emu(SLIDE_W)
    prs.slide_height = Emu(SLIDE_H)
    prs.core_properties.title = "固体分散体生产流程"
    prs.core_properties.subject = "Solid dispersion manufacturing flow"
    prs.core_properties.category = "Opening meeting"

    slide = prs.slides.add_slide(prs.slide_layouts[6])
    background = slide.background
    background.fill.solid()
    background.fill.fore_color.rgb = rgb(PAGE)

    # Deck-matching rule. One blue, used as a hairline rather than as a fill for every step.
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Emu(SLIDE_W), inches(0.06))
    fill_rgb(bar, BLUE)
    no_line(bar)
    bar.name = "Top rule"

    title = slide.shapes.add_textbox(inches(0.48), inches(0.14), inches(8.8), inches(0.40))
    write_lines(
        title,
        [("固体分散体生产流程", 26, INK, True, "zh-CN")],
        align="left",
        anchor="ctr",
        margins=(0.02, 0.02, 0.0, 0.0),
    )
    title.name = "Title"

    subtitle = slide.shapes.add_textbox(inches(0.48), inches(0.52), inches(9.0), inches(0.24))
    write_lines(
        subtitle,
        [("Manufacturing flow of the solid dispersion", 15, BLUE, False, "en-US")],
        align="left",
        anchor="ctr",
        margins=(0.02, 0.02, 0.0, 0.0),
    )
    subtitle.name = "Subtitle"

    russian = slide.shapes.add_textbox(inches(0.48), inches(0.74), inches(9.2), inches(0.22))
    write_lines(
        russian,
        [("Технологическая схема производства твёрдой дисперсии", 12, MUTED, False, "ru-RU")],
        align="left",
        anchor="ctr",
        margins=(0.02, 0.02, 0.0, 0.0),
    )
    russian.name = "Russian subtitle"

    # The panel is the Grade D boundary drawn on the source figure.
    # Controls stay outside that boundary. The slide does not state where testing is performed.
    panel_x, panel_y, panel_w, panel_h = 0.42, 1.02, 8.16, 5.90
    panel_r = panel_x + panel_w
    panel_b = panel_y + panel_h

    panel = round_rect(slide, panel_x, panel_y, panel_w, panel_h, 0.012)
    fill_rgb(panel, WHITE)
    border(panel, "D9E1E8", 1.25)
    panel.name = "Grade D boundary"

    zone = slide.shapes.add_textbox(inches(0.64), inches(panel_y + 0.05), inches(5.8), inches(0.40))
    zone.fill.background()
    no_line(zone)
    write_lines(
        zone,
        [
            ("车间  ·  D级洁净区", 13, BLUE, True, "zh-CN"),
            ("Grade D cleanroom  ·  Класс D", 12, BLUE, False, "en-US"),
        ],
        align="left",
        anchor="ctr",
        margins=(0.02, 0.02, 0.0, 0.0),
    )
    zone.name = "Cleanroom label"

    equip_x, equip_w = 0.58, 3.28
    step_x, step_w = 4.16, 3.90
    step_r = step_x + step_w
    spine_x = step_x + step_w / 2
    ctrl_x, ctrl_w = 9.08, 3.84

    # Uniform steps, with a wider channel after concentration so the
    # crystal-form branch is visibly between concentration and milling.
    flow_top = panel_y + 0.92
    flow_bottom = panel_b - 0.12
    count = 7
    gaps_after = [0.15, 0.15, 0.34, 0.15, 0.15, 0.15]
    branch_gap = gaps_after[2]
    card_h = (flow_bottom - flow_top - sum(gaps_after)) / count
    rows = []
    cursor = flow_top
    for i in range(count):
        rows.append(cursor)
        if i < count - 1:
            cursor += card_h + gaps_after[i]

    header_y = panel_y + 0.56
    header_h = 0.24

    def header(x, y, w, h, text, align):
        box = slide.shapes.add_textbox(inches(x), inches(y), inches(w), inches(h))
        box.fill.background()
        no_line(box)
        write_lines(
            box,
            [(text, 12, MUTED, False, "zh-CN")],
            align=align,
            anchor="ctr",
            margins=(0.04, 0.04, 0.0, 0.0),
        )
        return box

    header(equip_x, header_y, equip_w, header_h, "设备    Equipment", "right").name = "Header equipment"
    header(step_x, header_y, step_w, header_h, "工艺步骤    Process step", "center").name = "Header step"
    header(ctrl_x, header_y, ctrl_w, header_h, "控制    Control", "left").name = "Header control"

    hair_y = panel_y + 0.84
    inside_hair = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, inches(0.64), inches(hair_y), inches(panel_r - 0.78), inches(0.01)
    )
    fill_rgb(inside_hair, HAIR)
    no_line(inside_hair)
    outside_hair = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, inches(ctrl_x), inches(hair_y), inches(ctrl_w), inches(0.01)
    )
    fill_rgb(outside_hair, HAIR)
    no_line(outside_hair)

    steps = [
        ("物料", "Materials", None, "terminus"),
        ("溶解", "Dissolution", None, "step"),
        ("浓缩", "Concentration", ("旋转蒸发器", "Rotary Evaporator"), "step"),
        ("粉碎", "Milling", ("高效吸尘粉碎机", "High-Efficiency Dust-Extraction Mill"), "step"),
        ("干燥", "Drying", ("热风循环烘箱", "Hot Air Circulating Oven"), "step"),
        ("混合", "Blending", ("三维运动混合机", "Three-Dimensional Mixer"), "step"),
        ("固体分散体", "Solid Dispersion", None, "terminus"),
    ]

    for index, ((cn, en, equipment, kind), y) in enumerate(zip(steps, rows)):
        if kind == "terminus":
            card = round_rect(slide, step_x, y, step_w, card_h, 0.5)
            fill_rgb(card, TINT)
            border(card, BLUE, 1.25)
            write_lines(
                card,
                [(cn, 15, INK, True, "zh-CN"), (en, 11, SECONDARY, False, "en-US")],
                align="center",
                margins=(0.28, 0.28, 0.02, 0.02),
            )
        else:
            card = round_rect(slide, step_x, y, step_w, card_h, 0.12)
            fill_rgb(card, WHITE)
            border(card, LINE, 1.0)
            write_lines(
                card,
                [(cn, 15, INK, True, "zh-CN"), (en, 11, SECONDARY, False, "en-US")],
                align="center",
                margins=(0.10, 0.10, 0.04, 0.03),
            )
        card.name = f"Step {cn}"

        if equipment:
            label = slide.shapes.add_textbox(inches(equip_x), inches(y), inches(equip_w), inches(card_h))
            label.fill.background()
            no_line(label)
            write_lines(
                label,
                [
                    (equipment[0], 13, INK, False, "zh-CN"),
                    (equipment[1], 11, SECONDARY, False, "en-US"),
                ],
                align="right",
                margins=(0.04, 0.10, 0.04, 0.02),
            )
            label.name = f"Equipment {equipment[0]}"

        if index < count - 1 and index != 2:
            # The concentration-to-milling channel is drawn with the branch node.
            y1 = y + card_h
            y2 = rows[index + 1]
            add_connector(slide, spine_x, y1, spine_x, y2, tail=True).name = f"Flow {index}"

    def control_card(y, lines, name):
        card = round_rect(slide, ctrl_x, y, ctrl_w, card_h, 0.12)
        fill_rgb(card, WHITE)
        border(card, LINE, 1.0)
        card.name = name
        write_lines(
            card,
            lines,
            align="left",
            margins=(0.20, 0.10, 0.04, 0.03),
        )
        rail = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            inches(ctrl_x + 0.08),
            inches(y + 0.14),
            inches(0.045),
            inches(card_h - 0.28),
        )
        fill_rgb(rail, BLUE)
        no_line(rail)
        rail.name = name + " rail"
        return card

    # Sub-batch crystal form leaves the flow after concentration and before milling.
    junction_y = rows[2] + card_h + branch_gap / 2
    crystal_y = junction_y - card_h / 2
    dot_r = 0.038
    control_card(
        crystal_y,
        [
            ("亚批晶型检测", 15, INK, True, "zh-CN"),
            ("Sub-batch crystal form testing", 12, SECONDARY, False, "en-US"),
        ],
        "Control crystal form",
    )
    add_connector(
        slide, spine_x, rows[2] + card_h, spine_x, junction_y - dot_r, tail=False
    ).name = "Flow into branch"
    add_connector(
        slide, spine_x, junction_y + dot_r, spine_x, rows[3], tail=True
    ).name = "Flow out of branch"
    add_connector(
        slide, spine_x + dot_r, junction_y, ctrl_x, junction_y, tail=True
    ).name = "Branch crystal form"
    dot = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        inches(spine_x - dot_r),
        inches(junction_y - dot_r),
        inches(dot_r * 2),
        inches(dot_r * 2),
    )
    fill_rgb(dot, BLUE)
    no_line(dot)
    dot.name = "Branch node"

    drying_mid = rows[4] + card_h / 2
    control_card(
        rows[4],
        [
            ("过程控制：水分 < 3.0%", 15, INK, True, "zh-CN"),
            ("In-process control: Moisture < 3.0%", 11, SECONDARY, False, "en-US"),
        ],
        "Control moisture",
    )
    add_connector(slide, step_r, drying_mid, ctrl_x, drying_mid, tail=True).name = "Branch moisture"

    output_mid = rows[6] + card_h / 2
    control_card(
        rows[6],
        [
            ("按固体分散体质量标准检测", 14, INK, True, "zh-CN"),
            ("Per the solid dispersion quality specification", 11, SECONDARY, False, "en-US"),
        ],
        "Control specification",
    )
    add_connector(slide, step_r, output_mid, ctrl_x, output_mid, tail=True).name = "Branch specification"

    legend = slide.shapes.add_textbox(inches(0.42), inches(7.08), inches(12.50), inches(0.32))
    legend.fill.background()
    no_line(legend)
    write_lines(
        legend,
        [
            (
                "起止为物料与产物    ·    中间为单元操作    ·    左侧为设备    ·    右侧为检测与过程控制",
                11,
                MUTED,
                False,
                "zh-CN",
            ),
            (
                "Input and output at the ends    ·    Unit operations in the center    ·    Equipment on the left    ·    Controls on the right",
                10,
                MUTED,
                False,
                "en-US",
            ),
        ],
        align="center",
        anchor="ctr",
        margins=(0.0, 0.0, 0.0, 0.0),
    )
    legend.name = "Legend"

    notes = slide.notes_slide.notes_text_frame
    notes.text = (
        "本页用于首次会议说明固体分散体的生产流程。只调整了原图的颜色和版式，"
        "没有增加或删减步骤、设备、检测项目和限度。\n\n"
        "建议讲解顺序：\n"
        "1. 生产在车间 D 级洁净区内完成。白框内是生产流程和对应设备。\n"
        "2. 物料经溶解、浓缩、粉碎、干燥、混合，得到固体分散体。\n"
        "3. 浓缩使用旋转蒸发器，粉碎使用高效吸尘粉碎机，干燥使用热风循环烘箱，"
        "混合使用三维运动混合机。溶解步骤原图未标注设备，本页不补充。\n"
        "4. 亚批晶型检测位于浓缩之后、粉碎之前，与原图的分支位置一致。\n"
        "5. 干燥的过程控制为水分 < 3.0%，限度未改。此处“水分”按公司用语译为 Moisture，"
        "不改写成干燥失重。\n"
        "6. 得到的固体分散体按固体分散体质量标准检测。\n"
        "7. 三项检测仍画在洁净区边框之外，与原图一致。这是版式位置，不是对检测地点的结论。"
        "如果检查员问检测在何处进行，按实际操作和受控文件说明。\n\n"
        "英文采用公司受控术语：Grade D cleanroom、Rotary Evaporator、"
        "High-Efficiency Dust-Extraction Mill、Hot Air Circulating Oven、"
        "Three-Dimensional Mixer、Crystal Form、in-process control、Quality Specification。"
        "溶解译为 Dissolution，粉碎译为 Milling，混合译为 Blending，与现有固体分散体记录用语一致。"
        "Dissolution 在这里是生产中的溶解，不是溶出度检查。\n"
        "俄文只用于本页主题和洁净级别，方便俄方识别；设备名称未译成俄文，以避免未经核对的设备译名。"
    )

    print(
        f"card_h={card_h:.3f} branch_gap={branch_gap:.3f} "
        f"rows={[round(y, 3) for y in rows]}"
    )
    print(f"crystal_y={crystal_y:.3f} junction_y={junction_y:.3f} panel_b={panel_b:.3f}")
    return prs


if __name__ == "__main__":
    output = "/agent/repos/HUANGQIUXIA/deliverables/ru-opening-meeting/solid-dispersion-manufacturing-flow.pptx"
    build().save(output)
    print(output)
