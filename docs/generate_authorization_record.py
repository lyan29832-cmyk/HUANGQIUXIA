#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate GMP duty authorization record (Word)."""

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn, nsmap
from docx.shared import Cm, Pt, Emu, RGBColor, Twips


def set_run_font(run, name="宋体", size=10.5, bold=False, color=None):
    run.bold = bold
    run.font.size = Pt(size)
    run.font.name = name
    if color:
        run.font.color.rgb = color
    r = run._element
    rPr = r.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    rFonts.set(qn("w:ascii"), name)
    rFonts.set(qn("w:hAnsi"), name)
    rFonts.set(qn("w:eastAsia"), name)
    rFonts.set(qn("w:cs"), name)


def set_cell_shading(cell, fill="D9E2F3"):
    tc = cell._tePr if hasattr(cell, "_tePr") else cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), fill)
    shd.set(qn("w:val"), "clear")
    tcPr.append(shd)


def set_cell_margins(cell, top=40, bottom=40, left=60, right=60):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcMar = OxmlElement("w:tcMar")
    for m, v in (("top", top), ("left", left), ("bottom", bottom), ("right", right)):
        node = OxmlElement(f"w:{m}")
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")
        tcMar.append(node)
    tcPr.append(tcMar)


def set_table_borders(table, sz="8", color="000000"):
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}")
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), sz)
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), color)
        borders.append(el)
    tblPr.append(borders)


def prevent_row_split(row):
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)


def set_col_widths(table, widths_cm):
    table.autofit = False
    table.allow_autofit = False
    total = int(sum(Cm(w) for w in widths_cm))
    tbl = table._tbl
    tblPr = tbl.tblPr
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    tblW.set(qn("w:w"), str(total))
    tblW.set(qn("w:type"), "dxa")
    grid = tbl.find(qn("w:tblGrid"))
    if grid is not None:
        for child in list(grid):
            grid.remove(child)
    else:
        grid = OxmlElement("w:tblGrid")
        tblPr.append(grid)
    for w in widths_cm:
        gc = OxmlElement("w:gridCol")
        gc.set(qn("w:w"), str(int(Cm(w))))
        grid.append(gc)
    for row in table.rows:
        for i, cell in enumerate(row.cells):
            if i < len(widths_cm):
                cell.width = Cm(widths_cm[i])
                tc = cell._tc
                tcPr = tc.get_or_add_tcPr()
                tcW = tcPr.find(qn("w:tcW"))
                if tcW is None:
                    tcW = OxmlElement("w:tcW")
                    tcPr.append(tcW)
                tcW.set(qn("w:w"), str(int(Cm(widths_cm[i]))))
                tcW.set(qn("w:type"), "dxa")


def clear_cell(cell):
    for p in cell.paragraphs:
        p.clear()
        pf = p.paragraph_format
        pf.space_before = Pt(0)
        pf.space_after = Pt(0)
        pf.line_spacing = 1.0


def add_text(cell, text, size=10.5, bold=False, align="left", space_after=0, color=None, font="宋体"):
    p = cell.paragraphs[0] if (cell.paragraphs and not cell.paragraphs[0].text) else cell.add_paragraph()
    if cell.paragraphs[0].text == "" and len(cell.paragraphs) == 1:
        p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.08
    if align == "center":
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == "right":
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    else:
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    set_run_font(run, font, size, bold, color)
    return p


def write_cell(cell, lines, valign="center"):
    """lines: list of (text, kwargs) or str."""
    clear_cell(cell)
    cell.vertical_alignment = {
        "top": WD_CELL_VERTICAL_ALIGNMENT.TOP,
        "center": WD_CELL_VERTICAL_ALIGNMENT.CENTER,
        "bottom": WD_CELL_VERTICAL_ALIGNMENT.BOTTOM,
    }[valign]
    set_cell_margins(cell)
    if not lines:
        return
    first = True
    for item in lines:
        if isinstance(item, str):
            text, kwargs = item, {}
        else:
            text, kwargs = item[0], item[1] if len(item) > 1 else {}
        if first:
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(kwargs.get("space_after", 1))
            p.paragraph_format.line_spacing = 1.08
            align = kwargs.get("align", "left")
            p.alignment = {
                "center": WD_ALIGN_PARAGRAPH.CENTER,
                "right": WD_ALIGN_PARAGRAPH.RIGHT,
            }.get(align, WD_ALIGN_PARAGRAPH.LEFT)
            run = p.add_run(text)
            set_run_font(
                run,
                kwargs.get("font", "宋体"),
                kwargs.get("size", 10.5),
                kwargs.get("bold", False),
                kwargs.get("color"),
            )
            first = False
        else:
            p = cell.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(kwargs.get("space_after", 1))
            p.paragraph_format.line_spacing = 1.08
            align = kwargs.get("align", "left")
            p.alignment = {
                "center": WD_ALIGN_PARAGRAPH.CENTER,
                "right": WD_ALIGN_PARAGRAPH.RIGHT,
            }.get(align, WD_ALIGN_PARAGRAPH.LEFT)
            run = p.add_run(text)
            set_run_font(
                run,
                kwargs.get("font", "宋体"),
                kwargs.get("size", 10.5),
                kwargs.get("bold", False),
                kwargs.get("color"),
            )


def shade_label(cell):
    set_cell_shading(cell, "E7EEF7")


def merge(table, r1, c1, r2, c2):
    a = table.cell(r1, c1)
    b = table.cell(r2, c2)
    a.merge(b)
    return a


def add_header_footer(doc):
    section = doc.sections[0]
    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0]
    hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    hp.paragraph_format.space_after = Pt(0)
    run = hp.add_run("REC-QA-000-XXX  第 1 版    第 {PAGE} 页 / 共 {NUMPAGES} 页")
    set_run_font(run, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))
    # PAGE fields
    hp.clear()
    run = hp.add_run("内部受控文件  |  REC-QA-000-XXX  第1版  |  ")
    set_run_font(run, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))

    def add_field(paragraph, instr):
        r1 = paragraph.add_run()
        set_run_font(r1, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))
        fld1 = OxmlElement("w:fldChar")
        fld1.set(qn("w:fldCharType"), "begin")
        r1._r.append(fld1)
        r2 = paragraph.add_run()
        set_run_font(r2, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))
        instrEl = OxmlElement("w:instrText")
        instrEl.set(qn("xml:space"), "preserve")
        instrEl.text = instr
        r2._r.append(instrEl)
        r3 = paragraph.add_run()
        set_run_font(r3, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))
        fld3 = OxmlElement("w:fldChar")
        fld3.set(qn("w:fldCharType"), "end")
        r3._r.append(fld3)

    add_field(hp, " PAGE ")
    run = hp.add_run(" / ")
    set_run_font(run, "宋体", 9, False, RGBColor(0x55, 0x55, 0x55))
    add_field(hp, " NUMPAGES ")

    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    fp.paragraph_format.space_before = Pt(0)
    run = fp.add_run(
        "填写后原件交质量保证部归档；副本分发授权人部门。授权期满或提前终止须完成第8项。"
    )
    set_run_font(run, "宋体", 8, False, RGBColor(0x66, 0x66, 0x66))


def build():
    doc = Document()
    section = doc.sections[0]
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(1.4)
    section.right_margin = Cm(1.4)
    section.top_margin = Cm(1.3)
    section.bottom_margin = Cm(1.4)
    section.header_distance = Cm(0.6)
    section.footer_distance = Cm(0.5)
    add_header_footer(doc)

    # Title block
    t0 = doc.add_table(rows=3, cols=4)
    set_table_borders(t0, "8")
    widths = [3.6, 6.6, 3.6, 4.4]
    set_col_widths(t0, widths)

    merge(t0, 0, 0, 0, 3)
    write_cell(
        t0.cell(0, 0),
        [("职责授权记录", {"size": 18, "bold": True, "align": "center", "font": "黑体"})],
    )
    set_cell_shading(t0.cell(0, 0), "1F4E79")
    for p in t0.cell(0, 0).paragraphs:
        for r in p.runs:
            r.font.color.rgb = RGBColor(255, 255, 255)
            set_run_font(r, "黑体", 18, True, RGBColor(255, 255, 255))

    write_cell(t0.cell(1, 0), [("文件编号", {"size": 9, "bold": True, "align": "center"})])
    shade_label(t0.cell(1, 0))
    write_cell(t0.cell(1, 1), [("REC-QA-000-XXX", {"size": 10.5, "align": "center"})])
    write_cell(t0.cell(1, 2), [("版本 / 生效日期", {"size": 9, "bold": True, "align": "center"})])
    shade_label(t0.cell(1, 2))
    write_cell(t0.cell(1, 3), [("第1版 /    年   月   日", {"size": 10.5, "align": "center"})])

    write_cell(t0.cell(2, 0), [("授权编号", {"size": 9, "bold": True, "align": "center"})])
    shade_label(t0.cell(2, 0))
    write_cell(t0.cell(2, 1), [("SQ-______-____（QA编号）", {"size": 10.5, "align": "center"})])
    write_cell(t0.cell(2, 2), [("状态", {"size": 9, "bold": True, "align": "center"})])
    shade_label(t0.cell(2, 2))
    write_cell(
        t0.cell(2, 3),
        [("□ 有效    □ 已终止    □ 作废", {"size": 10.5, "align": "center"})],
    )
    for row in t0.rows:
        prevent_row_split(row)
        for cell in row.cells:
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("1  授权基本信息")
    set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))

    # Section 1
    t1 = doc.add_table(rows=8, cols=4)
    set_table_borders(t1, "8")
    w1 = [3.0, 6.1, 3.0, 6.1]
    set_col_widths(t1, w1)

    # row0 授权性质
    write_cell(t1.cell(0, 0), [("授权性质", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(0, 0))
    merge(t1, 0, 1, 0, 3)
    write_cell(
        t1.cell(0, 1),
        [
            ("□ 临时离岗代理（请假 / 出差 / 培训）", {"size": 10}),
            ("□ 岗位空缺代理    □ 专项授权（仅限指定文件或项目）    □ 紧急授权（须24小时内补签）", {"size": 10}),
        ],
        valign="center",
    )

    write_cell(t1.cell(1, 0), [("申请途径", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(1, 0))
    merge(t1, 1, 1, 1, 3)
    write_cell(
        t1.cell(1, 1),
        [
            ("□ 本记录直接书面申请    □ 先邮件申请，本记录补档    □ 先企业微信申请，本记录补档", {"size": 10}),
            ("电子申请须将原邮件/聊天记录打印附后，附件共 ____ 页。本记录为唯一正式授权凭证。", {"size": 9, "color": RGBColor(0x55, 0x55, 0x55)}),
        ],
    )

    write_cell(t1.cell(2, 0), [("授权人部门", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(2, 0))
    write_cell(t1.cell(2, 1), [(" ", {"size": 10.5})])
    write_cell(t1.cell(2, 2), [("岗位 / 职位", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(2, 2))
    write_cell(t1.cell(2, 3), [(" ", {"size": 10.5})])

    write_cell(t1.cell(3, 0), [("授权人姓名", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(3, 0))
    write_cell(t1.cell(3, 1), [("工号：          姓名：", {"size": 10.5})])
    write_cell(t1.cell(3, 2), [("联系电话", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(3, 2))
    write_cell(t1.cell(3, 3), [(" ", {"size": 10.5})])

    write_cell(t1.cell(4, 0), [("受权人部门", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(4, 0))
    write_cell(t1.cell(4, 1), [(" ", {"size": 10.5})])
    write_cell(t1.cell(4, 2), [("岗位 / 职位", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(4, 2))
    write_cell(t1.cell(4, 3), [(" ", {"size": 10.5})])

    write_cell(t1.cell(5, 0), [("受权人姓名", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(5, 0))
    write_cell(t1.cell(5, 1), [("工号：          姓名：", {"size": 10.5})])
    write_cell(t1.cell(5, 2), [("联系电话", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(5, 2))
    write_cell(t1.cell(5, 3), [(" ", {"size": 10.5})])

    write_cell(t1.cell(6, 0), [("受权人资质", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(6, 0))
    merge(t1, 6, 1, 6, 3)
    write_cell(
        t1.cell(6, 1),
        [
            ("□ 与授权人同岗位或具备同等职责能力    □ 已完成相关SOP培训并考核合格", {"size": 10}),
            ("培训记录编号：____________________    □ 不涉及操作/签字，仅联络协调（须在范围中写明）", {"size": 10}),
        ],
    )

    write_cell(t1.cell(7, 0), [("授权原因", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t1.cell(7, 0))
    merge(t1, 7, 1, 7, 3)
    write_cell(
        t1.cell(7, 1),
        [
            ("□ 年假  □ 事假  □ 病假  □ 出差  □ 培训/会议  □ 岗位暂缺  □ 工作量分担  □ 其他：________", {"size": 10}),
            ("原因说明（必填，写清离岗事实，勿只写“出差”）：", {"size": 9, "color": RGBColor(0x55, 0x55, 0x55)}),
            (" ", {"size": 10.5}),
            (" ", {"size": 10.5}),
        ],
        valign="top",
    )

    for row in t1.rows:
        prevent_row_split(row)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("2  授权期限")
    set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))

    t2 = doc.add_table(rows=3, cols=4)
    set_table_borders(t2, "8")
    set_col_widths(t2, w1)
    write_cell(t2.cell(0, 0), [("开始时间", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t2.cell(0, 0))
    write_cell(t2.cell(0, 1), [("____年____月____日  ____时____分", {"size": 10.5, "align": "center"})])
    write_cell(t2.cell(0, 2), [("结束时间", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t2.cell(0, 2))
    write_cell(t2.cell(0, 3), [("____年____月____日  ____时____分", {"size": 10.5, "align": "center"})])

    write_cell(t2.cell(1, 0), [("期限规则", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t2.cell(1, 0))
    merge(t2, 1, 1, 1, 3)
    write_cell(
        t2.cell(1, 1),
        [
            ("□ 固定起止时间（上栏）    □ 至授权人返岗当日结束，最长不超过 ____ 天", {"size": 10}),
            ("单次临时授权原则上不超过 15 个自然日；超过须部门负责人说明并经 QA 同意。期满未办终止视为逾期，须重新授权。", {"size": 9, "color": RGBColor(0x55, 0x55, 0x55)}),
        ],
    )

    write_cell(t2.cell(2, 0), [("在岗情况", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t2.cell(2, 0))
    merge(t2, 2, 1, 2, 3)
    write_cell(
        t2.cell(2, 1),
        [
            ("□ 授权人完全离岗，期间由受权人履行下列职责", {"size": 10}),
            ("□ 授权人仍在岗，受权人仅作备份（文件优先由授权人签署；授权人无法签署时由受权人签署）", {"size": 10}),
        ],
    )
    for row in t2.rows:
        prevent_row_split(row)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("3  授予的职责与范围（可多选，未勾选一律视为未授权）")
    set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))

    t3 = doc.add_table(rows=9, cols=2)
    set_table_borders(t3, "8")
    set_col_widths(t3, [4.2, 14.0])

    items = [
        ("文件审核 / 批准", "□ 起草  □ 审核  □ 批准\n文件类型：□ SOP  □ 记录  □ 验证方案/报告  □ 偏差/变更/CAPA  □ 其他：______\n具体文件编号（必填，可另附清单）：________________________________"),
        ("生产 / 包装记录", "□ 岗位记录填写  □ 记录复核  □ 批记录审核\n产品/工序：____________________    不得替代：□ 质量受权人批次放行"),
        ("设备与设施", "□ 使用操作  □ 点检/维保确认  □ 维修后放行  □ 仪器校准送检联络\n设备编号：____________________    相关SOP：____________________"),
        ("验证与确认", "□ 验证实施  □ 数据复核  □ 阶段审核  □ 报告审核/批准\n验证方案编号：____________________"),
        ("质量体系职责", "□ 偏差发起/调查参与  □ 变更评估  □ 培训审核  □ 供应商/物料相关审核\n说明：____________________"),
        ("信息系统 / 电子签名", "□ 需同步开通系统权限（IT/系统管理员另办）  系统名称：__________\n账号不得转借。电子签名授权须与本记录起止时间一致。"),
        ("其他职责", "□ ______________________________________________________________"),
        ("禁止事项\n（默认适用）", "1. 不得将本授权再转授第三人。\n2. 不得签署超出授权人本人权限的文件。\n3. 受权人不得审核/批准由本人完成的操作或记录。\n4. 质量受权人放行、法规规定不可委托事项，不在本授权范围内。\n□ 其他禁止：________________________________"),
        ("范围补充说明", "\n\n"),
    ]
    labels = [
        "□ A 文件签署",
        "□ B 批记录",
        "□ C 设备设施",
        "□ D 验证确认",
        "□ E 质量体系",
        "□ F 电子系统",
        "□ G 其他",
        "负面清单",
        "补充说明",
    ]
    for i, (lab, body) in enumerate(zip(labels, items)):
        write_cell(t3.cell(i, 0), [(lab, {"size": 10, "bold": True, "align": "center"})], valign="center")
        shade_label(t3.cell(i, 0))
        lines = []
        for j, para in enumerate(body[1].split("\n")):
            lines.append((para if para else " ", {"size": 10 if j == 0 else 9.5}))
        write_cell(t3.cell(i, 1), lines, valign="top")
    for row in t3.rows:
        prevent_row_split(row)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("4  声明与确认")
    set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))

    t4 = doc.add_table(rows=5, cols=3)
    set_table_borders(t4, "8")
    set_col_widths(t4, [6.07, 6.07, 6.06])

    write_cell(
        t4.cell(0, 0),
        [
            ("授权人声明", {"size": 10, "bold": True, "align": "center"}),
            ("本人对上述职责负有管理责任，且仅将本人权限范围内事项授予受权人。授权期间对受权人履职仍负管理责任。", {"size": 9}),
            (" ", {"size": 10}),
            ("签名：______________    日期：____年____月____日", {"size": 10}),
        ],
        valign="top",
    )
    write_cell(
        t4.cell(0, 1),
        [
            ("受权人声明", {"size": 10, "bold": True, "align": "center"}),
            ("本人已阅读授权范围及相关文件，具备相应能力，接受并仅在授权期限与范围内履职，不转授他人。", {"size": 9}),
            (" ", {"size": 10}),
            ("签名：______________    日期：____年____月____日", {"size": 10}),
        ],
        valign="top",
    )
    write_cell(
        t4.cell(0, 2),
        [
            ("授权人部门负责人", {"size": 10, "bold": True, "align": "center"}),
            ("确认授权必要、受权人能力匹配、期限合理。跨部门授权须双方部门负责人签字。", {"size": 9}),
            (" ", {"size": 10}),
            ("签名：______________    日期：____年____月____日", {"size": 10}),
        ],
        valign="top",
    )
    # merge row0 is already 3 cells - good. Row 1 for cross-dept
    merge(t4, 1, 0, 1, 2)
    write_cell(
        t4.cell(1, 0),
        [
            (
                "跨部门授权时受权人部门负责人：______________ / 日期：____年____月____日    □ 不适用（同部门）",
                {"size": 10},
            )
        ],
    )

    write_cell(
        t4.cell(2, 0),
        [
            ("质量保证部审核", {"size": 10, "bold": True, "align": "center"}),
            ("涉及GMP文件签署、批记录、偏差变更、验证、放行相关职责时必签；纯行政联络可勾不适用。", {"size": 9}),
        ],
        valign="top",
    )
    merge(t4, 2, 1, 2, 2)
    write_cell(
        t4.cell(2, 1),
        [
            ("□ 同意    □ 不同意    □ 不适用（不涉及GMP职责）", {"size": 10.5}),
            ("意见：________________________________________________", {"size": 10}),
            ("审核人/日期：______________________", {"size": 10}),
        ],
        valign="center",
    )

    write_cell(
        t4.cell(3, 0),
        [("系统权限办理（如适用）", {"size": 10, "bold": True, "align": "center"})],
    )
    merge(t4, 3, 1, 3, 2)
    write_cell(
        t4.cell(3, 1),
        [
            ("□ 不适用    □ 已开通，开通时间：__________    □ 授权终止后已关闭", {"size": 10}),
            ("办理人/日期：______________________", {"size": 10}),
        ],
    )

    write_cell(
        t4.cell(4, 0),
        [("分发与归档", {"size": 10, "bold": True, "align": "center"})],
    )
    merge(t4, 4, 1, 4, 2)
    write_cell(
        t4.cell(4, 1),
        [
            ("原件：□ 质量保证部（GMP相关）    副本：□ 授权人部门    □ 受权人    □ 行政/人力资源（考勤备查）", {"size": 10}),
            ("归档号：______________    接收人/日期：________________", {"size": 10}),
        ],
    )
    for row in t4.rows:
        prevent_row_split(row)

    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(2)
    run = p.add_run("5  授权终止（期满、提前返岗或撤销时填写，与本记录同页归档）")
    set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))

    t5 = doc.add_table(rows=4, cols=4)
    set_table_borders(t5, "8")
    set_col_widths(t5, w1)
    write_cell(t5.cell(0, 0), [("终止类型", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t5.cell(0, 0))
    merge(t5, 0, 1, 0, 3)
    write_cell(
        t5.cell(0, 1),
        [("□ 期满自然终止    □ 提前返岗终止    □ 授权人撤销    □ 受权人无法履职    □ 其他：______", {"size": 10})],
    )

    write_cell(t5.cell(1, 0), [("实际终止时间", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t5.cell(1, 0))
    write_cell(t5.cell(1, 1), [("____年____月____日  ____时____分", {"size": 10.5, "align": "center"})])
    write_cell(t5.cell(1, 2), [("系统权限", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t5.cell(1, 2))
    write_cell(t5.cell(1, 3), [("□ 已关闭  □ 不适用", {"size": 10.5, "align": "center"})])

    write_cell(t5.cell(2, 0), [("交接说明", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t5.cell(2, 0))
    merge(t5, 2, 1, 2, 3)
    write_cell(
        t5.cell(2, 1),
        [
            ("期间代签文件 / 未完事项交接：", {"size": 10}),
            (" ", {"size": 10}),
            (" ", {"size": 10}),
        ],
        valign="top",
    )

    write_cell(t5.cell(3, 0), [("终止确认", {"size": 10, "bold": True, "align": "center"})])
    shade_label(t5.cell(3, 0))
    merge(t5, 3, 1, 3, 3)
    write_cell(
        t5.cell(3, 1),
        [
            ("授权人/日期：________________    受权人/日期：________________    QA/日期：________________", {"size": 10}),
        ],
    )
    for row in t5.rows:
        prevent_row_split(row)

    # Page break then instructions
    doc.add_page_break()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(8)
    run = p.add_run("填写说明（可随记录发放，不作为每次必填页）")
    set_run_font(run, "黑体", 16, True, RGBColor(0x1F, 0x4E, 0x79))

    guide = [
        (
            "一、为什么改版",
            "原《授权书》只有大段空白，使用时常见：授权范围写“相关工作”、期限写到分钟却无返岗规则、邮件/企微授权无附件、行政部存档但QA看不到、授权到期无人收回。本记录按实际办理顺序设计：先定性→再写人→再写期限→用勾选锁定范围→签字批准→到期终止。",
        ),
        (
            "二、谁可以用、谁不可以用",
            "1. 授权人只能授予本人已经拥有的职责，不能把上级或QA的批准权转出去。\n"
            "2. 受权人应为同岗位代理人、已培训的同部门人员，或经双方部门负责人同意的跨部门人员。\n"
            "3. 质量受权人的产品放行、法律法规禁止委托的事项，不得使用本记录授权。\n"
            "4. 受权人不得审核或批准自己做的操作/记录（职责分离）。",
        ),
        (
            "三、怎么填才算填完",
            "1. 授权编号由QA按 SQ-年份-流水号 编制，未编号不得作为正式授权。\n"
            "2. “授予的职责与范围”必须勾选类别，并写文件编号、设备编号或验证方案编号；只勾选不写编号视为范围不清，QA应退回。\n"
            "3. 先邮件或企微打招呼的，必须在24小时内补本记录，并附打印件。紧急授权同样补签。\n"
            "4. 涉及电子签名或系统账号的，IT/系统管理员须在第4项办理开通，终止时关闭。\n"
            "5. 第3项未勾选的类别一律未授权，代签无效。",
        ),
        (
            "四、签字顺序",
            "受权人接受 → 授权人签署 → 授权人部门负责人 →（跨部门则受权人部门负责人）→ 涉及GMP职责时QA审核 → 归档分发。\n"
            "QA不是所有请假都要签：纯行政联络、不签署GMP文件的，可勾“不适用”。批记录、SOP批准、偏差变更、验证、设备放行相关必须QA审核。",
        ),
        (
            "五、期限与终止",
            "1. 临时授权建议不超过15天；更长周期用岗位代理或组织任命，不反复开本记录。\n"
            "2. 授权人提前返岗，当日办理第5项终止，不得继续由受权人代签。\n"
            "3. 期满未终止，QA将该记录状态改为逾期，相关代签从期满后起不生效。",
        ),
        (
            "六、归档",
            "GMP相关原件由质量保证部归档，保存至该授权所涉文件保存期孰长者；行政/人力资源只收副本用于考勤。不再将原件只交行政部。",
        ),
        (
            "七、与电子授权的关系",
            "企业微信、邮件只能作为启动申请，不能替代本记录。若公司启用电子签名工作流，电子记录须至少包含本表全部必填字段，并保留审计追踪。",
        ),
    ]
    for title, body in guide:
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        run = p.add_run(title)
        set_run_font(run, "黑体", 12, True, RGBColor(0x1F, 0x4E, 0x79))
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.2
        run = p.add_run(body)
        set_run_font(run, "宋体", 10.5, False)

    out = "/workspace/docs/REC-QA-000-XXX_职责授权记录.docx"
    doc.save(out)
    print(out)


if __name__ == "__main__":
    build()
