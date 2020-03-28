# Security Sample

#Prerequisites:
- Java 8 or greater
- Allure report

#Top 10 owasp vulnerabilities scan with behave

- Clone the project
- pip isntall -r requirements.txt
- behave -f allure_behave.formatter:AllureFormatter -o Reports/. features/security.feature
- allure serve Reports/