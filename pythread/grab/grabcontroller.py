import time
from selenium import webdriver
import json
import datetime
import pymysql
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from pythread import GrabModel
DOMAIN_NAME = 'https://fudao.qq.com/'


def insert_data(datalist, table_name):
    # 操作MySQL
    db = pymysql.connect('localhost', 'root', 'yuguangbao', 'test')
    cursor = db.cursor()
    sqli = ''

    try:
        # -----查询数据
        # result = cursor.execute(sql)
        # print(result)
        # info = cursor.fetchmany(result)
        # for li in info:
        #     print(li)
        # -----添加数据
        if table_name == 'course_dashboard':
            for ele in datalist:
                t = [ele.courseId,ele.courseName,ele.courseTotal,ele.createTime,ele.updateTime]
                sqli = "insert into "+str(table_name)+"(course_id,course_name,course_total,create_time,update_time) values (%s, %s, %s, %s, %s)"
                cursor.execute(sqli,t)
                db.commit()
        if table_name == 'course_list':
            for ele in datalist:
                t = [ele.courseParentId,ele.courseChildId,ele.courseType,ele.coursePackId,ele.courseName,ele.courseDuration,ele.courseEnlist,ele.coursePrice,ele.createTime,ele.updateTime]
                sqli = "insert into "+str(table_name)+"(course_parent_id,course_child_id,course_type,course_pack_id,course_name,course_duration,course_enlist,course_price,create_time,update_time) values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
                cursor.execute(sqli,t)
                db.commit()
        if table_name == 'course_teacher_mapping':
            for ele in datalist:
                t = [ele.coursePackId,ele.courseId,ele.className,ele.classDuration,ele.teacherName,ele.jobType,ele.remainNums,ele.classPrice,ele.createTime,ele.updateTime]
                sqli = "insert into "+str(table_name)+"(course_pack_id,course_id,class_name,class_duration,teacher_name,job_type,remain_nums,class_price,create_time,update_time) values (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
                cursor.execute(sqli,t)
                db.commit()
        if table_name == 'course_teacher_info':
            for ele in datalist:
                t = [ele.courseId,ele.teacherName,ele.rate,ele.note,ele.createTime,ele.updateTime]
                sqli = "insert into "+str(table_name)+"(course_id,teacher_name,rate,note,create_time,update_time) values(%s, %s, %s, %s, %s,%s)"
                cursor.execute(sqli,t)
                db.commit()
        cursor.close()
    except:
        # 回滚
        db.rollback()
    db.close()
    print(table_name+'插入数据'+str(len(datalist))+'条完成！')



def get_web_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    return webdriver.Chrome(options=options)


def grabSystemDetail(driver, url):
    driver.get(url)
    courseLists = driver.find_elements_by_xpath("//div[@class='sys-pkg-ct']/li")
    if len(courseLists)>0:
        list = []
        for li in courseLists:
            courses = li.text.split("\n")
            dataDtw = li.find_element_by_tag_name('a').get_attribute('data-tdw')
            myjson = json.loads(dataDtw)
            courseId = myjson["course_id"]
            vo = GrabModel.CourseTeacherMapping(url[url.rfind('/')+1:], courseId, courses[0], courses[1],
                                                ''.join(courses[2:len(courses)-2]),
                                                None, courses[len(courses)-2], courses[len(courses)-1],
                                                datetime.datetime.now(), datetime.datetime.now())
            list.append(vo)
            driver = get_web_driver()
            grabTeacherDetail(driver, DOMAIN_NAME+"pc/course.html?course_id="+str(courseId))
        insert_data(list, 'course_teacher_mapping')


def grabTeacherDetail(driver, url):
    driver.get(url)
    subjectLists = driver.find_elements_by_xpath("//ul[@class='teacherList']/li")
    if len(subjectLists)>0:
        list = []
        for li in subjectLists:
            split = li.text.split("\n")
            vo = GrabModel.CourseTeacherInfo(url[url.find("=")+1:], split[0], None, None,
                                             datetime.datetime.now(), datetime.datetime.now())
            if len(split)>2:
                vo.rate = split[1]
                vo.note = split[2]
            else:
                vo.note = split[1]
            list.append(vo)
        insert_data(list, 'course_teacher_info')


def grab(driver, element):
    attribute = element.find_element_by_tag_name('a').get_attribute('href')
    courseId = element.find_element_by_tag_name('a').get_attribute('data-value')
    courseName = element.find_element_by_tag_name('a').text
    driver.get(DOMAIN_NAME+attribute[attribute.find('subject'):])
    systemLists = driver.find_elements_by_xpath("//ul[@class='sub-system-list']/li")
    print("获取系统课程:" + str(len(systemLists)))
    if len(systemLists)>0:
        list = []
        for sysele in systemLists:
            courses = sysele.text.split('\n')
            dataDtw = sysele.find_element_by_tag_name('a').get_attribute('data-tdw')
            jsonResult = json.loads(dataDtw)
            coursePackId = jsonResult["course_pack_id"]
            vo = GrabModel.CourseList(courseId, None, '1', coursePackId, courses[0], courses[1], courses[2]
                                      , courses[3], datetime.datetime.now(), datetime.datetime.now())
            list.append(vo)
            driver = get_web_driver()
            grabSystemDetail(driver,  DOMAIN_NAME+"subject/"+str(courseId)+"/subject_system/"+str(coursePackId))
        insert_data(list, 'course_list')

    driver.get(DOMAIN_NAME+attribute[attribute.find('subject'):])
    subjectLists = driver.find_elements_by_xpath("//ul[@class='sub-subject-list']/li")
    print("获取专题课程:" + str(len(subjectLists)))
    if len(subjectLists) > 0:
        list = []
        courseLists = []
        for li in subjectLists:
            courses = li.text.split("\n")
            dataDtw = li.find_element_by_tag_name('a').get_attribute('data-tdw')
            jsonResult = json.loads(dataDtw)
            courseChildId = jsonResult["course_id"]
            courseListVO = GrabModel.CourseList(courseId, courseChildId, '2', None, courses[0]
                                                , courses[1], courses[4], courses[5],
                                                datetime.datetime.now(), datetime.datetime.now())
            courseLists.append(courseListVO)
            vo = GrabModel.CourseTeacherMapping(None, courseChildId, courses[0], courses[1],
                                                ''.join(courses[2:len(courses)-2]), None, None, courses[len(courses)-1],
                                                datetime.datetime.now(), datetime.datetime.now())
            list.append(vo)
            driver = get_web_driver()
            grabTeacherDetail(driver, DOMAIN_NAME+"pc/course.html?course_id="+str(courseChildId))
        insert_data(courseLists, 'course_list')
        insert_data(list, 'course_teacher_mapping')
    list = []
    vo = GrabModel.GrabDashboard(courseId, courseName, len(systemLists)+len(subjectLists),
                                 datetime.datetime.now(), datetime.datetime.now())
    list.append(vo)
    insert_data(list, 'course_dashboard')


def startup_grab():
    print("开始执行:" + str(datetime.datetime.now()))
    driver = get_web_driver()
    driver.get(DOMAIN_NAME)
    lists = driver.find_elements_by_xpath("//ul[@class='subject-list']/li")
    for ele in lists:
        if ele.text != '全部':
            print("------ 开始抓取课程【" + ele.text + "】数据 ------")
            driver = get_web_driver()
            grab(driver, ele)
            print("------ 完成抓取课程【" + ele.text + "】数据 ------")
    print("结束执行:" + str(datetime.datetime.now()))
    driver.close()


def dojob():
    scheduler = BlockingScheduler()
    scheduler.add_job(startup_grab, CronTrigger.from_crontab('0 0 * * *'))
    scheduler.start()

dojob()

