from __future__ import annotations

import sys
import threading
import traceback
from pathlib import Path
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from core import (
    SMTP_PRESETS,
    AppConfig,
    check_and_notify,
    create_template,
    infer_smtp,
    list_sheet_names,
    load_config,
    save_config,
    send_email,
    send_wecom_bot,
)

BASE_DIR = Path(__file__).resolve().parent


def _enable_windows_dpi() -> None:
    if sys.platform != "win32":
        return
    try:
        import ctypes

        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        return


class LedgerAlertApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("台账提醒助手")
        self.geometry("760x720")
        self.minsize(680, 640)
        self.configure(bg="#f4f6f8")

        self.config_data = load_config(BASE_DIR)
        self._monitor_job: str | None = None
        self._busy = False

        self.excel_var = tk.StringVar(value=self.config_data.excel_path)
        self.sheet_var = tk.StringVar(value=self.config_data.sheet_name)
        self.interval_var = tk.StringVar(value=str(self.config_data.interval_minutes))
        self.enable_email_var = tk.BooleanVar(value=self.config_data.enable_email)
        self.enable_wecom_var = tk.BooleanVar(value=self.config_data.enable_wecom)
        self.preset_var = tk.StringVar(value=self.config_data.mail_preset)
        self.smtp_host_var = tk.StringVar(value=self.config_data.smtp_host)
        self.smtp_port_var = tk.StringVar(value=str(self.config_data.smtp_port))
        self.mail_user_var = tk.StringVar(value=self.config_data.mail_user)
        self.mail_pass_var = tk.StringVar(value=self.config_data.mail_pass)
        self.wecom_var = tk.StringVar(value=self.config_data.wecom_webhook)
        self.status_var = tk.StringVar(value="还没有开始。请先选择台账文件。")

        self._build_style()
        self._build_ui()
        if self.excel_var.get():
            self._refresh_sheets(silent=True)
        self.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_style(self) -> None:
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure("TFrame", background="#f4f6f8")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("TLabel", background="#f4f6f8", font=("Microsoft YaHei UI", 10))
        style.configure("Card.TLabel", background="#ffffff", font=("Microsoft YaHei UI", 10))
        style.configure("Hint.TLabel", background="#ffffff", foreground="#5b6573", font=("Microsoft YaHei UI", 9))
        style.configure("Title.TLabel", background="#f4f6f8", font=("Microsoft YaHei UI", 16, "bold"))
        style.configure("Sub.TLabel", background="#f4f6f8", foreground="#5b6573", font=("Microsoft YaHei UI", 10))
        style.configure("TButton", font=("Microsoft YaHei UI", 10), padding=6)
        style.configure("Accent.TButton", font=("Microsoft YaHei UI", 11, "bold"), padding=8)
        style.configure("TCheckbutton", background="#ffffff", font=("Microsoft YaHei UI", 10))
        style.configure("TLabelframe", background="#ffffff")
        style.configure("TLabelframe.Label", background="#ffffff", font=("Microsoft YaHei UI", 10, "bold"))

    def _card(self, parent: tk.Misc) -> ttk.Frame:
        card = ttk.Frame(parent, style="Card.TFrame", padding=14)
        return card

    def _build_ui(self) -> None:
        root = ttk.Frame(self, padding=18)
        root.pack(fill="both", expand=True)

        ttk.Label(root, text="台账提醒助手", style="Title.TLabel").pack(anchor="w")
        ttk.Label(
            root,
            text="选好 Excel，填上发件邮箱，点开始即可。有人把「影响程度」改成「直接影响」时，会自动通知责任人。",
            style="Sub.TLabel",
            wraplength=700,
        ).pack(anchor="w", pady=(4, 14))

        file_card = self._card(root)
        file_card.pack(fill="x", pady=(0, 10))
        ttk.Label(file_card, text="1. 选择台账文件", style="Card.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(
            file_card,
            text="选爱数同步到电脑上的那份 Excel。还没有文件可以先点右边生成模板，再把 Word 表格复制进去。",
            style="Hint.TLabel",
            wraplength=700,
        ).grid(row=1, column=0, columnspan=4, sticky="w", pady=(2, 8))

        ttk.Entry(file_card, textvariable=self.excel_var).grid(row=2, column=0, columnspan=2, sticky="ew", padx=(0, 8))
        ttk.Button(file_card, text="选择台账文件", command=self._choose_excel).grid(row=2, column=2, padx=(0, 8))
        ttk.Button(file_card, text="生成空白台账", command=self._make_template).grid(row=2, column=3)

        ttk.Label(file_card, text="工作表", style="Card.TLabel").grid(row=3, column=0, sticky="w", pady=(10, 0))
        self.sheet_combo = ttk.Combobox(file_card, textvariable=self.sheet_var, state="readonly", width=24)
        self.sheet_combo.grid(row=3, column=1, sticky="w", pady=(10, 0))
        ttk.Label(file_card, text="每隔多少分钟检查一次", style="Card.TLabel").grid(row=3, column=2, sticky="e", padx=(12, 8), pady=(10, 0))
        ttk.Combobox(
            file_card,
            textvariable=self.interval_var,
            values=("5", "10", "15", "30", "60"),
            state="readonly",
            width=8,
        ).grid(row=3, column=3, sticky="w", pady=(10, 0))
        file_card.columnconfigure(0, weight=1)
        file_card.columnconfigure(1, weight=1)

        mail_card = self._card(root)
        mail_card.pack(fill="x", pady=(0, 10))
        ttk.Label(mail_card, text="2. 怎么通知", style="Card.TLabel").grid(row=0, column=0, sticky="w")
        ttk.Label(
            mail_card,
            text="一般只用邮箱。QQ/163 要在网页邮箱里开启 SMTP，并使用「授权码」而不是登录密码。",
            style="Hint.TLabel",
            wraplength=700,
        ).grid(row=1, column=0, columnspan=4, sticky="w", pady=(2, 8))

        ttk.Checkbutton(mail_card, text="发邮件给责任人", variable=self.enable_email_var).grid(row=2, column=0, sticky="w")
        ttk.Checkbutton(mail_card, text="同时发企业微信群（可选）", variable=self.enable_wecom_var).grid(
            row=2, column=1, columnspan=2, sticky="w"
        )

        ttk.Label(mail_card, text="邮箱类型", style="Card.TLabel").grid(row=3, column=0, sticky="w", pady=(10, 0))
        preset = ttk.Combobox(
            mail_card,
            textvariable=self.preset_var,
            values=list(SMTP_PRESETS.keys()),
            state="readonly",
            width=18,
        )
        preset.grid(row=3, column=1, sticky="w", pady=(10, 0))
        preset.bind("<<ComboboxSelected>>", self._on_preset)

        ttk.Label(mail_card, text="发件邮箱", style="Card.TLabel").grid(row=4, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(mail_card, textvariable=self.mail_user_var, width=32).grid(row=4, column=1, sticky="ew", pady=(8, 0), padx=(0, 8))
        ttk.Label(mail_card, text="授权码 / 密码", style="Card.TLabel").grid(row=4, column=2, sticky="w", pady=(8, 0))
        ttk.Entry(mail_card, textvariable=self.mail_pass_var, show="•", width=22).grid(row=4, column=3, sticky="ew", pady=(8, 0))

        ttk.Label(mail_card, text="SMTP 服务器", style="Card.TLabel").grid(row=5, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(mail_card, textvariable=self.smtp_host_var, width=32).grid(row=5, column=1, sticky="ew", pady=(8, 0), padx=(0, 8))
        ttk.Label(mail_card, text="端口", style="Card.TLabel").grid(row=5, column=2, sticky="w", pady=(8, 0))
        ttk.Entry(mail_card, textvariable=self.smtp_port_var, width=8).grid(row=5, column=3, sticky="w", pady=(8, 0))

        ttk.Label(mail_card, text="企微机器人地址", style="Card.TLabel").grid(row=6, column=0, sticky="w", pady=(8, 0))
        ttk.Entry(mail_card, textvariable=self.wecom_var).grid(row=6, column=1, columnspan=3, sticky="ew", pady=(8, 0))
        mail_card.columnconfigure(1, weight=1)
        mail_card.columnconfigure(3, weight=1)

        btn_row = ttk.Frame(root)
        btn_row.pack(fill="x", pady=(0, 10))
        ttk.Button(btn_row, text="发送测试邮件", command=self._test_email).pack(side="left")
        ttk.Button(btn_row, text="测试企微", command=self._test_wecom).pack(side="left", padx=8)
        ttk.Button(btn_row, text="立即检查一次", command=lambda: self._run_check(manual=True)).pack(side="left")
        ttk.Button(btn_row, text="开始自动提醒", style="Accent.TButton", command=self._start_monitor).pack(side="right")
        ttk.Button(btn_row, text="停止", command=self._stop_monitor).pack(side="right", padx=8)

        ttk.Label(root, textvariable=self.status_var, style="Sub.TLabel", wraplength=700).pack(anchor="w", pady=(0, 6))

        log_card = self._card(root)
        log_card.pack(fill="both", expand=True)
        ttk.Label(log_card, text="运行记录", style="Card.TLabel").pack(anchor="w")
        self.log = tk.Text(
            log_card,
            height=10,
            wrap="word",
            font=("Microsoft YaHei UI", 9),
            relief="flat",
            bg="#f8fafc",
        )
        self.log.pack(fill="both", expand=True, pady=(8, 0))
        self.log.insert("end", "使用提示：\n")
        self.log.insert("end", "1）台账第 1 行必须是：事项编号、事项名称、影响程度、责任人、责任人邮箱\n")
        self.log.insert("end", "2）请只在一台电脑上点「开始自动提醒」，窗口保持打开，爱数客户端保持登录\n")
        self.log.insert("end", "3）第一次检查只记当前内容，不会发信；之后新改成「直接影响」才会通知\n")
        self.log.configure(state="disabled")

    def _append_log(self, text: str) -> None:
        self.log.configure(state="normal")
        self.log.insert("end", text.rstrip() + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def _current_config(self) -> AppConfig:
        try:
            port = int(self.smtp_port_var.get().strip() or "465")
        except ValueError:
            port = 465
        try:
            interval = int(self.interval_var.get().strip() or "10")
        except ValueError:
            interval = 10
        return AppConfig(
            excel_path=self.excel_var.get().strip(),
            sheet_name=self.sheet_var.get().strip(),
            interval_minutes=max(1, interval),
            enable_email=self.enable_email_var.get(),
            enable_wecom=self.enable_wecom_var.get(),
            mail_preset=self.preset_var.get(),
            smtp_host=self.smtp_host_var.get().strip(),
            smtp_port=port,
            mail_user=self.mail_user_var.get().strip(),
            mail_pass=self.mail_pass_var.get().strip(),
            wecom_webhook=self.wecom_var.get().strip(),
        )

    def _persist(self) -> AppConfig:
        cfg = self._current_config()
        save_config(BASE_DIR, cfg)
        return cfg

    def _on_preset(self, _event: object | None = None) -> None:
        host, port = infer_smtp(self.mail_user_var.get(), self.preset_var.get())
        self.smtp_host_var.set(host)
        self.smtp_port_var.set(str(port))

    def _choose_excel(self) -> None:
        path = filedialog.askopenfilename(
            title="选择台账 Excel",
            filetypes=[("Excel 文件", "*.xlsx *.xlsm"), ("所有文件", "*.*")],
        )
        if not path:
            return
        self.excel_var.set(path)
        self._refresh_sheets()
        self._persist()
        self.status_var.set("已选中台账文件。")

    def _refresh_sheets(self, silent: bool = False) -> None:
        path = Path(self.excel_var.get().strip())
        if not path.exists():
            if not silent:
                messagebox.showwarning("找不到文件", "这个路径下没有文件，请重新选择。")
            return
        try:
            names = list_sheet_names(path)
        except Exception as exc:
            if not silent:
                messagebox.showerror("打不开 Excel", str(exc))
            return
        self.sheet_combo["values"] = names
        if self.sheet_var.get() not in names:
            self.sheet_var.set(names[0] if names else "")

    def _make_template(self) -> None:
        path = filedialog.asksaveasfilename(
            title="保存空白台账",
            defaultextension=".xlsx",
            initialfile="台账.xlsx",
            filetypes=[("Excel 文件", "*.xlsx")],
        )
        if not path:
            return
        create_template(Path(path))
        self.excel_var.set(path)
        self._refresh_sheets()
        self._persist()
        messagebox.showinfo(
            "已生成",
            "空白台账已保存。\n\n请打开它，把 Word 里的表格复制进去。\n第 1 行表头不要改。\n保存后再回到本窗口点「开始自动提醒」。",
        )

    def _validate_notify(self, cfg: AppConfig, *, test: bool = False) -> str | None:
        if not cfg.enable_email and not cfg.enable_wecom:
            return "请至少勾选一种通知方式：邮件或企业微信。"
        if cfg.enable_email:
            if not cfg.mail_user or not cfg.mail_pass:
                return "请填写发件邮箱和授权码。"
        if cfg.enable_wecom and not cfg.wecom_webhook:
            return "勾选了企业微信，请粘贴群机器人地址。"
        if not test and not cfg.excel_path:
            return "请先选择台账文件。"
        return None

    def _test_email(self) -> None:
        cfg = self._persist()
        if not cfg.mail_user or not cfg.mail_pass:
            messagebox.showwarning("还没填完", "请先填写发件邮箱和授权码。")
            return

        def work() -> None:
            try:
                send_email(
                    cfg,
                    cfg.mail_user,
                    "【台账提醒助手】测试邮件",
                    "这是一封测试邮件。如果能看到，说明邮箱设置正确。",
                )
                self.after(0, lambda: messagebox.showinfo("成功", f"测试邮件已发到 {cfg.mail_user}，请去收件箱（含垃圾箱）看一下。"))
                self.after(0, lambda: self._append_log("测试邮件发送成功。"))
            except Exception as exc:
                self.after(0, lambda: messagebox.showerror("发送失败", f"邮件没发出去。\n\n常见原因：授权码不对、未开启 SMTP、公司网络拦截。\n\n详情：{exc}"))
                self.after(0, lambda: self._append_log(f"测试邮件失败：{exc}"))

        threading.Thread(target=work, daemon=True).start()

    def _test_wecom(self) -> None:
        cfg = self._persist()
        if not cfg.wecom_webhook:
            messagebox.showwarning("还没填完", "请先粘贴企业微信群机器人地址。")
            return

        def work() -> None:
            try:
                send_wecom_bot(cfg.wecom_webhook, "台账提醒助手测试：如果看到这条，说明机器人地址正确。")
                self.after(0, lambda: messagebox.showinfo("成功", "已发到企业微信群，请到群里看一下。"))
                self.after(0, lambda: self._append_log("企微测试发送成功。"))
            except Exception as exc:
                self.after(0, lambda: messagebox.showerror("发送失败", str(exc)))
                self.after(0, lambda: self._append_log(f"企微测试失败：{exc}"))

        threading.Thread(target=work, daemon=True).start()

    def _run_check(self, manual: bool = False, ignore_mtime: bool = False) -> None:
        if self._busy:
            return
        cfg = self._persist()
        err = self._validate_notify(cfg)
        if err:
            if manual:
                messagebox.showwarning("还没填完", err)
            else:
                self._append_log(err)
            return
        self._busy = True
        self.status_var.set("正在检查台账…")

        def work() -> None:
            try:
                result = check_and_notify(BASE_DIR, cfg, ignore_mtime=ignore_mtime)
            except Exception:
                detail = traceback.format_exc()
                self.after(0, lambda: self._finish_check(f"检查出错：\n{detail}", failed=True))
                return
            extra = ""
            if result.errors:
                extra = "\n部分通知失败：\n" + "\n".join(result.errors)
            self.after(0, lambda: self._finish_check(result.message + extra, failed=bool(result.errors)))

        threading.Thread(target=work, daemon=True).start()

    def _finish_check(self, message: str, failed: bool = False) -> None:
        self._busy = False
        self.status_var.set(message.split("\n", 1)[0])
        self._append_log(message)
        if failed and "检查出错" in message:
            messagebox.showerror("检查出错", message)

    def _start_monitor(self) -> None:
        cfg = self._persist()
        err = self._validate_notify(cfg)
        if err:
            messagebox.showwarning("还没填完", err)
            return
        self._stop_monitor(silent=True)
        self._append_log(f"已开始自动提醒，每 {cfg.interval_minutes} 分钟检查一次。请保持本窗口打开。")
        self.status_var.set("自动提醒已开启。")
        self._run_check(manual=True, ignore_mtime=True)
        interval_ms = max(1, cfg.interval_minutes) * 60 * 1000
        self._monitor_job = self.after(interval_ms, self._monitor_tick)

    def _monitor_tick(self) -> None:
        self._run_check(manual=False)
        cfg = self._current_config()
        interval_ms = max(1, cfg.interval_minutes) * 60 * 1000
        self._monitor_job = self.after(interval_ms, self._monitor_tick)

    def _stop_monitor(self, silent: bool = False) -> None:
        if self._monitor_job:
            self.after_cancel(self._monitor_job)
            self._monitor_job = None
            if not silent:
                self.status_var.set("已停止自动提醒。")
                self._append_log("已停止自动提醒。")

    def _on_close(self) -> None:
        self._persist()
        self._stop_monitor(silent=True)
        self.destroy()


def main() -> None:
    _enable_windows_dpi()
    app = LedgerAlertApp()
    app.mainloop()


if __name__ == "__main__":
    main()
