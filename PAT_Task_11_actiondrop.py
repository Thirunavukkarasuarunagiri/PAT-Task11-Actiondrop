from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DragAndDropExample:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self):
        self.driver.get(self.url)

    def perform_drag_and_drop(self):
        self.driver.switch_to.frame(self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "demo-frame"))))

        draggable_element = self.wait.until(EC.presence_of_element_located((By.ID, "draggable")))
        droppable_element = self.wait.until(EC.presence_of_element_located((By.ID, "droppable")))

        actions = ActionChains(self.driver)
        actions.drag_and_drop(draggable_element, droppable_element).perform()

        assert "Dropped!" in droppable_element.text

    def close_browser(self):
        self.driver.quit()


# Perform the drag and drop operation
if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    drag_and_drop_example = DragAndDropExample(url)
    drag_and_drop_example.open_url()
    drag_and_drop_example.perform_drag_and_drop()
    drag_and_drop_example.close_browser()