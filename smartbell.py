import tkinter as tk
from tkinter import ttk, messagebox
import requests
import threading
from urllib.parse import urlencode
from datetime import datetime

# ==========================================
# 3 TILLI TARJIMALAR LUG'ATI
# ==========================================
TRANSLATIONS = {
    "uz_lat": {
        "lang_name": "O‘zbekça (Yangi lotin)",
        "app_title": "Aqlli Qönğiroq — Amox SmartBell",
        "about_title_text": "Aqlli Qönğiroq",
        "ip_label": "IP manzil:",
        "btn_connect": "Ulaniş",
        "time_unknown": "Joriy vaqt: Noma’lum",
        "time_current": "Joriy vaqt: {time}",
        "time_bell_off": "Joriy vaqt: {time} (Qönğiroq öçirilgan)",
        "time_invalid_fmt": "Vaqt formati notöğri!",
        "time_fetch_err": "Vaqt olişda xatolik!",
        "btn_add_break": "Tanaffus qöşiş",
        "btn_about": "Dastur haqida",
        "btn_change_dt": "Sana va vaqtni özgartiriş",
        "lbl_breaks_list": "Tanaffuslar röyxati:",
        "col_time": "Vaqt",
        "col_duration": "Davomiylik (minut)",
        "col_actions": "Amallar",
        "col_date": "Sana (YYYYMMDD)",
        "click_to_select": "Tanlaş uçun bosing",
        "btn_edit": "Tahrirlaş",
        "btn_delete": "Öçiriş",
        "lbl_holidays_list": "Bayramlar röyxati:",
        "btn_add_holiday": "Yangi bayram qöşiş",
        "btn_del_holiday": "Bayramni öçiriş",
        "dlg_add_break": "Tanaffus qöşiş",
        "dlg_edit_break": "Tanaffusni tahrirlaş",
        "lbl_hour": "Soat (0-23):",
        "lbl_minute": "Minut (0-59):",
        "lbl_duration": "Davomiylik (minut):",
        "btn_add": "Qöşiş",
        "btn_save": "Saqlaş",
        "btn_cancel": "Bekor qiliş",
        "dlg_set_dt": "Sana va vaqtni özgartiriş",
        "lbl_year": "Yil (YYYY):",
        "lbl_month": "Oy (1-12):",
        "lbl_day": "Kun (1-31):",
        "lbl_second": "Sekund (0-59):",
        "btn_change": "Özgartiriş",
        "dlg_add_holiday": "Yangi bayram qöşiş",
        "lbl_date_fmt": "Sana (YYYYMMDD):",
        "dlg_del_holiday": "Bayramni öçiriş",
        "lbl_select_holiday": "Öçiriş uçun bayramni tanlang:",
        "select_placeholder": "Tanlang",
        "dlg_about": "Dastur haqida",
        "about_author": "Dastur muallifi: Sh.X.I.Sulaymonov",
        "about_version": "Dastur versiyasi: 3.1.8.15",
        "about_tg": "Telegram: @sherzodxoja_sulaymonov",
        "about_email": "E-poçta: sherzodxojasulaymonov@gmail.com",
        "err_title": "Xatolik",
        "warn_title": "Ogohlantiriş",
        "info_title": "Muvaffaqiyat",
        "err_enter_ip": "IP manzilni kiriting!",
        "err_connect_first": "Avval NodeMCU ga ulaning!",
        "err_invalid_time_dur": "Notöğri vaqt yoki davomiylik!",
        "err_save_break": "Saqlaşda xatolik yuz berdi!",
        "err_only_numbers": "Faqat raqam kiriting!",
        "err_invalid_dt": "Notöğri sana yoki vaqt!",
        "msg_dt_updated": "Sana va vaqt özgartirildi!",
        "err_dt_update": "Sana va vaqtni özgartirişda xatolik yuz berdi!",
        "err_add_holiday": "Bayram qöşişda xatolik yuz berdi!",
        "err_invalid_holiday": "Sana notöğri! (YYYYMMDD formatida, 20200101 dan 20991231 gaça kiriting)",
        "err_del_holiday": "Bayramni öçirişda xatolik yuz berdi!",
        "warn_select_edit": "Iltimos, tahrirlaş uçun qatorni tanlang!",
        "warn_select_del": "Iltimos, öçiriş uçun qatorni tanlang!",
        "err_del_break": "Öçirişda xatolik yuz berdi!",
        "warn_no_holidays": "Öçiriş uçun bayram yöq!"
    },
    "uz_cyr": {
        "lang_name": "Ўзбекча (Кирилл)",
        "app_title": "Ақлли Қўнғироқ — Amox SmartBell",
        "about_title_text": "Ақлли Қўнғироқ",
        "ip_label": "IP манзил:",
        "btn_connect": "Уланиш",
        "time_unknown": "Жорий вақт: Номаълум",
        "time_current": "Жорий вақт: {time}",
        "time_bell_off": "Жорий вақт: {time} (Қўнғироқ ўчирилган)",
        "time_invalid_fmt": "Вақт формати нотўғри!",
        "time_fetch_err": "Вақт олишда хатолик!",
        "btn_add_break": "Танаффус қўшиш",
        "btn_about": "Дастур ҳақида",
        "btn_change_dt": "Сана ва вақтни ўзгартириш",
        "lbl_breaks_list": "Танаффуслар рўйхати:",
        "col_time": "Вақт",
        "col_duration": "Давомийлик (минут)",
        "col_actions": "Амаллар",
        "col_date": "Сана (YYYYMMDD)",
        "click_to_select": "Танлаш учун босинг",
        "btn_edit": "Таҳрирлаш",
        "btn_delete": "Ўчириш",
        "lbl_holidays_list": "Байрамлар рўйхати:",
        "btn_add_holiday": "Янги байрам қўшиш",
        "btn_del_holiday": "Байрамни ўчириш",
        "dlg_add_break": "Танаффус қўшиш",
        "dlg_edit_break": "Танаффусни таҳрирлаш",
        "lbl_hour": "Соат (0-23):",
        "lbl_minute": "Минут (0-59):",
        "lbl_duration": "Давомийлик (минут):",
        "btn_add": "Қўшиш",
        "btn_save": "Сақлаш",
        "btn_cancel": "Бекор қилиш",
        "dlg_set_dt": "Сана ва вақтни ўзгартириш",
        "lbl_year": "Йил (YYYY):",
        "lbl_month": "Ой (1-12):",
        "lbl_day": "Кун (1-31):",
        "lbl_second": "Секунд (0-59):",
        "btn_change": "Ўзгартириш",
        "dlg_add_holiday": "Янги байрам қўшиш",
        "lbl_date_fmt": "Сана (YYYYMMDD):",
        "dlg_del_holiday": "Байрамни ўчириш",
        "lbl_select_holiday": "Ўчириш учун байрамни танланг:",
        "select_placeholder": "Танланг",
        "dlg_about": "Дастур ҳақида",
        "about_author": "Дастур муаллифи: Ш.Х.И.Сулаймонов",
        "about_version": "Дастур версияси: 3.1.8.15",
        "about_tg": "Telegram: @sherzodxoja_sulaymonov",
        "about_email": "Э-почта: sherzodxojasulaymonov@gmail.com",
        "err_title": "Хатолик",
        "warn_title": "Огоҳлантириш",
        "info_title": "Муваффақият",
        "err_enter_ip": "IP манзилни киритинг!",
        "err_connect_first": "Аввал NodeMCU га уланинг!",
        "err_invalid_time_dur": "Нотўғри вақт ёки давомийлик!",
        "err_save_break": "Сақлашда хатолик юз берди!",
        "err_only_numbers": "Фақат рақам киритинг!",
        "err_invalid_dt": "Нотўғри сана ёки вақт!",
        "msg_dt_updated": "Сана ва вақт ўзгартирилди!",
        "err_dt_update": "Сана ва вақтни ўзгартиришда хатолик юз берди!",
        "err_add_holiday": "Байрам қўшишда хатолик юз берди!",
        "err_invalid_holiday": "Сана нотўғри! (YYYYMMDD форматида, 20200101 дан 20991231 гача киритинг)",
        "err_del_holiday": "Байрамни ўчиришда хатолик юз берди!",
        "warn_select_edit": "Илтимос, таҳрирлаш учун қаторни танланг!",
        "warn_select_del": "Илтимос, ўчириш учун қаторни танланг!",
        "err_del_break": "Ўчиришда хатолик юз берди!",
        "warn_no_holidays": "Ўчириш учун байрам йўқ!"
    },
    "ru": {
        "lang_name": "Русский",
        "app_title": "Умный Звонок — Amox SmartBell",
        "about_title_text": "Умный Звонок",
        "ip_label": "IP-адрес:",
        "btn_connect": "Подключиться",
        "time_unknown": "Текущее время: Неизвестно",
        "time_current": "Текущее время: {time}",
        "time_bell_off": "Текущее время: {time} (Звонок отключён)",
        "time_invalid_fmt": "Неверный формат времени!",
        "time_fetch_err": "Ошибка получения времени!",
        "btn_add_break": "Добавить звонок",
        "btn_about": "О программе",
        "btn_change_dt": "Изменить дату и время",
        "lbl_breaks_list": "Список звонков (перемен):",
        "col_time": "Время",
        "col_duration": "Длительность (мин)",
        "col_actions": "Действия",
        "col_date": "Дата (ГГГГММДД)",
        "click_to_select": "Нажмите для выбора",
        "btn_edit": "Редактировать",
        "btn_delete": "Удалить",
        "lbl_holidays_list": "Список праздничных дней:",
        "btn_add_holiday": "Добавить праздник",
        "btn_del_holiday": "Удалить праздник",
        "dlg_add_break": "Добавить звонок",
        "dlg_edit_break": "Редактировать звонок",
        "lbl_hour": "Час (0-23):",
        "lbl_minute": "Минута (0-59):",
        "lbl_duration": "Длительность (мин):",
        "btn_add": "Добавить",
        "btn_save": "Сохранить",
        "btn_cancel": "Отмена",
        "dlg_set_dt": "Изменить дату и время",
        "lbl_year": "Год (ГГГГ):",
        "lbl_month": "Месяц (1-12):",
        "lbl_day": "День (1-31):",
        "lbl_second": "Секунда (0-59):",
        "btn_change": "Изменить",
        "dlg_add_holiday": "Добавить праздник",
        "lbl_date_fmt": "Дата (ГГГГММДД):",
        "dlg_del_holiday": "Удалить праздник",
        "lbl_select_holiday": "Выберите праздник для удаления:",
        "select_placeholder": "Выберите",
        "dlg_about": "О программе",
        "about_author": "Автор программы: Ш.Х.И.Сулаймонов",
        "about_version": "Версия программы: 3.1.8.15",
        "about_tg": "Telegram: @sherzodxoja_sulaymonov",
        "about_email": "Эл. почта: sherzodxojasulaymonov@gmail.com",
        "err_title": "Ошибка",
        "warn_title": "Предупреждение",
        "info_title": "Успешно",
        "err_enter_ip": "Введите IP-адрес!",
        "err_connect_first": "Сначала подключитесь к NodeMCU!",
        "err_invalid_time_dur": "Неверное время или длительность!",
        "err_save_break": "Ошибка при сохранении!",
        "err_only_numbers": "Вводите только числа!",
        "err_invalid_dt": "Неверная дата или время!",
        "msg_dt_updated": "Дата и время успешно изменены!",
        "err_dt_update": "Ошибка при изменении даты и времени!",
        "err_add_holiday": "Ошибка при добавлении праздника!",
        "err_invalid_holiday": "Неверная дата! (Формат ГГГГММДД, от 20200101 до 20991231)",
        "err_del_holiday": "Ошибка при удалении праздника!",
        "warn_select_edit": "Пожалуйста, выберите строку для редактирования!",
        "warn_select_del": "Пожалуйста, выберите строку для удаления!",
        "err_del_break": "Ошибка при удалении!",
        "warn_no_holidays": "Нет праздников для удаления!"
    }
}


# ==========================================
# NODEMCU CONTROLLER
# ==========================================
class NodeMCUController:
    TOKEN = "AmoxSecretApi"

    def __init__(self, base_url):
        self.base_url = base_url.rstrip("/") + "/"

    def get_current_time(self):
        try:
            response = requests.get(self.base_url + "gettime", timeout=5)
            if response.status_code == 200:
                return response.text
            return None
        except requests.RequestException:
            return None

    def set_current_time(self, year, month, day, hour, minute, second):
        params = {
            "token": self.TOKEN, "year": year, "month": month,
            "day": day, "hour": hour, "minute": minute, "second": second
        }
        try:
            response = requests.post(self.base_url + "setdatetime", data=params, timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def get_schedule(self):
        try:
            response = requests.get(self.base_url + "getschedule", timeout=5)
            if response.status_code == 200:
                return self.parse_schedule(response.text)
            return []
        except requests.RequestException:
            return []

    def add_break(self, hour, minute, duration):
        params = {"token": self.TOKEN, "hour": hour, "minute": minute, "duration": duration}
        try:
            response = requests.post(self.base_url + "setschedule?" + urlencode(params), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def delete_break(self, index):
        params = {"token": self.TOKEN, "index": index}
        try:
            response = requests.post(self.base_url + "deleteschedule?" + urlencode(params), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def edit_break(self, index, hour, minute, duration):
        params = {"token": self.TOKEN, "index": index, "hour": hour, "minute": minute, "duration": duration}
        try:
            response = requests.post(self.base_url + "editschedule?" + urlencode(params), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def parse_schedule(self, response):
        schedules = []
        try:
            parts = response.split(";")
            count = int(parts[0])
            for i in range(1, min(count + 1, len(parts))):
                break_data = parts[i].split(",")
                if len(break_data) == 3:
                    schedules.append({
                        "hour": int(break_data[0]),
                        "minute": int(break_data[1]),
                        "duration": int(break_data[2])
                    })
        except (ValueError, IndexError):
            pass
        return schedules

    def set_datetime(self, year, month, day, hour, minute, second):
        return self.set_current_time(year, month, day, hour, minute, second)

    def add_holiday(self, date):
        params = {"token": self.TOKEN, "date": date}
        try:
            response = requests.post(self.base_url + "setholiday?" + urlencode(params), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def get_holidays(self):
        try:
            response = requests.get(self.base_url + "getholidays?token=" + self.TOKEN, timeout=5)
            if response.status_code == 200 and response.text:
                parts = response.text.split(";")
                if parts and parts[0].isdigit() and int(parts[0]) >= 0:
                    count = int(parts[0])
                    holidays = [int(x) for x in parts[1:] if x.isdigit()]
                    return holidays[:count] if holidays else []
            return []
        except requests.RequestException:
            return []

    def delete_holiday(self, index):
        params = {"token": self.TOKEN, "index": index}
        try:
            response = requests.post(self.base_url + "deleteholiday?" + urlencode(params), timeout=5)
            return response.status_code == 200
        except requests.RequestException:
            return False


# ==========================================
# DIALOG WINDOWS
# ==========================================
class AddBreakDialog(tk.Toplevel):
    def __init__(self, parent, controller, refresh_callback, tr, is_edit=False, schedule=None, index=-1):
        super().__init__(parent)
        self.controller = controller
        self.refresh_callback = refresh_callback
        self.tr = tr
        self.is_edit = is_edit
        self.index = index

        self.title(tr["dlg_edit_break"] if is_edit else tr["dlg_add_break"])
        self.geometry("350x250")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text=tr["lbl_hour"]).pack(pady=5)
        self.hour_entry = tk.Entry(self)
        self.hour_entry.pack(pady=5)

        tk.Label(self, text=tr["lbl_minute"]).pack(pady=5)
        self.minute_entry = tk.Entry(self)
        self.minute_entry.pack(pady=5)

        tk.Label(self, text=tr["lbl_duration"]).pack(pady=5)
        self.duration_entry = tk.Entry(self)
        self.duration_entry.pack(pady=5)

        if is_edit and schedule:
            self.hour_entry.insert(0, str(schedule["hour"]))
            self.minute_entry.insert(0, str(schedule["minute"]))
            self.duration_entry.insert(0, str(schedule["duration"]))

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        btn_text = tr["btn_save"] if is_edit else tr["btn_add"]
        tk.Button(button_frame, text=btn_text, bg="#3F51B5", fg="white", command=self.save).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=tr["btn_cancel"], command=self.destroy).pack(side=tk.LEFT, padx=5)

    def save(self):
        try:
            hour = int(self.hour_entry.get())
            minute = int(self.minute_entry.get())
            duration = int(self.duration_entry.get())
            if not (0 <= hour <= 23 and 0 <= minute <= 59 and duration > 0):
                messagebox.showerror(self.tr["err_title"], self.tr["err_invalid_time_dur"])
                return

            def perform_save():
                if self.is_edit and self.index >= 0:
                    success = self.controller.edit_break(self.index, hour, minute, duration)
                else:
                    success = self.controller.add_break(hour, minute, duration)

                if success:
                    self.after(0, self.refresh_callback)
                    self.after(0, self.destroy)
                else:
                    self.after(0, lambda: messagebox.showerror(self.tr["err_title"], self.tr["err_save_break"]))

            threading.Thread(target=perform_save, daemon=True).start()
        except ValueError:
            messagebox.showerror(self.tr["err_title"], self.tr["err_only_numbers"])


class SetDateTimeDialog(tk.Toplevel):
    def __init__(self, parent, controller, tr):
        super().__init__(parent)
        self.controller = controller
        self.tr = tr
        self.title(tr["dlg_set_dt"])
        self.geometry("350x400")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        now = datetime.now()

        tk.Label(self, text=tr["lbl_year"]).pack(pady=4)
        self.year_entry = tk.Entry(self)
        self.year_entry.insert(0, str(now.year))
        self.year_entry.pack(pady=4)

        tk.Label(self, text=tr["lbl_month"]).pack(pady=4)
        self.month_entry = tk.Entry(self)
        self.month_entry.insert(0, str(now.month))
        self.month_entry.pack(pady=4)

        tk.Label(self, text=tr["lbl_day"]).pack(pady=4)
        self.day_entry = tk.Entry(self)
        self.day_entry.insert(0, str(now.day))
        self.day_entry.pack(pady=4)

        tk.Label(self, text=tr["lbl_hour"]).pack(pady=4)
        self.hour_entry = tk.Entry(self)
        self.hour_entry.insert(0, str(now.hour))
        self.hour_entry.pack(pady=4)

        tk.Label(self, text=tr["lbl_minute"]).pack(pady=4)
        self.minute_entry = tk.Entry(self)
        self.minute_entry.insert(0, str(now.minute))
        self.minute_entry.pack(pady=4)

        tk.Label(self, text=tr["lbl_second"]).pack(pady=4)
        self.second_entry = tk.Entry(self)
        self.second_entry.insert(0, str(now.second))
        self.second_entry.pack(pady=4)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text=tr["btn_change"], bg="#3F51B5", fg="white", command=self.set_datetime).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=tr["btn_cancel"], command=self.destroy).pack(side=tk.LEFT, padx=5)

    def set_datetime(self):
        try:
            year = int(self.year_entry.get())
            month = int(self.month_entry.get())
            day = int(self.day_entry.get())
            hour = int(self.hour_entry.get())
            minute = int(self.minute_entry.get())
            second = int(self.second_entry.get())
            if not (2000 <= year <= 2099 and 1 <= month <= 12 and 1 <= day <= 31 and
                    0 <= hour <= 23 and 0 <= minute <= 59 and 0 <= second <= 59):
                messagebox.showerror(self.tr["err_title"], self.tr["err_invalid_dt"])
                return

            def perform_set_datetime():
                success = self.controller.set_datetime(year, month, day, hour, minute, second)
                if success:
                    self.after(0, lambda: messagebox.showinfo(self.tr["info_title"], self.tr["msg_dt_updated"]))
                    self.after(0, self.destroy)
                else:
                    self.after(0, lambda: messagebox.showerror(self.tr["err_title"], self.tr["err_dt_update"]))

            threading.Thread(target=perform_set_datetime, daemon=True).start()
        except ValueError:
            messagebox.showerror(self.tr["err_title"], self.tr["err_only_numbers"])


class AddHolidayDialog(tk.Toplevel):
    def __init__(self, parent, controller, refresh_callback, tr):
        super().__init__(parent)
        self.controller = controller
        self.refresh_callback = refresh_callback
        self.tr = tr
        self.title(tr["dlg_add_holiday"])
        self.geometry("320x180")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text=tr["lbl_date_fmt"]).pack(pady=10)
        self.date_entry = tk.Entry(self)
        self.date_entry.pack(pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=15)
        tk.Button(button_frame, text=tr["btn_add"], bg="#3F51B5", fg="white", command=self.add).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=tr["btn_cancel"], command=self.destroy).pack(side=tk.LEFT, padx=5)

    def add(self):
        date_str = self.date_entry.get().strip()
        try:
            if len(date_str) != 8 or not date_str.isdigit():
                raise ValueError
            date_int = int(date_str)
            if not (20200101 <= date_int <= 20991231):
                raise ValueError

            def perform_add():
                success = self.controller.add_holiday(date_int)
                if success:
                    self.after(0, self.refresh_callback)
                    self.after(0, self.destroy)
                else:
                    self.after(0, lambda: messagebox.showerror(self.tr["err_title"], self.tr["err_add_holiday"]))

            threading.Thread(target=perform_add, daemon=True).start()
        except ValueError:
            messagebox.showerror(self.tr["err_title"], self.tr["err_invalid_holiday"])


class DeleteHolidayDialog(tk.Toplevel):
    def __init__(self, parent, controller, holidays, refresh_callback, tr):
        super().__init__(parent)
        self.controller = controller
        self.holidays = holidays
        self.refresh_callback = refresh_callback
        self.tr = tr
        self.title(tr["dlg_del_holiday"])
        self.geometry("320x180")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text=tr["lbl_select_holiday"]).pack(pady=10)
        self.holiday_var = tk.StringVar(value=tr["select_placeholder"] if not holidays else str(holidays[0]))
        holiday_menu = ttk.Combobox(self, textvariable=self.holiday_var, values=[str(h) for h in holidays], state="readonly")
        holiday_menu.pack(pady=5)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=15)
        tk.Button(button_frame, text=tr["btn_delete"], bg="#E91E63", fg="white", command=self.delete).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text=tr["btn_cancel"], command=self.destroy).pack(side=tk.LEFT, padx=5)

    def delete(self):
        val = self.holiday_var.get()
        if not val.isdigit():
            return
        selected_date = int(val)
        index = self.holidays.index(selected_date)

        def perform_delete():
            success = self.controller.delete_holiday(index)
            if success:
                self.after(0, self.refresh_callback)
                self.after(0, self.destroy)
            else:
                self.after(0, lambda: messagebox.showerror(self.tr["err_title"], self.tr["err_del_holiday"]))

        threading.Thread(target=perform_delete, daemon=True).start()


class AboutDialog(tk.Toplevel):
    def __init__(self, parent, tr):
        super().__init__(parent)
        self.title(tr["dlg_about"])
        self.geometry("330x250")
        self.resizable(False, False)
        self.transient(parent)
        self.grab_set()

        tk.Label(self, text=tr["about_title_text"], font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self, text=tr["about_author"]).pack(pady=2)
        tk.Label(self, text=tr["about_version"]).pack(pady=2)
        tk.Label(self, text=tr["about_tg"]).pack(pady=2)
        tk.Label(self, text=tr["about_email"]).pack(pady=2)
        tk.Label(self, text="© Amox Fusion Lab", font=("Arial", 10, "italic")).pack(pady=10)
        tk.Button(self, text="OK", width=10, command=self.destroy).pack(pady=5)


# ==========================================
# MAIN APPLICATION WINDOW
# ==========================================
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_lang = "uz_lat"  # Standart til: Yangi o'zbek lotin
        self.tr = TRANSLATIONS[self.current_lang]

        self.title(self.tr["app_title"])
        self.geometry("820x630")
        self.resizable(False, False)
        self.controller = None
        self.schedules = []
        self.holidays = []
        self.last_time_state = ("unknown", "")

        # Yuqori panel: IP manzil va Til tanlash
        top_frame = tk.Frame(self)
        top_frame.pack(pady=10, padx=15, fill=tk.X)

        ip_frame = tk.Frame(top_frame)
        ip_frame.pack(side=tk.LEFT)
        self.lbl_ip = tk.Label(ip_frame, text=self.tr["ip_label"])
        self.lbl_ip.pack(side=tk.LEFT, padx=5)
        self.ip_entry = tk.Entry(ip_frame, width=18)
        self.ip_entry.insert(0, "192.168.4.1")
        self.ip_entry.pack(side=tk.LEFT, padx=5)
        self.btn_connect = tk.Button(ip_frame, text=self.tr["btn_connect"], bg="#4CAF50", fg="white", command=self.connect)
        self.btn_connect.pack(side=tk.LEFT, padx=5)

        # Til tanlash menyusi (O'ng tomonda)
        lang_frame = tk.Frame(top_frame)
        lang_frame.pack(side=tk.RIGHT)
        tk.Label(lang_frame, text="🌐").pack(side=tk.LEFT, padx=2)
        self.lang_map = {v["lang_name"]: k for k, v in TRANSLATIONS.items()}
        self.lang_var = tk.StringVar(value=self.tr["lang_name"])
        self.lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.lang_var,
            values=list(self.lang_map.keys()),
            state="readonly",
            width=22
        )
        self.lang_combo.pack(side=tk.LEFT)
        self.lang_combo.bind("<<ComboboxSelected>>", self.on_language_change)

        # Joriy vaqt yorlig'i
        self.time_label = tk.Label(self, text=self.tr["time_unknown"], font=("Arial", 10, "bold"))
        self.time_label.pack(pady=5)

        # Asosiy boshqaruv tugmalari
        button_frame = tk.Frame(self)
        button_frame.pack(pady=8)
        self.btn_add_break = tk.Button(button_frame, text=self.tr["btn_add_break"], bg="#3F51B5", fg="white", command=self.add_break)
        self.btn_add_break.pack(side=tk.LEFT, padx=5)
        self.btn_about = tk.Button(button_frame, text=self.tr["btn_about"], bg="#800080", fg="white", command=self.show_about)
        self.btn_about.pack(side=tk.LEFT, padx=5)
        self.btn_change_dt = tk.Button(button_frame, text=self.tr["btn_change_dt"], bg="#FF9800", fg="white", command=self.change_datetime)
        self.btn_change_dt.pack(side=tk.LEFT, padx=5)

        # Tanaffuslar jadvali
        self.lbl_breaks = tk.Label(self, text=self.tr["lbl_breaks_list"])
        self.lbl_breaks.pack(pady=4)
        self.tree = ttk.Treeview(self, columns=("Time", "Duration", "Actions"), show="headings", height=5)
        self.tree.heading("Time", text=self.tr["col_time"])
        self.tree.heading("Duration", text=self.tr["col_duration"])
        self.tree.heading("Actions", text=self.tr["col_actions"])
        self.tree.column("Time", width=120, anchor="center")
        self.tree.column("Duration", width=150, anchor="center")
        self.tree.column("Actions", width=220, anchor="center")
        self.tree.pack(pady=4, padx=15, fill=tk.BOTH, expand=True)

        action_frame = tk.Frame(self)
        action_frame.pack(pady=5)
        self.btn_edit = tk.Button(action_frame, text=self.tr["btn_edit"], bg="#FFC107", fg="black", command=self.edit_selected)
        self.btn_edit.pack(side=tk.LEFT, padx=5)
        self.btn_delete = tk.Button(action_frame, text=self.tr["btn_delete"], bg="#E91E63", fg="white", command=self.delete_selected)
        self.btn_delete.pack(side=tk.LEFT, padx=5)

        # Bayramlar jadvali
        self.lbl_holidays = tk.Label(self, text=self.tr["lbl_holidays_list"])
        self.lbl_holidays.pack(pady=4)
        self.holiday_tree = ttk.Treeview(self, columns=("Date", "Actions"), show="headings", height=5)
        self.holiday_tree.heading("Date", text=self.tr["col_date"])
        self.holiday_tree.heading("Actions", text=self.tr["col_actions"])
        self.holiday_tree.column("Date", width=180, anchor="center")
        self.holiday_tree.column("Actions", width=220, anchor="center")
        self.holiday_tree.pack(pady=4, padx=15, fill=tk.BOTH, expand=True)

        holiday_button_frame = tk.Frame(self)
        holiday_button_frame.pack(pady=10)
        self.btn_add_holiday = tk.Button(holiday_button_frame, text=self.tr["btn_add_holiday"], bg="#FF5722", fg="white", command=self.add_holiday)
        self.btn_add_holiday.pack(side=tk.LEFT, padx=5)
        self.btn_del_holiday = tk.Button(holiday_button_frame, text=self.tr["btn_del_holiday"], bg="#E91E63", fg="white", command=self.delete_holiday)
        self.btn_del_holiday.pack(side=tk.LEFT, padx=5)

    def on_language_change(self, event=None):
        selected_name = self.lang_var.get()
        lang_code = self.lang_map.get(selected_name, "uz_lat")
        if lang_code != self.current_lang:
            self.current_lang = lang_code
            self.tr = TRANSLATIONS[self.current_lang]
            self.apply_language()

    def apply_language(self):
        self.title(self.tr["app_title"])
        self.lbl_ip.config(text=self.tr["ip_label"])
        self.btn_connect.config(text=self.tr["btn_connect"])
        self.btn_add_break.config(text=self.tr["btn_add_break"])
        self.btn_about.config(text=self.tr["btn_about"])
        self.btn_change_dt.config(text=self.tr["btn_change_dt"])
        self.lbl_breaks.config(text=self.tr["lbl_breaks_list"])

        self.tree.heading("Time", text=self.tr["col_time"])
        self.tree.heading("Duration", text=self.tr["col_duration"])
        self.tree.heading("Actions", text=self.tr["col_actions"])

        self.btn_edit.config(text=self.tr["btn_edit"])
        self.btn_delete.config(text=self.tr["btn_delete"])
        self.lbl_holidays.config(text=self.tr["lbl_holidays_list"])

        self.holiday_tree.heading("Date", text=self.tr["col_date"])
        self.holiday_tree.heading("Actions", text=self.tr["col_actions"])

        self.btn_add_holiday.config(text=self.tr["btn_add_holiday"])
        self.btn_del_holiday.config(text=self.tr["btn_del_holiday"])

        # Vaqt holatini yangi tilda yangilash
        state, val = self.last_time_state
        if state == "unknown":
            self.time_label.config(text=self.tr["time_unknown"])
        elif state == "bell_off":
            self.time_label.config(text=self.tr["time_bell_off"].format(time=val))
        elif state == "normal":
            self.time_label.config(text=self.tr["time_current"].format(time=val))
        elif state == "invalid_fmt":
            self.time_label.config(text=self.tr["time_invalid_fmt"])
        elif state == "fetch_err":
            self.time_label.config(text=self.tr["time_fetch_err"])

        # Jadvaldagi matnlarni yangilash
        self.update_ui(self.schedules, self.holidays)

    def connect(self):
        ip_address = self.ip_entry.get().strip()
        if not ip_address:
            messagebox.showerror(self.tr["err_title"], self.tr["err_enter_ip"])
            return
        self.controller = NodeMCUController(f"http://{ip_address}")
        self.refresh_data()

    def refresh_data(self):
        if not self.controller:
            messagebox.showerror(self.tr["err_title"], self.tr["err_connect_first"])
            return

        def perform_refresh():
            time_str = self.controller.get_current_time()
            if time_str:
                try:
                    time_obj = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
                    current_day = time_obj.weekday()
                    current_date = int(time_str.split()[0].replace("-", ""))
                    schedules = self.controller.get_schedule()
                    holidays = self.controller.get_holidays()
                    is_holiday = current_date in holidays

                    if current_day == 6 or is_holiday:
                        self.last_time_state = ("bell_off", time_str)
                        lbl_text = self.tr["time_bell_off"].format(time=time_str)
                    else:
                        self.last_time_state = ("normal", time_str)
                        lbl_text = self.tr["time_current"].format(time=time_str)

                    self.after(0, lambda: self.time_label.config(text=lbl_text))
                    self.after(0, lambda: self.update_ui(schedules, holidays))
                except ValueError:
                    self.last_time_state = ("invalid_fmt", "")
                    self.after(0, lambda: self.time_label.config(text=self.tr["time_invalid_fmt"]))
            else:
                self.last_time_state = ("fetch_err", "")
                self.after(0, lambda: self.time_label.config(text=self.tr["time_fetch_err"]))

        threading.Thread(target=perform_refresh, daemon=True).start()

    def update_ui(self, schedules, holidays):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.schedules = schedules
        for schedule in schedules:
            time_str = f"{schedule['hour']:02d}:{schedule['minute']:02d}"
            self.tree.insert("", "end", values=(time_str, schedule['duration'], self.tr["click_to_select"]))

        for item in self.holiday_tree.get_children():
            self.holiday_tree.delete(item)
        self.holidays = holidays
        for holiday in holidays:
            self.holiday_tree.insert("", "end", values=(holiday, self.tr["click_to_select"]))

    def change_datetime(self):
        if not self.controller:
            messagebox.showerror(self.tr["err_title"], self.tr["err_connect_first"])
            return
        SetDateTimeDialog(self, self.controller, self.tr)

    def edit_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning(self.tr["warn_title"], self.tr["warn_select_edit"])
            return
        idx = self.tree.index(selected_item[0])
        if 0 <= idx < len(self.schedules):
            AddBreakDialog(self, self.controller, self.refresh_data, self.tr, is_edit=True, schedule=self.schedules[idx], index=idx)

    def delete_selected(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning(self.tr["warn_title"], self.tr["warn_select_del"])
            return
        idx = self.tree.index(selected_item[0])

        def perform_delete():
            success = self.controller.delete_break(idx)
            if success:
                self.after(0, self.refresh_data)
            else:
                self.after(0, lambda: messagebox.showerror(self.tr["err_title"], self.tr["err_del_break"]))

        threading.Thread(target=perform_delete, daemon=True).start()

    def add_break(self):
        if not self.controller:
            messagebox.showerror(self.tr["err_title"], self.tr["err_connect_first"])
            return
        AddBreakDialog(self, self.controller, self.refresh_data, self.tr)

    def add_holiday(self):
        if not self.controller:
            messagebox.showerror(self.tr["err_title"], self.tr["err_connect_first"])
            return
        AddHolidayDialog(self, self.controller, self.refresh_data, self.tr)

    def delete_holiday(self):
        if not self.controller:
            messagebox.showerror(self.tr["err_title"], self.tr["err_connect_first"])
            return
        if not self.holidays:
            messagebox.showwarning(self.tr["warn_title"], self.tr["warn_no_holidays"])
            return
        DeleteHolidayDialog(self, self.controller, self.holidays, self.refresh_data, self.tr)

    def show_about(self):
        AboutDialog(self, self.tr)


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
