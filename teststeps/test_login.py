from pytest_bdd import scenario,scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import time
import pytest


#@scenario('../testcases/login.feature', 'Verify a multiple choice question and any primary question can be added to a survey',
          #example_converters=dict(type=str, primary=str))
scenarios('../testcases/login.feature')

def test_login():
    pass

pytest.question_dict = {
    'single_survey_question': ' ',
    'multi_survey_question': ' ',
    'ranked_survey_question': ' ',
    'date_survey_question': ' ',
    'short_survey_question': ' ',
    'intensity_survey_question': ' ',
    'matrix_survey_question': ' '
}

@pytest.fixture
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    browser = webdriver.Chrome(options=chrome_options)
    browser.maximize_window()
    yield browser
    browser.close()


@given('Login page is displayed')
def launch_browser(browser):
    browser.get('https://dev3.mfourdiy.com/login')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#lemail')))


@when('the user enters valid admin credentials')
def valid_admin_credentials_entered(browser):
    browser.find_element(By.CSS_SELECTOR, '#lemail').send_keys('automationqatest@mfour.com')
    browser.find_element(By.CSS_SELECTOR, '#lpassword').send_keys('4nkgmd7p')
    browser.find_element(By.CSS_SELECTOR, '#loginform .text-center button').click()


@then('the user arrives on homepage')
def verify_on_homepage(browser):
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//li[@class="active"]//a[(text()="Dashboard")]')))


@when('the user enters invalid admin credentials')
def invalid_admin_credentials_entered(browser):
    browser.find_element(By.CSS_SELECTOR, '#lemail').send_keys('automationqatestmfour.com')
    browser.find_element(By.CSS_SELECTOR, '#lpassword').send_keys('4nkg7p')
    browser.find_element(By.CSS_SELECTOR, '#loginform .text-center button').click()


@then('the user receives an error')
def verify_user_receives_error(browser):
    assert WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@id="message"]//div[(text()="The email and/or password you entered is incorrect.")]')))


@given('Valid Admin user is logged in')
def valid_admin_login(browser):
    browser.get('https://dev3.mfourdiy.com/login')
    WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#lemail')))
    browser.find_element(By.CSS_SELECTOR, '#lemail').send_keys('automationqatest@mfour.com')
    browser.find_element(By.CSS_SELECTOR, '#lpassword').send_keys('4nkgmd7p')
    browser.find_element(By.CSS_SELECTOR, '#loginform .text-center button').click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, '//li[@class="active"]//a[(text()="Dashboard")]')))


@given('the user wants to create <type> survey')
def create_type_survey(browser, type):
    browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-success btn-lg pull-right create-survey-btn"]').click()
    surveylinks = {
        'custom': '#template-step-list-item-0',
        'US General Population': '#template-step-list-item-1',
        'US Millennial Generation': '#template-step-list-item-2',
        'US Plural Generation Z Population': '#template-step-list-item-3'
    }
    try:
        browser.find_element(By.CSS_SELECTOR, surveylinks.get(type)).click()
        browser.find_element(By.CSS_SELECTOR, '[class="btn btn-default next"]').click()
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#new-survey[style="z-index: 10040; display: block;"]')))
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#project-name')))
        browser.find_element(By.CSS_SELECTOR, '#project-name').send_keys('SurveyTest' + str(datetime.now()))
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#sample-size')))
        browser.find_element(By.CSS_SELECTOR, '#sample-size').send_keys('100')
    except:
        raise Exception('Invalid Survey link')


@when('create project is clicked')
def create_project_button_clicked(browser):
    browser.find_element(By.XPATH, '//button[(text()="Create Project")]').click()


@then('the survey is created')
def verify_survey_created(browser):
    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#progress-bar #pb-step-2.current')))


@when('the user creates a <primary> question')
def create_primary_question(browser, primary):

    def singlequestion():
        question = 'What time does the basketball game start?'
        pytest.question_dict['single_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) td[class="option-name"] [class*="input-sm"]').send_keys('7:30')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) td[class="option-name"] [class*="input-sm"]').send_keys('8:30')

    def multiplequestion():
        question = 'Which pets have you had?'
        pytest.question_dict['multi_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) td[class="option-name"] [class*="input-sm"]').send_keys('dog')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) td[class="option-name"] [class*="input-sm"]').send_keys('cat')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) a[class="btn-option-quick-add"]').click()
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'tbody:nth-of-type(3) td[class="option-name"] [class*="input-sm"]')))
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(3) td[class="option-name"] [class*="input-sm"]').send_keys('I have never had a pet')

    def rankedquestion():
        question = 'Rank these from 1 to 3'
        pytest.question_dict['ranked_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) td[class="option-name"] [class*="input-sm"]').send_keys('1')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) td[class="option-name"] [class*="input-sm"]').send_keys('2')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) a[class="btn-option-quick-add"]').click()
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(3) td[class="option-name"] [class*="input-sm"]').send_keys('3')

    def dateresponse():
        question = 'When were you born?'
        pytest.question_dict['date_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)

    def shortanswer():
        question = 'What is your best quality?'
        pytest.question_dict['short_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)

    def intensityscale():
        question = 'How cold are you?'
        pytest.question_dict['intensity_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
        browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-option-add-idk"]').click()

    def matrix():
        question = 'Do you approve or disapprove of these companies?'
        pytest.question_dict['matrix_survey_question'] = question
        browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) td[class="option-name"] [class*="input-sm"]').send_keys('Disney')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) td[class="option-name"] [class*="input-sm"]').send_keys('Google')
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) [id^="matrix-option-row"] [name="optionName"]').send_keys('Approve')
        browser.find_element(By.CSS_SELECTOR, '[class="btn-matrix-option-quick-add"]').click()
        browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) [id^="matrix-option-row"] [name="optionName"]').send_keys('Disapprove')

    primaryquestions = {
        'single selection': (singlequestion, "#singleSelection"),
        'multiple selection': (multiplequestion, "#multipleSelection"),
        'ranked order': (rankedquestion, "#rankedOrder"),
        'date/time response': (dateresponse, "#dateTimeResponse"),
        'short answer': (shortanswer, "#shortAnswer"),
        'intensity scale': (intensityscale, "#intensityScale"),
        'two-tap matrix': (matrix, "#twoTapMatrixGrids")

    }
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#progress-bar #pb-step-2.current')))
    if browser.find_elements(By.CSS_SELECTOR, '[class="survey-tools panel-collapse collapse in"]'):
        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, primaryquestions[primary][1])))
        browser.find_element(By.CSS_SELECTOR, primaryquestions[primary][1]).click()
        primaryquestions[primary][0]()
        browser.find_element(By.CSS_SELECTOR, '.question-save-label').click()
        WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.curtain')))

    else:
        browser.find_element(By.CSS_SELECTOR, 'div[data-target="#survey-tools-2-items"]').click()
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, primaryquestions[primary][1])))
        browser.find_element(By.CSS_SELECTOR, primaryquestions[primary][1]).click()
        primaryquestions[primary][0]()
        browser.find_element(By.CSS_SELECTOR, '.question-save-label').click()
        WebDriverWait(browser, 5).until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, '.curtain')))


@then('the <primary> questions are added to the survey')
def verify_questions_are_added_to_survey(browser, primary):
    primaryquestions = {
        'single selection': pytest.question_dict['single_survey_question'],
        'multiple selection': pytest.question_dict['multi_survey_question'],
        'ranked order': pytest.question_dict['ranked_survey_question'],
        'date/time response': pytest.question_dict['date_survey_question'],
        'short answer': pytest.question_dict['short_survey_question'],
        'intensity scale': pytest.question_dict['intensity_survey_question'],
        'two-tap matrix': pytest.question_dict['matrix_survey_question']
    }
    xpath = '//h4[(text()="' + primaryquestions[primary] + '")]'
    assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))

@when('the user creates a multiple choice question')
def create_multiple_choice_question(browser):
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#progress-bar #pb-step-2.current')))
    browser.find_element(By.CSS_SELECTOR, 'div[data-target="#survey-tools-2-items"]').click()
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#multipleSelection')))
    browser.find_element(By.CSS_SELECTOR, "#multipleSelection").click()
    question = 'Which pets have you had?'
    pytest.question_dict['multi_survey_question'] = question
    browser.find_element(By.CSS_SELECTOR, 'div[class="redactor_redactor redactor_editor"]').send_keys(question)
    browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(1) td[class="option-name"] [class*="input-sm"]').send_keys(
        'dog')
    browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) td[class="option-name"] [class*="input-sm"]').send_keys(
        'cat')
    browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(2) a[class="btn-option-quick-add"]').click()
    browser.find_element(By.CSS_SELECTOR, 'tbody:nth-of-type(3) td[class="option-name"] [class*="input-sm"]').send_keys(
        'I have never had a pet')
    browser.find_element(By.CSS_SELECTOR, '.question-save-label').click()
    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, '.curtain')))

@then('<primary> questions are added to the survey')
def verify_both_questions_are_added_to_the_survey(browser, primary):
    WebDriverWait(browser, 5).until_not(EC.visibility_of_element_located((By.XPATH,'[class="question-item focused"]')))
    primaryquestions = {
        'single selection': pytest.question_dict['single_survey_question'],
        'multiple selection': pytest.question_dict['multi_survey_question'],
        'ranked order': pytest.question_dict['ranked_survey_question'],
        'date/time response': pytest.question_dict['date_survey_question'],
        'short answer': pytest.question_dict['short_survey_question'],
        'intensity scale': pytest.question_dict['intensity_survey_question'],
        'two-tap matrix': pytest.question_dict['matrix_survey_question']
    }
    xpath = '//h4[(text()="' + primaryquestions[primary] + '")]'
    multiple = '//h4[(text()="Which pets have you had?")]'
    if primary == "multiple selection":
        count = browser.find_elements(By.XPATH, xpath)
        print(count)
        assert len(count) == 2
    else:
        assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, multiple)))
        assert WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))