import api_manipulator

terms = ['selenium-webdriver', 'robot', 'cypress', 'react', 'angular', 'vue', 'emberjs', 'd3', 'svg', 'web', 'bootstrap']
#terms = ['react', 'angular', 'vue', 'emberjs', 'd3', 'svg', 'web', 'bootstrap']
for i in terms:
    api_manipulator.search_respositories_by_topic('selenium-webdriver')