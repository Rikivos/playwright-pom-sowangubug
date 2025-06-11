import config
import time
from locators import citizen_locator as loc

class CitizenPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(f"{config.BASE_URL}/dashboard/penduduk/create")

    def create_citizen(self):
        self.page.fill(loc.NAME_INPUT, "Test Citizen")
        self.page.select_option(loc.GENDER_SELECT, "Perempuan")
        # time.sleep(55)
        self.page.fill(loc.AGE_INPUT, "20")
        self.page.select_option(loc.CATEGORY_AGE_SELECT, "Remaja")
        self.page.select_option(loc.BLOOD_TYPE_SELECT, "A")
        self.page.select_option(loc.STATUS_FAMILY_SELECT, "Anak")
        self.page.select_option(loc.STATUS_MARRIAGE_SELECT, "Belum Kawin")
        self.page.select_option(loc.STATUS_EDUCATION_SELECT, "Pernah Sekolah")
        self.page.select_option(loc.EDUCATION_SELECT, "SD")
        self.page.fill(loc.JOB_INPUT, "Belum Bekerja")
        self.page.select_option(loc.RELIGION_SELECT, "Islam")
        self.page.select_option(loc.RT_SELECT, "49")
        self.page.select_option(loc.ORIGINS_SELECT, "Luar Daerah")
        self.page.click(loc.SAVE_BUTTON)
        # time.sleep(60)
