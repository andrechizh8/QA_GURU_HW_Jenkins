1. Взять свой код для http://demoqa.com/automation-practice-form
2. Добавить аттачи для Allure – скриншот, page source, console.log и видео
3. Cделать сборку в Jenkins

В качестве ответа на нужно приложить ссылку на Allure-отчет в Jenkins (с видео)


---

pip install -r requirements.txt

pytest --alluredir=allure-results tests

allure.bat serve allure-results

---
![Image alt](https://github.com/andrechizh8/QA_GURU_HW_Jenkins/raw/main/resourses/allure-1.png)

![Image alt](https://github.com/andrechizh8/QA_GURU_HW_Jenkins/raw/main/resourses/b8606fef47f2de1def8562cf91192efe.gif)
