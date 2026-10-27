#!/usr/bin/env python3
"""Generate the restructured equipment classification and numbering SMP."""

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, Twips

OUT = "/workspace/生产设备与仪器分类、编号管理规程.docx"


def set_run_font(run, size=12, bold=False):
    run.bold = bold
    run.italic = False
    run.font.size = Pt(size)
    run.font.name = "宋体"
    rPr = run._element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), "宋体")


def set_paragraph_format(p, before=0, after=3, line=240, first_line=0, align="left"):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
    pf.line_spacing = line / 240
    pf.first_line_indent = Cm(first_line)
    pf.left_indent = Cm(0)
    align_map = {
        "left": WD_ALIGN_PARAGRAPH.LEFT,
        "center": WD_ALIGN_PARAGRAPH.CENTER,
        "justify": WD_ALIGN_PARAGRAPH.JUSTIFY,
    }
    p.alignment = align_map[align]


def add_text(p, text, size=12, bold=False):
    run = p.add_run(text)
    set_run_font(run, size=size, bold=bold)
    return run


def add_para(doc, text, size=12, bold=False, before=0, after=3, align="justify"):
    p = doc.add_paragraph()
    set_paragraph_format(p, before=before, after=after, align=align)
    add_text(p, text, size=size, bold=bold)
    return p


def add_heading_para(doc, text, level):
    size = 16 if level == 0 else (14 if level == 1 else 12)
    before = 0 if level == 0 else (10 if level == 1 else 6)
    after = 8 if level == 0 else 4
    align = "center" if level == 0 else "left"
    return add_para(doc, text, size=size, bold=True, before=before, after=after, align=align)


def shade_cell(cell, color):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color)
    tcPr.append(shd)


def set_cell_border(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    tcBorders = tcPr.find(qn("w:tcBorders"))
    if tcBorders is None:
        tcBorders = OxmlElement("w:tcBorders")
        tcPr.append(tcBorders)
    for edge in ("top", "left", "bottom", "right"):
        el = tcBorders.find(qn(f"w:{edge}"))
        if el is None:
            el = OxmlElement(f"w:{edge}")
            tcBorders.append(el)
        el.set(qn("w:val"), "single")
        el.set(qn("w:sz"), "4")
        el.set(qn("w:space"), "0")
        el.set(qn("w:color"), "000000")


def set_cell_width(cell, width_cm):
    tcPr = cell._tc.get_or_add_tcPr()
    tcW = tcPr.find(qn("w:tcW"))
    if tcW is None:
        tcW = OxmlElement("w:tcW")
        tcPr.append(tcW)
    tcW.set(qn("w:w"), str(int(width_cm * 567)))
    tcW.set(qn("w:type"), "dxa")


def fill_cell(cell, text, bold=False, size=10.5, center=False, fill=None):
    cell.text = ""
    p = cell.paragraphs[0]
    set_paragraph_format(p, before=1, after=1, line=216, align="center" if center else "left")
    add_text(p, text, size=size, bold=bold)
    set_cell_border(cell)
    if fill:
        shade_cell(cell, fill)
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    vAlign = tcPr.find(qn("w:vAlign"))
    if vAlign is None:
        vAlign = OxmlElement("w:vAlign")
        tcPr.append(vAlign)
    vAlign.set(qn("w:val"), "center")


def prevent_row_split(row):
    tr = row._tr
    trPr = tr.get_or_add_trPr()
    cant = OxmlElement("w:cantSplit")
    trPr.append(cant)


def add_table(doc, headers, rows, widths, header=True):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    tbl = table._tbl
    tblPr = tbl.tblPr if tbl.tblPr is not None else OxmlElement("w:tblPr")
    tblW = tblPr.find(qn("w:tblW"))
    if tblW is None:
        tblW = OxmlElement("w:tblW")
        tblPr.append(tblW)
    total = int(sum(widths) * 567)
    tblW.set(qn("w:w"), str(total))
    tblW.set(qn("w:type"), "dxa")

    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        fill_cell(cell, h, bold=True, size=10.5, center=True, fill="D9E2F3")
        set_cell_width(cell, widths[i])
    prevent_row_split(table.rows[0])
    if header:
        trPr = table.rows[0]._tr.get_or_add_trPr()
        tblHeader = OxmlElement("w:tblHeader")
        trPr.append(tblHeader)

    for r_idx, row in enumerate(rows):
        for c_idx, value in enumerate(row):
            cell = table.rows[r_idx + 1].cells[c_idx]
            fill_cell(cell, value, bold=False, size=10.5, center=False, fill="FFFFFF")
            set_cell_width(cell, widths[c_idx])
        prevent_row_split(table.rows[r_idx + 1])
    return table


def add_caption(doc, text):
    return add_para(doc, text, size=10.5, bold=True, before=8, after=2, align="center")


def add_page_field(paragraph, instr):
    run = paragraph.add_run()
    set_run_font(run, size=9, bold=False)
    r = run._r
    fld1 = OxmlElement("w:fldChar")
    fld1.set(qn("w:fldCharType"), "begin")
    instr_el = OxmlElement("w:instrText")
    instr_el.set(qn("xml:space"), "preserve")
    instr_el.text = instr
    fld2 = OxmlElement("w:fldChar")
    fld2.set(qn("w:fldCharType"), "end")
    r.append(fld1)
    r.append(instr_el)
    r.append(fld2)


def configure_styles(doc):
    normal = doc.styles["Normal"]
    normal.font.name = "宋体"
    normal.font.size = Pt(12)
    rPr = normal.element.get_or_add_rPr()
    rFonts = rPr.find(qn("w:rFonts"))
    if rFonts is None:
        rFonts = OxmlElement("w:rFonts")
        rPr.append(rFonts)
    for attr in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rFonts.set(qn(attr), "宋体")


def configure_section(section):
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.4)
    section.header_distance = Cm(1.0)
    section.footer_distance = Cm(0.8)

    header = section.header
    header.is_linked_to_previous = False
    hp = header.paragraphs[0]
    hp.clear()
    set_paragraph_format(hp, before=0, after=0, line=216, align="center")
    add_text(hp, "生产设备分类与编号管理规程", size=9, bold=False)

    footer = section.footer
    footer.is_linked_to_previous = False
    fp = footer.paragraphs[0]
    fp.clear()
    set_paragraph_format(fp, before=0, after=0, line=216, align="center")
    add_text(fp, "修订稿    第 ", size=9)
    add_page_field(fp, " PAGE ")
    add_text(fp, " 页 / 共 ", size=9)
    add_page_field(fp, " NUMPAGES ")
    add_text(fp, " 页", size=9)

    settings = section._sectPr
    # fields update on open is set at document level


def enable_update_fields(doc):
    settings = doc.settings.element
    update = settings.find(qn("w:updateFields"))
    if update is None:
        update = OxmlElement("w:updateFields")
        settings.append(update)
    update.set(qn("w:val"), "true")


def build():
    doc = Document()
    configure_styles(doc)
    configure_section(doc.sections[0])
    enable_update_fields(doc)

    add_heading_para(doc, "生产设备分类与编号管理规程", 0)
    add_para(doc, "（修订稿）", size=12, bold=True, before=0, after=6, align="center")

    add_caption(doc, "文件信息")
    add_table(
        doc,
        ["项目", "内容"],
        [
            ["文件名称", "生产设备分类与编号管理规程"],
            ["文件编号", "按公司文件编号规则填写"],
            ["版本号", "按本次修订的版本号填写"],
            ["起草部门", "设备工程部"],
            ["生效日期", "批准后填写"],
            ["状态", "修订稿。批准前不替代现行受控文本。"],
        ],
        [3.6, 12.3],
    )

    add_heading_para(doc, "1  目的", 1)
    add_para(
        doc,
        "1.1  本规程规定生产设备的分类及分类后的管理要求，以及设备、仪器的唯一编号规则，使设备、仪器能够识别和追溯，并使其使用、清洁、维护、维修和确认处于受控状态。",
    )

    add_heading_para(doc, "2  范围", 1)
    add_para(doc, "2.1  本规程适用于生产设备的分类、分类后的管理和编号，以及仪器的编号。")
    add_para(
        doc,
        "2.2  本规程对质量控制部只适用于仪器编号。质量控制部仪器的分类、校准和检验使用管理执行 SMP-QC-000-021《检验仪器管理规程》。",
    )
    add_para(
        doc,
        "2.3  生产设备的系统影响性评估和组件关键性评估执行 SMP-QA-000-037《系统影响性评估及组件关键性评估管理规程》。本规程只将系统影响性评估结论对应为 A 类或 B 类，不另设组件分级。",
    )

    add_heading_para(doc, "3  职责", 1)
    add_para(
        doc,
        "3.1  设备工程部负责人和 QA 负责监督本规程的实施。发现设备类别与评估结论不一致、编号重复，或现场标识与设备台账不一致时，应当督促责任部门纠正。",
    )
    add_para(
        doc,
        "3.2  设备工程部及相关人员负责执行本规程，维护设备台账，并保证纳入台账的设备、仪器编号唯一。",
    )
    add_para(
        doc,
        "3.3  设备归属部门负责组织本部门设备操作规程、清洁规程和维护规程的起草、修订、审核和培训，指定 A 类设备负责人，并完成交接。",
    )
    add_para(
        doc,
        "3.4  仪器所在部门负责使仪器的现场编号与设备台账一致。质量控制部仪器的分类、校准和检验使用管理由 SMP-QC-000-021 规定。",
    )

    add_heading_para(doc, "4  编制依据", 1)
    add_para(
        doc,
        "4.1  《药品生产质量管理规范（2010年修订）》（卫生部令第79号）第二十六条、第二十七条、第七十二条、第七十九条、第八十条、第八十一条、第八十二条、第八十三条、第八十六条、第八十七条和第八十八条。",
    )
    add_para(doc, "4.2  本规程引用下列公司文件。文件修订后，按修订后的受控文本执行。")
    add_caption(doc, "表1  引用文件")
    add_table(
        doc,
        ["文件编号", "文件名称", "在本规程中的用途"],
        [
            ["SMP-QA-000-037", "系统影响性评估及组件关键性评估管理规程", "系统影响性评估和组件关键性评估"],
            ["SMP-QA-000-030", "变更控制管理制度", "改变已确定的设备类别"],
            ["SMP-QC-000-021", "检验仪器管理规程", "质量控制部仪器的分类、校准和检验使用管理"],
            ["SMP-VP-000-004", "设施、设备确认管理规程", "设备确认和再确认"],
            ["SMP-EQ-100-004", "设备设施故障报告与维修管理规程", "设备维修"],
            ["SMP-EQ-100-003", "设备预防性维护、维修管理规程", "设备预防性维护"],
        ],
        [3.6, 6.6, 5.7],
    )
    add_para(
        doc,
        "4.3  本规程中的“确认”对应 qualification，“预防性维护”对应 preventive maintenance，设备、仪器编号用于唯一识别，对应 unique identification。中国生产现场的执行依据为第4.1款和表1。",
        before=6,
    )

    add_heading_para(doc, "5  定义", 1)
    for item in [
        "5.1  直接影响系统、非直接影响系统：按 SMP-QA-000-037 得出的系统影响性评估结论。该规程对上述术语另有定义时，以该规程为准。",
        "5.2  A 类设备：系统影响性评估结论为直接影响系统的设备。",
        "5.3  B 类设备：系统影响性评估结论为非直接影响系统的设备。",
        "5.4  设备归属部门：组织本部门设备操作规程、清洁规程和维护规程的起草、修订、审核和培训的部门。",
        "5.5  一级编号：由设备大类代号、部门代号和三位流水号依次连接形成的编号。",
        "5.6  二级编号：在一级编号后加半角连字符“-”和两位辅助设备或附属装置序号形成的编号。",
        "5.7  辅助设备：作为设备大类时，代号为 F，按一级编号编制。作为某台已编号设备的辅助设备或附属装置且需要二级编号时，序号附在该设备编号之后。",
        "5.8  使用日志：用于药品生产或检验的设备和仪器的记录，内容包括使用、清洁、维护和维修情况以及日期、时间、所生产及检验的药品名称、规格和批号等。本规程中 A 类设备的使用记录属于使用日志。",
    ]:
        add_para(doc, item)

    add_heading_para(doc, "6  内容", 1)
    add_heading_para(doc, "6.1  设备分类", 2)
    add_para(
        doc,
        "6.1.1  生产设备投入使用前，归属部门按 SMP-QA-000-037 完成系统影响性评估。评估结论为直接影响系统的，按 A 类管理；评估结论为非直接影响系统的，按 B 类管理。组件关键性评估按 SMP-QA-000-037 执行，不在本规程中另行分级。",
    )
    add_para(doc, "6.1.2  管理类别见下表。表中“如”后的设备为示例，具体设备的类别以其系统影响性评估结论为准。")
    add_caption(doc, "表2  设备管理类别")
    add_table(
        doc,
        ["类别", "评估结论及示例"],
        [
            ["A 类", "直接影响系统，如：压片机、铝塑包装机、制粒机、空调净化系统、压缩空气系统等。"],
            ["B 类", "非直接影响系统，如：叉车、洗衣机、干衣机等。"],
        ],
        [2.8, 13.1],
    )
    add_para(
        doc,
        "6.1.3  设备类别记入设备台账。类别确定后不得改变。确需改变时，应当重新评估，并按 SMP-QA-000-030《变更控制管理制度》批准。变更批准前，设备继续按原类别管理。",
        before=6,
    )
    add_para(
        doc,
        "6.1.4  本规程不对质量控制部的仪器进行分类。质量控制部仪器的分类由 SMP-QC-000-021 管理。该类仪器的编号按第6.3款执行。",
    )

    add_heading_para(doc, "6.2  分类后的管理", 2)
    add_para(
        doc,
        "6.2.1  从事设备操作和维护的人员应当经过与岗位要求相适应的培训，培训记录予以保存。培训合格后方可上岗。",
    )
    add_para(
        doc,
        "6.2.2  设备应当建立使用、清洁、维护和维修的操作规程，并保存相应记录。A 类设备的规程形式执行第6.2.3款，B 类设备的规程形式执行第6.2.4款。",
    )
    add_para(doc, "6.2.3  A 类设备", before=4)
    add_para(
        doc,
        "6.2.3.1  归属部门应当组织 A 类设备操作规程、清洁规程和维护规程的起草、修订和审核，建立使用记录并如实记录设备运行情况，同时对相关人员进行培训。用于药品生产的设备，使用记录至少包括使用、清洁、维护和维修情况以及日期、时间、所生产药品的名称、规格和批号等。多个批次共用的公用系统，使用记录应当包括运行、清洁、维护、维修以及日期和时间，并使相应批记录能够追溯到该运行记录。",
    )
    add_para(
        doc,
        "6.2.3.2  归属部门应当指定设备负责人。设备负责人离职或调岗时，应当与继任者交接第6.2.3.1款形成的规程和使用记录，以及维护保养记录、备品备件、设备当前运行情况和注意事项。交接应当形成记录并纳入设备档案。公司已有交接记录的，使用该记录，本规程不另建表单。",
    )
    add_para(doc, "6.2.4  B 类设备", before=4)
    add_para(
        doc,
        "6.2.4.1  归属部门应当根据 B 类设备的结构复杂程度和设备说明书的要求，组织操作规程、清洁规程和维护规程的起草、修订和审核。相关操作人员、维护人员应当满足第6.2.1款的培训要求后方可上岗。",
    )
    add_para(
        doc,
        "6.2.4.2  结构简单、操作及维护要求明确的 B 类设备，可以将操作规程、清洁规程和维护规程合并为一份操作维护清洁规程。合并后仍应当确保使用、清洁和维护要求完整、清晰、可执行，并保存使用、清洁、维护和维修的相应记录。",
    )
    add_para(
        doc,
        "6.2.4.3  不用于药品生产的 B 类设备，应当保存与其实际使用、清洁和维护相适应的记录。用于药品生产的 B 类设备，使用记录的内容执行第6.2.3.1款。",
    )
    add_para(
        doc,
        "6.2.5  设备确认按照 SMP-VP-000-004《设施、设备确认管理规程》执行。已完成确认的生产设备应当在确认的参数范围内使用。经改造或重大维修的设备，应当按该规程完成再确认，符合要求后方可用于生产。",
        before=4,
    )
    add_para(
        doc,
        "6.2.6  设备维修、预防性维护按照 SMP-EQ-100-004《设备设施故障报告与维修管理规程》和 SMP-EQ-100-003《设备预防性维护、维修管理规程》执行。维护和维修不得影响产品质量，并应当有记录。记录使用本规程规定的设备编号。",
    )

    add_heading_para(doc, "6.3  设备、仪器编号", 2)
    add_para(
        doc,
        "6.3.1  设备、仪器的一级编号由设备大类代号、部门代号和三位流水号依次连接组成，段间不插入空格或其他符号。纳入设备台账的每台设备、仪器只有一个现行编号，完整编号在公司内唯一。已经用于记录的编号不再授予另一台设备或仪器。",
    )
    add_para(
        doc,
        "6.3.2  某台设备的辅助设备或附属装置需要编制二级编号时，在该设备的一级编号后加半角连字符“-”和两位序号。二级编号不另取设备大类代号。",
    )
    add_para(
        doc,
        "6.3.3  大类代号 F 用于按一级编号单独编制的辅助设备。按第6.3.2款编制二级编号的辅助设备或附属装置，使用主设备编号加序号。",
    )
    add_para(doc, "6.3.4  设备大类代号按表3使用。编号中的 S1、S2 按表内字母和数字书写。")
    add_caption(doc, "表3  设备大类代号")
    add_table(
        doc,
        ["代号", "含义", "代号", "含义"],
        [
            ["S1", "原料药车间生产设备", "S2", "口服固体制剂车间生产设备"],
            ["F", "辅助设备", "P", "配电及电力设备"],
            ["Q", "办公及其它设备", "J", "检测仪器"],
        ],
        [3.2, 4.75, 3.2, 4.75],
    )
    add_para(doc, "6.3.5  部门代号按表4使用。", before=6)
    add_caption(doc, "表4  部门代号")
    add_table(
        doc,
        ["代号", "车间或部门", "代号", "车间或部门"],
        [
            ["A", "办公室", "B", "301车间、302车间"],
            ["C", "401车间", "D", "设备工程部"],
            ["E", "质量控制部", "F", "物料部"],
            ["G", "质量保证部", "H", "其它"],
        ],
        [3.2, 4.75, 3.2, 4.75],
    )
    add_para(
        doc,
        "6.3.6  流水号为三位阿拉伯数字，自 001 起按顺序编制。辅助设备或附属装置的序号为两位阿拉伯数字，自 01 起按顺序编制。",
        before=6,
    )
    add_para(
        doc,
        "6.3.7  301 车间和 302 车间的部门代号均为 B。同一设备大类下，这两个车间共用一个流水号序列，以保证编号唯一。",
    )
    add_para(
        doc,
        "6.3.8  以 401 车间全自动胶囊填充机为例。该设备属于口服固体制剂车间生产设备，部门为 401 车间。假设流水号为 009，编号为 S2C009。其中 S2 为设备大类，C 为部门代号，009 为流水号。",
    )
    add_para(
        doc,
        "6.3.9  以 401 车间压片机的辅助设备吸尘器为例。假设压片机编号为 S2C080，该吸尘器为其第 1 台辅助设备并需要编制二级编号，则编号为 S2C080-01。",
    )
    add_caption(doc, "表5  示例编号的读法")
    add_table(
        doc,
        ["示例", "大类", "部门", "流水号", "辅助序号", "完整编号"],
        [
            ["401车间全自动胶囊填充机", "S2", "C", "009", "—", "S2C009"],
            ["401车间压片机（假设）", "S2", "C", "080", "—", "S2C080"],
            ["该压片机的第1台吸尘器", "沿用压片机", "沿用压片机", "沿用压片机", "01", "S2C080-01"],
        ],
        [4.6, 2.2, 2.4, 2.2, 2.2, 2.3],
    )
    add_para(
        doc,
        "6.3.10  生产设备应当有明显的状态标识，并标明本规程规定的设备编号。有内容物时，应当标明内容物的名称、规格和批号；无内容物时，应当标明清洁状态。不合格的设备在移出生产区或质量控制区之前，应当有醒目的状态标识。",
        before=6,
    )
    add_para(
        doc,
        "6.3.11  仪器的现场标识使用本规程配发的编号。仪器的校准状态标识和使用记录执行其适用规程；质量控制部仪器执行 SMP-QC-000-021。",
    )

    add_heading_para(doc, "7  注意事项", 1)
    add_para(doc, "7.1  设备类别以系统影响性评估结论为准。表2中的示例用于说明类别，不代替该设备的评估结论。")
    add_para(doc, "7.2  大类代号 F 与二级编号是两种编法。需要二级编号的辅助设备或附属装置，编号写在主设备编号之后。")
    add_para(doc, "7.3  301 车间与 302 车间使用同一部门代号 B，同一大类下的流水号连续编制，不各自从 001 起编。")
    add_para(doc, "7.4  质量控制部仪器的分类执行 SMP-QC-000-021，编号的结构和唯一性执行本规程。")
    add_para(
        doc,
        "7.5  现场编号与设备台账不一致时，使用部门通知设备工程部核对。核对完成前，不把该编号上的使用、维修或确认记录改记到另一台设备或仪器。历史记录保持原编号。",
    )

    add_heading_para(doc, "8  环境、健康、安全（EHS）要求", 1)
    add_para(doc, "8.1  设备分类和编号不另设环境、职业健康或安全限度。")
    add_para(
        doc,
        "8.2  设备维修和预防性维护中的安全要求，执行 SMP-EQ-100-003 和 SMP-EQ-100-004。",
    )

    add_heading_para(doc, "9  派生记录", 1)
    add_para(doc, "9.1  纸质受控记录")
    add_para(
        doc,
        "9.1.1  设备台账使用公司现有台账，本规程不另建表单。台账应当能够追溯现行编号、名称、部门或部门代号、安装地点和状态。生产设备还应当追溯管理类别。仪器登记编号，不按本规程填写 A 类或 B 类。",
    )
    add_para(
        doc,
        "9.1.2  A 类设备使用记录按第6.2.3.1款填写，使用公司现有使用记录，本规程不另建表单。",
    )
    add_para(doc, "9.1.3  A 类设备负责人交接记录按第6.2.3.2款纳入设备档案。")
    add_para(doc, "9.2  电子模板受控记录", before=4)
    add_para(
        doc,
        "9.2.1  设备台账为电子系统时，该系统即本规程的设备台账，应当保证现行编号唯一。本规程不另建电子模板。",
    )
    add_para(
        doc,
        "9.2.2  确认记录、维护维修记录按所引用的规程保存，并使用本规程规定的编号。变更前已经形成的记录保留当时的编号。",
    )

    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
