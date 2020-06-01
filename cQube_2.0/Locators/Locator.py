import base64


class Xpath():
    D1= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[2]"
    D2 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[3]"
    D3= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[4]"
    D4 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[5]"
    D5 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[6]"
    D6 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[7]"
    D7= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[8]"
    D8 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[9]"
    D9 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[10]"
    D10 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[11]"
    D11 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[12]"
    D12 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[13]"
    D13 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[14]"
    D14 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[15]"
    D15 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[16]"
    D16 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[17]"
    D17 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[18]"
    D18 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[19]"
    D19 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[20]"
    D20 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[21]"
    D21 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[22]"
    D22 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[23]"
    D23 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[24]"
    D24 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[25]"
    D25 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[26]"
    D26 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[27]"
    D27 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[28]"
    D28 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[29]"
    D29 ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[30]"
    D30 ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[31]"
    D31 ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[32]"
    D32 ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[33]"
    D33 ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[34]"

    B1= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[2]"
    B2 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[3]"
    B3= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[4]"
    B4 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[5]"
    B5 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[6]"
    B6 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[7]"
    B7= "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[8]"
    B8 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[9]"
    B9 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[10]"
    B10 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[11]"
    B11 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[12]"
    B12 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[13]"
    B13 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[14]"
    B14 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option[15]"

    C1 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[2]"
    C2 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[3]"
    C3 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[4]"
    C4 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[5]"
    C5 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[6]"
    C6 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[7]"
    C7 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[8]"
    C8 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[9]"
    C9 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[10]"
    C10 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[11]"
    C11 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[12]"
    C12 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[13]"
    C13 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[14]"
    C14 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[15]"
    C15 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[16]"
    C16 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[17]"
    C17 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[18]"
    C18 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[19]"
    C19 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[20]"
    C20 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[21]"
    C21 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[22]"
    C22 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[23]"
    C23 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[24]"
    C24 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[25]"
    C25 = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option[26]"


    Blocks_btn = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[1]/button[1]"
    Clusters_btn ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[1]/button[2]"
    Schools_btn ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[1]/button[3] "
    Home_icon ="//*[@id='home']"
    Download_icon ="//img[@alt='Download Report']"

    zoom_in = "//a[@title='Zoom in']"
    zoom_out = "//a[@title='Zoom out']"

#list of names
    Dnames = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[1]/option"
    Bnames = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option"
    cnames ="/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[3]/option"

    year = "//select[@id='year']/option[1]"
    monthnames = "//select[@id='month']/option"
    august = "//select[@id='month']/option[contains(text(),'August')]"
    Sept = "//select[@id='month']/option[contains(text(),' September')]"
    Oct = "//select[@id='month']/option[contains(text(),' October ')]"
    blockslist = "//select[@name='myBlock']/option"
    clusterlist = "//select[@name='myCluster']/option"
    dots = "leaflet-interactive"
    back = "//a"
    reg_user = "//a"
    details="//div[@class='col-sm-4']/span"
    # Dash board
    Dashboard = "/html/body/app-root/app-home/mat-toolbar/button[1]/span/mat-icon"
    login_in = "//span[@class='span']"
    SAR = "//div[@class='mat-list-item-content']/td[contains(text(),'Student')]"
    TAR = "//div[@class='mat-list-item-content']/td[contains(text(),'Teacher')]"
    SR = "//div[@class='mat-list-item-content']/td[contains(text(),'Semester')]"
    crc = "//div[@class='mat-list-item-content']/td[contains(text(),'CRC Report')]"
    Log_out = "//button/span[contains(text(),'Log Out')]"
    Home_icon = "//img[@id='home']"
    hyper_link = "//p/span"
    directory = "//p[contains(text(),' Semester report for:')]/span"
    students = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[1]/span"
    schoolcount = " /html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[2]/span"
    DateRange = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-map-view/div/div[4]/div[3]/span"

    # xpath of Dashboard

    crcvisits = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[1]/span"
    totalschools = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[2]/span"

    visited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[3]/span"
    notvisited = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[4]/span"

    range = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div[5]/span"

    # Table in CRC

    # rowby data
    distrows = "//tr[@class='odd']/td"
    headers = "//tr[@role='row']/th"
    footer = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-bar-chart/div/div[5]/div/span"

    # select_type
    distwise = "//select[@name='downloadType']/option[2]"
    blkwise = "//select[@name='downloadType']/option[3]"
    clusterwise = "//select[@name='downloadType']/option[4]"
    schoolwise = "//select[@name='downloadType']/option[5]"
    # X axis and Y axis
    xaxis = "//select[@name='xAxis']/option"
    yaxis = "//select[@name='yAxis']/option"

    crcdistrict = "//select[@name='myDistrict']/option"
    selecttype = "//*[@id='select']/select/option"

    Notemsg = "//div[@class='col-sm-12']/p/b"

    # semester Report
    srDist = "//select[@class='ng-untouched ng-pristine ng-valid']/option"
    srcluster = "//select[@class='ng-pristine ng-valid ng-touched']/option"
    srblock = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/div/app-sem-view/div/div[2]/div[2]/select[2]/option"

    #login_paths
    email = "//input[@id='exampleInputEmail']"
    pwd = "//input[@id='exampleInputPassword']"
    loginbtn = "//button[@type='submit']"
    Path = executable_path = "/home/chetan/Documents/Semester/chromedriver_linux64/chromedriver"

    fpath = "/home/chetan/PycharmProjects/cQube/Driverfile/geckodriver"

    # URL = base64.b64decode("aHR0cHM6Ly9jcXViZS50aWJpbHByb2plY3RzLmNvbQ==").decode("utf-8")





